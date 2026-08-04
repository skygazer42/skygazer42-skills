---
name: writing-plans
description: Use when you have a spec or requirements for a multi-step task, before touching code
---

# 写实现计划

## 概述

写全面的实现计划——假定工程师对代码库零上下文、对品味也拿不准。记录他们需要知道的一切：每个任务改哪些文件、代码、测试、需要查阅的文档、怎么测试。把整个计划拆成一口大小的 task。DRY。YAGNI。TDD。频繁提交。

**开始时宣布：**"I'm using the writing-plans skill to create the implementation plan."

**计划保存到：**`docs/plans/YYYY-MM-DD-<feature-name>.md`（用户偏好可覆盖此默认路径）

## 范围检查

如果规格覆盖多个独立子系统，应该在 brainstorming 阶段就拆成子项目规格。如果没拆，建议拆成多个独立计划。每个计划应产出可独立运行、可独立测试的软件。

## 文件结构

定义 task 前先理清哪些文件要创建或修改，各自负责什么。这就是把拆解决策锁定的地方。

- 设计单元要有清晰边界和定义良好的接口。每个文件一个清楚的职责。
- 一次能放进上下文的代码才是最好推理的代码；文件聚焦时编辑更可靠。宁要小而聚焦的文件，不要什么都在的大文件。
- 一起变的文件放一起。按职责拆分，不按技术层。
- 已有代码库里遵循现有模式。不单方面重构——但如果你在改的文件已经臃肿得难以驾驭，把拆分纳入计划是合理的。

## Task 合适的大小

每个 task 应是自带测试循环且值得 reviewer 把关的最小单位。划边界时：把和 task 交付物相关的 setup、配置、脚手架和文档步骤融进这个 task；只在 reviewer 可以独立拒绝一个 task 而批准相邻 task 时才拆分。每个 task 结尾应有独立可测的交付物。

## Bite-Sized Task 粒度

**每步一个动作（2-5 分钟）：**
- "写失败测试"——一步
- "运行确认它失败"——一步
- "实现最小代码通过测试"——一步
- "运行确认通过"——一步
- "提交"——一步

## 计划文档 Header

**每个计划必须以这个 header 开头：**

```markdown
# [功能名] 实现计划

> **给 agentic worker：** 必须用 `engineering.subagent-driven-development` 执行计划——子代理驱动（推荐，带审查）或内联执行（简单场景）。

**目标：**[一句话说清要构建什么]

**架构：**[2-3 句关于技术方案]

**技术栈：**[关键技术/库]

---
```

## 执行交接

计划保存后，给出执行选项，并根据工作领域路由到领域 Skill：

**执行方式由 `engineering.subagent-driven-development` 提供：**
- **模式 A（推荐）**：子代理驱动——每个 task 独立子代理 + task 间审查。
- **模式 B**：内联执行——当前会话中批量执行，简单 task 或无子代理能力时用。

**根据 spec 涉及的工作领域，task 执行者应路由到对应的领域 Skill：**

| 工作领域 | 领域 Skill |
| --- | --- |
| 前端 UI / 交互 / 组件 | `web.frontend-implementation` |
| 前端审查 | `web.frontend-review` |
| 前端测试 / 浏览器验证 | `web.frontend-testing` |
| 后端 API / 服务 / 数据库 | `backend.backend-implementation` |
| 后端审查 | `backend.backend-review` |
| 后端排障 | `backend.backend-debugging` |

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `writing-plans` Skill（MIT License）。本地改造：
1. Skill 引用改为 `engineering.*` 命名空间。
2. 新增「执行交接」路由表，指向本仓领域 Skill。
3. 计划文档路径从 `docs/superpowers/plans/` 改为 `docs/plans/`。
4. 简化 plan-document-reviewer-prompt.md 引用（本仓在 references/ 中提供等价内容）。
