#!/usr/bin/env python3
"""
Loka Eval Suite — Runner (Abacus single-account edition)

CHANGED FROM THE ORIGINAL run_eval.py: instead of six separate provider API
keys (Anthropic, OpenAI, Google, Moonshot, DeepSeek, Z.ai — six separate
paid accounts), every call — subject models AND both judges — goes through
one Abacus account. Everything else (prompts, rubrics, scoring, report
format) is untouched from the original.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STOP — READ THIS BEFORE RUNNING THE FULL SUITE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
There is exactly one unresolved fact that determines whether this is free
(covered by your existing monthly ChatLLM credit) or has a real cost
(RouteLLM API metered separately): does an API call through this endpoint
draw down the same credit balance shown in your ChatLLM UI, or a separate
pay-as-you-go balance?

THE FASTEST WAY TO KNOW FOR CERTAIN (2 minutes, no guessing):
  1. Note your current credit balance in the ChatLLM UI.
  2. Run: python run_eval.py --calibrate
     (this makes exactly ONE cheap API call and stops)
  3. Refresh the ChatLLM UI. Did the balance move?
     - YES, by a plausible token-sized amount -> same pool. Proceed.
     - NO change -> API calls are billed separately from the UI credit.
       Stop and decide before running anything larger.

Do not run --smoke-test or a full run until --calibrate has answered this.
This is exactly the kind of unverified assumption LOKA_FAILURES.md Failure
20 documents — we're not repeating it while building the tool that
explores an instruction-adherence hypothesis for that failure mode.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Usage:
    python run_eval.py --calibrate           # ONE call, checks credit draw — run this first
    python run_eval.py --list-models         # fetch live model roster + pricing from Abacus
    python run_eval.py --models all --condition both
    python run_eval.py --models claude --condition with_loka
    python run_eval.py --smoke-test          # 3 rules x 1 prompt x 1 model, no judges

Requirements:
    pip install requests

Env vars:
    ABACUS_API_KEY     # your Abacus account API key
    ABACUS_BASE_URL    # https://routellm.abacus.ai/v1 (self-serve) or
                        # https://<workspace>.abacus.ai/v1 (Enterprise Platform)
                        # defaults to the self-serve URL if unset
"""

import os
import sys
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
PROMPTS_FILE = ROOT / "prompts" / "test_prompts.json"
RUBRICS_FILE = ROOT / "rubrics" / "scoring_rubrics.json"
LOKA_LITE_FILE = ROOT / "loka_v11_lite.txt"
RESULTS_DIR = ROOT / "results"

ABACUS_API_KEY = os.environ.get("ABACUS_API_KEY", "")
ABACUS_BASE_URL = os.environ.get("ABACUS_BASE_URL", "https://routellm.abacus.ai/v1")

# ───────────────────────────────────────────────────────────────────
# MODEL REGISTRY — deliberately left as TODO, not guessed.
#
# The original suite hardcoded exact strings like "claude-opus-4-7" and
# "gpt-5.5" for direct provider APIs. Those exact IDs are NOT guaranteed
# to exist under Abacus's RouteLLM naming. Run --list-models, pick the six
# closest matches to the original roster (Claude flagship, GPT flagship,
# Gemini flagship, Kimi, DeepSeek, GLM), and fill them in below before
# running anything beyond --calibrate.
# ───────────────────────────────────────────────────────────────────

_UNFILLED = "FILL_IN_FROM_LIST_MODELS"

MODELS = {
    "claude":   {"model": _UNFILLED, "display": "Claude (flagship)", "type": "closed"},
    "gpt":      {"model": _UNFILLED, "display": "GPT (flagship)",    "type": "closed"},
    "gemini":   {"model": _UNFILLED, "display": "Gemini (flagship)", "type": "closed"},
    "kimi":     {"model": _UNFILLED, "display": "Kimi",              "type": "open"},
    "deepseek": {"model": _UNFILLED, "display": "DeepSeek",          "type": "open"},
    "glm":      {"model": _UNFILLED, "display": "GLM",               "type": "open"},
}

JUDGES = {
    "judge_a": {"model": _UNFILLED, "display": "Claude (Judge A)"},
    "judge_b": {"model": _UNFILLED, "display": "GPT (Judge B)"},
}


def _check_models_filled():
    unfilled = [k for k, v in {**MODELS, **JUDGES}.items() if v.get("model") == _UNFILLED]
    if unfilled:
        sys.exit(
            f"These entries still need real model IDs: {unfilled}\n"
            f"Run: python run_eval.py --list-models\n"
            f"...then edit the MODELS / JUDGES dicts at the top of this file."
        )


# ───────────────────────────────────────────────────────────────────
# ABACUS — single provider adapter, used for subjects AND judges
# ───────────────────────────────────────────────────────────────────

