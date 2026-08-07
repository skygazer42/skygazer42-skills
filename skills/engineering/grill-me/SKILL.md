---
name: grill-me
description: |
  在干净的对话中对任何想法（代码、业务、写作、产品方向）启动一场无情的审问式访谈。
  不写文件、不依赖仓库、不留工作区——审问结束后只在用户脑子里留下更清晰的方案。
  用于 /grill-me 指令；Agent 不会自动调用。路由到 engineering.grilling 执行实际审问协议。
disable-model-invocation: true
---

# Grill Me — 审问我

启动 `/grilling` 会话，路由到 `engineering.grilling` 执行审问协议。

## 与 grilling 的关键区别

| 维度 | `grill-me`（本 Skill） | `engineering.grilling` |
|------|------------------------|------------------------|
| 角色 | **用户入口**——启动审问 | **执行引擎**——运行审问协议 |
| 依赖 | 不需要仓库，不需要文件 | 可在仓库上下文中查代码证据 |
| 范围 | 任何主题：代码、业务决策、写作、产品方向 | 偏代码/技术决策 |
| 写文件 | 否 | 否 |
| 调用方式 | 用户显式 `/grill-me` | 用户说「grill 我」或被其他 Skill 调用 |

## 怎么做

1. 收到 `/grill-me` 后，按 `engineering.grilling` 的协议开始审问。
2. **全程不写文件、不留工作区。** 这是纯对话——审问的产物是用户脑子里的清晰度，不是工作区里的文档。
3. 默认不需要仓库上下文（用户没说要审代码相关的东西时，别去读仓库）。
4. 审问结束后自然结束——不需要路由到实现 Skill（除非用户要求）。

## 什么时候该用 grill-me 而不是 grilling

- 想法还很模糊，想通过审问让它变清晰。
- 不是在代码仓库里（或者不想让 Agent 读代码）。
- 审的是非代码主题：业务决策、写作、产品方向。
- 想在干净的新对话里开始，不给 Agent 预判上下文。

## 审得了的和审不了的

**审得了的**：可以通过对话回答的问题——「用长文还是三个页面？」「先做哪个功能？」「怎么验证假设？」

**审不了的**：需要看到东西才能判断的问题——「这个交互感觉对不对？」「颜色选哪个？」审不了的事不要硬审，去用 `engineering.prototype` 做个快速原型看了再说。

## 审问成功的标志

- 你有不同意的问题——全程没反驳，说明你不需要这次审问。
- 问题按轮次来，后面轮次明显建立在前面答案之上。
- 你最后到了意料之外的地方——因为有个问题挖出了你一直在无意中做着的决定。
- 审完后，你能对着没参加审问的人解释清楚每个选择的理由。

---

## 来源与改造说明

本 Skill 基于 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `grill-me`（MIT License，commit `84fdeff`），本地改造：

1. 上游 SKILL.md 是极薄触发器（仅 8 行：「Run a `/grilling` session」），保留了 `disable-model-invocation` 和路由到 grilling 的核心机制。
2. 从上游 `docs/productivity/grill-me.md` 提取关键概念注入本文件：stateless / any subject / fresh conversation / grillable vs ungrillable / 成功标志。
3. 将路由目标改为本仓 `engineering.grilling`。
4. 按本仓库目录契约补充 manifest.yaml、中文 README.md、provenance.yaml、tests/cases.yaml。
5. 与已有的 `engineering.grilling` 形成「入口 ← 引擎」的互补关系。