---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
---

# 执行实现计划

按实现计划执行全部 task。两种模式可选——选哪个取决于 task 是否独立、是否需要隔离审查。

## 选择执行模式

| 条件 | 模式 A：子代理驱动（推荐） | 模式 B：内联执行 |
| --- | --- | --- |
| Task 基本独立 | ✅ | — |
| 需要 task 级审查 | ✅ | — |
| 留在当前 session | ✅ | ✅ |
| Task 高度耦合 | — | ✅（单线程不打架） |
| 没有子代理能力 | — | ✅ |

**两种模式共享：**隔离工作区（`engineering.using-git-worktrees`）、读计划、创建 todo、完成收尾（`engineering.finishing-a-development-branch`）。

## 并行派发（两种模式都可用）

当计划中有 2+ 个 task **完全没有共享状态且不修改同一文件**时，可以并发派发：
- 同一响应中发出多个 dispatch → 并行执行。
- 一次一个 dispatch → 串行执行。
- **不要并行**：task 可能编辑同一文件、有先后依赖、失败可能共享根因。

并行代理返回后：读每个摘要 → 核实不冲突 → 跑完整测试 → 集成。

## 模式 A：子代理驱动

每个 task 派一个全新 implementer 子代理 + task 后审查 + 最终全分支审查。

**循环：**
1. 派发 implementer（只给当前 task 的 brief + 接口，不给整个计划）。
2. 处理报告：DONE → 审查 / CONCERNS → 先处理 / NEEDS_CONTEXT → 补上下文 / BLOCKED → 评估原因。
3. Task 审查（spec 合规 + 代码质量，两者都不能跳）。
4. 修复循环：最多 5 轮。R1-3 恢复原 implementer。R4-5 新 implementer + 更强模型。
5. 完成 task → 下一个。

**最终审查：**全部 task 后用 `engineering.code-review` 做全分支审查 → 有 finding 就一次修复 → 一次划定范围重新审查 → 裁决残余。

## 模式 B：内联执行

当前 session 中逐 task 执行。无子代理隔离、无 task 级审查——适合简单 task 或无子代理能力时。

1. 读计划，批判性审查，创建 todo。
2. 每个 task：标记 in_progress → 精确按步骤 → 跑验证 → 标记 completed。
3. 遇阻塞立即停。不要猜。请求澄清。
4. 全部完成后用 `engineering.code-review` 做一次审查（如果可以派发审查子代理的话），再用 `engineering.finishing-a-development-branch` 收尾。

## 完成

`engineering.finishing-a-development-branch`。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `subagent-driven-development` + `executing-plans`（MIT License），做过：合并两个执行 skill 为一个（双模式）、吸收 `dispatching-parallel-agents` 核心为「并行派发」、Skill 引用改为 engineering.*、简化流程。
