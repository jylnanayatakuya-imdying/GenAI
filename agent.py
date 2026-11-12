
"""
PLC Coding Agent and custom harness.

Handles ST code generation, compiler-driven repair, test-driven repair,
context management and termination conditions.

Loop per task
    generate -> extract ST -> CODESYS compile
       compile error   -> repair prompt with compiler messages
       compiled        -> run the task's *feedback* test cases (sim)
           failures    -> repair prompt with the failing steps
           all pass    -> stop
    stop also on: repeated / empty code, tool error, budget exhausted.

Feedback split: when `feedback_cases` is given, only those cases are shown
to the model during repair. Final scoring (evaluate.py) always uses the full
case file, identically for every framework.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from autogen_agentchat.agents import AssistantAgent
from autogen_core import CancellationToken

from benchmark import extract_st
from tools import compile_code, summarize_test_failures


class PLCHarness:
    def __init__(self, generator, max_repairs, test_feedback=True):
        self.generator = generator
        self.max_repairs = max_repairs
        self.test_feedback = test_feedback

    async def run(self, task, pou=None, feedback_cases=None):
        await self.generator.on_reset(CancellationToken())
        code = ""
        feedback = None
        feedback_kind = None
        history = []
        prompt_tokens = 0
        completion_tokens = 0
        llm_calls = 0
        success = False
        compiled_ok = False
        reason = "max_attempts_reached"
        previous_codes = set()
        best = None  # (cases_passed, code) of the best compiled version

        for i in range(self.max_repairs + 1):
            if i == 0:
                prompt = task
            elif feedback_kind == "compile":
                prompt = (
                    "The previous ST code FAILED compilation in CODESYS.\n"
                    "Compiler messages:\n"
                    f"{feedback}\n\n"
                    "Fix the errors while preserving the task requirements and the "
                    "required declarations. Return the COMPLETE corrected ST code only."
                )
            else:
                prompt = (
                    "The previous ST code compiled, but it FAILED functional tests "
                    "(one scan cycle per step, outputs checked at the end of the cycle).\n"
                    "Failing steps:\n"
                    f"{feedback}\n\n"
                    "Re-read the requirement, find the logic error and fix it. Keep the "
                    "required declarations unchanged. Return the COMPLETE corrected ST code only."
                )
            generation = await self.generator.run(task=prompt)
            llm_calls += 1
            p, c = token_usage(generation.messages)
            prompt_tokens += p
            completion_tokens += c
            print(f"--- attempt {i + 1}: stop={generation.stop_reason} tokens={p}/{c}")

            code = extract_st(str(generation.messages[-1].content))
            if not code or code in previous_codes:
                reason = "empty_or_repeated_code"
                break
            previous_codes.add(code)

            result = json.loads(compile_code(code, pou))
            entry = {
                "attempt": i + 1,
                "compiled": result["success"],
                "errors": result["errors"],
                "stage": result.get("stage"),
                "result": result.get("result"),
            }
            history.append(entry)
            if result.get("tool_error"):
                reason = "compile_tool_error"
                break
            if not result["success"]:
                feedback = "\n".join(str(error) for error in result["errors"])
                feedback_kind = "compile"
                if not feedback:
                    reason = "missing_compiler_feedback"
                    break
                continue

            compiled_ok = True
            if not (self.test_feedback and feedback_cases):
                success = True
                reason = "compiled"
                break

            test = sim_feedback(code, feedback_cases)
            entry["feedback_tests"] = f"{test['passed']}/{test['total']}"
            if best is None or test["passed"] > best[0]:
                best = (test["passed"], code)
            if test["passed"] == test["total"] and not test.get("error"):
                success = True
                reason = "compiled_and_feedback_tests_passed"
                break
            feedback = summarize_test_failures(test)
            feedback_kind = "test"
            reason = "feedback_tests_failing"

        # Never hand back a worse repair: if the loop ends without success, return
        # the compiled version that passed the most feedback cases.
        if not success and best is not None and code != best[1]:
            code = best[1]
            history.append({"attempt": "final", "selected": "best_compiled_version",
                            "compiled": True, "errors": []})

        return {
            "success": success,
            "compiled": compiled_ok,
            "reason": reason,
            "code": code,
            "attempts": len([h for h in history if h["attempt"] != "final"]),
            "llm_calls": llm_calls,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "history": history
        }


def sim_feedback(code, case_data):
    """Run a subset of cases (dict in run_tests format) on the sim backend."""
    from evaluate import sim_test
    with tempfile.NamedTemporaryFile("w", suffix=".testcase.json", delete=False,
                                     encoding="utf-8") as fh:
        json.dump(case_data, fh)
        path = Path(fh.name)
    try:
        return sim_test(code, path)
    finally:
        path.unlink(missing_ok=True)


SYSTEM_MESSAGE = (
    "You are the ST Code Generator Agent and you are a PLC "
    "programmer. Generate complete IEC 61131-3 Structured Text compatible with "
    "CODESYS V3.5. Follow the requirements and the given declarations exactly. "
    "The function block is executed once per scan cycle; keep state in internal "
    "variables. If compiler or test feedback is provided, repair the code while "
    "preserving the intended behaviour. Return ONLY the complete ST source "
    "(TYPE definitions first, then FUNCTION_BLOCK ... END_FUNCTION_BLOCK). "
    "Do not include explanations or commentary. Keep the solution concise."
)


def build_team(model_client):
    generator = AssistantAgent(
        "CodeGeneratorAgent",
        model_client=model_client,
        description="Generates ST code",
        system_message=SYSTEM_MESSAGE,
    )
    return generator


def token_usage(messages):
    """ Calculates the token usage for each message. """
    prompt_tokens = 0
    completion_tokens = 0
    for message in messages:
        usage = getattr(message, "models_usage", None)
        if usage is not None:
            prompt_tokens += usage.prompt_tokens
            completion_tokens += usage.completion_tokens
    return prompt_tokens, completion_tokens