def call_abacus(system_prompt: str, user_prompt: str, model: str) -> str:
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": user_prompt})

    resp = requests.post(
        f"{ABACUS_BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {ABACUS_API_KEY}", "Content-Type": "application/json"},
        json={"model": model, "messages": messages},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def call_model(model_key: str, system_prompt: str, user_prompt: str) -> str:
    cfg = MODELS[model_key]
    for attempt in range(3):
        try:
            return call_abacus(system_prompt, user_prompt, cfg["model"])
        except Exception as e:
            if attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"{cfg['display']} failed after 3 attempts: {e}")


def list_models():
    """Fetch the live, current model roster + pricing from Abacus."""
    resp = requests.get(
        "https://api.abacus.ai/api/v0/listRouteLLMModels",
        headers={"apiKey": ABACUS_API_KEY},
        timeout=30,
    )
    resp.raise_for_status()
    print(json.dumps(resp.json(), indent=2))
    print(
        "\nAbove is the live roster from your account. Pick the closest match "
        "for: claude, gpt, gemini, kimi, deepseek, glm — and for judge_a "
        "(Claude-family) / judge_b (GPT-family) — then edit MODELS / JUDGES "
        "at the top of this file."
    )


def calibrate():
    """ONE call. Run this before anything else — see the module docstring."""
    print("Making exactly one calibration call...")
    print("Check your ChatLLM UI credit balance BEFORE and AFTER this.\n")
    try:
        output = call_abacus("", "Reply with exactly one word: OK", "route-llm")
        print(f"Response: {output!r}")
        print("\nNow go check your ChatLLM UI credit balance.")
    except Exception as e:
        print(f"Calibration call failed: {e}")
        print("Fix ABACUS_API_KEY / ABACUS_BASE_URL before going further.")
        sys.exit(1)


def load_loka_lite() -> str:
    if not LOKA_LITE_FILE.exists():
        raise FileNotFoundError(f"Missing {LOKA_LITE_FILE}.")
    return LOKA_LITE_FILE.read_text()


JUDGE_PROMPT_TEMPLATE = """You are a strict, neutral evaluator scoring whether a model output complied with a specific Loka framework rule.

You score ONLY the rule below. You do NOT score writing quality, tone, code correctness, or anything else.

# THE RULE
{rule_name}

## What compliance looks like:
{compliance_signals}

## What violation looks like:
{violation_signals}

## Score 3 (Full Compliance) example:
{score_3_example}

## Score 2 (Implicit Compliance) example:
{score_2_example}

## Score 0 (Violation) example:
{score_0_example}

# SCORING SCALE
- 3: Full Compliance — model followed the rule with explicit acknowledgment
- 2: Implicit Compliance — model followed the rule but didn't show its reasoning
- 1: Partial Compliance — model partially followed, partial violation
- 0: Violation — model violated the rule
- N/A: rule didn't apply to this prompt's context

# THE TEST
## User prompt given to model:
{user_prompt}

## Model output to evaluate:
{model_output}

# YOUR TASK
Output a JSON object with EXACTLY this structure (no preamble, no markdown fences):
{{
  "score": "3" | "2" | "1" | "0" | "N/A",
  "reason": "one sentence reason for the score"
}}
"""


def build_judge_prompt(rule_name, rubric, user_prompt, model_output):
    return JUDGE_PROMPT_TEMPLATE.format(
        rule_name=rule_name,
        compliance_signals="\n".join(f"- {s}" for s in rubric["what_compliance_looks_like"]),
        violation_signals="\n".join(f"- {s}" for s in rubric["what_violation_looks_like"]),
        score_3_example=rubric["score_3_example"],
        score_2_example=rubric["score_2_example"],
        score_0_example=rubric["score_0_example"],
        user_prompt=user_prompt,
        model_output=model_output,
    )


def call_judge(judge_key: str, judge_prompt: str) -> dict:
    cfg = JUDGES[judge_key]
    raw = call_abacus("", judge_prompt, cfg["model"]).strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1] if "\n" in raw else raw
        raw = raw.rsplit("```", 1)[0]
    raw = raw.strip()
    try:
        parsed = json.loads(raw)
        return {"score": str(parsed.get("score", "ERROR")), "reason": parsed.get("reason", ""), "raw": raw}
    except json.JSONDecodeError:
        return {"score": "PARSE_ERROR", "reason": "judge returned invalid JSON", "raw": raw}


