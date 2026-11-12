"""
Unified evaluator for all four experiments.

Every framework writes one directory per run:

    results/<run_name>/<TASK_ID>/code.st        final ST code
    results/<run_name>/<TASK_ID>/result.json    generation metadata (tokens, time,
                                                 compile history, ...)

This script scores such a run with ONE procedure for all frameworks:

  * compile  - CODESYS result. Taken from result.json["history"] when the
               framework already compiled through the service (our harness),
               otherwise compiled here via /api/compile (`--compile`).
  * test     - the task's test cases on the offline `sim` backend
               (codesys_service/st_sim.py), the same cases for every framework.
               Code that did not compile is reported as compile-failed and its
               cases count as failed (it would not run on a PLC).

Usage
    python evaluate.py results/harness_model_a_20261112_1530
    python evaluate.py results/codex_model_a_xxx --compile        # baseline
    python evaluate.py --oracle                                   # reference ST, sanity check
    python evaluate.py --compare results/run1 results/run2 ...   # 2x2 table

Outputs (inside the run directory)
    eval.json        per-task + aggregate metrics
    eval.md          summary tables for the report
    test_tables.md   per-case tables in the course template format
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SERVICE = ROOT / "codesys_service"
sys.path.insert(0, str(SERVICE))

from benchmark import load_tasks, heldout_case_ids  # noqa: E402


# ---------------------------------------------------------------- testing

def sim_test(code: str, case_path) -> dict:
    """Run one task's cases on the sim backend. Never raises."""
    import run_tests  # codesys_service/run_tests.py

    case = run_tests.load_case(Path(case_path))
    with tempfile.NamedTemporaryFile("w", suffix=".st", delete=False,
                                     encoding="utf-8") as fh:
        fh.write(code or "")
        st_path = Path(fh.name)
    try:
        res = run_tests.run_sim(case, st_path)
    except Exception as exc:  # interpreter crash -> every case NOT_RUN
        res = {"error": f"{type(exc).__name__}: {exc}",
               "cases": [{"id": c.get("id"), "name": c.get("name"),
                          "result": "NOT_RUN", "steps": []}
                         for c in case.get("cases", [])]}
    finally:
        st_path.unlink(missing_ok=True)
    cases = res.get("cases", [])
    return {
        "total": len(case.get("cases", [])),
        "passed": sum(c["result"] == "PASS" for c in cases),
        "not_run": sum(c["result"] == "NOT_RUN" for c in cases),
        "error": res.get("error"),
        "cases": cases,
        "_raw": res,
    }


def lint(code: str) -> dict:
    from st_lint import lint_source
    return lint_source(code or "")


# ---------------------------------------------------------------- one run

def _compile_from_history(meta: dict):
    """(first_pass, final_pass, attempts_to_pass) from a harness result.json."""
    hist = meta.get("history") or []
    if not hist:
        return None
    oks = [bool(h.get("compiled")) for h in hist]
    first = oks[0]
    final = oks[-1]
    to_pass = (oks.index(True) + 1) if any(oks) else None
    return first, final, to_pass


def evaluate_run(run_dir: Path, do_compile: bool = False) -> dict:
    if do_compile:
        from tools import compile_code  # needs httpx + a reachable CODESYS service

    run_dir = Path(run_dir)
    tasks = load_tasks()
    rows = []
    for t in tasks:
        tdir = run_dir / t["id"]
        code_p = tdir / "code.st"
        meta = {}
        if (tdir / "result.json").is_file():
            meta = json.loads((tdir / "result.json").read_text(encoding="utf-8"))
        if not code_p.is_file():
            rows.append({"id": t["id"], "pou": t["pou"], "source": t["source"],
                         "difficulty": t["difficulty"], "status": "missing"})
            continue
        code = code_p.read_text(encoding="utf-8")

        comp = _compile_from_history(meta)
        compile_errors = []
        if comp is None and do_compile:
            r = json.loads(compile_code(code))
            if r.get("tool_error"):
                comp = None
                compile_errors = r.get("errors", [])
            else:
                comp = (r["success"], r["success"], 1 if r["success"] else None)
                compile_errors = r.get("errors", [])
        lint_ok = lint(code)["ok"]

        test = sim_test(code, t["case_path"])
        compiled = comp[1] if comp else None
        counted_pass = test["passed"] if compiled is not False else 0
        held = heldout_case_ids(t)
        held_pass = sum(c["result"] == "PASS" for c in test["cases"]
                        if c.get("id") in held) if compiled is not False else 0
        row = {
            "id": t["id"], "pou": t["pou"], "source": t["source"],
            "difficulty": t["difficulty"], "status": "ok",
            "lint_ok": lint_ok,
            "compile_first": comp[0] if comp else None,
            "compile_final": compiled,
            "compile_attempts_to_pass": comp[2] if comp else None,
            "compile_errors": compile_errors[:5],
            "cases_total": test["total"],
            "cases_passed_sim": test["passed"],
            "cases_passed": counted_pass,
            "cases_not_run": test["not_run"],
            "heldout_total": len(held),
            "heldout_passed": held_pass,
            "task_pass": compiled is not False and test["total"] > 0
                         and test["passed"] == test["total"],
            "sim_error": test["error"],
            "prompt_tokens": meta.get("prompt_tokens", 0),
            "completion_tokens": meta.get("completion_tokens", 0),
            "execution_time": meta.get("execution_time", 0),
            "llm_calls": meta.get("attempts") or meta.get("llm_calls"),
            "case_results": [{"id": c.get("id"), "name": c.get("name"),
                              "result": c["result"]} for c in test["cases"]],
        }
        rows.append(row)
        (tdir / "test_result.json").write_text(
            json.dumps(test["_raw"], ensure_ascii=False, indent=2), encoding="utf-8")

    summary = aggregate(rows)
    out = {"run": str(run_dir), "summary": summary, "tasks": rows}
    (run_dir / "eval.json").write_text(json.dumps(out, ensure_ascii=False, indent=2),
                                       encoding="utf-8")
    (run_dir / "eval.md").write_text(render_md(run_dir.name, summary, rows), encoding="utf-8")
    write_case_tables(run_dir, tasks)
    return out


