---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to decide how to integrate the work
---

# 完成开发分支

## 概述

**核心原则：**验证测试 → 检测环境 → 展示选项 → 执行选择 → 更新规格 → 清理。

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

- 合并本地：merge → 对合并结果跑测试 → 全绿后继续 Step 6。
- 推送 PR：`git push -u origin <branch>` → 创建 PR → 保留 worktree → 跳过 Step 6 清理（PR 迭代需要 worktree）。
- 保持不动：报告分支名和 worktree 路径 → 跳过清理。

## Step 6: 更新 Living Specs（借鉴 OpenSpec Archive）

**合并成功后，检查是否需要更新规格文档。** 规格腐烂（spec rot）是常见问题——实现过程中发现的约束、做出的取舍、实际与设计的不一致，如果不写回文档，下次读时就过期了。

检查本仓库是否存在 `docs/specs/` 下的相关设计文档：

1. 对比实际实现和原始设计：有差异吗？有新的约束吗？有什么取舍是"实现时才发现的"？
2. 向用户报告：
   > "实现完成。我注意到设计中提到的 `<设计假设>`，实际实现时变成了 `<实际做法>`。需要我更新规格文档 `docs/specs/<path>` 吗？"
3. 若用户说"要"——更新对应的 spec 文件，在末尾追加一节 `## 实现偏差` 或直接修正原文，标注日期。
4. 若没有 `docs/specs/`、或没有偏差——跳过。

**这一步只做一次确认，不由你自行决定。**

## Step 7: 清理

仅合并和确认丢弃时清理。worktree 由谁创建就由谁清理。

## 快速参考

| 选项 | 合并 | 推送 | 保留 worktree | 更新 spec |
| --- | :---: | :---: | :---: | :---: |
| 合并本地 | ✓ | — | — | 检查 |
| 创建 PR | — | ✓ | ✓ | —（PR 迭代完再更新） |
| 保持不动 | — | — | ✓ | — |

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License），第二轮改造借鉴了 [OpenSpec](https://github.com/Fission-AI/openspec) 的 archive 概念（自动更新 living specs）。本地改造：
1. 新增 Step 6「更新 Living Specs」——合并后检查是否需回写设计文档。
2. Skill 引用中立化。
3. 翻译精简。
