# Loka Context Harness Agent Plugin

A portable bundle of the original Loka family in Agent Skill and Meta Prompt
form. Start with `skills/loka-router/` so the Agent selects the correct
version-specific framework. Do not treat this bundle as a single mega prompt.

The bundle contains ACE, V10, V11, V12 Supervised, V12 Autonomous Edition, V13,
Guard, Build, and the Failures reference. For repository work, start Guard
before V11 and use Build for understood implementation work. V12 editions are
V11 overlays; V10, V11, and V13 remain separate environment-specific
frameworks.

Map this directory into the target Agent platform's plugin/instruction-package
format. No particular model, API, tool, or provider is required.
