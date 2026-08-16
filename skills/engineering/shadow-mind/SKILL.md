---
name: shadow-mind
description: Run parallel cognitive cores (architecture review / project grounding / documentation maintenance / completion review) alongside the main line of work — each core owns one persistent responsibility and decides independently when to intervene; adapted from the Pi Shadow Mind runtime
---

# 并行认知核心（Shadow Mind）

## 这是什么

「让实现与审阅发生在同一轮工作中。」主 Agent 持续推进主线任务；同时存在多个**持久、独立**的认知核心，各自认领一项稳定职责（架构审阅、项目事实核验、文档维护、完成度审阅），在主 Agent 工作的过程中独立决定何时检查、行动或汇报，并在错误变得昂贵之前介入。

这不是主 Agent 临时委派的任务，也不是一次性的代码审查请求。核心是持续存在的认知角色：**它决定是否介入，而不是被叫来审查**。

本 Skill 是 Pi Shadow Mind 运行时（`liuzhengdongfortest/pi-shadow-mind`，MIT）的**可移植概念层**。上游用 TypeScript 运行时（heartbeat 概率唤醒、临时 AgentSession、净化轨迹）承载这一能力；本仓库不内化该运行时，只内化**认知核心的契约与定义**，适配到本仓库的 Agent 环境。若你运行 Pi，直接 `pi install npm:pi-shadow-mind@0.1.10` 可获得运行时本体（见 `provenance.yaml`）。

## 何时使用

- 主 Agent 正在实现一个**中等以上复杂度**的变更（会动到多个模块、接口、状态），且你希望实现过程中就有人独立盯着架构、事实、文档和完成度。
- 在**大改动的实现中途**、**声称完成之前**这两个时刻，需要独立于主 Agent 的核验视角。
- 你希望文档随实现同步更新，而不是事后补。
- 需要防止主 Agent 编造项目事实、遗漏约束、错误路线。

## 何时不用

- **没有持续的主线工作**（纯问答、单次查询）——没有「并行」可言。
- 变更只是纯文案 / 文档小改——用轻量检查，不要拉起整套认知核心。
- 需要**发布前的自动化外审门禁**（打包 diff + 密钥扫描 + 外部引擎）→ 用 `engineering.autoreview`。
- 需要一次性的、由主 Agent 主导的代码审查对话 → 用 `engineering.code-review`。
- 需要主 Agent 自己先跑验证再声称完成 → 用 `engineering.verification-before-completion`（完成度审阅核心是其独立旁证，不是替代）。

## 认知核心铁律

每个认知核心（无论哪个职责）必须遵守：

1. **一项职责，持久存在**。每个核心只认领一个责任域，不贪多。
2. **独立决定介入**。核心根据职责判断当前工作是否相关；不相关就沉默。
3. **证据优先，永不编造**。只报告能从轨迹或仓库得到证据的问题；先用自己的工具核实，再下结论。
4. **报告一条、可行动**。有发现时给一条简洁状态：引用具体证据 + 最有效的下一步；没有发现时输出固定的 `check: OK` 行；不重复已报且已解决的问题。
5. **不接管主任务**。核心的产出是报告与（对写职责核心而言的）维护动作，不是替主 Agent 做实现决定。
6. **有界检查**。一次疑点用有限的读/grep 工具确认后即收手，不演变成全仓审计。

## 部署：两种方式

### 方式一：并行子代理（贴近上游，首选）

在本仓库支持子代理的环境中，把每个启用的认知核心当作一个**并行子代理**派发：

- 给每个核心：本 Skill 的净化工作轨迹（见「上下文纪律」）+ 对应 `references/<core>.md` 定义。
- 核心并行运行，各自决定是否报告；主 Agent 不阻塞等待。
- 子代理的派发/收口机制参考 `engineering.subagent-driven-development`；本 Skill 只规定认知核心的契约。
- 报告按核心来源归名（如 `[架构审阅]`、`[完成度审阅]`），不伪装成用户消息。

### 方式二：检查点佩戴（串行，无子代理时）

