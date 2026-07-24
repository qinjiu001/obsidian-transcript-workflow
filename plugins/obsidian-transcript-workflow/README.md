# Obsidian Transcript Workflow Plugin

这个 Plugin 一次安装两个相互协作的 Skill：

- `podcast-bridge`：把播客、访谈或博客全文稿整理成 Obsidian 中文深度笔记。
- `mermaid-visualizer`：在内容确实存在流程、层级、决策或因果系统时，生成兼容 Obsidian/GitHub 的 Mermaid 图。

## 本地文稿配置

首次处理本地 DOCX 队列时，让 Codex“初始化本地文稿路径配置”。`podcast-bridge` 会把配置模板复制到：

```text
~/.codex/obsidian-transcript-workflow/library-workflow.json
```

然后填写：

- `source_root`：原始 DOCX 根目录；
- `target_root`：Obsidian 的 `raw/02-papers` 目录；
- `human_sop`：当前 Human SOP；
- `iteration_log`：迭代记录；
- `workbuddy_handoff`：跨 Agent 交接文档。

个人路径配置、订阅、数据库、音频和转写成品不会进入公开仓库。

## 主要资料

- `docs/Human_SOP_标准化模板.md`
- `docs/迭代记录.md`
- `docs/WorkBuddy_播客文稿处理交接文档.md`
- `skills/podcast-bridge/ARCHITECTURE.md`

## 第三方来源

- Podcast Bridge 基于 `Hatari130/podcast-bridge`，MIT License。
- Mermaid Visualizer 来自 `axtonliu/axton-obsidian-visual-skills`，MIT License。
