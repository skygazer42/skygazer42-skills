# Finishing a Development Branch（完成开发分支）

## 一句话定位

实现完成、测试全部通过后，提供三种集成选项（合并/PR/保持），安全执行并清理。

## 适用场景

- `engineering.subagent-driven-development` 或 `engineering.executing-plans` 全部 task 完成。
- 实现工作完成，需要决定如何收尾。

## 不适用场景

- 还有未完成的 task 或未通过测试——先完成再收尾。
- 刚开始开发——先用 `engineering.using-git-worktrees`。

## 执行流程

1. 跑测试（全绿再继续）。
2. 检测环境（普通仓库 / worktree / detached HEAD）。
3. 确定 base 分支。
4. 展示 2-3 个集成选项。
5. 执行用户选择。
6. 清理（仅合并和确认丢弃时）。

## 默认边界

- **读文件**：是。
- **写文件**：否。
- **执行命令**：是（git、测试）。
- **网络**：否（推送和 PR 创建需用户明确授权）。

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。
