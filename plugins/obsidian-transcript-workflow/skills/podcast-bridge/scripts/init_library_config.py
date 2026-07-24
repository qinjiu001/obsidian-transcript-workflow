#!/usr/bin/env python3
"""Initialize the per-user local transcript workflow configuration."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
EXAMPLE_CONFIG = SKILL_ROOT / "library-workflow.example.json"


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    return Path(configured).expanduser() if configured else Path.home() / ".codex"


def default_target() -> Path:
    return codex_home() / "obsidian-transcript-workflow" / "library-workflow.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="初始化本地文稿转写工作流配置")
    parser.add_argument("--target", type=Path, default=default_target())
    parser.add_argument("--force", action="store_true", help="覆盖已有配置")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    target = args.target.expanduser().resolve()
    if target.exists() and not args.force:
        print(f"配置已存在，未覆盖: {target}")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(EXAMPLE_CONFIG, target)
    print(f"已创建配置: {target}")
    print("请填写 source_root、target_root、human_sop 和 iteration_log 后再扫描队列。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
