# Loka Context Harness

Loka is a family of context-engineered operating frameworks for improving the
quality, safety, structure, and honesty of AI Agent work. Each version is for a
specific environment. This repository preserves that structure and distributes
it as Agent Skills, an Agent Plugin bundle, and Meta Prompts. See the
[complete Loka Index](LOKA_INDEX.md) for Full, Lite, and overlay mapping.

## Start here — no code required

Use Loka selectively. A quick factual question or casual chat does not need it;
choose a matching Lite edition when you want more structure without a long
prompt, and use a Full edition only when the task genuinely needs its process.

Loka is not an app or a service. For ordinary chat use, a person does **not**
need to install anything. Paste the block below into an Agent, replace the task
placeholder, and let the Agent read the public files.

```text
Use Loka Context Harness for this task:

[PASTE MY TASK HERE]

Read these files in order:
1. https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/LOKA_ROOT.md
2. https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-router/SKILL.md
3. The one matching Skill under https://github.com/Wazifati/loka-context-harness/tree/main/agent-skills

If the selected Skill points to a reference source, retrieve that matching file
from the same repository. Do not merge V10, V11, and V13. Tell me which Loka
route you selected in one sentence, then do the task.
```

If the Agent cannot open GitHub links, open [`LOKA_ROOT.md`](LOKA_ROOT.md) and
[`loka-router/SKILL.md`](agent-skills/loka-router/SKILL.md) in a browser, copy
both into the chat, then attach or paste the one selected Skill. Attach the
matching source PDF when the selected Skill requests it. You never need to
paste the whole repository.

For a more guided version, see [`QUICKSTART.md`](QUICKSTART.md).

## Choose the correct Loka version

| Situation | Use |
|---|---|
| Vague intent, research, strategy, content, workflow, or assistant design | **Loka ACE** / **ACE Lite** for compact copy-paste use |
| Prompt architecture, secure app/SaaS planning, or technical audit without repo/shell execution | **LokaV10** / **V10 Lite** |
| Repo/CLI/IDE Agent that can inspect files, edit code, run commands, or use tools | **LokaV11** / **V11 Lite** |
| Instruction trust, scope, architecture, dependency, or security gate | **Loka Guard** |
| New implementation under V11: decide if code is needed and where it belongs | **Loka Build** on V11 |
| Supervised 1–3 hour V11 coding session with periodic human review | **LokaV12 Supervised** / **V12 Lite** on V11 |
| Bounded autonomous V11 mission with a delegated authority contract | **LokaV12 Autonomous Edition** / **Autonomous Edition Lite** on V11 |
| Vibe coding, visual prompt builders, or agentic visual IDEs | **LokaV13** / **V13 Lite** |

After a V13 project is exported to a normal repository/IDE, stop V13 and move
to V11. Do not combine V10, V11, and V13. V12 is the sole intentional stack,
and its Supervised and Autonomous editions are alternatives, not a combined
prompt.

## Full and Lite editions

Every primary Loka route has a Lite alternative: **ACE Lite, V10 Lite, V11
Lite, V12 Lite (Supervised), V12 Autonomous Edition Lite, and V13 Lite**.
Lite is the original compact, copy-paste edition for the **same environment** as
its Full counterpart. Select one: Full for the complete framework, Lite for a
short session or limited context. Never load Full and Lite together. V12 Lite is
the original **supervised** V12 overlay. **V12 Autonomous Edition Lite** is a
separate compact companion to the new autonomous edition. Guard, Build, and
Failures are supporting modules, not alternate environment frameworks, so they
do not have separate Lite forms. Direct-use Lite prompts are in
[`meta-prompts/`](meta-prompts/).

## Use it as an Agent Skill, Agent Plugin, or Meta Prompt

- **Agent Skills:** copy or install [`agent-skills/`](agent-skills/) into an
  Agent host that supports the SKILL.md convention. Start with
  [`LOKA_ROOT.md`](LOKA_ROOT.md) or the router, then load only the matching
  module. The folder includes Full and Lite ACE, V10, V11, V12 Supervised,
  V12 Autonomous, and V13 forms, plus Guard, Build, and Failures.
- **Agent Plugin:** [`agent-plugins/loka-context-harness/`](agent-plugins/loka-context-harness/)
  is a self-contained portable bundle.
- **Meta Prompts:** [`meta-prompts/`](meta-prompts/) provides direct-use
  context for DIY harnesses. `agent-skills/` and `meta-prompts/` are the
canonical sources; the portable Plugin mirrors them and is checked in CI to
prevent version drift.

The package is Agent-neutral and can be adapted to OpenClaw, Hermes, Claude,
GPT, local models, or another Agent platform. No evaluation, VPS, API,
subscription, or specific model is required to use it.

## V12 editions

**V12 Supervised** is the preserved original: a V11 overlay for 1–3 hour
sessions with a user available at checkpoints.

**V12 Autonomous Edition** is a separate second edition for capable Agents. It
uses a bounded mission contract, explicit delegated authority, adaptive
milestone checkpoints, recoverability, and concise evidence handoffs. It does
not replace the original supervised framework or authorize excluded actions.

## Evidence and maturity

Loka is usable without an evaluation. The included dry-run materials verify an
evaluation workflow on synthetic data; they are not performance evidence. This
repository makes no claim that Loka turns smaller models into frontier models.
Use measured results only for measured claims. Do not cite the included synthetic
dry-run report as evidence of effectiveness.

LokaV12 Autonomous Edition is a new, separately labelled edition. Use it for
bounded missions only and treat it as evolving material; LokaV12 Supervised
remains the preserved original.

## Sources and provenance

The supplied original Full and Lite ACE, Failures, Index, usage guide, and V10–V13
references are preserved under [`reference-source/`](reference-source/). New Agent Skills
and V12 Autonomous Edition are clearly identified as distribution adapters or
new material; they do not overwrite the originals.

## Licence

MIT. See [`LICENSE`](LICENSE). Please read [`ATTRIBUTION.md`](ATTRIBUTION.md)
before contributing external material.
