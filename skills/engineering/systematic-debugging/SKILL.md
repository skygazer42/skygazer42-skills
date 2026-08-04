---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# 系统性排障

## 概述

**核心原则：永远先找到根因再尝试修复。修复症状是失败。**

**违反这个流程的文字就是违反排障的精神。**

## 铁律

```
不先做根因调查，不提任何修复
```

如果你没完成 Phase 1，就不能提修复方案。

## 四阶段

你必须完成每个阶段再进入下一个。

### Phase 1: 根因调查

**在尝试任何修复之前：**

1. **仔细读错误信息**——不要跳过错误或 warning，它们常含精确答案。完整读 stack trace。注意行号、文件路径、错误码。

2. **一致复现**——能可靠触发吗？精确步骤是什么？每次都发生吗？若不可复现→收集更多数据，不要猜。

3. **检查最近变更**——什么变了？`git diff`、最近提交、新依赖、配置变化、环境差异。

4. **多组件系统中收集证据**——在每个组件边界记录：什么数据进来、什么数据出去。跑一次收集证据，看断在哪里。

5. **追踪数据流**——从错误点逐层往上游追踪，找到原始触发点。在源头修，不在症状处修。

### Phase 2: 模式分析

**找模式再修：**

1. 找同代码库中相似且正常工作的代码。
2. 对比参考实现——不要略读，逐行读完。
3. 列出正常和异常之间的每一个差异，不假设"那个不可能"。
4. 理解依赖——这个组件还需要什么？什么设置、配置、环境？

### Phase 3: 假设与验证

**科学方法：**

1. 形成单一假设——"我认为 X 是根因，因为 Y"。写下来，要具体。
2. 最小测试——做最小修改来验证假设。一次一个变量。
3. 验证再继续——有效？→ Phase 4。没效？→ 形成新假设。不要在上面叠更多修复。
4. 不懂就说"我不理解 X"。不要假装懂。

### Phase 4: 实施修复

**修根因，不修症状：**

1. **创建失败测试用例**——用 `engineering.test-driven-development` 写正确的失败测试。修复之前必须有测试。
2. **实施单一修复**——针对已确认的根因，一次一个改动。不顺手"改进"。
3. **验证修复**——测试通过？其他测试全绿？问题真的解决了？用 `engineering.verification-before-completion` 再声称成功。
4. **如果修复无效**——停。数一下试了几次？<3→回到 Phase 1 重新分析。**≥3→停下来质疑架构**。不要试第 4 次。

## 路由到领域 Skill

| 问题领域 | 应路由到的 Skill |
| --- | --- |
| 后端 API 错误 / 超时 / 数据库异常 | `backend.backend-debugging` |
| 前端 UI 异常 / 浏览器报错 | `web.frontend-testing` |
| 后端代码行为正确性 | `backend.backend-review` |
| 前端代码行为正确性 | `web.frontend-review` |

`systematic-debugging` 提供**通用方法论**；领域 Skill 提供**领域专属工具和诊断路径**。两者互补——先用方法论定范围，再把领域问题路由到领域 Skill。

## Red Flags — STOP 并回到流程

- "先快速修一下，等下再查"
- "试试改 X 看看行不行"
- "一次改好几个东西，一起跑测试"
- "跳过测试，手动验证"
- "应该是 X，修它"
- "再来一次修复"（已经试了 2+ 次）
- 在追踪数据流之前就提解决方案

**所有这些都是：停。回到 Phase 1。**

---

## 来源与改造说明

基于 [obra/superpowers](https://github.com/obra/superpowers) 的 `systematic-debugging` Skill（MIT License）。本地改造：
1. 新增「路由到领域 Skill」节（backend-debugging / frontend-testing 等）。
2. Skill 引用改为 `engineering.*` 命名空间。
3. 合理化借口表翻译为中文。
4. 原版附属参考文件（root-cause-tracing.md 等）移入 `references/`。
