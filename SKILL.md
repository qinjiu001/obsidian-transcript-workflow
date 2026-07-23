---
name: podcast-bridge
description: 一个让 AI Agent 订阅、转录、检索并理解全球播客的 Skill。适用于用户提供小宇宙单集链接、RSS 源、播客名称或单集编号，或直接提供 DOCX/Markdown/TXT 全文稿，并要求转录、总结、Deep 深度笔记、Product/Investment 视角分析、Deep+Obsidian 知识库笔记、把本地英文播客文稿批量整理成可读中文文章、跨单集搜索、播客推荐、订阅同步或 RSS 维护。触发词包括“按我的人工 SOP”“处理本地播客文件夹”“中文可读文稿”“Obsidian 知识库笔记”。Obsidian 模式默认保留 Deep 证据覆盖，再增加精简 YAML、双链、图表/指标与可执行层；视觉使用用户现有的 Obsidian 主题和原生 Markdown，不默认生成 cssclasses 或 HTML。
---

# podcast-bridge

podcast-bridge 用于管理播客订阅、同步 RSS 单集元数据、转录播客、生成章节、搜索本地播客知识库，并基于全文稿生成摘要或笔记。

## 核心原则

根据用户请求选择最窄、最直接的工作流：

| 用户请求 | 执行动作 |
|---|---|
| 提供单集链接并要求全文稿 | 运行 `python transcribe.py "<url>" --chapters`，返回全文稿路径和基础统计；4h+ 超长节目默认输出上集/下集两份 Markdown。 |
| 提供单集链接并要求总结、要点或笔记 | 先转录，读取生成的全文稿；若输出上/下集，必须读取两份稿件后再总结。 |
| 提供现成 DOCX/Markdown/TXT 全文稿并要求总结 | 完整读取用户提供的全文稿，不要重复转录；按用户指定模式生成摘要或笔记。 |
| 要求 Obsidian、知识库笔记或 deep + obsidian | 默认生成“Deep 内容基线 + Obsidian 组织 + 可执行层”的 `.md`，同时读取 `references/summarization.md` 和 `references/obsidian-deep.md`。 |
| 要求处理本地英文播客文稿、文件夹、人工 SOP 或批量入库 | 读取 `references/local-library-workflow.md`、`references/obsidian-deep.md` 和 `references/obsidian-native-style.md`；先扫描未处理队列，默认一次只处理 1 篇。 |
| 提供 RSS URL 或播客名称并要求添加 | 添加、同步或列出元数据；默认不要批量转录。 |
| 询问某个节目是否聊过某个话题 | 同步或查询本地库，并区分“全文命中”和“仅标题/简介命中”。 |
| 要求推荐播客 | 读取 `podcast-bridge-feeds/feeds/*.json`，按主题推荐；只有用户明确要求时才导入订阅。 |
| RSS 源损坏或订阅维护 | 使用 `podcast-bridge-feeds/resolve_feeds.py` 和 `podcast-bridge-feeds/import_feeds.py`。 |

重要边界：

- `transcribe.py` 是确定性的执行入口，负责转录、章节生成、RSS 入库和搜索。
- 超过 `long_audio_threshold_minutes` 的节目默认先拆成 `long_audio_parts=2` 个大段，再输出 `_上集.md` 和 `_下集.md` 两份稿件；最终回复应同时报告两份路径。
- 摘要需要在读取全文稿之后由 Agent 自己生成；`--summary` 只是兼容旧参数和表达期望风格，不会稳定地产生摘要文件。
- `obsidian` 不是仅给 Deep 文稿加 YAML。默认必须先满足 Deep 的证据覆盖，再增加属性、双链、图表或指标、行动清单和知识拆分。
- 本地文稿入库默认只生成一个 Obsidian Markdown 成品，不先生成 Deep 文件再调用 zine，也不生成重复 HTML。使用用户现有的 Obsidian 主题，不添加自定义 `cssclasses` 或重复的正文“基本信息”。
- 重要案例、数字、因果链和原稿不确定性不能因格式化而丢失。Agent 新增的运营判断必须放在“我的思考”或“应用建议”中，不得伪装成原文观点。
- 本地文稿 Workflow 每次执行结束后，必须把运行结果、困难、临时假设、人工确认项和规则升级状态写回当前《迭代记录》，形成 Human → Agent → Human 的闭环。
- 默认 ASR provider 使用 `bcut`，不需要 API Key。
- 查询当前状态时，应读取实时文件或 SQLite 数据库，不要依赖文档里的固定订阅数量。
- 如果用户要求摘要，最终回复必须包含摘要正文，不能只回复“转录完成”。

