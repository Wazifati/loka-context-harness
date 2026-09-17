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

Read and follow this chat-agent guide:
https://raw.githubusercontent.com/Wazifati/loka-context-harness/main/CHAT_START_HERE.md

Do not browse a GitHub directory or repository listing. The guide contains the
exact direct raw URL for each route. Fetch only the matching Skill or Lite
prompt; it is sufficient for normal use. State the route in one sentence, then
do the task.
```

## Option 2: the Agent cannot open links

1. Open [`CHAT_START_HERE.md`](CHAT_START_HERE.md) in this repository.
2. Copy it into your chat, followed by your task.
3. Paste only the selected `SKILL.md` or Lite prompt if the Agent cannot fetch
   its direct raw URL.
4. A preserved PDF is optional source material; attach it only when you or the
   Agent explicitly needs the original text.

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

## Want the shortest copy-paste form?

Choose the matching **Lite** edition from [`meta-prompts/`](meta-prompts/). Lite
means the compact original or companion for the same environment, not a different
route. Do not load a Full prompt and its Lite form together. Use
[`LOKA_INDEX.md`](LOKA_INDEX.md) if you are deciding between supervised V12 Lite
and the separate Autonomous Edition Lite.
