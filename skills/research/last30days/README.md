# Last 30 Days Research（近 30 天调研）

## 一句话定位

多源调研引擎——并行搜索 Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub/Web，按真实用户互动（赞/投票/金钱）排序，AI 融合成摘要。回答"过去 30 天人们真正在说什么"。

## 适用场景

- 调研某个人/公司/产品在社群中的近期口碑
- 了解某个技术/工具的社区真实反馈（替代 Google 搜不到的 Reddit/X 讨论）
- 追踪 AI 等行业快速变化的最新动态
- 会议前的背景调研（对方最近在做什么、说了什么）
- 竞品分析（用户对竞品的真实评价）

## 不适用场景

- 精确事实查询（如"某个 API 的参数名"）——这是搜索引擎/文档的职责
- 历史深度研究（超过 30 天范围）——本 Skill 偏近期信号
- 需要访问内部数据或私有 API 的调研
- 替代传统搜索引擎做通用 Web 搜索

## 执行前需要的信息

- 调研主题（一句话即可，如 `nvidia earnings reaction`、`AI video tools`）
- 可选：API 密钥（SCRAPECREATORS_API_KEY 等），无密钥时走 keyless 降级路径

## 执行流程

1. 运行 `scripts/last30days.py` 引擎，并行搜索 Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub/Web
2. 按真实用户互动（upvotes/likes/odds）排序
3. AI Judge 融合多源结果，生成摘要
4. 输出到终端（也可选 HTML 发布）

## 交付结果

- 按信号强度排序的证据簇
- 每个簇含：来源平台 + 互动数据 + 关键引用
- 一句话总结（AI Judge 融合）

## 默认边界

- **读文件**：是
- **写文件**：否（仅输出到终端，可选 HTML 报告）
- **执行命令**：是（python3/node）
- **网络**：是（核心功能需搜索各平台 API）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `marketing.seo` | SEO 审计/诊断/实施，本 Skill 是多源社群调研 |
| `engineering.brainstorming` | 设计方案探索，本 Skill 是外部信息搜集 |

本 Skill 是调研/信息搜集类，不与现有任何 Skill 重叠。

## 行为案例

### 案例 1：典型人物调研

**输入**：`/last30days Peter Steinberger`

**预期行为**：
1. 并行搜索 Reddit/X/GitHub/YouTube 等平台
2. 返回近期动态：加入 OpenAI、Codex 相关讨论、PR 活跃度、社群讨论热度
3. 按互动数据排序，AI 融合成摘要

### 案例 2：无 API 密钥降级

**输入**：用户未配置任何 API 密钥，运行 `/last30days AI video tools`

**预期行为**：
1. 走 keyless 路径（RSS/scraping 降级）
2. Reddit/HN/Polymarket/GitHub 仍可用（零配置）
3. X/YouTube/TikTok 标记为不可用，不编造数据
4. 本地评分替代 LLM 排序

## 版本与来源

- **版本**：`0.1.0` / `beta`（上游 v3.18.4）
- **来源**：基于 [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 的 `skills/last30days/` 模块（MIT License），完整保留执行内容，做了本仓适配（见 `provenance.yaml`）。