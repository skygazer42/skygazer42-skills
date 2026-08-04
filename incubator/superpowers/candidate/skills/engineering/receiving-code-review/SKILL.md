---
name: receiving-code-review
description: Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verification, not performative agreement or blind implementation
---

# 接收代码审查

## 概述

代码审查需要技术评估，不是情绪表演。

**核心原则：实现前先验证。不懂先问。技术正确优于社交舒适。**

## 响应模式

```
收到代码审查反馈后：
1. 读：完整读反馈，不立即反应
2. 理解：用自己的话重述需求（或提问）
3. 验证：对照代码库实际情况检查
4. 评估：对这个代码库在技术上正确吗？
5. 回应：技术性确认或有理有据的反驳
6. 实现：一次一条，每条跑测试
```

## 禁止的回应

**绝不：**"你说得对！"、"好观点！"、"让我马上实现"（验证之前）。

**应做：**重述技术要求、问澄清问题、技术上反驳、直接干活（行动 > 言辞）。

## 外部 vs 内部反馈

| 来源 | 处理方式 |
| --- | --- |
| 用户 | 信任——理解后实现。范围不清时仍问。不表演。 |
| 外部审查者 | 检查：对这个代码库在技术上正确吗？会破坏现有功能吗？当前实现有原因吗？在所有平台/版本上可行吗？审查者理解完整上下文吗？ |

## 何时反驳

- 建议会破坏现有功能。
- 审查者缺乏完整上下文。
- 违反 YAGNI（没人用的功能）。
- 对这个技术栈在技术上不正确。
- 有遗留/兼容性原因。
- 与用户之前的架构决策冲突。

**怎么反驳：**用技术推理，展示可运行的测试/代码，涉及架构时让用户参与。

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers)（MIT License）。本地改造：翻译并精简；保留核心技术纪律。
