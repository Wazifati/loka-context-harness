# Loka Meta Prompts

Use the original structure. Select one framework for the active environment;
do not merge all versions into a single mega prompt.

| Situation | Prompt or source |
|---|---|
| Vague intent, research, strategy, content, workflow | `LOKA_CONTEXT_HARNESS.md` / Loka ACE |
| App/prompt planning or audit without repo tools | Original LokaV10 in `reference-source/5-LokaV10.pdf` |
| Repository-capable build work | `LOKA_V11_LITE.md` / original V11 |
| Instruction trust or a gate failure during repository work | `agent-skills/loka-guard/SKILL.md` |
| New implementation under V11 | `agent-skills/loka-build/SKILL.md` |
| Supervised 1–3 hour V11 session | Original V12 in `reference-source/8-LokaV12.pdf` |
| Bounded autonomous V11 mission | `LOKA_V12_AUTONOMOUS_EDITION.md` |
| Vibe coding or visual builders | Original V13 in `reference-source/9-LokaV13-Full-v13_2.pdf` |

V12 Supervised and V12 Autonomous are distinct editions. Both load only on V11.
