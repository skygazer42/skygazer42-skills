# Matt Pocock Skills 审核报告

> 审核日期：2026-08-04
> 来源：`incubator/mattpocock-skills/source.yaml`（MIT，commit 2ab9580）
> 审核人：skygazer42（Agent 辅助）

## 一、借鉴目标

从 `mattpocock/skills` 借鉴两个理念，**不直接照搬**：

| 借鉴对象 | 核心理念 | 内化为 |
| --- | --- | --- |
| `grill-me` + `grilling` | 无情审问一个计划/设计/决策，一次一个问题走决策树，压力测试思路 | `engineering.grilling` |
| `improve-codebase-architecture` + `codebase-design` | 找「深化机会」（浅模块→深模块），deletion test，架构可测性 | `engineering.architecture-review` |

## 二、关键问题：依赖链（AGENTS.md §8.2）

原版**深度依赖 mattpocock 生态**，不能直接导入：

- `grill-me` 正文只有一行「Run a `/grilling` session」——空壳，实质在 `/grilling`。
- `improve-codebase-architecture` 依赖 `/codebase-design`（词汇表）+ `/domain-modeling` + `/grilling` + `HTML-REPORT.md` + 项目级 `CONTEXT.md`/ADR 约定。

这些依赖在本仓不存在。直接导入会产生大量悬空引用。

## 三、规范化决策（去依赖 + 剃刀）

**`engineering.grilling`：**
- 提取 `grilling` 的核心（12 行）为独立 Skill，零外部依赖。
- 注入本仓上下文：grilling 与 `brainstorming` 互补（探索 vs 攻击）；grill 完成后路由到 `writing-plans`。

**`engineering.architecture-review`：**
- **内联**深模块词汇（module/interface/depth/seam/leverage/locality）和 deletion test——不依赖 `codebase-design`。
- **砍掉**（剃刀）：强制 HTML/Tailwind/Mermaid CDN 报告 → 改为「呈现候选，可视化可选」；`domain-modeling`/`CONTEXT.md`/ADR 硬依赖 → 移除。
- grilling 步骤指向本仓 `engineering.grilling`。

## 四、其它检查

| 检查项 | 结论 |
| --- | --- |
| 隐式提交/推送/删除 | ✅ 无 |
| 密钥/网络/遥测 | ✅ 无 |
| 与现有 Skill 重复 | ✅ grilling ≠ brainstorming（批判 vs 建设）；architecture-review 填补架构级审查空白（code-review 是代码级） |
| License | ✅ MIT，允许改写 |
| 平台绑定 | ⚠️ 原版绑定 mattpocock 生态——已去依赖 |

## 五、状态

**审核通过（去依赖改写）。** 已规范化到 `skills/engineering/grilling/` 和 `skills/engineering/architecture-review/`。
