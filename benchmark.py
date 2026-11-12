"""
Unified benchmark registry (20 public + 12 custom tasks).

Single source of truth used by BOTH frameworks (our harness in main.py and
the Codex baseline in baseline_codex.py) and by evaluate.py, so every
experiment sees the same task text, the same interface contract and is
scored with the same test cases.

Each task is a dict:
    id          E01..E06 / M01..M08 / H01..H06 (public), C01..C12 (custom)
    pou         FUNCTION_BLOCK name required by the test cases
    source      "public" | "custom"
    difficulty  "easy" | "medium" | "hard"
    title       short title
    description natural-language requirement (Markdown)
    case_path   test-case JSON (codesys_service/run_tests.py format)
    spec_path   LTL specification
    ref_st      reference implementation (used ONLY to extract the
                interface declaration and for the oracle sanity run;
                its body is never shown to a model)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SERVICE = ROOT / "codesys_service"
BANK = SERVICE / "bank"

# data/tasks.json keeps the public questions in question-bank order;
# the test cases / reference ST use these names (same order).
PUBLIC_POU = {
    "easy": ["E01_Filling", "E02_DualEdge", "E03_Hysteresis",
             "E04_JamPump", "E05_WeldGap", "E06_Blower"],
    "medium": ["M01_PumpSwitch", "M02_AnalogBatch", "M03_MovingAvg",
               "M04_TempCtrl", "M05_ProdLine", "M06_SlabThick",
               "M07_HVAC", "M08_IPv4"],
    "hard": ["H01_Proportion", "H02_FlexProcess", "H03_RecipeMgr",
             "H04_FIFO", "H05_MechArm", "H06_Production"],
}

# Conventions the test suite relies on where the question text is ambiguous
# (settled in docs/CROSSCHECK.md). Given identically to every framework.
GENERAL_CONVENTIONS = """\
- The function block is called exactly once per PLC scan cycle.
- Operator push-buttons, confirmation buttons and "...Complete" signals that
  advance a sequence act on their rising edge (FALSE -> TRUE), so holding a
  button does not trigger the same transition again.
- Sensors, limit switches, emergency-stop and mode inputs are level signals.
- Debounce, delay and hold requirements are measured as real elapsed time
  with the standard TON / TOF / TP timers.
- Runtime accumulators add CycleTime in milliseconds (TIME_TO_UDINT) and are
  written to the LTIME output as a millisecond count.
