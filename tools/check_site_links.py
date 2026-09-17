#!/usr/bin/env python3
"""Verify and pin Loka repository links embedded in the GitHub Pages source."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_INDEX = ROOT / "site" / "index.html"
REPO_URL = "https://github.com/Wazifati/loka-context-harness"
LINK_RE = re.compile(
    rf"{re.escape(REPO_URL)}/(?P<kind>blob|tree)/(?P<revision>[^/\"']+)/(?P<path>[^\"'#?]+)"
)


def links_to_check(content: str) -> list[tuple[str, str, str]]:
    return [
        (match.group("kind"), match.group("revision"), match.group("path"))
        for match in LINK_RE.finditer(content)
    ]


def verify_paths(content: str) -> list[str]:
    missing: list[str] = []
    for _, _, relative_path in links_to_check(content):
        if not (ROOT / relative_path).exists():
            missing.append(relative_path)
    return sorted(set(missing))


def pin_revision(content: str, revision: str) -> str:
    return LINK_RE.sub(
        lambda match: f"{REPO_URL}/{match.group('kind')}/{revision}/{match.group('path')}",
        content,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pin-revision", metavar="SHA", help="replace internal GitHub main links with SHA")
    args = parser.parse_args()

    content = SITE_INDEX.read_text()
    missing = verify_paths(content)
    if missing:
        print("Published site links target paths absent from this revision:")
        print("\n".join(f"- {path}" for path in missing))
        return 1

    if args.pin_revision:
        if not re.fullmatch(r"[0-9a-f]{40}", args.pin_revision):
            parser.error("--pin-revision must be a 40-character commit SHA")
        SITE_INDEX.write_text(pin_revision(content, args.pin_revision))
        print(f"Verified and pinned {len(links_to_check(content))} internal repository links to {args.pin_revision}.")
    else:
        print(f"Verified {len(links_to_check(content))} internal repository links against this revision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