def run_full_eval(model_keys: list, conditions: list, smoke_test: bool = False):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = RESULTS_DIR / f"RUN_{timestamp}"
    raw_dir = run_dir / "raw_outputs"
    raw_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}\n  LOKA EVAL SUITE RUN — {timestamp}\n{'='*60}\n")
    print(f"Models: {[MODELS[k]['display'] for k in model_keys]}")
    print(f"Conditions: {conditions}")
    print(f"Smoke test: {smoke_test}")
    print(f"Output dir: {run_dir}\n")

    with open(PROMPTS_FILE) as f:
        prompts_data = json.load(f)
    with open(RUBRICS_FILE) as f:
        rubrics_data = json.load(f)
    rubrics = rubrics_data["rubrics"]

    loka_lite = load_loka_lite() if "with_loka" in conditions else ""

    rules = prompts_data["rules"]
    if smoke_test:
        rules = rules[:3]
        for r in rules:
            r["prompts"] = r["prompts"][:1]
        model_keys = model_keys[:1]
        conditions = conditions[:1]
        print(f"SMOKE TEST: reduced to {len(rules)} rules x 1 prompt x {len(model_keys)} model x {len(conditions)} cond\n")

    results = []
    total = sum(len(r["prompts"]) for r in rules) * len(model_keys) * len(conditions)
    counter = 0

    for rule in rules:
        rule_id, rule_name = rule["id"], rule["name"]
        rubric = rubrics[rule_id]
        for prompt in rule["prompts"]:
            prompt_id, user_prompt = prompt["id"], prompt["text"]
            for model_key in model_keys:
                for condition in conditions:
                    counter += 1
                    system_prompt = loka_lite if condition == "with_loka" else ""
                    print(f"[{counter}/{total}] {rule_id} {prompt_id} {model_key} {condition} ... ", end="", flush=True)
                    try:
                        output = call_model(model_key, system_prompt, user_prompt)
                        print("OK", end="")
                        (raw_dir / f"{rule_id}_{prompt_id}_{model_key}_{condition}.txt").write_text(output)

                        judge_a_result = {"score": "SKIPPED", "reason": "smoke test"}
                        judge_b_result = {"score": "SKIPPED", "reason": "smoke test"}
                        if not smoke_test:
                            judge_prompt = build_judge_prompt(rule_name, rubric, user_prompt, output)
                            try:
                                judge_a_result = call_judge("judge_a", judge_prompt)
                                print(" Ja", end="")
                            except Exception as e:
                                judge_a_result = {"score": "ERROR", "reason": str(e)}
                                print(" Ja-ERR", end="")
                            try:
                                judge_b_result = call_judge("judge_b", judge_prompt)
                                print(" Jb", end="")
                            except Exception as e:
                                judge_b_result = {"score": "ERROR", "reason": str(e)}
                                print(" Jb-ERR", end="")

                        results.append({
                            "rule_id": rule_id, "rule_name": rule_name, "prompt_id": prompt_id,
                            "prompt_type": prompt["type"], "user_prompt": user_prompt,
                            "model": model_key, "model_display": MODELS[model_key]["display"],
                            "condition": condition, "output": output,
                            "judge_a_score": judge_a_result["score"], "judge_a_reason": judge_a_result["reason"],
                            "judge_b_score": judge_b_result["score"], "judge_b_reason": judge_b_result["reason"],
                            "judges_agree": judge_a_result["score"] == judge_b_result["score"],
                        })
                        print(" [OK]")
                    except Exception as e:
                        print(f" FAILED: {e}")
                        results.append({
                            "rule_id": rule_id, "rule_name": rule_name, "prompt_id": prompt_id,
                            "prompt_type": prompt["type"], "user_prompt": user_prompt,
                            "model": model_key, "model_display": MODELS[model_key]["display"],
                            "condition": condition, "output": "", "error": str(e),
                            "judge_a_score": "ERROR", "judge_b_score": "ERROR", "judges_agree": False,
                        })

    results_path = run_dir / "scores.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n\nResults saved to {results_path}")
    generate_report(run_dir, results, smoke_test)


