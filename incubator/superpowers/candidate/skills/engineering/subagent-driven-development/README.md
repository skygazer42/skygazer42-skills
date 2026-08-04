# Subagent-Driven Development（子代理驱动开发）

## 一句话定位

按实现计划，每个 task 派全新子代理 + task 审查 + 最终全分支审查，在当前 session 中高质量快速迭代。

## 适用场景

- `engineering.writing-plans` 已产出实现计划。
- Task 基本独立（可各自派子代理）。
- 想留在当前 session 中执行（不切到另一个 session）。

## 不适用场景

- Task 高度耦合、共享大量状态——用 `engineering.executing-plans` 单线程执行。
- 还没有实现计划——先用 `engineering.brainstorming` + `engineering.writing-plans`。
- 不想要子代理审查——用 `engineering.executing-plans`。

## 执行流程

1. 确保隔离工作区（`engineering.using-git-worktrees`）。
2. 读计划，创建 todo，扫描冲突。
3. 对每个 task：派发 implementer → 审查 → 修复循环（最多 5 轮）→ 完成。
4. 全分支最终审查（`engineering.requesting-code-review`）。
5. 收尾（`engineering.finishing-a-development-branch`）。

## 默认边界

- **读文件**：是（读计划、读代码库）。
- **写文件**：是（子代理写代码、ledger 文件）。
- **执行命令**：是（跑测试、lint、build）。
- **网络**：否。
- Controller 自己不修代码——所有实现改动由子代理完成并审查。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
