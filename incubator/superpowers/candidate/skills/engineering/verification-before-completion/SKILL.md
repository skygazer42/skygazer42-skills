---
name: verification-before-completion
description: Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always
---

# 声称完成前先验证

## 概述

**核心原则：证据在断言之前，永远。**

**违反这条规则的字面就是违反它的精神。**

## 铁律

```
没有新鲜的验证证据，不能声称完成
```

如果你在这一轮消息里没跑过验证命令，你就不能声称它通过。

## 把关函数

```
在声称任何状态或表达任何满意之前：

1. 识别：什么命令能证明这个声称？
2. 跑：执行完整命令（新鲜、完整）
3. 读：完整输出，检查退出码，数失败数
4. 核实：输出是否确认了声称？
   - 没有？→ 用证据说明实际状态
   - 有？→ 带证据说明声称
5. 只有做完以上：才能声称

跳过任何一步 = 撒谎，不是验证
```

## 根据领域跑对验证命令

| 工作领域 | 至少应跑的验证命令 |
| --- | --- |
| 前端改动 | 项目的前端测试 + lint + build（若 web.frontend-testing 可用则走浏览器验证） |
| 后端改动 | 项目后端测试 + lint + build（若涉及数据则加 migration 检查） |
| 工具/脚本 | `python tools/validate_repository.py` 等仓内校验工具 |
| 文档 | 仔细重读改动，检查链接和残留旧名称 |

## 常见失败

| 声称 | 需要什么 | 不够的 |
| --- | --- | --- |
| 测试通过 | 测试命令输出：0 失败 | 上次跑的，"应该能过" |
| Lint 干净 | Lint 输出：0 错误 | 部分检查，推断 |
| 构建成功 | 构建命令：exit 0 | Lint 通过，日志看起来还好 |
| Bug 已修 | 测试原始症状：通过 | 代码改了，假定修好了 |
| Agent 完成 | VCS diff 显示实际改动 | Agent 报告 "成功" |
| 需求满足 | 逐行检查清单 | "测试都过了" |

## Red Flags — STOP

- 使用"应该"、"大概"、"好像"
- 在验证之前表达满意（"太好了！"、"搞定！"、"完成了！"等）
- 即将提交/推送/PR 但没验证
- 信任 agent 的成功报告
- 依赖不完整的验证
- 觉得"就这一次"
- 累了想结束工作
- **任何暗示成功的措辞，但没跑过验证**

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `verification-before-completion` Skill（MIT License）。本地改造：
1. 新增「根据领域跑对验证命令」节，指向本仓领域验证路径。
2. 合理化借口表翻译为中文。
