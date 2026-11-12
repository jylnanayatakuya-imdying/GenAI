
"""
Shared methods for the PLC Coding Agent.

Handles configuration, LLM clients, command-line
arguments, output directories and result saving.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent


def load_settings() -> dict[str, Any]:
    """Load configuration from .env."""

    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("DMX_API_KEY")
    if not api_key or api_key.startswith("your_"):
        raise RuntimeError(
            "Missing API key. Copy .env.example to .env and add your DMX_API_KEY."
        )

    return {
        "api_key": api_key,
        "base_url": os.getenv("LLM_BASE_URL", "https://www.dmxapi.cn/v1"),
        "models": {
            "model_a": os.getenv("MODEL_A"),
            "model_b": os.getenv("MODEL_B"),
        },
        "max_tokens": int(os.getenv("LLM_MAX_TOKENS", "4096")),
        "temperature": float(os.getenv("LLM_TEMPERATURE", "0.2"))
    }


def build_model_client(settings: dict[str, Any], model: str) -> OpenAIChatCompletionClient:
    """Create a DMXAPI OpenAI-compatible client."""

    if model not in settings["models"]:
        raise ValueError(f"Unknown model selection: {model}.")

    model_name = settings["models"][model]

    if not model_name:
        raise ValueError(f"{model} is not configured in .env.")

    return OpenAIChatCompletionClient(
        model=model_name,
        api_key=settings["api_key"],
        base_url=settings["base_url"],
        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": False,
            "family": "unknown",
            "structured_output": False,
        },
        temperature=settings["temperature"],
        max_tokens=settings["max_tokens"],
        timeout=900,
        max_retries=2,
        parallel_tool_calls=False,
        add_name_prefixes=True,
    )


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description="PLC Code Generation Agent")
    parser.add_argument(
        "--model",
        choices=["model_a", "model_b"],
        required=True,
        help="Select the language model: MODEL_A or MODEL_B"
    )
    parser.add_argument("--subset", default="all", choices=["all", "public", "custom"],
                        help="Which part of the benchmark to run (default: all 32 tasks)")
    parser.add_argument("--tasks", default="",
                        help="Comma-separated task ids or POU names, e.g. E01,M03,C05")
    parser.add_argument("--max-repairs", type=int, default=3,
                        help="Repair rounds after the first generation (default 3)")
    parser.add_argument("--no-test-feedback", action="store_true",
                        help="Repair on compiler errors only (ablation)")
    return parser.parse_args()


def make_run_dir(name: str) -> Path:
    """Create results/<name>_<timestamp>/ for a run."""

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    res_dir = PROJECT_ROOT / "results" / f"{name}_{stamp}"
    res_dir.mkdir(parents=True, exist_ok=True)
    return res_dir


def save_json(path: Path, value: Any) -> None:
    """Save structured results as JSON."""

    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def save_run_summary(
    out_dir: Path,
    *,
    model_option: str,
    model:str,
    total: int,
    succeeded: int,
    success_rate: float,
    execution_time: float,
    prompt_tokens: int = 0,
    completion_tokens: int = 0,
    results: list[dict],
) -> None:
    """Save results."""

    summary = {
        "model_option": model_option,
        "model": model,
        "total_tasks": total,
        "compiled_tasks": succeeded,
        "compiled_success_rate": success_rate,
        "execution_time_seconds": execution_time,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": (prompt_tokens + completion_tokens),
        "results": results,
    }

    save_json(out_dir / "run_summary.json", summary)