def _rate(a, b):
    return round(a / b, 4) if b else 0.0


def aggregate(rows: list[dict]) -> dict:
    def agg(sel):
        rs = [r for r in rows if sel(r)]
        ok = [r for r in rs if r["status"] == "ok"]
        n = len(rs)
        comp_known = [r for r in ok if r["compile_final"] is not None]
        ct = sum(r["cases_total"] for r in ok)
        # missing code: its cases still count in the denominator
        tasks_by_id = {t["id"]: t for t in load_tasks()}
        for r in rs:
            if r["status"] != "ok":
                ct += len(json.loads(Path(tasks_by_id[r["id"]]["case_path"])
                                     .read_text(encoding="utf-8"))["cases"])
        return {
            "tasks": n,
            "compile_first_pass": _rate(sum(bool(r["compile_first"]) for r in ok), n),
            "compile_final_pass": _rate(sum(bool(r["compile_final"]) for r in ok), n),
            "compile_known": len(comp_known),
            "lint_pass": _rate(sum(bool(r["lint_ok"]) for r in ok), n),
            "cases_total": ct,
            "cases_passed": sum(r["cases_passed"] for r in ok),
            "case_pass_rate": _rate(sum(r["cases_passed"] for r in ok), ct),
            "task_pass_rate": _rate(sum(bool(r["task_pass"]) for r in ok), n),
            "heldout_total": sum(len(heldout_case_ids(tasks_by_id[r["id"]])) for r in rs),
            "heldout_passed": sum(r.get("heldout_passed", 0) for r in ok),
            "heldout_pass_rate": _rate(sum(r.get("heldout_passed", 0) for r in ok),
                                       sum(len(heldout_case_ids(tasks_by_id[r["id"]])) for r in rs)),
            "mean_task_case_rate": round(sum(
                (r["cases_passed"] / r["cases_total"]) if r.get("cases_total") else 0
                for r in ok) / n, 4) if n else 0.0,
            "prompt_tokens": sum(r.get("prompt_tokens", 0) or 0 for r in ok),
            "completion_tokens": sum(r.get("completion_tokens", 0) or 0 for r in ok),
            "time_s": round(sum(r.get("execution_time", 0) or 0 for r in ok), 1),
        }
    return {
        "all": agg(lambda r: True),
        "public": agg(lambda r: r["source"] == "public"),
        "custom": agg(lambda r: r["source"] == "custom"),
        "easy": agg(lambda r: r["difficulty"] == "easy"),
        "medium": agg(lambda r: r["difficulty"] == "medium"),
        "hard": agg(lambda r: r["difficulty"] == "hard"),
    }


def _pct(x):
    return f"{x * 100:.1f}%"


