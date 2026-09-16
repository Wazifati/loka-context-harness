#!/usr/bin/env python3
"""Synchronize or verify the portable Agent Plugin mirrors canonical sources."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILLS = ROOT / "agent-skills"
PLUGIN_SKILLS = ROOT / "agent-plugins" / "loka-context-harness" / "skills"
CANONICAL_PROMPTS = ROOT / "meta-prompts"
PLUGIN_PROMPTS = ROOT / "agent-plugins" / "loka-context-harness" / "meta-prompts"
# This historical prompt is intentionally Plugin-only, so it is not a mirror.
PLUGIN_ONLY_PROMPTS = {"LOKA_SESSION_ADAPTIVE.md"}


def file_pairs() -> list[tuple[Path, Path]]:
    skills = [
        (source, PLUGIN_SKILLS / source.parent.name / "SKILL.md")
        for source in sorted(CANONICAL_SKILLS.glob("*/SKILL.md"))
    ]
    prompts = [
        (source, PLUGIN_PROMPTS / source.name)
        for source in sorted(CANONICAL_PROMPTS.glob("*.md"))
    ]
    return skills + prompts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()

    mismatches: list[Path] = []
    for source, target in file_pairs():
        if not target.exists() or source.read_bytes() != target.read_bytes():
            mismatches.append(target.relative_to(ROOT))
            if not args.check:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)

    expected_prompt_names = {source.name for source in CANONICAL_PROMPTS.glob("*.md")} | PLUGIN_ONLY_PROMPTS
    actual_prompt_names = {source.name for source in PLUGIN_PROMPTS.glob("*.md")}
    for name in sorted(expected_prompt_names ^ actual_prompt_names):
        mismatches.append((PLUGIN_PROMPTS / name).relative_to(ROOT))

    if mismatches and args.check:
        print("Portable plugin is out of sync:")
        print("\n".join(f"- {path}" for path in mismatches))
        print("Run: python tools/sync_portable_plugin.py")
        return 1

    action = "already matches" if not mismatches else "synchronized"
    print(f"Portable plugin {action} canonical Agent Skills and Meta Prompts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
