---
name: brainstorming
description: "You MUST use this before any creative work — creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation."
---

# 头脑风暴：把想法变成设计

通过自然的协作对话把想法变成完整的设计与规格说明。

先理解当前项目上下文，然后一次问一个问题来细化想法。一旦理解了要构建什么，就展示设计并获得用户批准。

<HARD-GATE>
在展示设计并获得用户批准之前，**禁止**调用任何实现类 Skill、写任何代码、搭建任何项目或采取任何实现行动。这对**所有**项目都适用，不论看起来多简单。
</HARD-GATE>

## 反模式："这太简单了不需要设计"

每个项目都要走这个流程。Todo 列表、单函数工具、配置修改——全都一样。「简单」项目才是未经审视的假设造成最多浪费的地方。设计可以很短（真正简单的项目几句话就行），但**必须**展示并获得批准。

## 检查表

你必须为以下每项创建任务，按顺序完成：

1. **探索项目上下文**——检查文件、文档、最近提交
2. **一次一个问题地澄清**——理解目的、约束、成功标准
3. **提出 2-3 个方案**——给出权衡和你的推荐
4. **逐节展示设计**——根据复杂度缩放每节，每节后获得用户批准
5. **写设计文档**——保存到 `docs/specs/YYYY-MM-DD-<topic>-design.md` 并提交
6. **规格自审**——快速检查占位符、矛盾、歧义、范围（见下文）
7. **用户审阅规格**——请用户在继续前审阅规格文件
8. **过渡到实现**——调用 `engineering.writing-plans` 创建实现计划

## 过渡到实现

设计获批、计划就绪后，根据工作领域路由到本仓对应的领域 Skill：

| 工作领域 | 应路由到的 Skill |
| --- | --- |
| 前端 UI / 交互 / 样式 / 组件实现 | `web.frontend-implementation` |
| 前端代码审查 / PR | `web.frontend-review` |
| 前端测试 / 浏览器验证 | `web.frontend-testing` |
| 后端 API / 服务 / 数据库 / 集成 | `backend.backend-implementation` |
| 后端审查 / 安全检查 | `backend.backend-review` |
| 后端排障 / 根因定位 | `backend.backend-debugging` |

本仓全部可用 Skill 的最新列表见根 `README.md` 的能力目录。不确定路由到哪个时，先确认问题的领域归属（web 还是 backend）和意图（实现 / 审查 / 测试 / 排障）。

在 brainstorming 终端状态之后，**只能**调用 `engineering.writing-plans`。不要直接调用实现类 Skill。

## 规格自审

写完规格文件后，用新鲜眼光看它：

1. **占位符扫描**：有没有 "TBD"、"TODO"、不完整的节、模糊的需求？修掉。
2. **内部一致性**：有没有节与节之间的矛盾？架构是否与功能描述匹配？
3. **范围检查**：是否聚焦到一份实现计划能覆盖的程度，还是需要进一步拆解？
4. **歧义检查**：有没有需求能被两种不同方式解读？有的话选一种并明确下来。

在规格文件中直接修掉问题。不需要重新审查——修完就继续。

## 用户审阅关

在规格自审通过后，请用户在继续前审阅规格文件：

> "规格已写入并提交到 `<path>`。请审阅，若有任何要改的请在开始写实现计划前告诉我。"

等待用户回应。若他们要求改，就改完重新跑规格自审。只有用户批准后才继续。

## 现有代码库中的工作

- 在提出变更前先探索当前结构。遵循已有模式。
- 当现有代码有问题会影响当前工作时（如文件过大、边界不清、职责纠缠），把有针对性的改进纳入设计——就像优秀开发者在工作中改善代码一样。
- 不要提出无关重构。专注服务于当前目标。

## 来源与改造说明

本 Skill 基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `brainstorming` Skill（MIT License），做了以下本地改造：

1. 新增「过渡到实现」路由表，指向本仓的领域 Skill（web.* / backend.*）。
2. 将 `writing-plans` 引用改为 `engineering.writing-plans`（本仓 engineering 分类）。
3. 简化 Visual Companion 部分（原版需要浏览器服务器脚本，本仓未包含）。
4. 规格文档路径从 `docs/superpowers/specs/` 改为 `docs/specs/`（本仓惯例）。
5. 工具名改为平台中立表述（Task/Agent/Edit/Write 等保留原文，各平台自行映射）。
