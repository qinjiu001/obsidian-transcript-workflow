# Summarization Workflow

Use this reference after transcription, or when the user provides an existing transcript/document and asks for a summary, takeaways, notes, Obsidian output, product insights, or investment analysis.

## Execution Boundary

`transcribe.py` creates transcripts and chapters. It does not reliably create the summary body. The current Agent must read the complete transcript and write the summary or note.

Never answer only with “transcription complete, I can summarize.” If the user requested a summary, include the summary body or create the requested `.md` file.

## Source Fidelity Gate

Apply this before every mode:

1. Read the complete source. If a long episode was split, read every part.
2. Build an internal evidence ledger containing the thesis, frameworks, material numbers, named cases, causal claims, short quote candidates, contradictions, and uncertainties.
3. Preserve important evidence. A formatted note must not silently drop the strongest examples or quantitative details that would appear in a good Deep summary.
4. Do not repair uncertain ASR facts by guessing. Flag unclear names, numbers, or causal attribution and recommend replay or verification.
5. Separate source content from Agent inference. Put extrapolations under labels such as “应用建议”“我的思考” or “待验证问题”.
6. Use short quotations only; do not reproduce long transcript passages.

## Mode Router

| Mode | Purpose | Required shape |
|---|---|---|
| `brief` | 快速判断这期是否值得深入 | 500–900 中文字；一句话主题 + 5–8 个具体信息点 + 收束判断。 |
| `deep` | 忠实、系统地理解原文 | Brief 基线 + 背景、主线、核心概念、重要数字和案例、短原话、行动启示、后续问题。 |
| `product` | 从产品和运营角度重组证据 | 用户需求、场景、痛点、产品/内容机会、可执行动作；仍需保留支撑这些判断的原文证据。 |
| `investment` | 从商业和投资角度重组证据 | 行业判断、供需变化、商业模式、竞争与风险、可验证信号；不得把访谈观点当成已证实事实。 |
| `obsidian` | 长期沉淀、连接和复用 | 默认等于 Deep 内容基线 + Obsidian 组织 + 可执行层；必须继续读取 `obsidian-deep.md`。 |

If the user asks for “deep + obsidian”, “Obsidian 知识库笔记”, “双链笔记”, or simply “Obsidian 版本”, route to `obsidian`.

## Default Brief Format

Use this when the user gives no style. Target 500–900 Chinese characters unless requested otherwise.

```text
<标题> — <时长> / <字数> / <段数>

一句话概括真正主题，不超过 80 字。

核心线索：
<关键词 1> — 2–4 句具体说明。
<关键词 2> — ...
<关键词 3> — ...
<关键词 4> — ...
<关键词 5> — ...

最后/最值得带走的判断 — 2–3 句收束。
```

## Deep Content Baseline

A good Deep summary must normally include:

- Source statistics and a one-sentence thesis.
- Five to eight concrete core points.
- Background/problem definition and the main argument chain.
- Frameworks and concepts in reusable language.
- Material cases, names, numbers, and counterexamples.
- ASR ambiguities or evidence limitations.
- A concise action list when the source supports action.
- Three to five follow-up or verification questions.

Do not make Deep verbose merely by repeating the transcript. Compress while preserving the evidence that changes interpretation or action.

## File Output

- If the user requests a Markdown/Obsidian file, create an actual `.md` artifact rather than only pasting text into chat.
- Prefer the user-specified output directory. If it is unwritable, save to the current workspace and report that fact.
- Use UTF-8. The title and filename should remain human-readable on Windows.

`--summary <mode>` is a compatibility and logging hint. The Agent still performs the summary workflow.
