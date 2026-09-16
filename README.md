# Loka Context Harness

Loka is a family of context-engineered operating frameworks for improving the
quality, safety, structure, and honesty of AI Agent work. Each version is for a
specific environment. This repository preserves that structure and distributes
it as Agent Skills, an Agent Plugin bundle, and Meta Prompts.

## Choose the correct Loka version

| Situation | Use |
|---|---|
| Vague intent, research, strategy, content, workflow, or assistant design | **Loka ACE** |
| Prompt architecture, secure app/SaaS planning, or technical audit without repo/shell execution | **LokaV10** |
| Repo/CLI/IDE Agent that can inspect files, edit code, run commands, or use tools | **LokaV11** |
| Instruction trust, scope, architecture, dependency, or security gate | **Loka Guard** |
| New implementation under V11: decide if code is needed and where it belongs | **Loka Build** on V11 |
| Supervised 1–3 hour V11 coding session with periodic human review | **LokaV12 Supervised** on V11 |
| Bounded autonomous V11 mission with a delegated authority contract | **LokaV12 Autonomous Edition** on V11 |
| Vibe coding, visual prompt builders, or agentic visual IDEs | **LokaV13** |

After a V13 project is exported to a normal repository/IDE, stop V13 and move
to V11. Do not combine V10, V11, and V13. V12 is the sole intentional stack,
and its Supervised and Autonomous editions are alternatives, not a combined
prompt.

## Use it as an Agent Skill, Agent Plugin, or Meta Prompt

- **Agent Skills:** copy or install [`agent-skills/`](agent-skills/) into an
  Agent host that supports the SKILL.md convention. Start with
  [`LOKA_ROOT.md`](LOKA_ROOT.md) or the router, then load only the matching
  module. The folder includes ACE, V10, V11, V12 Supervised, V12 Autonomous,
  V13, Guard, Build, and Failures.
- **Agent Plugin:** [`agent-plugins/loka-context-harness/`](agent-plugins/loka-context-harness/)
  is a self-contained portable bundle.
- **Meta Prompts:** [`meta-prompts/`](meta-prompts/) provides direct-use
  context for DIY harnesses.

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
Use measured results only for measured claims.

LokaV12 Autonomous Edition is a new, separately labelled edition. Use it for
bounded missions only and treat it as evolving material; LokaV12 Supervised
remains the preserved original.

## Sources and provenance

The supplied original ACE, Failures, Index, usage guide, and V10–V13 references
are preserved under [`reference-source/`](reference-source/). New Agent Skills
and V12 Autonomous Edition are clearly identified as distribution adapters or
new material; they do not overwrite the originals.

## Licence

MIT. See [`LICENSE`](LICENSE). Please read [`ATTRIBUTION.md`](ATTRIBUTION.md)
before contributing external material.