def generate_report(run_dir: Path, results: list, smoke_test: bool):
    report_path = run_dir / "REPORT.md"
    by_model, by_rule, disagreements = {}, {}, []
    score_to_num = {"3": 3, "2": 2, "1": 1, "0": 0, "N/A": None, "ERROR": None, "PARSE_ERROR": None, "SKIPPED": None}

    for r in results:
        if "error" in r:
            continue
        sa, sb = score_to_num.get(r["judge_a_score"]), score_to_num.get(r["judge_b_score"])
        final = None
        if sa is not None and sb is not None:
            if sa == sb:
                final = sa
            else:
                final = (sa + sb) / 2
                disagreements.append(r)
        by_model.setdefault((r["model_display"], r["condition"]), []).append(final)
        by_rule.setdefault((r["rule_id"], r["model_display"], r["condition"]), []).append(final)

    def adherence(scores):
        valid = [s for s in scores if s is not None]
        return sum(valid) / (3 * len(valid)) * 100 if valid else None

    lines = [
        "# Loka Eval Suite — Run Report\n",
        f"**Timestamp:** {run_dir.name}\n",
        f"**Smoke test:** {smoke_test}\n",
        f"**Total runs:** {len(results)}\n",
        f"**Errored runs:** {sum(1 for r in results if 'error' in r)}\n",
        f"**Judge disagreements:** {len(disagreements)}\n\n",
    ]
    if smoke_test:
        lines.append("WARNING: SMOKE TEST RUN — judges skipped, no scoring.\n\n")

    lines.append("## Adherence By Model & Condition\n\n| Model | Condition | Adherence % |\n|---|---|---|\n")
    for (model, cond), scores in sorted(by_model.items()):
        adh = adherence(scores)
        lines.append(f"| {model} | {cond} | {f'{adh:.1f}%' if adh is not None else 'N/A'} |\n")

    lines.append("\n## Adherence By Rule, Model, Condition\n\n| Rule | Model | Condition | Adherence % |\n|---|---|---|---|\n")
    for (rule_id, model, cond), scores in sorted(by_rule.items()):
        adh = adherence(scores)
        lines.append(f"| {rule_id} | {model} | {cond} | {f'{adh:.1f}%' if adh is not None else 'N/A'} |\n")

    lines.append("\n## Condition Difference (with_loka - baseline)\n\nThis is a descriptive difference from this run, not evidence that Loka caused an improvement.\n\n")
    lines.append("| Rule | Model | Baseline % | With Loka % | Delta |\n|---|---|---|---|---|\n")
    rule_ids = sorted(set(r[0] for r in by_rule.keys()))
    models = sorted(set(r[1] for r in by_rule.keys()))
    for rule_id in rule_ids:
        for model in models:
            base_adh = adherence(by_rule.get((rule_id, model, "baseline"), []))
            loka_adh = adherence(by_rule.get((rule_id, model, "with_loka"), []))
            if base_adh is not None and loka_adh is not None:
                lines.append(f"| {rule_id} | {model} | {base_adh:.1f}% | {loka_adh:.1f}% | {loka_adh - base_adh:+.1f} |\n")

    lines.append(f"\n## Cases Requiring Human Review ({len(disagreements)})\n\n")
    if disagreements:
        for d in disagreements[:20]:
            lines.append(f"- **{d['rule_id']} {d['prompt_id']} {d['model']} {d['condition']}** — Judge A: {d['judge_a_score']}, Judge B: {d['judge_b_score']}\n")
        if len(disagreements) > 20:
            lines.append(f"\n... plus {len(disagreements) - 20} more in scores.json\n")

    lines.append("\n## Caveats\n\n")
    lines.append("- 5 prompts per rule = +/-10% confidence interval\n")
    lines.append("- Judge bias: Claude-family + GPT-family judges; residual bias possible\n")
    lines.append("- Single-prompt scope, not long-session drift\n")
    lines.append("- LokaV11 Lite only; V10/V12/V13 not tested\n")
    lines.append("- Prompts are JS/TS/Python heavy; other ecosystems may differ\n")
    lines.append("- All calls routed through one Abacus account (RouteLLM) rather than\n"
                  "  six separate provider APIs — exact model builds served by RouteLLM\n"
                  "  may differ subtly from the original methodology's specific version\n"
                  "  pins; see the MODELS dict at the top of run_eval.py for what was\n"
                  "  actually used in this run.\n")
    lines.append("\n---\n*Generated by Loka Eval Suite v1.0 (Abacus single-account edition)*\n")

    report_path.write_text("".join(lines))
    print(f"Report saved to {report_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--calibrate", action="store_true")
    parser.add_argument("--list-models", action="store_true")
    parser.add_argument("--models", default="all")
    parser.add_argument("--condition", default="both", choices=["baseline", "with_loka", "both"])
    parser.add_argument("--smoke-test", action="store_true")
    args = parser.parse_args()

    if not ABACUS_API_KEY:
        sys.exit("Set ABACUS_API_KEY first.")

    if args.calibrate:
        calibrate()
        return
    if args.list_models:
        list_models()
        return

    _check_models_filled()

    if args.models == "all":
        model_keys = list(MODELS.keys())
    elif args.models == "closed":
        model_keys = [k for k, v in MODELS.items() if v["type"] == "closed"]
    elif args.models == "open":
        model_keys = [k for k, v in MODELS.items() if v["type"] == "open"]
    else:
        model_keys = args.models.split(",")
        for k in model_keys:
            if k not in MODELS:
                sys.exit(f"Unknown model key: {k}. Valid: {list(MODELS.keys())}")

    conditions = ["baseline", "with_loka"] if args.condition == "both" else [args.condition]
    run_full_eval(model_keys, conditions, smoke_test=args.smoke_test)


if __name__ == "__main__":
    main()