## 参考文件路由

只读取当前任务需要的参考文件：

- `references/transcription.md`：单集转录、启动前检查、ASR provider 选项、输出路径。
- `references/summarization.md`：所有摘要模式的共通证据规则，以及 brief、deep、product、investment、obsidian 的路由。
- `references/obsidian-deep.md`：用户偏好的 Deep+Obsidian 生成流程、模板、可选模块和质量门槛。
- `references/local-library-workflow.md`：用户人工 SOP 的可执行版本；负责本地 DOCX 队列、中文可读化、目录映射、跳过已完成和低 token 规则。
- `references/obsidian-native-style.md`：使用原生 Markdown 和用户现有主题，不默认添加 CSS 类或 HTML。
- `references/rss-workflows.md`：订阅管理、订阅库导入、RSS 同步/列表/搜索/转录。
- `references/troubleshooting.md`：常见失败、编码问题、API/provider 错误、状态查询。
- `references/project-layout.md`：仓库结构、数据文件、路径假设。

## 摘要模式默认值

- 用户只说“总结”：使用 `brief`。
- 用户要求深度理解：使用 `deep`。
- 用户要求产品或投资视角：分别使用 `product` 或 `investment`，但仍保留证据与不确定性。
- 用户提到 Obsidian、知识库、双链或长期沉淀：使用 `obsidian`；本地约定为 Deep+Obsidian，而不是轻量格式转换。
- 用户提到人工 SOP、本地 300+ 文稿、处理文件夹或批量入库：进入本地文稿库 Workflow；实时扫描数量，不能依赖旧 SOP 里的固定总数。
- 用户要求 `.md` 文件：生成实际 Markdown 文件并返回路径。优先写入用户指定目录；目录不可写时保存到当前工作区并明确说明。

## 常用命令

在 podcast-bridge 项目根目录运行以下命令。`config.json` 中的 `library_dir` 会决定使用哪个本地播客库。

```bash
python transcribe.py --preflight-only "<episode-url>"
python transcribe.py "<episode-url>" --chapters
python transcribe.py "<episode-url>" --chapters --long-audio-parts 2
python transcribe.py rss subs
python transcribe.py rss sync "<podcast-name>" --limit 50
python transcribe.py rss list "<podcast-name>" --limit 50
python transcribe.py rss search "<podcast-name>" "<topic>" --days 90
python transcribe.py rss transcribe "<podcast-name>" <episode-id> --chapters
python transcribe.py rss transcribe "<podcast-name>" <episode-id> --chapters --long-audio-parts 2
```

如果当前工作目录不在项目根目录，应使用 `transcribe.py` 的绝对路径。

维护内置订阅库：

```bash
cd podcast-bridge-feeds
python resolve_feeds.py bootstrap
python resolve_feeds.py add "Latent Space" --category ai --country us
python resolve_feeds.py validate feeds/
python import_feeds.py --all
```

## 交付要求

转录完成后，尽量报告生成的全文稿路径和基础统计信息，包括时长、分段数量、字数或字符数。超长节目可能生成上集/下集两份 Markdown，必须同时报告两份路径。

回答搜索类问题时，必须说明覆盖范围：有多少单集具备可搜索全文，有多少单集只有标题/简介元数据可搜索。
