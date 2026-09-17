# Loka Start Here for Chat Agents

Use this guide when the Agent can fetch individual public raw files but cannot
browse a GitHub directory or install a plugin.

## Rules

1. Do **not** browse a repository tree, directory listing, or plugin catalog.
2. Choose the first matching route below and fetch **only that direct raw URL**.
3. The selected Agent Skill is sufficient for normal use. Do not ask for a
   preserved reference PDF unless the user specifically asks to inspect the
   original source or the task genuinely needs it.
4. State the selected route in one sentence, then perform the task. Do not
   merge V10, V11, and V13.
5. Host platform policies and the user’s current instructions outrank Loka.

## Direct route map

- Vague idea, research, strategy, content, workflow, or assistant design:
  [Loka ACE](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-ace/SKILL.md)
- Planning, prompt architecture, implementation planning, or audit without
  repository/shell execution: [LokaV10](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v10/SKILL.md)
- Repository, CLI, IDE, files, shell, or coding tools:
  [LokaV11](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v11/SKILL.md). For risk boundaries first
  fetch [Loka Guard](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-guard/SKILL.md); for understood
  implementation fetch [Loka Build](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-build/SKILL.md).
- Supervised 1–3 hour V11 session with human checkpoints: fetch
  [LokaV11](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v11/SKILL.md) then
  [LokaV12 Supervised](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v12-supervised/SKILL.md).
- Explicitly bounded autonomous V11 mission: fetch
  [LokaV11](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v11/SKILL.md) then
  [LokaV12 Autonomous Edition](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v12-autonomous/SKILL.md).
- Vibe coding, visual prompt builders, or visual-agent IDEs:
  [LokaV13](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/agent-skills/loka-v13/SKILL.md). After export to a normal
  repository/IDE, stop V13 and switch to V11.

## Compact chat editions

If the user asks for a short copy-paste prompt or has limited context, use the
matching Lite form instead of the Full form:

- [ACE Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_ACE_LITE.md)
- [V10 Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_V10_LITE.md)
- [V11 Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_V11_LITE.md)
- [V12 Supervised Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_V12_LITE.md), only on V11/V11 Lite
- [V12 Autonomous Edition Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_V12_AUTONOMOUS_LITE.md), only on V11/V11 Lite
- [V13 Lite](https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/meta-prompts/LOKA_V13_LITE.md)

Full and Lite are alternatives; do not load both. V12 Supervised and V12
Autonomous Edition are alternatives; do not load both.