在**实现完成一个实质阶段**与**声称完成之前**两个检查点，按顺序逐个运行启用的认知核心的审查 pass。每次佩戴一个核心的职责视角，独立检查并产出报告，然后换下一个。

## 上下文纪律（净化轨迹）

核心能看到的，是主 Agent 工作的**净化文本轨迹**：用户消息、主 Agent 的普通文本、工具调用及其结果概述（如 `read(src/auth.ts) · 成功，返回 186 行`）。**不是**：

- 主 Agent 的思考 / 推理过程；
- 工具返回的完整内容；
- 其他核心未上报的推理。

核心**不继承主 Agent 的证据链**——需要核实时用自己分配的工具重新调查，形成独立证据。工具调用参数可能含敏感信息，核心报告时不得转述密钥、令牌等凭据。

## 报告契约

- 报告要么是「一条差异 + 引用证据 + 最有效下一步」，要么是固定的 `check: OK`。不输出空报告、不提出「更美」的重构、不引入可选工作。
- 报告可来自主 Agent 工作中的介入（steer）或完成后的补充；**用户已开启新任务后**，迟到的旧结果作废，不投递。
- 主 Agent **在采纳任何发现前先核验**（读真实代码路径，判断是否成立）；拒绝有依据的发现时，只在确有必要时留一行内联注释说明不变量/归属决定。

## 工具纪律

- 认知核心**默认只读**（read / grep / Glob / ls）。只读核心永不请求写文件或执行命令。
- 只有职责要求写文件的核心（如文档维护）才被授予 `write`；**授予即视为授权**，该核心可直接写，不逐次确认——这同时意味着接受它与主 Agent 并发写同一文件的冲突风险。
- 文档维护核心默认只写它负责的文件（`docs/`、`README`、架构说明），不碰代码与测试。

## 停止规则 / Red Flags

- 核心开始「顺便」修主 Agent 的代码、改测试、重写实现 → STOP，它越界了。
- 报告变成完整重构方案、长篇设计文档 → 违背「一条、可行动」。
- 主 Agent 花在核验核心报告上的时间超过做主线工作 → 停用多余核心或降低介入频率。
- 核心报告没有证据支撑的「我觉得」→ 违反铁律 3，丢弃该条。
- 迟到的旧核心结果在新任务开始后才到 → 作废，不投递（epoch 纪律）。

## 参考核心

`references/` 下 4 个现成认知核心定义，可直接部署：

| 核心 | 职责 | 写权限 |
| --- | --- | --- |
| `architecture-review.md` | 架构审阅——上帝组件/职责错位/边界缺失/错误扩展点 | 只读 |
| `project-grounding.md` | 项目事实核验——编造 API/文件/约束/未证实的断言 | 只读 |
| `documentation-maintenance.md` | 文档维护——架构说明/决策/用法随实现同步 | 可写（只写文档） |
| `completion-review.md` | 完成度审阅——独立裁决「是否真完成」 | 只读 |

它们只是起点。认知核心是**可扩展的**：新视角 = 新 Markdown 定义。按上述铁律写自己的核心即可。

## 来源与改造说明

基于 [liuzhengdongfortest/pi-shadow-mind](https://github.com/liuzhengdongfortest/pi-shadow-mind)（MIT License, Copyright (c) 2026 liuzhengdongfortest）的 Shadow Mind 概念与认知核心定义。本地改造：
1. 剥离 TypeScript 运行时（heartbeat 调度、临时 AgentSession、净化轨迹构建、`report_to_main`、/shadow 面板）——本仓库不内化编译型 Pi 扩展。
2. 保留并适配「持久认知核心 + 独立介入 + 有界报告」的行为契约，部署为并行子代理 / 检查点两种本仓可用的方式。
3. 4 个认知核心定义改为平台无关的职责卡（去除 activation_probability / run_with_model / timeout_seconds 等运行时字段，工具名适配本仓环境），并吸收上游 benchmark 定义的报告纪律（固定 OK 行、有界核验、单条最有效行动）。
4. 明确与 `engineering.code-review` / `verification-before-completion` / `autoreview` 的分工。
