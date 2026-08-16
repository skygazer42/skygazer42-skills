# 审核报告：pi-shadow-mind（Pi 并行认知运行时 / Shadow Mind）

- 候选来源：`incubator/pi-shadow-mind/candidate/`（上游 `liuzhengdongfortest/pi-shadow-mind`，revision `ba75a670`，repo 根）
- 审核日期：2026-08-16
- 审核人：skygazer42（由 AI 代审）
- 结论：**有条件通过**——工程扎实、安全设计优秀，但**它不是一个 skill，而是 Pi 运行时的 npm 扩展**。脱离 Pi 运行时无法运行，与仓库现有 skill 形态不兼容。是否引入、以什么形态引入，需仓库所有者决策，见文末。

---

## 1. 是否解决个人工作流中的真实问题

是，且独特。它提供的是「并行认知运行时」：在主 Agent 持续推进的同时，让多个持久职责的 Shadow Mind 独立审阅决策、核验事实、维护文档，并在错误变得昂贵之前介入（`Build and review in the same pass`）。4 个内置认知核心：架构审阅、项目事实核验、文档维护、完成度审阅。

问题在于**触发场景与实现载体分离**：这个能力由 Pi 运行时提供（heartbeat 调度 + 临时 AgentSession + 净化轨迹），不是本仓库能直接调用的 skill。若用户不运行 Pi，则价值为零；若用户运行 Pi，则完整扩展直接 `pi install npm:pi-shadow-mind@0.1.10` 即可，内化进本仓库反而是复制源码。

## 2. 与现有 Skill 的重叠

| 现有 Skill | 与 pi-shadow-mind 的关系 |
| --- | --- |
| `engineering.code-review` / `engineering.verification-before-completion` / `engineering.systematic-debugging` | 4 个认知核心在**职责**上与之重叠（架构审阅≈code-review、完成度审阅≈verification-before-completion、事实核验≈systematic-debugging 的根因调查前提）。但**机制**完全不同：那些是主 Agent 与用户协作的对话协议，Shadow Mind 是运行时级、并行的独立临时 Agent |
| `engineering.autoreview` | autoreview 是发布前的自动化外审门禁（打包 diff + TruffleHog + 外部引擎）；Shadow 是持续的、随 heartbeat 并行唤醒的认知核心。方向不同（门禁 vs 常驻并行审阅） |

**结论**：职责有重叠，机制全新。仓库里没有任何「并行认知核心」这类运行时机制。

## 3. SKILL.md 与脚本的隐式写入 / 对外副作用

- 全部文件写入集中在 `~/.pi/agent/shadow-minds/`（config.json + Shadow Markdown + 仅 debug 时的 logs/）。无 push、无远端改动。
- **所有写操作都经 `ctx.ui.confirm`**：AI 发起的 create/update/enable/disable/delete/config 写都要求 UI 确认；无 UI（headless）直接抛错拒绝。
- 创建用 `flag: "wx"`（不覆盖既有文件）；delete 只删 `.md` 定义、保留 debug 日志。
- config 采用 last-known-good：无效配置不覆盖用户文件，仅显示错误并沿用上次有效值。

## 4. 密钥 / 个人数据 / 敏感信息

- **净化轨迹**：Shadow 只接收净化后的纯文本轨迹——移除 Main 的 thinking、完整工具结果；工具调用**参数原样保留**，结果只留确定性概述。
- **数据外发**：Shadow 用 `run_with_model` 指定的模型时，净化轨迹（含工具调用参数，可能含密钥/令牌）会发给该模型供应商；若与 Main 同供应商，则仍是同一条模型通道。DESIGN.md 第 250 行明确声明了这一信息边界，要求用户配置执行模型时接受。
- **debug 日志**：`debug: true` 时保存完整 Session JSONL（含净化轨迹、Shadow thinking、其读取的项目内容），存于用户目录 logs/，默认关闭、不自动清理。属用户可控的敏感数据保留。
- 设计良好：Main thinking 与完整工具结果永远不进 Shadow 上下文。

## 5. 远程执行 / 网络行为 / 遥测

- **无**：src/ 全量扫描无 `fetch`/`http`/`WebSocket`/child_process/exec/spawn/eval/new Function/vm/遥测（无 posthog/sentry/analytics）。
- 唯一网络面是 Pi 自身的模型调用通道（Shadow 的模型推理），由 Pi 管线承载，插件不自行建连。
- 插件只做本地文件读写与调度；不下载、不执行远程脚本。

