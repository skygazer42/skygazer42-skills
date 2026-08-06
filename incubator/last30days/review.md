# Review: last30days

## 结论

**保留**。这是一个成熟的多源调研 Skill（v3.18.4，GitHub Trending #1），
用 AI Agent 并行搜索 Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub/Web，
按真实用户互动（赞/投票/金钱）排序，融合成摘要。解决"Google 搜不到社群真实声音"的问题。

## 保留理由

- 与现有仓库能力互补：无类似多源调研/社群搜索 Skill。
- 成熟度高：v3.18.4，持续维护，有中文 README，社区活跃。
- 自包含：Python 引擎（88 个模块）+ SKILL.md 契约，零配置即可用 Reddit/HN/Polymarket/GitHub。
- 分类建议：`research`（调研），与现有 `marketing`/`engineering` 区分。

## 规模

- 2.5MB / 118 文件
- SKILL.md：2255 行
- 核心引擎：88 个 Python 模块（`scripts/lib/`）
- 第三方库：`scripts/lib/vendor/bird-search/`（X/Twitter 搜索，已含 LICENSE）

## 安全与 License 检查

- **License**：MIT（Copyright c 2026 Matt Van Horn），允许复制、修改、再分发。
- **网络行为**：核心功能需网络（搜索各平台 API），但 SKILL.md 含 permission_preflight 权限前检查。
- **API 密钥**：可选 env var（SCRAPECREATORS_API_KEY 等），无密钥时走 keyless 路径（RSS/scraping 降级）。
- **无隐式外部写操作**：不提交/推送/发布；结果仅输出到终端或 HTML 文件。
- **无害依赖**：运行时仅调用 Python 脚本和 node（bird-search），无远程脚本下载执行。

## 需要修改的内容（晋级前）

1. **补全仓库契约**：manifest.yaml、中文 README.md、provenance.yaml、tests/cases.yaml。
2. **SKILL.md 适配**：尾加"来源与改造说明"节；路径引用需适配本仓库目录结构。
3. **分类命名**：建议新分类 `research`（调研），ID 为 `research.last30days`。
4. **权限声明**：`network: true`（核心功能需网络），`read_files: true`，`write_files: false`，`execute_commands: true`。
5. **上游依赖声明**：Python 3 + node（bird-search），各平台 API key 为可选 env var。

## 处理结果

当前状态：**孵化候选**。已固化 source.yaml + candidate（移除 14MB 上游宣传素材，仅保留执行内容）。