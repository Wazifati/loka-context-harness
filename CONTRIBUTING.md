# Contributing to Loka

Thank you for improving Loka. This project is a family of distinct
context-engineered frameworks, not one monolithic prompt. Preserve that shape:
ACE, V10, V11, V12 Supervised, V12 Autonomous Edition, and V13 have different
jobs. Read [`LOKA_ROOT.md`](LOKA_ROOT.md) and [`LOKA_INDEX.md`](LOKA_INDEX.md)
before proposing a change.

## Good ways to contribute

You do not need to be a programmer. Useful contributions include:

- a redacted real-world example showing when one route helped or confused you;
- a compatibility report for an Agent host, chat service, Skill convention, or
  plugin format;
- a documentation correction, translation, clearer route explanation, or
  accessibility improvement;
- a reproducible bug in a distributed Skill, Meta Prompt, link, or plugin
  mirror;
- a carefully scoped adapter for a supported Agent environment;
- a proposed example or template that preserves the route map and labels its
  assumptions.

Use Discussions for questions, examples, compatibility reports, and proposals.
Use Issues for reproducible defects. Do not open placeholder “good first issue”
reports: a starter contribution should solve a real, narrow problem.

## Before you open a pull request

- Keep the original V10–V13 structure intact. Do not merge different routes
  into a single default prompt.
- Add Agent Skills as valid `SKILL.md` packages with clear triggers and scope.
- Preserve original source materials. Label new adapters and editions clearly.
- Do not submit secrets, private repositories, private tool output, or unsafe
  instructions embedded in external content.
- Credit every external contribution or influence and comply with its licence.
- For an effectiveness claim, include a reproducible methodology, exact
  configuration, and appropriately qualified findings. Do not alter an
  evaluated prompt set after publishing results; publish a new version instead.

## Portable plugin synchronization

`agent-skills/` and `meta-prompts/` are the canonical editable sources. The
portable plugin intentionally mirrors them so it can be installed alone.
Before opening a pull request, run:

```bash
python tools/sync_portable_plugin.py --check
```

Run the command without `--check` to refresh the mirror. CI rejects drift.

## Review standard

A strong contribution makes a specific route easier to understand or use
without inventing unverified capabilities, flattening the version map, or
turning a personal preference into a universal rule. The pull request template
includes the checks reviewers will use.
