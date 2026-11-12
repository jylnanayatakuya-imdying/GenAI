# PLCGen

This program is an LLM-based coding agent system that automatically
generates, compiles and repairs PLC Structured Text (ST) code. It uses
a custom single-agent harness to manage task executions, interact with 
the CODESYS compiler and iteratively fix compilation errors, allowing up to three repair
attempts. 

This project also evaluates and compares the performance of different
LLMs models and agent architectures.

The project is built on Microsoft's AutoGen AgentChat API and uses an
OpenAI-compatible interface. It is configured to use DMXAPI by default, 
supporting models such as Deepseek and Qwen, but can be adapted to other
compatible API providers.

## System Architecture

PLCGen uses a lightweight single-agent architecture.

There are three main components:
* **CodeGeneratorAgent**: An AutoGen Assistant-Agent that generates 
PLC ST code from natural-language requirements and repairs code using feedback provided 
by the compiler.
* **PLCHarness**: An independently developed orchestration layer responsible for task
execution, context management, compilation, iterative repair and termination conditions.
* **CODESYS Compilation Service**: An external HTTP service that compiles generated ST 
code and returns structured compilation results.

Compilation is a mandatory step after code generation. The harness invokes the compiler
directly rather than delegating the decision to an additional LLM Agent, reducing unnecessary
API calls and improving reproducibility.

### Harness Design

PLCHarness implements five core design principles:
* **Task Organization**: Loads PLC problems from a structured JSON dataset and executes a 
predefined generation → compilation → repair workflow.
* **Context Management**: Resets Agent conversation states between independent problems and
retains necessary task requirements and compiler feedback during repair iterations.
* **Tool Invocation**: Automatically invokes CODESYS HTTP compilation service after code generation
and extracts relevant error messages.
* **Compilation and Repair**: Uses compiler feedback to guide code refinement.
* **Termination Conditions**: Stops when compilation succeeds, the compilation service fails or
the maximum number of repair attempts is reached. The system allows up to three repair attempts by
default.

## Quick Start

Python 3.11 or higher is required.

### 1. Create a Virtual Environment and Install Dependencies

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure the LLM API

Copy `.env.example` to `.env` and add your own DMXAPI API key.

Set CODESYS_API_URL to the service address provided by the device hosting CODESYS. 
The service runs remotely, so users do not need to install CODESYS locally.

The `.env` file is excluded from Git to prevent accidental exposure of API credentials.

**Note:** The CODESYS service must be running for compilation to work. If the service host 
restarts the Cloudflare tunnel, the public URL may change and CODESYS_API_URL must be updated.

**Default configuration:**

```dotenv
DMX_API_KEY=your_dmxapi_key
LLM_BASE_URL=https://www.dmxapi.cn/v1

MODEL_A=deepseek-v4-pro-0813
MODEL_B=qwen3-coder-flash

LLM_MAX_TOKENS=16384
LLM_TEMPERATURE=0.2

CODESYS_API_URL=https://associations-food-firmware-riders.trycloudflare.com
```

### 3. CODESYS Toolchain HTTP Service

The `codesys_service/` directory contains the toolchain provided by Part 2:
offline ST lint, CODESYS compilation, and test-case execution (dry / sim / ads backends),
exposed as an HTTP API so the Agent framework and other parts can simply POST JSON.

**Users of the service** (everyone): see `codesys_service/README.md` for the full
API reference and usage examples. Once the service host is running, just:

```python
import httpx
r = httpx.post("http://<service-host>:8000/api/pipeline", json={
    "st_code": st_code, "cases": case_json, "test_backend": "sim",
}, timeout=600).json()
```

Interactive API docs are available at `http://<service-host>:8000/docs`.

**Service host** (the machine with CODESYS installed):

```bash
pip install -r requirements.txt        # includes fastapi / uvicorn
python codesys_service/serve_public.py # one-click: local service + free public URL
```

`serve_public.py` starts the service and a cloudflared quick tunnel, then prints a
public `https://...trycloudflare.com` URL (needs the single-file
[cloudflared](https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe)
binary, no account required; see `codesys_service/README.md` section 4). For LAN-only
use instead: `python codesys_service/server.py --host 0.0.0.0`.

`codesys_service/selftest.py` runs the whole toolchain end-to-end for verification.

### 4. Run the Experiments

The benchmark has 32 tasks: 20 public (`E01`…`H06`) and 12 custom (`C01`…`C12`).
`benchmark.py` is the single task registry: for every task it gives the prompt,
the required FUNCTION_BLOCK name, the test cases and the LTL spec. Both
frameworks receive exactly the same prompt (`python benchmark.py --prompt E01`
prints it) and are scored by the same script.

```bash
python benchmark.py                       # list the 32 tasks and check all files exist

# Experiments 3 / 4 - our harness (generate -> compile -> test -> repair)
python main.py --model model_a
python main.py --model model_b
python main.py --model model_a --tasks E01,C05     # quick trial on a subset

# Experiments 1 / 2 - Codex CLI baseline (npm i -g @openai/codex)
python baseline_codex.py --model model_a
python baseline_codex.py --model model_b

# Score every run with the same procedure, then tabulate
python evaluate.py results/harness_model_a_<stamp>
python evaluate.py results/codex_model_a_<stamp> --compile   # Codex code is compiled here
python evaluate.py --compare results/codex_model_a_<stamp> results/codex_model_b_<stamp> \
                             results/harness_model_a_<stamp> results/harness_model_b_<stamp>

python evaluate.py --oracle               # sanity check: reference solutions score 116/116
```

**Metrics.** Compile pass rate (first attempt and after repairs, CODESYS),
case pass rate (all cases, `sim` backend), held-out case pass rate, task pass
rate (all cases of a task pass), tokens and wall time.

**Fairness of test feedback.** During repair our harness may see only the
*first* test case of each task (`benchmark.feedback_cases`); all other cases are
held out. `evaluate.py` reports the pass rate on all cases and on held-out cases
separately. `--no-test-feedback` runs the compile-only ablation, and
`baseline_codex.py --with-check` gives Codex the same compile + example-case tool.

**Ambiguity conventions.** Where the question text is ambiguous the test cases
follow the conventions in `docs/CROSSCHECK.md`; these are appended to the prompt
of every framework (`benchmark.GENERAL_CONVENTIONS`).

## Dataset and Results
### Dataset

* Public tasks: `data/tasks.json` (question-bank order; mapped to `E01_Filling` … `H06_Production`
  in `benchmark.PUBLIC_POU`). Specs: `codesys_service/specs/`, cases: `codesys_service/bank/cases_part4/`,
  reference ST: `codesys_service/bank/st_part4/`.
* Custom tasks: `data/custom_questions.json` + `data/custom_manifest.json`. Specs: `specs/custom/`,
  cases: `codesys_service/bank/custom/cases/`, reference ST: `codesys_service/bank/custom/st/`.

### Outputs

Each run writes `results/<framework>_<model>_<stamp>/<TASK_ID>/` with

* `prompt.md`: the exact prompt given to the framework.
* `code.st`: final generated ST code.
* `result.json`: generation metrics (tokens, time, attempts, compile history).
* after `evaluate.py`: `test_result.json` (per-step actual outputs).

and at run level `run_summary.json`, then `eval.json`, `eval.md` (summary tables) and
`test_tables.md` (per-case tables in the course test-case template, with actual outputs).