- Status / error codes are WORD values written as 16#xxxx.
- Do not use VARIANT, ARRAY[*], pointers or references; use the concrete
  declarations given above."""

TASK_NOTES = {
    "E04_JamPump": "500 hours = 1 800 000 000 ms.",
    "M01_PumpSwitch": "`start` latches operation, `stop` clears it and has "
                      "priority; while operating, pumps are commanded "
                      "according to the selected mode.",
    "M02_AnalogBatch": "The arrays have a fixed length of 2 in this test "
                       "environment (see declaration).",
    "H04_FIFO": "The queue storage is a concrete ARRAY[0..7] OF DINT "
                "(capacity 8) and item is a DINT (see declaration).",
}


# ---------------------------------------------------------------- helpers

def _strip_comments(text: str) -> str:
    text = re.sub(r"\(\*.*?\*\)", "", text, flags=re.S)
    return re.sub(r"//[^\n]*", "", text)


def interface_contract(ref_st: Path) -> str:
    """TYPE blocks + FUNCTION_BLOCK header + VAR_INPUT/OUTPUT/IN_OUT blocks.

    Internal VAR blocks and the body of the reference are NOT included.
    """
    text = _strip_comments(Path(ref_st).read_text(encoding="utf-8"))
    parts = []
    for m in re.finditer(r"\bTYPE\b.*?\bEND_TYPE\b", text, re.S | re.I):
        parts.append(m.group(0))
    m = re.search(r"\bFUNCTION_BLOCK\s+\w+", text, re.I)
    if m:
        parts.append(m.group(0))
    for m in re.finditer(r"^[ \t]*(VAR_INPUT|VAR_OUTPUT|VAR_IN_OUT)\b.*?^[ \t]*END_VAR\b",
                         text, re.S | re.I | re.M):
        parts.append(m.group(0))
    lines = []
    for block in parts:
        for line in block.splitlines():
            if line.strip():
                lines.append(line.rstrip())
        lines.append("")
    return "\n".join(lines).strip()


def extract_st(text: str) -> str:
    """Pull ST source out of an LLM reply (Markdown fences, leading prose)."""
    text = (text or "").strip()
    fences = re.findall(r"```[a-zA-Z]*\s*\n(.*?)```", text, re.S)
    if fences:
        text = max(fences, key=len).strip()
    m = re.search(r"^[ \t]*(TYPE|FUNCTION_BLOCK|FUNCTION|PROGRAM)\b", text, re.M | re.I)
    if m and m.start() > 0:
        text = text[m.start():]
    return text.strip()


# ---------------------------------------------------------------- loading

def load_tasks(subset: str = "all", only: list[str] | None = None) -> list[dict]:
    tasks: list[dict] = []
    if subset in ("all", "public"):
        data = json.loads((ROOT / "data" / "tasks.json").read_text(encoding="utf-8"))
        for difficulty in ("easy", "medium", "hard"):
            for problem, pou in zip(data[difficulty], PUBLIC_POU[difficulty]):
                title = problem["en"].splitlines()[0].lstrip("# ").strip()
                tasks.append({
                    "id": pou.split("_")[0],
                    "pou": pou,
                    "source": "public",
                    "difficulty": difficulty,
                    "title": title,
                    "description": problem["en"],
                    "case_path": BANK / "cases_part4" / f"{pou}.testcase.json",
                    "spec_path": SERVICE / "specs" / f"{pou}_spec.md",
                    "ref_st": BANK / "st_part4" / f"{pou}.st",
                })
    if subset in ("all", "custom"):
        data = json.loads((ROOT / "data" / "custom_questions.json").read_text(encoding="utf-8"))
        for difficulty in ("easy", "medium", "hard"):
            for q in data.get(difficulty, []):
                tasks.append({
                    "id": q["id"],
                    "pou": q["pou"],
                    "source": "custom",
                    "difficulty": difficulty,
                    "title": q["title"],
                    "description": q["en"],
                    "case_path": BANK / "custom" / "cases" / f"{q['id']}.testcase.json",
                    "spec_path": ROOT / "specs" / "custom" / f"{q['id']}.ltl.json",
                    "ref_st": BANK / "custom" / "st" / f"{q['pou']}.st",
                })
    if only:
        wanted = {x.strip().upper() for x in only if x.strip()}
        tasks = [t for t in tasks if t["id"].upper() in wanted or t["pou"].upper() in wanted]
    return tasks


def feedback_cases(task: dict) -> dict:
    """Cases the harness may show to the model during repair.

    Fixed rule: the FIRST case of every case file (usually the nominal flow).
    All remaining cases are held out and only used for scoring, so
    evaluate.py reports the pass rate on all cases AND on held-out cases.
    """
    data = json.loads(Path(task["case_path"]).read_text(encoding="utf-8"))
    data = dict(data)
    data["cases"] = data["cases"][:1]
    return data


def heldout_case_ids(task: dict) -> set[str]:
    data = json.loads(Path(task["case_path"]).read_text(encoding="utf-8"))
    return {c["id"] for c in data["cases"][1:]}


def build_prompt(task: dict, conventions: bool = True) -> str:
    """The exact prompt given to every framework for this task."""
    parts = [
        task["description"].strip(),
        "",
        "## Implementation contract",
        "",
        f"Implement the requirement as one IEC 61131-3 Structured Text "
        f"FUNCTION_BLOCK named `{task['pou']}` for CODESYS V3.5.",
        "Use exactly the following declarations (names, types, sections). "
        "You may add internal variables in a VAR block. Place any TYPE "
        "definitions before the function block.",
        "",
        "```",
        interface_contract(task["ref_st"]),
        "```",
    ]
    if conventions:
        parts += ["", "## Conventions", "", GENERAL_CONVENTIONS]
        note = TASK_NOTES.get(task["pou"])
        if note:
            parts += [f"- {note}"]
    parts += [
        "",
        "Return the complete ST source (TYPE definitions, if any, followed by "
        "the FUNCTION_BLOCK ... END_FUNCTION_BLOCK).",
    ]
    return "\n".join(parts)


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="List benchmark tasks / print a prompt")
    ap.add_argument("--subset", default="all", choices=["all", "public", "custom"])
    ap.add_argument("--prompt", help="print the prompt of one task id, e.g. E01")
    a = ap.parse_args()
    if a.prompt:
        print(build_prompt(load_tasks(only=[a.prompt])[0]))
    else:
        for t in load_tasks(a.subset):
            ok = all(Path(t[k]).is_file() for k in ("case_path", "spec_path", "ref_st"))
            print(f"{t['id']:4} {t['pou']:16} {t['source']:6} {t['difficulty']:6} "
                  f"{'ok' if ok else 'MISSING FILE'}  {t['title']}")
