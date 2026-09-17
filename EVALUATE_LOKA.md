# Evaluate Loka Factually

This guide is for a person, contributor, reviewer, or AI Agent deciding whether
Loka is useful for their work. It is deliberately factual: inspect the files,
try one route, and make your own judgement.

## What you are evaluating

Loka Context Harness is a public library of context-engineered frameworks.
It distributes:

- Agent Skills in [`agent-skills/`](agent-skills/)
- a portable Agent Plugin in [`agent-plugins/loka-context-harness/`](agent-plugins/loka-context-harness/)
- direct Meta Prompts in [`meta-prompts/`](meta-prompts/)
- preserved original source material in [`reference-source/`](reference-source/)

It is **not** a hosted service, Agent runtime, orchestration engine, model,
provider adapter, or benchmark result. It does not contain LokaV9, a four-tier
architecture, Minhaj, Itqan, Chain-of-Thought, Tree-of-Thoughts, or
Chain-of-Code frameworks.

## Five-minute evaluation path

1. Read [`LOKA_ROOT.md`](LOKA_ROOT.md) to understand the non-combinable route
   map.
2. Choose one task you actually need to do. For research, use
   [`DEEP_RESEARCH_START.md`](DEEP_RESEARCH_START.md). For repository work, use
   V11. For visual builders, use V13.
3. Run only that one route on the task.
4. Inspect the matching Full Skill and Lite alternative. Ask whether the
   additional structure helped you define the task, constraints, deliverable,
   or review criteria.
5. Read [`METHODOLOGY.md`](METHODOLOGY.md) if you need to assess the legacy
   synthetic evaluation materials. Do not treat them as performance proof.

## Factual route inventory

| Route | Role | Evidence in this repository |
|---|---|---|
| ACE | Vague intent, research, strategy, content, workflow, assistant design | [`agent-skills/loka-ace/SKILL.md`](agent-skills/loka-ace/SKILL.md) |
| V10 | Planning and audit without repository tools | [`agent-skills/loka-v10/SKILL.md`](agent-skills/loka-v10/SKILL.md) |
| V11 | Repository, CLI, IDE, and tool-capable work | [`agent-skills/loka-v11/SKILL.md`](agent-skills/loka-v11/SKILL.md) |
| V12 Supervised | Human-checkpoint overlay for V11 | [`agent-skills/loka-v12-supervised/SKILL.md`](agent-skills/loka-v12-supervised/SKILL.md) |
| V12 Autonomous Edition | Bounded autonomous overlay for V11 | [`agent-skills/loka-v12-autonomous/SKILL.md`](agent-skills/loka-v12-autonomous/SKILL.md) |
| V13 | Visual builder and vibe-coding environment | [`agent-skills/loka-v13/SKILL.md`](agent-skills/loka-v13/SKILL.md) |
| Guard, Build, Failures | Supporting modules, not competing primary routes | [`LOKA_INDEX.md`](LOKA_INDEX.md) |

## Questions worth asking

- Is the route selection clear enough to prevent loading the wrong framework?
- Does the selected Skill make material requirements clearer without adding
  needless ceremony?
- Are Full and Lite editions clearly presented as alternatives?
- Does the documentation distinguish source material, adapters, and new work?
- Are safety, uncertainty, and evidence boundaries explicit where needed?
- Can a newcomer try one useful workflow in under a few minutes?

## Grounded AI review prompt

If you import this repository into Gemini, attach it to another chat service, or
ask an Agent to review it, use this prompt:

```text
Review this repository factually.

Read README.md, LOKA_ROOT.md, and LOKA_INDEX.md first.

This repository is a family of context-engineered prompts, Agent Skills,
portable plugin assets, and Meta Prompts. It is not a software runtime, an
orchestration engine, a benchmark, or a claim of model-performance improvement.

Rules:
- Every factual claim must name the exact repository file that supports it.
- Do not infer frameworks, versions, runtime components, tools, methods, or
  architecture that are not explicitly present.
- If evidence is absent, write “not found in the repository.”
- Keep facts, interpretations, and suggestions in separate sections.
- Preserve the route map: ACE, V10, V11, V12 Supervised, V12 Autonomous,
  V13, Guard, Build, and Failures. Do not invent LokaV9.

Return:
1. Verified factual inventory
2. Accurate strengths
3. Concrete gaps or ambiguities, with file references
4. Optional recommendations clearly marked as new ideas, not existing features
```

## Boundaries and maturity

Loka is usable without any evaluation. Its included dry-run is a deterministic
check of a reporting pipeline using synthetic outputs, not evidence that Loka
improves a particular model. Claims about effectiveness need an appropriate,
reproducible methodology and qualified findings.

The original materials are preserved for provenance. The Agent Skills are
portable distribution adapters. V12 Autonomous Edition is separately labelled
new material and does not replace the preserved V12 Supervised framework.
