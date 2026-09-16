# Loka Index

Loka is a family of environment-specific context-engineering frameworks. Start
with the environment, then choose **one** Full or Lite edition. Lite is the
compact original or companion prompt for the same route; it is not a second
framework to load alongside Full.

| Situation | Full / primary route | Lite route | Combination rule |
|---|---|---|---|
| Vague idea, research, strategy, content, workflow, or assistant design | [Loka ACE](agent-skills/loka-ace/SKILL.md) | [ACE Lite](agent-skills/loka-ace-lite/SKILL.md) | Choose one; hand off only if specialized work follows. |
| Planning, prompt architecture, implementation planning, or audit without repo/shell tools | [LokaV10](agent-skills/loka-v10/SKILL.md) | [V10 Lite](agent-skills/loka-v10-lite/SKILL.md) | Choose one; do not use for repository execution. |
| Repository, CLI, IDE, files, shell, or coding tools | [LokaV11](agent-skills/loka-v11/SKILL.md) | [V11 Lite](agent-skills/loka-v11-lite/SKILL.md) | Choose one. Guard and Build support this route. |
| Supervised V11 session, 1–3 hours, periodic human review | [V12 Supervised](agent-skills/loka-v12-supervised/SKILL.md) | [V12 Lite](agent-skills/loka-v12-lite/SKILL.md) | Overlay on V11 or V11 Lite only. |
| Explicitly bounded autonomous V11 mission | [V12 Autonomous Edition](agent-skills/loka-v12-autonomous/SKILL.md) | [V12 Autonomous Edition Lite](agent-skills/loka-v12-autonomous-lite/SKILL.md) | Overlay on V11 or V11 Lite only; distinct from supervised V12. |
| Vibe coding or a prompt-driven visual builder | [LokaV13](agent-skills/loka-v13/SKILL.md) | [V13 Lite](agent-skills/loka-v13-lite/SKILL.md) | Choose one; switch to V11 after export to a normal repo/IDE. |

## Supporting modules

- [Loka Guard](agent-skills/loka-guard/SKILL.md): instruction trust and gate communication.
- [Loka Build](agent-skills/loka-build/SKILL.md): smallest sufficient,
  architecture-aware implementation on V11.
- [Loka Failures](agent-skills/loka-failures/SKILL.md): relevant risk lens, not
  a competing execution route.

## Non-negotiable mapping rules

1. Do not combine V10, V11, and V13.
2. Do not combine a Full edition and its Lite edition.
3. V12 is the only intentional overlay, always on V11 or V11 Lite.
4. V12 Supervised and V12 Autonomous Edition are alternatives, never a combined prompt.
5. Host platform rules and explicit current user instructions always outrank Loka.

The supplied originals, including Lite source files, are preserved in
[`reference-source/`](reference-source/). For non-technical use, begin with
[`QUICKSTART.md`](QUICKSTART.md).
