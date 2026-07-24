# Local Transcript Library Workflow

Use this workflow when the user asks to process local English podcast transcripts into readable Chinese Obsidian notes, mentions the Human SOP, asks to process a folder, or wants to continue the 300+ document backlog.

## Goal

Convert each source DOCX into one canonical Chinese Markdown article that is:

- Easier to read than a literal transcript.
- Faithful enough to preserve important arguments, cases, numbers, and uncertainty.
- Structured as Deep+Obsidian knowledge.
- Rendered by the user's existing Obsidian theme without generated HTML or custom CSS classes.
- Saved under a mirrored category path so source and output remain traceable.

## Local Configuration

Read `library-workflow.json` for the current source root, target root, filename suffix, and overwrite policy. Do not hardcode the Human SOP's old “309 files” count. Always run the live scanner.

```powershell
python -X utf8 scripts/scan_transcript_queue.py
```

Current default mapping:

```text
SOURCE_ROOT/<relative-folder>/<name>_原文.docx
    ->
<OBSIDIAN_VAULT>/raw/02-papers/<relative-folder>/<name>_Obsidian笔记.md
```

The scanner treats an existing exact note, a same-stem `.md`, or common Obsidian-note suffix variants as already done.

## Default Batch Policy

- Default batch size is 1 source file per task.
- Process 2–3 only when the user explicitly asks for a batch and the files are short enough to preserve quality.
- Never attempt the whole library in one model context.
- Skip completed targets unless the user explicitly asks to refresh or overwrite them.
- Stop when the scanner reports `pending: 0`.

## One-File Workflow

### Step 1: Select And Verify

1. Run the scanner.
2. Choose the first pending item or the exact file named by the user.
3. Confirm the source exists and the target does not, unless overwrite is authorized.
4. Preserve the source-relative folder structure under the target root.

### Step 2: Extract Once

Read the complete DOCX, including headings and tables when present. Do not create a separate raw extraction file unless needed for debugging.

If the source is already a transcript, do not run ASR again.

### Step 3: Convert Spoken English Into Readable Chinese

The target is a readable knowledge article, not a sentence-by-sentence translation and not merely a short summary.

- Remove greetings, repeated filler, false starts, verbal tics, sponsor/subscribe boilerplate, and obvious ASR noise unless meaningful.
- Reconstruct the argument in natural Chinese paragraphs.
- Preserve the speaker's actual position, examples, material numbers, counterexamples, and causal logic.
- Keep useful specialist terms in English on first use when that helps precision.
- Flag uncertain names or numbers; do not silently guess.
- Avoid turning every sentence into bullets. Use prose for reasoning and lists only for repeated items or actions.

### Step 4: Generate One Deep+Obsidian Note

Read `summarization.md`, `obsidian-deep.md`, and `obsidian-native-style.md`.

Create a single Markdown artifact. Do not first write a Deep file and then regenerate it through zine-skill.

The note should normally contain:

- Compact YAML with useful source fields and tags.
- One-sentence summary.
- Readable Chinese article body with Deep evidence coverage.
- Real frameworks/causal systems expressed as at most one useful Mermaid diagram.
- At most two tables by default; use them only for metrics, stages, cases, or decisions.
- Material cases and numbers.
- An action/experiment section when the content is operational.
- Uncertainty and verification notes.
- Backlinks and atomic-note candidates.
- Agent inference separated under “我的思考”.

For local-library YAML, do not generate `source_type`, `language`, `status`, `human_sop`, or `cssclasses`. Keep source, podcast, guest, duration, and transcript scale in YAML only. Do not create a body section named `## 基本信息`.

### Step 5: Save And Verify

1. Save UTF-8 Markdown to the mapped target path.
2. Verify YAML closes correctly, excludes the unwanted V03 properties, and the file has a title, summary, evidence, tags, and links.
3. Confirm no raw HTML document shell was generated.
4. Re-run the scanner and confirm the pending count decreased by one.
5. Report the source path, final note path, and new queue counts.

### Step 6: Write Back Agent Feedback

After every local-library run, append one execution-feedback entry under the current version in the iteration log configured by `library-workflow.json`.

The feedback entry must state:

- What changed and what was intentionally left unchanged.
- Verification results.
- The most time-consuming and error-prone steps.
- The largest token consumer.
- Missing rules and temporary assumptions.
- Questions or hidden knowledge that require human input.
- Whether each change remains an observation, passed human review, entered the Human SOP, synced to the Skill, and passed regression testing.

Do not silently promote an observation into the Human SOP or Skill. The human approves the target and stable rule; the Agent implements the approved rule and records the result.

For long documents, first try complete extraction and segmented processing. Stop and ask the human only when the source cannot be read completely or the available environment cannot preserve full evidence coverage.

## Low-Token Rules

- One canonical note, not Deep + zine + HTML duplicates.
- Use the user's existing Obsidian theme; do not add CSS or theme classes to each note.
- Do not reproduce the full transcript.
- Do not create decorative sections with no information value.
- Maximum one Mermaid diagram and two tables by default.
- Do not generate separate designer notes, HTML, or image prompts unless explicitly requested.
- Reuse the fixed Markdown structure from `obsidian-deep.md` instead of inventing a new layout every time.

## HTML Policy

HTML is off by default because it does not integrate cleanly with the user's Obsidian reading workflow and costs substantially more tokens.

Only generate zine HTML when the user explicitly asks for an external publishing/export artifact. In that case, use the completed Markdown as the canonical source and do not re-summarize the transcript.

## Completion Definition

A source is complete when:

- The mapped `.md` exists.
- It is readable Chinese rather than raw oral transcript.
- Deep evidence and uncertainty are retained.
- Obsidian YAML and links are present without the excluded V03 properties or a repeated “基本信息” section.
- The scanner reports it as done.

The overall backlog is complete only when a fresh scan reports zero pending items.
