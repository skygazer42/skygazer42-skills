# Exploratory Analysis 审核报告

> 审核日期：2026-08-11
> 来源：`incubator/exploratory-analysis/source.yaml`
> 审核人：skygazer42（Agent 辅助）

## 一、概况

来源为 [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) 的 Data Analyst 插件（固定 commit `2cf4294`），合并两个 Skill 为一个候选：

- `data/skills/explore-data/SKILL.md`（325 行）——数据画像与探索：表格指标、逐列画像（缺失率/基数/分布分位数/字符串/日期/布尔）、数据质量问题识别（缺失/基数异常/可疑值/重复/偏斜/编码）、关系发现（外键候选/层级/相关性/派生列）、维度与度量建议、后续分析推荐。
- `data/skills/validate-data/SKILL.md`（383 行）——分享前审查：方法论与假设审查、交付前 QA 清单、常见分析陷阱目录（join 爆炸/幸存者偏差/不完整期对比/分母漂移/平均值的平均/时区错配/选择偏差）、计算复核、可视化审查、信心评级（可分享/带注记分享/需修订）。

两者均为纯提示词（无脚本、无附属文件），Apache-2.0 许可。

## 二、检查（AGENTS.md §8.2）

| 检查项 | 结论 |
| --- | --- |
| 解决真实工作流问题 | ✅ 是——本仓缺「数据分析与质量评估」能力，用户调研文件明确要求内化 |
| 与现有 Skill 重复 | ✅ 无直接重复。`research.last30days` 是外部调研，本 Skill 是用户已有数据文件的画像与验证，不冲突 |
| 隐式提交/推送/删除 | ✅ 无。两 Skill 均不触发外部写入 |
| 密钥/隐私/内部地址 | ⚠️ 需处理——分析可能读取含个人数据的文件。v0.1 明确：本地授权文件、报告只读/另写、不自动清洗、不覆盖源文件。不读取远程仓库 |
| 下载执行远程脚本 | ✅ 无 |
| 网络行为/遥测 | ✅ 无（manifest network:false） |
| 平台绑定 | ⚠️ 需处理——源文含 `~~data warehouse`、`~~notebook` 连接器占位符和 PostgreSQL schema 查询。本仓 v0.1 不提供数据库连接器，必须移除，不假装具备 DB 查询能力 |
| 强制署名/外链/上传 | ✅ 无 |
| License 允许复制修改 | ✅ Apache-2.0——允许，需保留 LICENSE 和版权声明 |

## 三、规范化决策

1. **合并成一个 Skill**：`exploratory-analysis`（探索分析），分类 `data`，ID `data.exploratory-analysis`。explore-data 为主流程，validate-data 的质量审查作为「分享前验证」第二流程合并进 SKILL.md，避免一次导入两套几乎独立的入口。
2. **移除数据仓库/连接器要求**：删除 `~~data warehouse` / `~~notebook` 占位符、PostgreSQL schema 查询（`information_schema`、`pg_size_pretty`、`pg_catalog`）和 `[CONNECTORS.md]` 引用。v0.1 只支持用户提供的本地文件（CSV/TSV/JSON/Parquet/XLSX）或对话内表格。
3. **保留核心方法论**：数据画像（缺失/基数/分布/时间范围）、质量评分框架、模式发现、陷阱目录、信心评级、后续分析建议。
4. **License 保留**：Apache-2.0 要求保留声明，`LICENSE.txt` 随 Skill 保存，`provenance.yaml` 记录 `identifier: Apache-2.0` / `file: LICENSE.txt`。
5. **权限**：读文件是、写文件是（Markdown/JSON 报告，不覆盖源数据）、执行命令是（python3 数据脚本）、网络否。默认只读源数据；不自动清洗、填补、删除异常值。
6. **事实边界**：不编造数据集内容；分析对象是用户提供的本地数据，不联网猜测。

## 四、状态

**审核通过。** 已规范化到 `skills/data/exploratory-analysis/`。
