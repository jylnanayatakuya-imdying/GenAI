"""
Run the self-developed harness on the benchmark (20 public + 12 custom tasks).

    python main.py --model model_a
    python main.py --model model_b --tasks E01,M03,C05      # subset
    python main.py --model model_a --no-test-feedback       # compile feedback only

Output: results/harness_<model_option>_<timestamp>/<TASK_ID>/{code.st,result.json}
Then score it with:  python evaluate.py results/harness_<...>
"""
import asyncio
import time

from agent import PLCHarness, build_team
from benchmark import build_prompt, feedback_cases, load_tasks
from common import (build_model_client, load_settings, make_run_dir,
                    parse_args, save_json, save_run_summary)


async def main():
    args = parse_args()
    settings = load_settings()
    model_name = settings["models"][args.model]
    print(f"Model option: {args.model}")
    print(f"Model: {model_name}")
    model_client = build_model_client(settings, args.model)
    generator = build_team(model_client)
    harness = PLCHarness(generator, max_repairs=args.max_repairs,
                         test_feedback=not args.no_test_feedback)
    tasks = load_tasks(args.subset, args.tasks.split(",") if args.tasks else None)
    out_dir = make_run_dir(f"harness_{args.model}")
    print(f"Output: {out_dir}  ({len(tasks)} tasks)")
    overall_summary = []
    try:
        for task in tasks:
            task_id = task["id"]
            print(f"\n=== {task_id} {task['pou']} ({task['difficulty']}) with {model_name}")
            task_dir = out_dir / task_id
            task_dir.mkdir(parents=True, exist_ok=True)
            prompt = build_prompt(task)
            (task_dir / "prompt.md").write_text(prompt, encoding="utf-8")
            start_time = time.perf_counter()
            try:
                result = await harness.run(task=prompt, pou=task["pou"],
                                           feedback_cases=feedback_cases(task))
                execution_time = time.perf_counter() - start_time
                (task_dir / "code.st").write_text(result.get("code", ""), encoding="utf-8")
                summary = {
                    "task_id": task_id,
                    "pou": task["pou"],
                    "source": task["source"],
                    "difficulty": task["difficulty"],
                    "framework": "harness",
                    "model_option": args.model,
                    "model": model_name,
                    "success": result["success"],
                    "compiled": result["compiled"],
                    "reason": result["reason"],
                    "attempts": result.get("attempts"),
                    "llm_calls": result.get("llm_calls"),
                    "execution_time": execution_time,
                    "prompt_tokens": result.get("prompt_tokens", 0),
                    "completion_tokens": result.get("completion_tokens", 0),
                    "history": result.get("history", [])
                }
            except Exception as e:
                execution_time = time.perf_counter() - start_time
                summary = {
                    "task_id": task_id,
                    "pou": task["pou"],
                    "source": task["source"],
                    "difficulty": task["difficulty"],
                    "framework": "harness",
                    "model_option": args.model,
                    "model": model_name,
                    "success": False,
                    "compiled": False,
                    "reason": "execution_error",
                    "error": f"{type(e).__name__}: {e}",
                    "execution_time": execution_time,
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                }
            save_json(task_dir / "result.json", summary)
            overall_summary.append(summary)
            print(f"    -> {summary['reason']}  ({execution_time:.1f}s)")
        total = len(overall_summary)
        compiled = sum(1 for r in overall_summary if r.get("compiled"))
        execution_time = sum(r.get("execution_time", 0) for r in overall_summary)
        prompt_tokens = sum(r.get("prompt_tokens", 0) for r in overall_summary)
        completion_tokens = sum(r.get("completion_tokens", 0) for r in overall_summary)
        save_run_summary(
            out_dir,
            model_option=args.model,
            model=model_name,
            total=total,
            succeeded=compiled,
            success_rate=((compiled / total) if total else 0),
            execution_time=execution_time,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            results=overall_summary
        )
        print(f"\nTotal tasks: {total}")
        print(f"Compiled: {compiled} ({(compiled / total * 100 if total else 0):.1f}%)")
        print(f"Execution time: {execution_time:.1f}s")
        print(f"Tokens: {prompt_tokens} in / {completion_tokens} out")
        print(f"Next: python evaluate.py \"{out_dir}\"")
    finally:
        await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())
