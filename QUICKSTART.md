# Loka Quick Start

## The simple answer

You do not need to code, install a package, run an evaluation, or have a VPS to
use Loka. It is a set of instructions that an AI Agent can read before working
on your task.

## Option 1: paste one message into an Agent

This is the best starting point for ChatGPT, Claude, Gemini, OpenClaw, Hermes,
or another Agent that can open public links. Copy everything inside the box,
replace the placeholder, and send it.

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

## Option 2: the Agent cannot open links

1. Open [`LOKA_ROOT.md`](LOKA_ROOT.md) and
   [`loka-router/SKILL.md`](agent-skills/loka-router/SKILL.md) in this
   repository.
2. Copy both files into your chat, followed by your task.
3. When the Agent selects a route, attach or paste only that matching `SKILL.md`.
4. If that Skill points to a PDF under `reference-source/`, attach that one PDF.

Do not paste every version. Loka works best when the Agent receives the single
framework that matches the current environment.

## Option 3: install it for repeated use

If your Agent host supports the `SKILL.md` convention, install or copy the
[`agent-skills/`](agent-skills/) directory once. Start each new task by asking
the Agent to read `LOKA_ROOT.md` and route the task. The portable
[`agent-plugins/loka-context-harness/`](agent-plugins/loka-context-harness/)
bundle is for hosts that use plugin-style instruction packages.

## Choose by plain language

- “Help me turn an idea into a clear brief” → ACE.
- “Plan or audit an app; do not touch a repository” → V10.
- “Work in my repository, terminal, or IDE” → V11.
- “I want the Agent to create an app in a visual/vibe-coding builder” → V13.
- “This V11 job needs regular human checkpoints” → V12 Supervised.
- “This V11 job is explicitly delegated and bounded” → V12 Autonomous Edition.

For V11 work, Guard handles instruction trust and Build helps the Agent choose
the smallest suitable implementation. They support V11; they do not replace it.
