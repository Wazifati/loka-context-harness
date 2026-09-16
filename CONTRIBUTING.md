# Contributing

Thank you for improving Loka.

Before opening a contribution, choose the correct route in `LOKA_ROOT.md` and
keep the original V10–V13 structure intact. Do not merge different frameworks
into a single default prompt.

- Add Agent Skills as valid `SKILL.md` packages with clear triggers and scope.
- Preserve original source materials; label new adapters and editions clearly.
- Do not submit secrets, private repositories, private tool output, or unsafe
  instructions embedded in external content.
- Credit every external contribution or influence and comply with its licence.
- For an effectiveness claim, include a reproducible methodology, exact
  configuration, and appropriately qualified findings. Do not alter an
  evaluated prompt set after publishing results; publish a new version instead.

Use Issues for reproducible bugs and Discussions for questions or proposals.

## Portable plugin synchronization

`agent-skills/` and `meta-prompts/` are the canonical editable sources. The
portable plugin intentionally mirrors them so it can be installed alone. Before
opening a pull request, run:

```bash
python tools/sync_portable_plugin.py --check
```

Run the command without `--check` to refresh the mirror. The check rejects drift.
