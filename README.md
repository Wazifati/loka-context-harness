# Loka Context Harness

![A human researcher and an Agent working together](assets/loka-human-agent-research.png)

> **Clear context for AI work that matters.**
>
> Loka is a library of context-engineered frameworks that helps an Agent turn an
> under-specified task into clear, bounded, useful work. Use one matching route
> as an Agent Skill, a portable Agent Plugin, or a copy-paste Meta Prompt.

Loka is **not** an Agent runtime, a model benchmark, an orchestration engine,
or a claim that a prompt makes any model smarter. It is a practical set of
instructions for making objectives, process, constraints, deliverables, and
quality criteria explicit.

## Try it in 60 seconds: Deep Research

You do not need code, an API key, a VPS, or a plugin install to try Loka.
Paste this into a chat Agent that can open public raw links:

```text
Use this Loka Deep Research protocol as your operating instructions:
https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/DEEP_RESEARCH_START.md

My research task: [write your question here]
```

The single-file protocol uses **Loka ACE Research Context**. It tells the Agent
what to clarify, how to distinguish evidence from assumptions, and how to
return a decision-ready report. It cannot give a chat service browsing or file
access it does not already have.

![Loka and her Agent collaborator comparing research evidence](assets/loka-deep-research.png)

- **Gemini:** on Gemini web, choose **Add file → More uploads → Import code**,
  paste this repository URL, then start a chat. A pasted GitHub URL alone is
  not a reliable import. See [Gemini use](docs/USE_WITH_GEMINI.md).
- **A chat Agent that cannot open links:** download and attach just
  [`DEEP_RESEARCH_START.md`](DEEP_RESEARCH_START.md), then state the task.
- **An Agent host with Skills or Plugins:** start with the route map below.

## What Loka is and is not

| Loka is | Loka is not |
|---|---|
| A family of environment-specific context-engineering frameworks | A hosted app, model, runtime, or orchestration engine |
| Agent Skills, a portable plugin bundle, and direct Meta Prompts | A promise that prompts improve every model or task |
| A way to make a task's aim, process, constraints, output, and evaluation explicit | A single giant prompt to load everywhere |
| Original Full and Lite materials preserved with new Agent-ready adapters | A replacement for host safety rules, tools, or human judgment |

## Choose one route

Start with the environment, not the most elaborate prompt. Load one Full or
Lite route, then add an overlay only where the map explicitly permits it.

| Your situation | Choose | What it gives you |
|---|---|---|
| Vague idea, deep research, strategy, content, workflow, or assistant design | **Loka ACE** or **ACE Lite** | ACE-6 context: Aim, Character, Execution, Constraints, Export, Evaluation |
| Planning, prompt architecture, secure app/SaaS planning, or technical audit without repository tools | **LokaV10** or **V10 Lite** | A planning and audit framework for non-repository work |
| Repository, CLI, IDE, files, shell, or coding tools | **LokaV11** or **V11 Lite** | Evidence-aware, minimal-change repository work |
| Risk, scope, instruction trust, architecture, dependency, or security boundary | **Loka Guard** | A supporting gate for tool-capable work |
| Understood V11 implementation | **Loka Build** on V11 | Smallest sufficient, architecture-aware implementation |
| Supervised 1–3 hour V11 coding session | **LokaV12 Supervised** on V11 | Periodic human-review checkpoints |
| Explicitly bounded autonomous V11 mission | **LokaV12 Autonomous Edition** on V11 | Delegated authority, recoverability, and evidence handoffs |
| Vibe coding or visual prompt builders | **LokaV13** or **V13 Lite** | A visual-builder route; move to V11 after export to a normal repo/IDE |

Do not combine V10, V11, and V13. Full and Lite are alternatives. V12 is the
sole designed overlay, and its Supervised and Autonomous editions are
alternatives, not a combined prompt. See the complete
[route map](LOKA_INDEX.md).

## See the approach before you adopt it

A vague request such as “research whether this product idea is worth pursuing”
usually leaves the Agent guessing the audience, decision, evidence standard,
constraints, output, and definition of success.

Loka ACE makes those elements explicit. The result is a brief that asks for a
specific decision, sources and uncertainty labels, competing explanations,
risks, and next validation steps. Read the complete example in
[Deep Research Start](DEEP_RESEARCH_START.md).

This is a framework for better task definition, not proof of a particular model
performance outcome. Evaluate it using an actual task and the transparent
[evaluator guide](EVALUATE_LOKA.md).

## Use it in your environment

- **Agent Skills:** copy or install [`agent-skills/`](agent-skills/) into a host
  that supports the `SKILL.md` convention. Start with [`LOKA_ROOT.md`](LOKA_ROOT.md)
  or [`agent-skills/loka-router/SKILL.md`](agent-skills/loka-router/SKILL.md),
  then load the single matching module.
- **Agent Plugin:** [`agent-plugins/loka-context-harness/`](agent-plugins/loka-context-harness/)
  is a self-contained portable bundle. Its Skill and Meta Prompt mirrors are
  checked in CI to prevent drift.
- **Meta Prompts:** [`meta-prompts/`](meta-prompts/) contains direct-use prompts
  for chat sessions and DIY harnesses.
- **Chat-only Agents:** use [`CHAT_START_HERE.md`](CHAT_START_HERE.md), which
  supplies direct raw URLs rather than asking the Agent to browse directories.

Loka is Agent-neutral and can be adapted to OpenClaw, Hermes, Claude, GPT,
Gemini, local models, or another Agent platform.

## Evaluate before you install

Want to inspect Loka rather than trust marketing? Start with
[`EVALUATE_LOKA.md`](EVALUATE_LOKA.md). It provides a factual inventory, a
five-minute evaluation path, and a grounded-review prompt for AI reviewers.

![Loka and her Agent collaborator evaluating a project before adoption](assets/loka-factual-evaluation.png)

The included synthetic dry-run verifies an evaluation workflow only. It is not
model-performance evidence. Read [`METHODOLOGY.md`](METHODOLOGY.md) for the
boundary and [`RUN_THIS_ON_VPS.md`](RUN_THIS_ON_VPS.md) only if you want to
inspect that legacy runner.

## Contribute

Useful contributions include improved examples, compatibility reports,
translations, documentation corrections, reproducible distribution bugs, and
carefully scoped new adapters. Preserve original source materials, keep routes
distinct, credit external work, and do not make effectiveness claims without a
reproducible methodology. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Sources and provenance

The supplied original Full and Lite ACE, Failures, Index, usage guide, and
V10–V13 references are preserved under [`reference-source/`](reference-source/).
New Agent Skills and the V12 Autonomous Edition are clearly labelled adapters
or new material; they do not overwrite the originals.

## License

MIT. See [`LICENSE`](LICENSE), [`ATTRIBUTION.md`](ATTRIBUTION.md),
[`SECURITY.md`](SECURITY.md), and [`SUPPORT.md`](SUPPORT.md).
