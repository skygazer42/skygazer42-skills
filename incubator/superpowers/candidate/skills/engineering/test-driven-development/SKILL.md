---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# 测试驱动开发（TDD）

## 概述

**先写测试。看它失败。写最小代码通过。**

**核心原则：**没亲眼看过测试失败，就不知道它测的东西对不对。

**违反规则的字面就是违反规则的精神。**

## 铁律

```
没有先写失败测试，不写任何生产代码
```

在测试之前写了代码？删掉。重来。

**没有例外：**不保留作"参考"、不在写测试时"改编"、不要看它。删就是删。从测试重新实现。

## Red-Green-Refactor

### RED — 写失败测试

写一个最小测试展示应该发生什么。

- 一个行为。
- 清楚的名字。
- 真实代码（非 mock，除非不可避免）。

### 验证 RED — 看着它失败

**强制。永不可跳过。**

确认：测试失败（非报错）；失败消息符合预期；失败原因是功能缺失（非拼写错误）。

**测试通过了？**你在测已有行为——修正测试。

### GREEN — 最小代码

写最简单代码通过测试。不加功能、不重构其他代码、不"改进"超出测试范围的东西。

### 验证 GREEN — 看着它通过

**强制。**

确认：测试通过；其他测试仍通过；输出干净。

### REFACTOR — 清理

只在全绿之后：去重、改善命名、提取 helper。保持测试绿。不加行为。

### 重复

下一个失败测试 → 下一个功能。

## 实现完成后：路由到领域 Skill

TDD 保证的是**代码行为正确**。实现完成后，根据工作领域验证：

| 工作领域 | 后续步骤 |
| --- | --- |
| 前端 UI / 组件 | `web.frontend-implementation`（确保交互、样式、无障碍） |
| 前端代码审查 | `web.frontend-review` |
| 前端浏览器验证 | `web.frontend-testing` |
| 后端 API / 数据 | `backend.backend-implementation` |
| 后端审查 | `backend.backend-review` |
| 后端排障 | `backend.backend-debugging` |

在声称"完成"之前：`engineering.verification-before-completion`。

## 常见合理化借口

| 借口 | 现实 |
| --- | --- |
| "太简单了不用测" | 简单代码也会坏。写测试只要 30 秒。 |
| "我之后再测" | 事后写的测试直接通过——什么也证明不了。可能测的是实现而非行为。你没看过它失败，所以不知道它能否抓住 bug。 |
| "已经花 X 小时了，删了浪费" | 沉没成本谬误。保持不可信的代码才是浪费。 |
| "先探索一下" | 可以。扔掉探索代码，从 TDD 开始。 |
| "测试难写 = 设计有问题" | 听测试的。难测试 = 难使用。 |

## Red Flags — STOP 并重来

- 测试之前写了代码
- 测试立即通过
- 说不清为什么测试失败
- "之后再加"测试
- "就这一次"合理化
- "我已经手动测过了"

**所有这些都意味着：删掉代码，用 TDD 重新来。**

## 最终规则

```
生产代码 → 存在测试且测试先失败过
否则 → 不是 TDD
```

未经你的人类搭档允许，没有例外。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `test-driven-development` Skill（MIT License）。本地改造：
1. 新增「实现完成后路由到领域 Skill」节。
2. Skill 引用改为 `engineering.*` 命名空间。
3. 将原版 writing-good-tests.md 中的核心原则内联为「好测试」表。
4. 工具名平台中立化。
