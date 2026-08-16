# 审核报告：autoreview（提交/发布前代码审查门禁）

- 候选来源：`incubator/autoreview/candidate/`（上游 `openclaw/openclaw`，revision `0dd8d3ea`，原路径 `.agents/skills/autoreview`）
- 审核日期：2026-08-16
- 审核人：skygazer42（由 AI 代审）
- 结论：**有条件通过**——核心能力真实且工程上扎实，但存在「与现有 review 类 Skill 边界重叠」「OpenClaw 组织专属内容占比高」「默认引擎是 Codex」三个需要仓库所有者决策的点，见文末。

---

## 1. 是否解决个人工作流中的真实问题

是。它提供的是一种「提交/发布前自动审查门禁」：把待审变更打包 → TruffleHog 密钥扫描 → 调用外部模型引擎在隔离环境做结构化审查 → 输出按严重度分级的发现。与「人参与、由主 Agent 自己读代码审查」的现有 Skill 是不同的工作时刻（closeout gate vs 按需审查），对需要更高审查置信度的变更（安全审计、发布前）有真实价值。

但价值前提是：**用户确实安装了 `codex`（默认引擎）/ `claude` / `pi` CLI 与 `trufflehog`**，并且接受把待审代码发给 OpenAI / Anthropic 的外部模型引擎。

## 2. 与现有 Skill 的重叠

| 现有 Skill | 与 autoreview 的关系 |
| --- | --- |
| `engineering.code-review` | 同属「代码审查」领域。但前者是超级技能式的「请求审查 + 接收反馈 + 先验证再实现」对话协议，由主 Agent 与用户协作；autoreview 是**自动化门禁**，打包 diff + 密钥扫描 + 调外部引擎，含 1.2 万行辅助脚本。机制与产出完全不同，边界需在 README 写清 |
| `backend.backend-review` / `web.frontend-review` | 领域化的人工审查清单，无外部引擎、无密钥扫描，不冲突 |

**结论**：机制上不重复，但同属「review」领域，若两套并存需明确分工：autoreview 是**发布前的自动化外审+密钥扫描门禁**，其它 review 是**主 Agent 人工审查流程**。

## 3. SKILL.md 与脚本的隐式写入 / 对外副作用

- **默认只写 stdout**；文件输出仅当 `--output` / `--json-output` / 流式引擎 stderr 开启。
- 临时工作区与测试隔离 home 在系统 `/tmp` 下，`--parallel-tests` 用后即删。
- **不 push**：SKILL.md 明确「Do not push just to review. Push only when the user requested push/ship/PR update」。
- 不写 `.env`、不改全局配置；引擎凭据由用户已有的 CLI 自带。
- 会创建临时 git 快照与空工作区供引擎审查，范围受控。

## 4. 密钥 / 个人数据 / 敏感信息 —— 本 Skill 按设计就是密钥敏感型

- **TruffleHog 扫描**：对精确新增/修改/删除内容做 `verified,unknown` 低误报扫描；对「整文件删除且仅出现在删除行」的疑似密钥**就地打码**；若删除值也出现在新增/上下文/混合暂存内容中则 **fail closed**（拒绝审查）。
- TruffleHog **绝不自动安装**：缺失时报错并给官方安装链接。
- 引擎调用前会剥离 process-injection、Git override、带凭据的代理变量；隔离环境内运行（Codex 空工作区 + `--ignore-rules`，Claude `--safe-mode` + 禁文件/Shell 工具，Pi `--no-tools`）。
- 风险面：外部引擎会把**打包后的 diff 文本发送到 OpenAI / Anthropic**（Codex/Claude/Pi 的模型调用），这是 Skill 的核心用途，但属于必须声明的数据外发。TruffleHog 只降低「密钥进引擎」的概率，不消除「代码出域」的事实。

## 5. 远程执行 / 网络行为 / 遥测

