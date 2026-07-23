# Deep+Obsidian Workflow

Use this reference whenever the selected summary mode is `obsidian`.

## User Preference Encoded Here

For this local skill, an Obsidian note is not a lightweight reformat of a summary. It is:

```text
Deep evidence coverage
+ Obsidian knowledge structure
+ operator/action layer
```

The goal is to retain the fidelity of a Deep summary while making the note easier to retrieve, connect, and apply later.

## Three-Pass Method

### Pass 1: Evidence Ledger

Before drafting, identify:

- The central thesis in one sentence.
- Five to eight material claims.
- Every framework, sequence, model, or decision rule.
- Material numbers, thresholds, named cases, and counterexamples.
- Short original quote candidates.
- ASR conflicts, unsupported causal claims, and facts needing verification.
- Practical actions explicitly supported by the source.

Do not show the raw ledger unless useful, but use it as a coverage checklist.

### Pass 2: Deep Note

Write the note as if it first had to pass the Deep quality bar:

- Explain the background and main argument chain.
- Preserve cases and numbers that materially support the argument.
- Explain why the framework works, not only what its labels are.
- Keep evidence limitations near the affected claim.
- Include follow-up questions that would change a real decision.

### Pass 3: Obsidian And Operator Layer

Add only structures that improve later use:

- A compact YAML property set and tags following `obsidian-native-style.md`.
- A one-sentence summary callout.
- `[[backlink candidates]]` for reusable concepts.
- A Mermaid diagram when the source contains a real process, hierarchy, or causal system.
- A table when the content has repeated comparable fields, such as metrics, stages, cases, or decisions.
- Action checklist or experiment plan when the source supports action.
- “待验证问题” for uncertain claims and ASR conflicts.
- “我的思考” for Agent inference, clearly separated from source content.
- “可拆分的原子笔记” for concepts worth developing independently.

Do not force every optional module into every note. A reflective interview may need themes and questions but no KPI table; an operational marketing episode may benefit from metrics and an experiment plan.

For the user's local transcript library, do not generate HTML or custom `cssclasses`. Use native Markdown components and the user's existing Obsidian theme.

## Required Output Contract

Every Obsidian note must contain:

1. Valid YAML frontmatter.
2. Human-readable title.
3. Source metadata.
4. One-sentence summary.
5. Deep core content with material evidence.
6. At least one uncertainty/verification statement when the source is imperfect.
7. Tags and backlink candidates.
8. Short original quotes only when useful.
9. For local-library notes, omit `source_type`, `language`, `status`, `human_sop`, and `cssclasses`; do not repeat YAML metadata in a body section named “基本信息”.

For business, marketing, product, or operations content, also include when supported:

- Framework/process visualization.
- Metric or decision table.
- Concrete action plan or experiment.
- Operator implications.

## Recommended YAML

```yaml
---
title: "<clear note title>"
aliases:
  - "<short alias>"
source_file: "<source filename or URL>"
source_path: "<local source path if known>"
source_url: "<official source URL if known>"
podcast: "<podcast name if known>"
episode: "<episode title if known>"
guest: "<guest if known>"
duration: "<duration if known>"
transcript_segments: <number if known>
version: "<version if applicable>"
created: YYYY-MM-DD
tags:
  - <topic>
  - <topic>
---
```

Omit unknown properties rather than inventing them.

## Recommended Note Skeleton

```markdown
# <title>

> [!summary] 一句话摘要
> <central thesis>

> [!warning] 证据或转录提示
> <ASR ambiguity, missing context, or verification boundary>

## 背景与问题
<explain the context, why the problem matters, and the main argument setup>

## 核心判断
### 1. <claim>
<evidence and reasoning>

## <main framework>
<explanation, optional Mermaid>

## 重要案例与数字
<retain material Deep evidence>

## 指标 / 决策 / 对比
<optional table when useful>

## 可执行动作或实验
- [ ] <action>

## 待验证问题
1. <question>

## 短原话
> “<short quote>”

## 可拆分的原子笔记
- [[concept]]

## 关联主题
- [[topic]]

## 我的思考
- <Agent inference, not attributed to the source>
```

## Fidelity Versus Utility Gate

Before delivery, ask:

- Did this note preserve all material cases and numbers from the Deep evidence ledger?
- Are uncertain transcript details explicitly marked rather than silently corrected?
- Can a reader distinguish source claims from Agent inference?
- Does each diagram/table make a real relationship easier to understand?
- Are action items supported by the source or clearly labeled as extrapolation?
- Do backlinks represent reusable concepts instead of decorative tags?
- Is the note useful months later without reopening the transcript?

If the Obsidian note feels more actionable but has lost decisive evidence, restore the evidence. If it is faithful but hard to reuse, improve the organization rather than adding generic prose.

## Token And Format Gate

- Produce one canonical `.md`, not separate Deep, zine, and HTML versions.
- Do not embed CSS or a full HTML shell in the note.
- Do not add custom `cssclasses`; let the user's Obsidian theme control presentation.
- Keep source metadata in YAML and do not repeat it under “基本信息”.
- Use at most one Mermaid diagram and two tables by default.
