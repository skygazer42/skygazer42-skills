---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work
---

# 完成开发分支

## 概述

**核心原则：**验证测试 → 检测环境 → 展示选项 → 执行选择 → 清理。

**开始时宣布：**"I'm using the finishing-a-development-branch skill to complete this work."

## Step 1: 验证测试

跑项目完整测试套件。**若失败**报告失败并停止——菜单在全绿之后才出现。**若通过**继续 Step 2。

## Step 2: 检测环境

检测是普通仓库还是 worktree、分支还是 detached HEAD——决定菜单内容和清理方式。

## Step 3: 确定 base 分支

base 分支是此次工作的 fork 出处——通常来自计划、对话或分支 upstream。不确定时向用户确认。合入错误 base 是不可逆的。

## Step 4: 展示选项

**普通仓库 / 命名分支 worktree — 恰好 3 项：**
1. 本地合并到 `<base-branch>`
2. 推送并创建 PR
3. 保持分支不动

**Detached HEAD — 恰好 2 项（无合并）：**
1. 推送为新分支并创建 PR
2. 保持不动

**丢弃工作仅响应用户明确要求**——确认后再执行。

## Step 5: 执行选择

- 合并本地：merge → 对合并结果跑测试 → 全绿后清理 worktree → 删除分支。
- 推送 PR：`git push -u origin <branch>` → 创建 PR → 保留 worktree。
- 保持不动：报告分支名和 worktree 路径。

## Step 6: 清理

仅合并和确认丢弃时清理。worktree 由谁创建就由谁清理。

## 快速参考

| 选项 | 合并 | 推送 | 保留 worktree |
| --- | :---: | :---: | :---: |
| 合并本地 | ✓ | — | — |
| 创建 PR | — | ✓ | ✓ |
| 保持不动 | — | — | ✓ |

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：Skill 引用中立化；翻译精简。
