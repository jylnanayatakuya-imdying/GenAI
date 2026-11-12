
"""
Tools used by the program.
"""
from __future__ import annotations


import json
import os

import httpx
from dotenv import load_dotenv

load_dotenv()


def compile_code(code: str, pou: str | None = None) -> str:
    """
    CODESYS compilation tool.

    Sends generated ST code to the CODESYS HTTP service and
    returns structured compilation results. `pou` is optional: when omitted
    the service uses the name declared in the code (FUNCTION_BLOCK xxx).
    """
    base_url = os.getenv("CODESYS_API_URL", "").rstrip("/")
    if not base_url:
        return json.dumps({
            "success": False,
            "errors": ["CODESYS_API_URL is not configured."],
            "tool_error": True
        })

    payload = {"st_code": code, "backend": "codesys", "timeout": 900}
    if pou:
        payload["pou"] = pou

    try:
        response = httpx.post(
            f"{base_url}/api/compile",
            json=payload,
            timeout=930.0
        )
        response.raise_for_status()
        result = response.json()
        status = result.get("result")
        stage = result.get("stage")
        compilation_success = (
            result.get("ok") is True
            and result.get("result") == "PASS"
            and stage == "codesys"
        )
        valid_outcome = (
            (status in ("PASS", "COMPILE_FAIL") and stage == "codesys")
            or (status == "STATIC_FAIL" and stage == "lint")
        )

        errors = [
            error.get(
                "text",
                error.get("message", str(error))
            ) if isinstance(error, dict) else str(error)
            for error in result.get("errors", [])
        ]

        tool_error = not valid_outcome or bool(result.get("fatal"))

        if tool_error and not errors:
            errors = [
                "Compilation was not completed: "
                + str(result.get("result", stage))
            ]

        return json.dumps({
            "success": compilation_success,
            "errors": errors,
            "tool_error": tool_error,
            "stage": stage,
            "result": result.get("result"),
            "duration_s": result.get("duration_s", 0)
        })

    except (httpx.HTTPError, ValueError) as exc:
        return json.dumps({
            "success": False,
            "errors": [str(exc)],
            "tool_error": True
        })



def summarize_test_failures(test: dict, limit: int = 6) -> str:
    """Compact failure description for a repair prompt (failed steps only)."""
    lines = []
    if test.get("error"):
        lines.append(f"Simulator could not execute the code: {test['error']}")
    for c in test.get("cases", []):
        if c["result"] == "PASS":
            continue
        for s in c.get("steps", []):
            if s.get("ok"):
                continue
            diffs = [d.replace(" 预期 ", ": expected ").replace(" 实际 ", ", actual ")
                     .replace("解释器不支持: ", "simulator cannot execute: ")
                     for d in s.get("diff", [])]
            lines.append(
                f"{c['id']} {c.get('name', '')} | cycle {s.get('cycle')} | "
                f"inputs {json.dumps(s.get('inputs', {}))} | "
                + "; ".join(diffs)
            )
            break
        if len(lines) >= limit:
            break
    return "\n".join(lines)
