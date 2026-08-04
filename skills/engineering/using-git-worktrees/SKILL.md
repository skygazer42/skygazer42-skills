---
name: using-git-worktrees
description: Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via native tools or git worktree fallback
---

# 使用 Git Worktrees

## 概述

确保工作在隔离的工作区中进行。优先用平台原生的 worktree 工具。仅在无原生工具时回退到 git worktree。

**核心原则：**先检测是否已有隔离。再用原生工具。最后回退到 git。不和 harness 对抗。

## Step 0: 检测现有隔离

**创建之前先检查是否已在隔离工作区。** 若已是 linked worktree → 跳过创建。若普通仓库 → 问用户是否创建。

## Step 1: 创建隔离工作区

1a. 原生 worktree 工具（优先）→ 若有就用来创建。
1b. Git worktree 回退 → 仅在无原生工具时使用。选目录、验证 `.gitignore`、创建。

## Step 2: 项目设置

自动检测并安装依赖（npm/cargo/pip/go）。

## Step 3: 验证干净基线

跑测试确保工作区从干净状态开始。

## 快速参考

| 情况 | 动作 |
| --- | --- |
| 已在 linked worktree | 跳过创建 |
| 在 submodule 中 | 视为普通仓库 |
| 有原生工具 | 用它 |
| 无原生工具 | git worktree 回退 |

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：Skill 引用中立化；翻译精简。