- **无** `curl|bash`、无远程脚本下载、无遥测。脚本自身只做 URL 解析（`urllib.parse`），不直接发 HTTP。
- 会 `subprocess` 调用已安装的外部 CLI：`codex` / `claude` / `pi` / `trufflehog` / `gh` / `git`，并传入严格隔离 flag。
- Droid / Copilot / Cursor / OpenCode **fail closed**：因当前 CLI 契约无法把项目指令、文件读取、网络抓取限制在审查边界内。
- 风险点：`--parallel-tests` 的隔离 Testbox home 会 staged Blacksmith 凭据——SKILL.md 明确「narrow trusted-maintainer-code exception」，不可用于不可信分支代码。属设计内高风险路径，必须保留限制声明。

## 6. 路径 / 命令 / 失败安全性

- 文件写入大量使用 `os.open(..., dir_fd=...)`（openat 风格）防符号链接逃逸；输出目标先 `resolve()`。
- 外部命令只从绝对 `PATH` 解析，不从被审仓库解析（防仓库内恶意可执行文件劫持）。
- 退出码契约清晰；心跳行标识 30 分钟长审查仍在运行，非挂死。
- 整体防御性明显优于普通 skill 脚本；未见明显命令注入。

## 7. 平台绑定与可移植性

- **默认引擎是 Codex**（`gpt-5.6-sol` → 访问失败重试 `gpt-5.6-terra`）；Claude（`claude-fable-5`）与 Pi 为可选。需要对应 CLI 版本（Claude `v2.1.169+`、Pi `v0.79.0+`）。
- `scripts/autoreview` 是纯 Python 3（约 1.2 万行），可移植；Windows 有 `.ps1` 封装。
- 上游 SKILL.md 有大量 **OpenClaw 组织专属内容**：`clawsweeper[bot]` 自动合并追踪、`gitcrawl` shim、`Blacksmith` 凭据 staged、发布分支冻结纪律、组织默认模型等。内化时必须剥离，否则不可读、不可用。
- skill 内 AGENTS.md 声明 canonical source 是 `openclaw/agent-skills`（本仓是下游副本）——内化以本次固定的 revision 为准即可。

## 8. 署名 / 外链 / 对外状态

- 无强制署名、无外链植入、无案例上传。review 面板（`--reviewers codex,claude,pi`）默认关闭，需显式启用。

## 9. License

- **MIT**（Copyright (c) 2026 OpenClaw Foundation），允许复制与修改，需保留版权声明（`candidate/LICENSE` 已随附）。上游 `THIRD_PARTY_NOTICES.md` 仅涉及 OpenClaw 整体对 Pi 的依赖，与 autoreview 无关，不需随附。

## 10. README 宣传是否属实

- SKILL.md 与脚本实现一致度高：隔离 flag（`--safe-mode`、`--ignore-rules`、`--no-tools` 等）、TruffleHog 策略、退出码、心跳行为均能在脚本中找到对应实现。抽查未见明显夸大。

---

## 结论与需仓库所有者决策的点

**核心判断**：这是工程上扎实、安全设计优秀的工具（密钥扫描 + fail-closed + 引擎隔离 + 防御性文件处理），引入价值真实。但相对本仓库现有 Skill 有三个特殊性，直接决定要不要、以及以什么形态引入：

1. **与 `engineering.code-review` 的边界**：是否需要一个自动化外审门禁，还是维持轻量人工审查即可？
2. **默认引擎是 Codex**：本仓库以 Claude Code 为主，若用户不常跑 `codex` CLI，默认引擎价值打折（可改用 `--engine claude`，但那是改动上游默认）。
3. **组织专属内容占比高**：SKILL.md 里 clawsweeper/gitcrawl/Blacksmith/发布冻结等大量内容与个人工作流无关，内化意味着「只保留核心契约 + 1.2 万行脚本 + 引擎隔离说明」的大幅裁剪，且 1.2 万行脚本作为正式 Skill 内容很重。

**我的建议**：若决定引入，采用「做减法」形态——保留 helper 脚本与核心契约、剥离组织政策、明确与 `engineering.code-review` 的分工，归类 `engineering`，并如实声明「外发代码给第三方模型引擎 + 需 codex/claude/pi/trufflehog」。若这些前提用户不满足，建议先留在孵化区不发布。
