# Obsidian Native Markdown Style

Use this reference for every local-library Obsidian note.

## Principle

The user manages presentation through the vault's existing Obsidian theme. Output normal Markdown only. Do not add `cssclasses`, embedded CSS, HTML layout, or a second beautification pass unless the user explicitly requests an export or custom visual treatment.

## YAML Policy

Keep YAML compact and operationally useful. For local-library notes, omit:

- `source_type`
- `language`
- `status`
- `human_sop`
- `cssclasses`

Keep source details in YAML instead of repeating them in the article body. Do not create a `## 基本信息` section.

## Native Component Mapping

| Zine idea | Obsidian-native representation |
|---|---|
| Cover | Compact YAML + H1 |
| Pull quote | Markdown blockquote |
| Tracing card | `[!quote]` or `[!principle]` callout |
| Appendix | `[!note] 附页` callout |
| Section label | H2/H3 headings |
| Process graphic | Mermaid, maximum one by default |
| Data module | Markdown table, maximum two by default |
| Action strip | `[!todo]` callout + checkboxes |
| Related reading | `[[wikilinks]]` |

Do not insert HTML `<div>`, inline CSS, external scripts, a full HTML document shell, or custom theme classes.

## Content Rhythm

- Use short paragraphs of 2–5 sentences.
- Prefer prose for argument and bullets for repeated items.
- Place one visual anchor after a dense argument section: callout, diagram, table, or quote.
- Do not decorate every section. The user's Obsidian theme already controls typography, spacing, and colors.
- Use horizontal rules sparingly; headings should provide most navigation.

## Token Budget

The note should not contain CSS, font declarations, component HTML, theme classes, or layout boilerplate. Use native callouts when meaningful, plus at most one Mermaid block and two Markdown tables by default.