## 6. 路径 / 命令 / 失败安全性

- **ID→路径无遍历**：`id` 双重校验 `^[a-z0-9][a-z0-9_-]*$`（typebox 参数层 + registry 解析层），`join(dir, id.md)` 安全。
- 工具白名单显式授权：`tools` 之外的写入/Shell 能力不隐式继承自 Main；列入白名单即视为用户授权该 Shadow 直接调用，插件不增加逐次确认（DESIGN 明确「白名单本身就是授权」）。
- 并发边界诚实声明：不承诺文件级写入互斥，用户给 Shadow 配写入工具即接受与 Main 并发冲突的风险——这是设计上的明确取舍，不是隐瞒。
- 上游 AGENTS.md 的发布流程含防御性路径检查（release/ 清理前校验绝对路径）。

## 7. 平台绑定与可移植性

- **硬绑定 Pi**：peer deps 全为 `@earendil-works/pi-*`（agent-core/ai/coding-agent/tui）+ typebox；用 Pi 扩展 API、`/shadow` 命令、Pi SDK `readOnlyTools`；需 `npm install && npm run build`（tsc + esbuild）产出 `dist/index.js` 后由 `pi install` 加载。
- 仓库当前环境（Claude Code）**无法直接运行**。内化为 skill 只能得到一份需要 Pi + 完整 Node 构建才能使用的源码树。
- 可移植的是**概念层**：Shadow Markdown 定义（普通 Markdown + frontmatter）是平台无关的「认知核心」描述，可适配到其他 Agent。

## 8. 署名 / 外链 / 对外状态

- 无强制署名、无外链植入、无案例上传。README 双语，MIT 声明作者 liuzhengdongfortest。

## 9. License

- **MIT**（Copyright (c) 2026 liuzhengdongfortest），允许复制与修改，需保留版权声明（`candidate/LICENSE` 已随附）。无第三方 notices 依赖。

## 10. README 宣传是否属实

- 抽查全部属实：heartbeat 1/3、max_parallel_shadows 2、默认超时 300s、聚合窗 400ms、默认 thinking low、`report_to_main` 终止本轮（`terminate: true`）、debug 日志默认关、last-known-good 配置、`/shadow` 系列命令、管理工具需确认——均在 `src/config.ts` / `src/shadow-runner.ts` / `src/management-tools.ts` 找到对应实现。
- 12 个 vitest 测试文件覆盖 config/protocol/registry/runner/scheduler/session-lifetime/trajectory 等核心模块，工程可信度高于仓库内多数 skill。

---

## 结论与需仓库所有者决策的点

**核心判断**：这是工程扎实、安全设计优秀（净化轨迹 + UI 确认 + ID 正则 + last-known-good + 无网络无遥测）的 Pi 运行时扩展。引入价值真实，但**形态不兼容是本仓库的 Skill 契约**——它不是行为型 skill，是编译型 npm 扩展，且只在 Pi 上可运行。相比 gpt-image（CLI 工具，可随 skill 直接跑）与 autoreview（纯 Python helper，跨平台），它缺少「可移植执行体」。

三个决策点：

1. **运行时依赖**：是否接受「内化后仍需 `pi install npm:pi-shadow-mind` + 完整 Node 构建才能用」？若不运行 Pi，完整源码内化是死重。
2. **形态**：(a) 完整内化整个 TS 项目为 `engineering.shadow-mind`；(b) 只内化「概念 + 4 个认知核心定义」为可移植的行为 skill（适配本仓库的 Agent 环境，脱离 Pi 也能用）；(c) 两者都要（行为 skill 为主 + 完整源码进 references/ 供 Pi 用户）；(d) 放弃。
3. **与现有 review 类 skill 的分工**：认知核心与 `engineering.code-review` / `verification-before-completion` 职责重叠，若引入需在 README 写清边界。

**我的建议**：若用户运行 Pi，直接 `pi install` 上游即可，本仓库内化完整源码收益低；若想要「并行认知核心」这个能力，最有价值的内化形态是 (b) 或 (c)——把 Shadow Mind 的**概念与认知核心定义**沉淀为可移植 skill，运行时机制作为来源记录而非复制品。
