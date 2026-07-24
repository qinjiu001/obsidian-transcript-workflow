#!/usr/bin/env python3
"""Scan local transcript DOCX files and map them to expected Obsidian notes."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
LEGACY_CONFIG = SKILL_ROOT / "library-workflow.json"


def codex_home() -> Path:
    configured = os.environ.get("CODEX_HOME")
    return Path(configured).expanduser() if configured else Path.home() / ".codex"


def default_config() -> Path:
    user_config = codex_home() / "obsidian-transcript-workflow" / "library-workflow.json"
    return user_config if user_config.exists() or not LEGACY_CONFIG.exists() else LEGACY_CONFIG


def load_config(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(
            "配置不存在: "
            f"{path}\n请先运行 scripts/init_library_config.py，"
            "或使用 --config 指定配置文件。"
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ("source_root", "target_root")
    missing = [key for key in required if not data.get(key)]
    if missing:
        raise ValueError(f"配置缺少字段: {', '.join(missing)}")
    return data


def clean_stem(stem: str) -> str:
    for suffix in ("_原文", "-原文", " 原文"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)].rstrip(" _-")
    return stem


def candidate_outputs(target_dir: Path, stem: str, output_suffix: str) -> list[Path]:
    return [
        target_dir / f"{stem}{output_suffix}.md",
        target_dir / f"{stem}.md",
        target_dir / f"{stem}-Obsidian笔记.md",
        target_dir / f"{stem}_Obsidian笔记.md",
    ]


def scan(config: dict, create_folders: bool = False) -> list[dict]:
    source_root = Path(config["source_root"]).expanduser().resolve()
    target_root = Path(config["target_root"]).expanduser().resolve()
    output_suffix = str(config.get("output_suffix", "_Obsidian笔记"))
    mirror = bool(config.get("mirror_source_folders", True))

    if not source_root.is_dir():
        raise FileNotFoundError(f"源目录不存在: {source_root}")
    if create_folders:
        target_root.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for source in sorted(source_root.rglob("*.docx"), key=lambda p: str(p).lower()):
        relative = source.relative_to(source_root)
        relative_parent = relative.parent if mirror else Path()
        target_dir = target_root / relative_parent
        if create_folders:
            target_dir.mkdir(parents=True, exist_ok=True)
        stem = clean_stem(source.stem)
        candidates = candidate_outputs(target_dir, stem, output_suffix)
        existing = next((p for p in candidates if p.exists()), None)
        rows.append(
            {
                "status": "done" if existing else "pending",
                "source": str(source),
                "relative_source": str(relative),
                "target": str(existing or candidates[0]),
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="扫描 DOCX 文稿与 Obsidian 笔记处理队列")
    parser.add_argument("--config", type=Path, default=default_config())
    parser.add_argument("--limit", type=int, default=20, help="文本输出最多列出的 pending 数")
    parser.add_argument("--format", choices=("text", "json", "csv"), default="text")
    parser.add_argument("--create-folders", action="store_true", help="创建镜像目标文件夹")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    config = load_config(args.config.resolve())
    rows = scan(config, create_folders=args.create_folders)
    pending = [row for row in rows if row["status"] == "pending"]
    done = [row for row in rows if row["status"] == "done"]
    next_items = pending[: max(args.limit, 0)]

    if args.format == "json":
        print(json.dumps({"total": len(rows), "done": len(done), "pending": len(pending), "items": next_items}, ensure_ascii=False, indent=2))
    elif args.format == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=("status", "source", "relative_source", "target"))
        writer.writeheader()
        writer.writerows(next_items)
    else:
        print(f"总文稿: {len(rows)}")
        print(f"已完成: {len(done)}")
        print(f"待处理: {len(pending)}")
        if pending:
            print("\n下一批待处理:")
            for index, row in enumerate(next_items, start=1):
                print(f"{index}. {row['relative_source']}")
                print(f"   -> {row['target']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
