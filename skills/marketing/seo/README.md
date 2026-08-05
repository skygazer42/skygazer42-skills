# SEO（网站搜索优化）

## 一句话定位

审计、诊断、研究、规划、实施和验证网站 SEO，覆盖 Google/Bing/AI 搜索——证据优先，不编造指标、不保证排名。

## 适用场景

- 技术 SEO：爬取、渲染、索引、JS SEO、robots.txt、sitemap、canonical、重定向、状态码、结构化数据、Core Web Vitals。
- 关键词与意图研究、内容质量与精简、内部链接、信息架构。
- SEO 实验设计、流量下跌诊断、站点迁移、国际化与 hreflang。
- 电商/产品 SEO、图片/视频搜索、大型站与程序化 SEO。
- Search Console 分析、IndexNow、AI 搜索可见性（AI Overviews / ChatGPT Search / Copilot / Perplexity）。

## 不适用场景

- 付费搜索/竞价管理、App Store 优化（ASO）、通用 LLM prompt 优化。
- 排名/引用保证、链接垃圾、无支撑的指标或因果断言——本 Skill 明确拒绝这些。

## 执行前需要的信息

- URL、网站代码、渲染页、服务器日志、爬取文件、第一方导出、关键词数据集（视工作模式而定）。
- 目标：搜索面（Google/Bing/AI）、引擎/provider、目标页、时间窗、授权动作。

## 执行流程

Skill 按需读取 `references/` 下的模块（审计手册、技术 SEO、关键词内容、内容质量、性能测量、国际电商、垂直搜索、引擎矩阵、AI 搜索、证据政策、审计契约、知识新鲜度）。核心工作流：

1. 定义结果、范围、搜索面、引擎、目标页、时间窗、授权动作。
2. 选工作模式（advisory/page/site inventory/incident/migration/experiment/specialty）和证据模式。
3. 建立覆盖账本（发现/选中/抓取/渲染/数据支撑/失败/排除/未检查）。
4. 按依赖顺序评估：访问 → 发现 → 抓取渲染 → 索引资格 → canonical → 技术交付 → 页面含义 → 有用性 → 架构 → 垂直面 → 测量。
5. 每条发现标记 observed / inferred / missing evidence，分离影响与置信度，引用支撑证据。
6. 按业务影响优先级排序；授权时才实施最小安全变更并验证。

## 交付结果

- 执行摘要 + 覆盖账本 + 分级发现（含证据级别、影响、置信度、修复、验证）。
- 快赢/战略/实验/破坏性动作分开列。
- 关键词页面图、内容 brief、URL 映射等（按需）。
- 机器可读审计可用 `scripts/validate_audit.py` 校验（依赖 python3）。

## 默认边界

- **网络**：是（live 检查、抓取渲染页、查官方源）。
- **读文件**：是。
- **写文件**：是（仅在授权范围内 optimize/fix）。
- **执行命令**：是（校验脚本、运行时检查）。
- **Action Boundary**：`audit/diagnose` 只看不改；`optimize/fix` 只改授权范围，先存证后验证；未经授权不提交 URL、不改索引控制、不发布/删页、不动 Merchant/Business Profile。

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `marketing.seo` | 网站有机搜索优化——审计/诊断/实施 |
| `web.frontend-*` | SEO 发现的前端渲染/性能问题，修复路由到 web 实现 Skill |
| `backend.backend-*` | SEO 发现的状态码/重定向/服务端渲染问题，路由到 backend |

## 行为案例

### 案例 1：典型成功场景（技术审计）

**输入**：用户给一个站点 URL，说「帮我做 SEO 审计」。

**预期行为**：
1. 确定搜索面、工作模式、证据模式，建立覆盖账本。
2. 按依赖顺序评估（访问→索引→canonical→技术→内容→架构）。
3. 每条发现标 observed/inferred/missing evidence 并引用证据。
4. 按业务影响优先级输出，快赢/战略/实验分开。
5. **只审计不改代码**（audit 边界）。

### 案例 2：边界/失败场景（证据缺失）

**输入**：用户问「我这页能排第一吗？搜索量多少？」但没提供数据。

**预期行为**：
1. **不得**编造搜索量、难度、排名、流量等指标——证据缺失时用 `unknown`。
2. **不得**保证排名/索引/AI 引用/流量。
3. 说明需要什么证据（Search Console 导出、关键词数据集）才能给结论。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：导入自 [joeseesun/qiaomu-seo](https://github.com/joeseesun/qiaomu-seo)（MIT License，作者向阳乔木）。references/scripts/data/schemas 保留原文，本仓做了分类和入口适配。详见 `provenance.yaml`、SKILL.md 末尾、`LICENSE`。
