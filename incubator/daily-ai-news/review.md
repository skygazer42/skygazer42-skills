# Review: Daily AI News（每日 AI 简报）

## 结论

**有保留地晋级。** 多来源 AI 新闻聚合技能：抓取 3-5 个主要新闻源 + 搜索补充 → 筛选去重 → 五类分类呈现（重大公告/研究论文/行业融资/工具发布/政策伦理），输出带原文链接的每日简报。支持简要/标准/深度三种模板。

用户明确请求内化此技能（ModelScope @NanjingHJLP/Daily-AI-News，git 镜像为 github.com/NanjingHJLP/hjlp-skills 的 skills/Daily-AI-News，revision 390ec9d，2026-08-11 抓取）。

## 真实需求

- 用户需要"每天获取 AI 新闻汇总"的能力
- 与 deep-research 类流程（多轮搜索、多源交叉验证）不同：本技能是轻量级聚合简报，核心是提示词编排，辅助脚本仅生成搜索查询日期
- 输出是 Markdown 简报（非研究报告），适合快速浏览当天 AI 动态

## 与现有 Skill 的重复分析

| 维度 | research.last30days | research.daily-ai-news（本次） |
|------|---------------------|-------------------------------|
| 时间范围 | 近 30 天趋势 | 最近 24-48h 新闻 |
| 数据源 | Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub/Web | 主要 AI 新闻站 + 搜索引擎 |
| 排序依据 | 真实用户互动（赞/投票/金钱） | 时间新鲜度 + 重要性判断 |
| 输出 | 按信号强度排序的证据簇 + AI Judge 融合摘要 | 分类新闻简报（类别/标题/要点/来源链接） |
| 执行方式 | 脚本驱动（python3/node） | 提示词编排（辅助脚本可选） |
| 触发场景 | "过去 30 天人们真正在说什么" | "今天的 AI 新闻" |

**不重叠。** last30days 是趋势调研引擎，daily-ai-news 是每日新闻聚合简报。触发场景、时间范围、数据源、输出格式均不同。**独立引入，不合并。**

## 安全与平台检查

- **隐式提交/推送/发消息/PR/发布/删除/生产写入**：SKILL.md 全文为聚合工作流提示词 + CSS/JS 模板引用，无任何此类指令。逐行扫描通过。
- **密钥/敏感数据**：无密钥、个人数据、内部地址或敏感日志读写。
- **远程脚本/未声明网络行为**：脚本 generate_queries.py 仅生成搜索查询字符串（纯文本输出到 stdout），不执行网络请求、不下载、不调用外部服务。
- **本地行为**：脚本仅输出文本；辅助脚本无写文件操作。
- **平台绑定**：不绑定特定平台/工具/环境变量；搜索服务通过环境变量注入是可选的。
- **署名/外链/上传/对外状态**：无强制署名，无强制外链，无案例上传，无对外状态创建。

## License 检查

- 上游仓库 `NanjingHJLP/hjlp-skills` 无 LICENSE 文件（git 历史从未添加）。
- 仓库 README 的"许可证"节写"各技能的许可证信息请参见对应 SKILL.md 中的 license 字段"；Daily-AI-News 的 SKILL.md 中无 license 字段。
- 处理方案：与 html-ppt 同例——上游声明 MIT 的可信度高于完全无声明；本仓按上游声明以 MIT 记录，并在 LICENSE 文件中复制 MIT 许可证文本随副本保存，在 provenance 中明确注明"上游未提供 LICENSE 文件"。
- 不进入 `NOASSERTION`：README 是作者持续声明，可信度高于完全无声明；本仓 README 的已知限制页说明外部技能需独立遵守上游许可证。

## 需要修改的内容

1. 适配 SKILL.md：新增"输出契约 / 写入边界 / 信息不足时不编造"节；保留源全文核心流程不变。
2. 补全仓库契约文件：manifest.yaml / 中文 README.md / provenance.yaml / tests/cases.yaml / LICENSE。
3. references/ 与 scripts/ 内容与源一致，逐字复制，不修改。
4. 归入 research 分类（research.daily-ai-news），与 research.last30days 无职责重叠。

## 处理结果

**晋级为 `skills/research/daily-ai-news/`。**
