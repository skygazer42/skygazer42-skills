---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# 执行计划

## 概述

加载计划，审查批判性地，执行所有 task，完成后汇报。

**开始时宣布：**"I'm using the executing-plans skill to implement this plan."

**注意：**若子代理可用，应使用 `engineering.subagent-driven-development` 代替本 skill。

## 流程

### Step 1: 加载并审查计划

1. 确保隔离工作区（用 `engineering.using-git-worktrees` 创建或验证）。
2. 读计划文件。
3. 批判性审查——识别任何问题或疑虑。
4. 若有疑虑：在开始前向用户提出。
5. 若无疑虑：创建 todos 并继续。

### Step 2: 执行 Task

每个 task：标记 in_progress → 精确按步骤执行 → 按指定跑验证 → 标记 completed。

### Step 3: 完成开发

所有 task 完成并验证后，用 `engineering.finishing-a-development-branch` 完成工作。

## 何时停止求助

遇到以下情况**立即停止执行**：阻塞（缺依赖、测试失败、指令不清）、计划有严重缺口导致无法开始、不理解某个指令、验证反复失败。

**请求澄清而非猜测。**

## 执行时路由到领域 Skill

计划中的 task 若涉及具体领域工作，执行时应路由：

| 领域 | 领域 Skill |
| --- | --- |
| 前端实现 | `web.frontend-implementation` |
| 前端审查 | `web.frontend-review` |
| 前端测试 | `web.frontend-testing` |
| 后端实现 | `backend.backend-implementation` |
| 后端审查 | `backend.backend-review` |
| 后端排障 | `backend.backend-debugging` |

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：Skill 引用改为 engineering.*，新增领域路由表。
