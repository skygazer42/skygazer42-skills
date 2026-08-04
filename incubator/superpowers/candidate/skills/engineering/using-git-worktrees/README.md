# Using Git Worktrees（使用 Git Worktrees）

## 一句话定位

开始功能开发或执行实现计划前，确保隔离工作区存在。优先检测已有隔离，再尝试原生工具，最后回退到 git worktree。

## 适用场景

- 开始一个不同于当前分支的功能工作。
- 执行 `engineering.writing-plans` 产出的实现计划。
- `engineering.subagent-driven-development` 或 `engineering.executing-plans` 的设置阶段。

## 不适用场景

- 已经在一个 worktree 中——Step 0 会自动跳过。
- 简单的单行修改不需要隔离。

## 执行流程

1. 检测是否已在隔离工作区。
2. 若否→问用户是否创建。
3. 用原生工具或 git worktree 创建。
4. 安装依赖，跑基线测试。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
