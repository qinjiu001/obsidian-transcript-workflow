# Project Layout

Use this reference when changing the skill structure, explaining where files live, or debugging path assumptions.

## Layout

```text
podcast-bridge/
├── SKILL.md
├── ARCHITECTURE.md
├── library-workflow.json
├── references/
│   ├── transcription.md
│   ├── summarization.md
│   ├── obsidian-deep.md
│   ├── obsidian-native-style.md
│   ├── local-library-workflow.md
│   ├── rss-workflows.md
│   ├── troubleshooting.md
│   └── project-layout.md
├── scripts/
│   └── scan_transcript_queue.py
├── assets/
│   └── podcast-zine.css
├── agents/
│   └── openai.yaml
├── transcribe.py
├── config.json
├── subscriptions.json
├── podcast_library/
│   ├── library.sqlite3
│   └── transcripts/
└── podcast-bridge-feeds/
    ├── feeds/
    │   ├── ai.json
    │   ├── tech-business.json
    │   ├── humanities-society.json
    │   ├── culture-art.json
    │   └── health.json
    ├── resolve_feeds.py
    └── import_feeds.py
```

## Path Assumptions

The executable scripts currently live at the repository root and under `podcast-bridge-feeds/` to preserve relative paths used by existing commands.

Do not move `transcribe.py`, `podcast-bridge-feeds/resolve_feeds.py`, or `podcast-bridge-feeds/import_feeds.py` into `scripts/` unless you also update command examples, imports, working-directory assumptions, and any path logic in the code.

## Skill Packaging Notes

A strict skill package needs `SKILL.md`. `references/` is for detailed instructions loaded on demand. `agents/openai.yaml` is UI metadata. `scripts/` is useful for deterministic helper scripts, but this project already has operational scripts in established locations.

`ARCHITECTURE.md` is the human-readable explanation of how routing, runtime execution, data state, and summary generation fit together.

`library-workflow.json` stores this user's local source/target mapping and batch defaults; the current target root is `raw/02-papers`. `scan_transcript_queue.py` computes live completion state. `assets/podcast-zine.css` remains an optional legacy asset, but local-library notes do not use it or add YAML `cssclasses` by default.

`podcast_library/` and `subscriptions.json` are runtime state. They are useful in this local working skill, but should be excluded or reset for a clean distributable template if the skill is packaged for others.