def render_md(name: str, s: dict, rows: list[dict]) -> str:
    L = [f"# Evaluation: {name}", "",
         "| Subset | Tasks | Compile 1st | Compile final | Case pass (all) | Case pass (held-out) | Task pass | Tokens (in/out) | Time (s) |",
         "|---|---|---|---|---|---|---|---|---|"]
    for k in ("all", "public", "custom", "easy", "medium", "hard"):
        a = s[k]
        c1 = _pct(a['compile_first_pass']) if a['compile_known'] else "n/a"
        cf = _pct(a['compile_final_pass']) if a['compile_known'] else "n/a"
        L.append(f"| {k} | {a['tasks']} | {c1} | "
                 f"{cf} | {a['cases_passed']}/{a['cases_total']} "
                 f"({_pct(a['case_pass_rate'])}) | {a['heldout_passed']}/{a['heldout_total']} "
                 f"({_pct(a['heldout_pass_rate'])}) | {_pct(a['task_pass_rate'])} | "
                 f"{a['prompt_tokens']}/{a['completion_tokens']} | {a['time_s']} |")
    L += ["", "| Task | POU | Compile 1st | Compile final | Repairs | Cases | Task pass | Note |",
          "|---|---|---|---|---|---|---|---|"]
    yn = {True: "Y", False: "N", None: "-"}
    for r in rows:
        if r["status"] != "ok":
            L.append(f"| {r['id']} | {r['pou']} | - | - | - | - | N | no code |")
            continue
        note = (r["sim_error"] or "")[:60].replace("|", "/")
        if r["compile_final"] is False:
            note = "compile failed; " + note
        L.append(f"| {r['id']} | {r['pou']} | {yn[r['compile_first']]} | {yn[r['compile_final']]} | "
                 f"{(r['compile_attempts_to_pass'] or 0) - 1 if r['compile_attempts_to_pass'] else '-'} | "
                 f"{r['cases_passed']}/{r['cases_total']} | {yn[r['task_pass']]} | {note} |")
    return "\n".join(L) + "\n"


def write_case_tables(run_dir: Path, tasks: list[dict]):
    """Per-case tables (course template: steps, inputs, expected, actual, result)."""
    import run_tests
    parts = []
    for t in tasks:
        p = run_dir / t["id"] / "test_result.json"
        if not p.is_file():
            continue
        res = json.loads(p.read_text(encoding="utf-8"))
        res.setdefault("task_id", t["pou"])
        res.setdefault("mode", "sim")
        parts.append(run_tests.render_markdown(res))
    (run_dir / "test_tables.md").write_text("\n\n".join(parts), encoding="utf-8")


# ---------------------------------------------------------------- oracle / compare

def oracle(out_root: Path):
    """Score the reference implementations as if they were a run (sanity check)."""
    run = out_root / "oracle_reference"
    for t in load_tasks():
        d = run / t["id"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "code.st").write_text(Path(t["ref_st"]).read_text(encoding="utf-8"),
                                   encoding="utf-8")
    return evaluate_run(run)


def compare(run_dirs: list[Path]) -> str:
    L = ["| Run | Compile 1st | Compile final | Case pass | Held-out case pass | Task pass | Public task pass | Custom task pass | Tokens | Time (s) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for d in run_dirs:
        e = json.loads((Path(d) / "eval.json").read_text(encoding="utf-8"))["summary"]
        a = e["all"]
        L.append(f"| {Path(d).name} | {_pct(a['compile_first_pass'])} | {_pct(a['compile_final_pass'])} | "
                 f"{_pct(a['case_pass_rate'])} | {_pct(a['heldout_pass_rate'])} | {_pct(a['task_pass_rate'])} | "
                 f"{_pct(e['public']['task_pass_rate'])} | {_pct(e['custom']['task_pass_rate'])} | "
                 f"{a['prompt_tokens'] + a['completion_tokens']} | {a['time_s']} |")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Score a generation run")
    ap.add_argument("run_dir", nargs="?", help="results/<run_name>")
    ap.add_argument("--compile", action="store_true",
                    help="compile via the CODESYS service when result.json has no compile history")
    ap.add_argument("--oracle", action="store_true", help="score the reference implementations")
    ap.add_argument("--compare", nargs="+", help="evaluated run dirs to tabulate")
    a = ap.parse_args()
    if a.compare:
        md = compare([Path(x) for x in a.compare])
        print(md)
        (ROOT / "results" / "comparison.md").write_text(md, encoding="utf-8")
        return
    if a.oracle:
        out = oracle(ROOT / "results")
    elif a.run_dir:
        out = evaluate_run(Path(a.run_dir), do_compile=a.compile)
    else:
        ap.error("give a run directory, --oracle or --compare")
    s = out["summary"]["all"]
    print(f"{out['run']}: tasks {s['tasks']}  compile 1st {_pct(s['compile_first_pass'])}  "
          f"final {_pct(s['compile_final_pass'])}  cases {s['cases_passed']}/{s['cases_total']}  "
          f"task pass {_pct(s['task_pass_rate'])}")
    print("details:", Path(out["run"]) / "eval.md")


if __name__ == "__main__":
    main()
