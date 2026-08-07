# Grill Me — 审问我

## 一句话定位

在干净对话中对**任何想法**启动一场无情的审问式访谈。不写文件、不依赖仓库、不留工作区——审问的价值是用户脑子里的清晰度，不是磁盘上的文档。

## 适用场景

- 有一个模糊但值得认真对待的想法——功能、产品方向、业务决策、写作主题
- 想被「灵魂拷问」，把藏着的假设和没想清的依赖挖出来
- 不在代码仓库里（或不想让 Agent 读代码），只想纯对话
- 在动手之前想确认方案经得起推敲

## 不适用场景

- 已经有可执行的详细规格——直接 `engineering.writing-plans`
- 只是想探索可能性、没有成型的想法——用 `engineering.brainstorming`
- 需要审问 + 把结论记录到仓库——用 `engineering.grilling` + `engineering.grilling-with-docs`（规划中）
- 需要看到实物才能判断的问题——先 `engineering.prototype` 做原型

## 执行前需要的信息

**零。** 不需要仓库、不需要文件、不需要预先准备。有一个想法就够了。想法模糊不是问题——正是 grill-me 要处理的原材料。

## 执行流程

1. 用户输入 `/grill-me` 并描述想法
2. 按 `engineering.grilling` 的审问协议开始：决策树 → 前端问题 → 每轮全量 + 推荐答案 → 等用户回答
3. 全程不写文件、不读仓库（除非用户明确说「去查一下 XX」）
4. 前端清空（所有分支都已访问，没有沉默的假设）时审问结束
5. 不自动路由到实现——审问结束后用户自己决定下一步

## 交付结果

- 用户脑子里更清晰的方案（不是文件）
- 对话上下文可以直接交给 `engineering.writing-plans` 或 `engineering.to-spec` 继续

## 默认边界

- **读文件**：否
- **写文件**：否
- **执行命令**：否
- **网络**：否
- **依赖本仓 Skill**：`engineering.grilling`

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.grilling` | grill-me 是**用户入口**（stateless / any subject / fresh conversation）；grilling 是**执行引擎**（可在仓库上下文中查证据） |
| `engineering.brainstorming` | 建设性探索；grill-me 是批判性审问 |
| `engineering.writing-plans` | 把已确定的方案拆成计划；grill-me 帮你把方案先确定下来 |
| `engineering.grilling-with-docs` | 规划中——审问 + CONTEXT.md + ADR 记录 |

## 行为案例

### 案例 1：典型审问

**输入**：用户说 `/grill-me 我想把单体拆成微服务，但不确定从哪里开始`

**预期行为**：
1. 不读仓库（没有要求）
2. 按决策树开始审问：先确认为什么要拆 → 当前痛点是开发速度还是部署可靠性 → 数据怎么拆 → 团队能不能接住
3. 每轮给推荐答案并等用户回应
4. 前端清空后自然结束
5. 全程不写任何文件

### 案例 2：审不了的就叫停

**输入**：用户说 `/grill-me 这个按钮放在左边还是右边更好`

**预期行为**：
1. 意识到这是「ungrillable」——需要通过原型看到实物才能判断
2. 不做无效审问，建议用户用 `engineering.prototype` 做快速原型看了再决定

### 案例 3：用户要求查仓库

**输入**：用户说 `/grill-me 我们的认证模块怎么重构`，并在审问中说「帮我看下现有的 auth 代码」

**预期行为**：
1. 此时切换到 `engineering.grilling` 的仓库上下文模式
2. 读取代码、搜索相关文件，在事实证据基础上继续审问
3. 但仍不写文件

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `grill-me`（MIT License，c 2026 Matt Pocock）。上游 SKILL.md 为极薄触发器（仅 8 行），本实现从配套文档 `docs/productivity/grill-me.md` 提取关键概念并注入本仓上下文。详见 `provenance.yaml`。