"""
Baseline: Codex CLI on the same benchmark, same prompts, same scoring.

    python baseline_codex.py --model model_a
    python baseline_codex.py --model model_b --tasks E01,C05
    python baseline_codex.py --model model_a --with-check    # give Codex a compile/test tool

For every task a fresh, empty workspace is created containing only TASK.md
(the exact prompt that our harness also receives, from benchmark.build_prompt).
Codex is run non-interactively (`codex exec --json`) and must write the
solution to `<POU>.st`. Token usage is read from Codex's JSON event stream.

Default mode is "out of the box": Codex gets no CODESYS access. With
--with-check the workspace also contains check_st.py, which calls the same
CODESYS compile service and runs the same *feedback* cases (first case of each
task) that our harness may see - so both frameworks get identical tool power.

Output: results/codex_<model_option>_<timestamp>/<TASK_ID>/{code.st,result.json,codex.jsonl}
Score it with:  python evaluate.py results/codex_<...> --compile

Requirements: Codex CLI on PATH (`npm i -g @openai/codex`), .env as for main.py.
The model is reached through DMXAPI's OpenAI-compatible endpoint, configured
on the command line (no change to ~/.codex/config.toml).
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

from benchmark import build_prompt, extract_st, feedback_cases, load_tasks
from common import load_settings, make_run_dir, save_json

ROOT = Path(__file__).resolve().parent

CHECK_SCRIPT = '''"""Compile ST with CODESYS and run the example test case.
Usage: python check_st.py <file.st>"""
import json, os, sys, urllib.request
code = open(sys.argv[1], encoding="utf-8").read()
cases = json.load(open("example_case.json", encoding="utf-8"))
req = urllib.request.Request(os.environ["CODESYS_API_URL"].rstrip("/") + "/api/pipeline",
    data=json.dumps({"st_code": code, "cases": cases, "compile_backend": "codesys",
                     "test_backend": "sim"}).encode(), headers={"Content-Type": "application/json"})
r = json.load(urllib.request.urlopen(req, timeout=900))
print("stage:", r.get("stage"), "result:", r.get("result"))
for e in r.get("errors", [])[:10]:
    print("error:", e.get("text") or e.get("message") or e)
t = (r.get("steps") or {}).get("tests") or {}
for g in t.get("results", []):
    for c in g.get("cases", []):
        print("case", c.get("id"), c.get("result"))
        for s in c.get("steps", []):
            for d in s.get("diff", []):
                print("   cycle", s.get("cycle"), d)
'''


def codex_cmd(args, settings, model_name, workdir: Path, prompt: str) -> list[str]:
    base_url = settings["base_url"]
    provider = (
        'model_providers.dmx={name="DMXAPI", base_url="%s", env_key="DMX_API_KEY", '
        'wire_api="%s"}' % (base_url, args.wire_api)
    )
    cmd = [
        args.codex_bin, "exec", "--json", "--skip-git-repo-check",
        "--sandbox", "workspace-write",
        "-C", str(workdir),
        "-m", model_name,
        "-c", 'model_provider="dmx"',
        "-c", provider,
        "-c", "model_reasoning_effort=\"%s\"" % args.reasoning_effort,
    ]
    if args.with_check:
        cmd += ["-c", "sandbox_workspace_write.network_access=true"]
    cmd.append(prompt)
    return cmd


def parse_usage(events: list[dict]) -> tuple[int, int]:
    """Sum token usage over Codex JSON events (format differs between versions)."""
    pin = pout = 0
    for ev in events:
        usage = ev.get("usage") or (ev.get("msg") or {}).get("info", {}).get("last_token_usage")
        if not isinstance(usage, dict):
            continue
        pin += int(usage.get("input_tokens") or usage.get("prompt_tokens") or 0)
        pout += int(usage.get("output_tokens") or usage.get("completion_tokens") or 0)
    return pin, pout


def run_task(args, settings, model_name, task, out_dir: Path) -> dict:
    tdir = out_dir / task["id"]
    work = tdir / "workspace"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    prompt_text = build_prompt(task)
    (work / "TASK.md").write_text(prompt_text, encoding="utf-8")
    (tdir / "prompt.md").write_text(prompt_text, encoding="utf-8")
    target = f"{task['pou']}.st"
    instruction = (
        f"Read TASK.md in the current directory and implement it. "
        f"Write the complete Structured Text solution to the file {target} "
        f"(TYPE definitions first, then the FUNCTION_BLOCK). Do not create other source files."
    )
    if args.with_check:
        (work / "check_st.py").write_text(CHECK_SCRIPT, encoding="utf-8")
        (work / "example_case.json").write_text(
            json.dumps(feedback_cases(task), ensure_ascii=False, indent=2), encoding="utf-8")
        instruction += (
            f" You can check your file with `python check_st.py {target}`: it compiles the code "
            f"in CODESYS and runs the example test case in example_case.json. "
            f"Stop after at most {args.max_repairs + 1} checks."
        )

    env = dict(os.environ)
    env["DMX_API_KEY"] = settings["api_key"]
    start = time.perf_counter()
    try:
        proc = subprocess.run(codex_cmd(args, settings, model_name, work, instruction),
                              capture_output=True, text=True, env=env,
                              timeout=args.timeout)
        stdout, stderr, rc = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = (exc.stderr or "") + "\nTIMEOUT"
        rc = -1
        if isinstance(stdout, bytes):
            stdout = stdout.decode("utf-8", "replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode("utf-8", "replace")
    elapsed = time.perf_counter() - start

    (tdir / "codex.jsonl").write_text(stdout or "", encoding="utf-8")
    if stderr:
        (tdir / "codex.stderr.txt").write_text(stderr, encoding="utf-8")
    events = []
    for line in (stdout or "").splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            pass
    pin, pout = parse_usage(events)

    code = ""
    if (work / target).is_file():
        code = (work / target).read_text(encoding="utf-8")
    else:  # fall back: any .st file, or ST in the final message
        sts = sorted(work.glob("*.st"))
        if sts:
            code = sts[0].read_text(encoding="utf-8")
        else:
            msgs = [e for e in events if "text" in json.dumps(e)]
            if msgs:
                code = extract_st(json.dumps(msgs[-1]))
    (tdir / "code.st").write_text(code, encoding="utf-8")

    return {
        "task_id": task["id"], "pou": task["pou"], "source": task["source"],
        "difficulty": task["difficulty"], "framework": "codex",
        "model_option": args.model, "model": model_name,
        "with_check": args.with_check,
        "returncode": rc, "has_code": bool(code.strip()),
        "execution_time": elapsed,
        "prompt_tokens": pin, "completion_tokens": pout,
        "llm_calls": sum(1 for e in events if e.get("type") == "turn.completed") or None,
    }


def main():
    ap = argparse.ArgumentParser(description="Codex CLI baseline")
    ap.add_argument("--model", choices=["model_a", "model_b"], required=True)
    ap.add_argument("--subset", default="all", choices=["all", "public", "custom"])
    ap.add_argument("--tasks", default="")
    ap.add_argument("--with-check", action="store_true",
                    help="give Codex the CODESYS compile + example-case tool")
    ap.add_argument("--max-repairs", type=int, default=3)
    ap.add_argument("--timeout", type=int, default=900, help="seconds per task")
    ap.add_argument("--codex-bin", default="codex")
    ap.add_argument("--wire-api", default="chat", choices=["chat", "responses"],
                    help="DMXAPI endpoint type used by Codex (try 'responses' if 'chat' is rejected)")
    ap.add_argument("--reasoning-effort", default="medium")
    args = ap.parse_args()

    if not shutil.which(args.codex_bin):
        sys.exit("Codex CLI not found. Install with: npm i -g @openai/codex")
    settings = load_settings()
    model_name = settings["models"][args.model]
    tasks = load_tasks(args.subset, args.tasks.split(",") if args.tasks else None)
    out_dir = make_run_dir(f"codex{'_check' if args.with_check else ''}_{args.model}")
    print(f"Codex baseline, model {model_name}, {len(tasks)} tasks -> {out_dir}")
    rows = []
    for t in tasks:
        print(f"=== {t['id']} {t['pou']}", flush=True)
        meta = run_task(args, settings, model_name, t, out_dir)
        save_json(out_dir / t["id"] / "result.json", meta)
        rows.append(meta)
        print(f"    rc={meta['returncode']} code={'yes' if meta['has_code'] else 'NO'} "
              f"{meta['execution_time']:.0f}s tokens {meta['prompt_tokens']}/{meta['completion_tokens']}")
    save_json(out_dir / "run_summary.json", {"framework": "codex", "model": model_name,
                                             "with_check": args.with_check, "results": rows})
    print(f"Next: python evaluate.py \"{out_dir}\" --compile")


if __name__ == "__main__":
    main()
