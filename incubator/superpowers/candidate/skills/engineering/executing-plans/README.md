# Executing Plans（执行计划）

## 一句话定位

在有写好的实现计划时，在独立 session 中逐 task 执行，每个 task 跑验证，完成后汇报。

## 适用场景

- `engineering.writing-plans` 已产出实现计划。
- 想在独立 session 中执行（不污染当前上下文）。
- 计划中的 task 有清晰边界和验证命令。

## 不适用场景

- 子代理可用且 task 独立——用 `engineering.subagent-driven-development`（推荐）。
- 还没有计划——先用 `engineering.writing-plans`。

## 执行流程

1. 创建/验证隔离工作区。
2. 加载实现计划，批判性审查。
3. 创建 todo，逐 task 执行，每步跑验证。
4. 全部完成后用 `engineering.finishing-a-development-branch` 收尾。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
