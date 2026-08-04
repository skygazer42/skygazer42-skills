---
name: subagent-driven-development
description: Use when executing implementation plans with independent tasks in the current session
---

# 子代理驱动开发

按实现计划，每个 task 派一个全新 implementer 子代理，每个 task 后做审查（spec 合规 + 代码质量），最后做全分支审查。

**核心原则：**每 task 全新子代理 + task 审查（spec + 质量）+ 最终全分支审查 = 高质量、快速迭代。

## 何时使用

有实现计划 & task 基本独立 & 留在当前 session → subagent-driven-development。

与 `engineering.executing-plans` 的区别：同一 session、无上下文切换、每个 task 后审查、更快迭代。

## 设置

- 用 `engineering.using-git-worktrees` 确保隔离工作区。
- 读计划一次，为每个 task 创建 todo。
- 派发 Task 1 前扫描一次：task 间矛盾、计划强制要求与审查规则冲突 → 一次性批量提问。

## Model Selection

- 机械实现 task（1-2 个文件，完整 spec）→ 便宜快速模型
- 集成和判断 task → 标准模型
- 架构和设计 task → 最强模型
- 最终全分支审查 → 最强模型
- 修复循环 R4-5 → 比卡住的 implementer 高一档

## Task 循环

### 1. 派发 implementer
- 记录 BASE commit。用 task-brief 提取 task 文本发给子代理。
- 子代理只看到自己的 task 和必要接口——不给整个计划文件。
- 指定 report 文件路径，子代理把完整报告写文件，返回仅状态+commit+一行测试摘要。

### 2. 处理报告
- DONE → 生成 review package，派发 task reviewer。
- DONE_WITH_CONCERNS → 读 concern，若是正确性/范围问题则先处理再审查。
- NEEDS_CONTEXT → 提供缺失上下文，重新派发。
- BLOCKED → 评估原因（上下文/推理能力/task 太大/计划有错），相应处理。

### 3. Task 审查
每 task 审查是 task 级把关。最终全分支审查只做一次。两个裁决都需要：spec 合规 AND task 质量。implementer 自审不替代 task 审查。

### 4. 修复循环
最多 5 轮。R1-3 → 恢复原 implementer。R4-5 → 全新 implementer + 更强模型。每轮：修复 → 覆盖测试 → 追加报告 → 划定范围重新审查。

### 5. 完成 task
审查全绿或所有 open finding 在断路器处 parked-with-ruling → ledger 标记完成。

## 最终审查

用 `engineering.requesting-code-review` 的 code-reviewer 模板派发全分支审查。有 finding → 派一次修复（合并非多次）→ 做一次划定范围重新审查 → 裁决残余。

## 完成

清理 workspace。用 `engineering.finishing-a-development-branch`。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：Skill 引用改为 engineering.*，简化流程描述以适配本仓生态。
