#!/usr/bin/env python3
"""Regression test: plugin mirror validation must reject an extra skill folder."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sync_portable_plugin", ROOT / "tools" / "sync_portable_plugin.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary)
        canonical = base / "canonical"
        plugin = base / "plugin"
        (canonical / "loka-ace").mkdir(parents=True)
        (plugin / "loka-ace").mkdir(parents=True)
        (plugin / "_stale").mkdir(parents=True)

        mismatches = MODULE.skill_directory_mismatches(canonical, plugin)
        expected = plugin / "_stale" / "SKILL.md"
        assert mismatches == [expected], mismatches

    print("Portable plugin mirror rejects an extra stale skill directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
