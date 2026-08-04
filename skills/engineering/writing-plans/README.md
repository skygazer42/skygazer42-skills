# Writing Plans（写实现计划）

## 一句话定位

把已批准的设计规格（由 brainstorming 产出）拆成可执行、可审查的实现计划——每个 task 含精确文件路径、代码、测试和验证命令。

## 适用场景

- 刚刚完成了 brainstorming 并拿到已批准的设计规格。
- 有一个多步骤的实现任务需要拆解。
- 需要产出一份另一个 session 或另一个 agent 可以直接照着执行的计划。

## 不适用场景

- 还没有设计规格——先走 `engineering.brainstorming`。
- 任务简单到不需要计划（如单行修改）。
- 这是代码审查、测试或排障任务——用对应的领域 Skill。

## 执行前需要的信息

- 一份已批准的设计规格（来自 `engineering.brainstorming`）。
- 对当前代码库的访问权限（Skill 自己会读）。

## 执行流程

1. 读规格，检查范围——是否应该拆成多个独立计划？
2. 理清文件结构——哪些文件要创建、修改、删除，各自什么职责。
3. 按 task 粒度拆分（每个 task 自带测试循环，2-5 分钟可完成）。
4. 用计划 header 模板写完整计划文档，每个 task 含精确路径、接口、代码和验证命令。
5. 自审（规格覆盖、占位符扫描、类型一致性）。
6. 保存到 `docs/plans/`。
7. 执行交接——根据工作领域路由到对应的领域 Skill（web.frontend-* / backend.backend-*）。

## 交付结果

- 一份实现计划文档（`docs/plans/YYYY-MM-DD-<name>.md`）。
- 明确的执行方式选择（Subagent-Driven 或 Inline）。
- 指向执行时需要调用的领域 Skill。

## 默认边界

- **读文件**：是（读规格、读代码库）。
- **写文件**：是（写计划文档）。
- **执行命令**：否。
- **网络**：否。
- **写生产代码**：否——只写计划，不写实现。

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.brainstorming` | brainstorming 产出**设计方案**（做什么）；writing-plans 把方案拆成**实现计划**（怎么做） |
| `engineering.subagent-driven-development` | writing-plans 写计划；subagent-driven-development 执行计划 |
| `engineering.executing-plans` | writing-plans 写计划；executing-plans 在当前 session 批量执行 |

## 行为案例

### 案例 1：典型成功场景

**输入**：一份已批准的「目录迁移」设计规格。

**预期行为**：
1. 读规格和目标代码库。
2. 按降险顺序拆成 14 个 task（Phase 1 工具→Phase 2 降险→Phase 3 迁移→Phase 4 同步→Phase 5 文档→Phase 6 验证）。
3. 每个 task 含精确路径、sed 命令、预期输出。
4. 保存到 `docs/plans/2026-08-04-skills-category-migration.md`。
5. 提供两种执行方式，路由到领域 Skill。

### 案例 2：边界场景（规格覆盖多个子系统）

**输入**：一份覆盖了「用户认证 + 支付 + 通知」三个独立子系统的规格。

**预期行为**：
1. 识别这是多个独立子系统。
2. 建议拆成三份独立计划（auth / payment / notification），各可独立测试。
3. **不得**强行写一份巨型计划。
4. 等用户确认拆分方案后再为第一个子系统写计划。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `writing-plans` Skill（MIT License），做了本仓适配改造。详见 `provenance.yaml` 和 SKILL.md 末尾。
