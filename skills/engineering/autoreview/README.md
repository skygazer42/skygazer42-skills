# autoreview · 提交/发布前自动化代码审查门禁

## 一句话定位

把待审变更打包（本地脏改动 / branch / commit / PR），先跑 TruffleHog 对精确新增/修改/删除内容做密钥扫描，再调用外部模型引擎（Codex 默认，Claude / Pi 可选）在严格隔离环境做结构化审查，输出按严重度分级的发现。这是一个**closeout gate**——在提交/发布前把变更再过一遍的自动化外审，不是主 Agent 自己读代码的人工审查。

> 重要前提：它会把你打包好的 diff 文本发送给第三方模型引擎（OpenAI / Anthropic）。TruffleHog 只降低「密钥进引擎」的概率，不消除「代码出域」的事实。使用前需接受这一点。

## 适用场景

- 用户在提交 / 发布 / 合并前明确要求 **Codex review / Claude review / Pi review / autoreview / 第二模型审查**。
- 非平凡代码改动之后、`final` / 提交 / 发布之前，做一次门禁式外审。
- 修复后需要复查本地分支或 PR 分支。
- 需要更高审查置信度的变更（安全审计、发布前、大 diff）。

## 不适用场景

- **纯文案内部笔记 / 文档改动**：整个 diff 只是 prose-only 内部笔记或 `SKILL.md` 文档时，不强制跑 autoreview；直接读 diff 并跑仓库的轻量文档校验即可。此例外**不**覆盖用户可见文档、可执行示例、配置、脚本、生成文件或行为变更。
- **行为验证**：autoreview 只判定「变更包与代码一致、没有可操作的问题」，**不是**证明 UI / CLI / API / 生成产物在用户视角可用。验证产物是否可用请交给测试 / smoke 类 Skill。
- **按需人工审查**：需要主 Agent 与你协作、逐条讨论、先验证再实现的审查对话，走 `engineering.code-review`。
- **领域化人工清单**：后端 / 前端专项审查清单走 `backend.backend-review` / `web.frontend-review`，它们无外部引擎、无密钥扫描。
- **没有安装引擎/工具**：未装 `codex`（或 `claude` / `pi`）与 `trufflehog` 时价值不成立——缺引擎会明确报错给指引，但不会自动安装。

## 执行前需要的信息

- **变更目标**：本地脏改动 / branch / commit / PR。branch 模式需提供 `--base`（如 `origin/main`），或已有可解析的 PR base（`gh pr view` 自动探测）。
- **（可选）审查上下文**：repo 相对路径的 `--prompt-file`（如 `review-notes.md`）与 `--dataset`（如 `evidence.json`）。必须是 repo 相对路径，防止审查包拉取任意宿主文件。
- **（可选）引擎选择**：默认 Codex；`--engine claude` / `--engine pi`，或 `--reviewers codex,claude,pi` 面板。`--model` / `--thinking` 全局或按引擎覆盖。
- **（可选）并行测试**：`--parallel-tests "<focused test command>"`，与审查并行跑聚焦测试。
- **环境**：`git`；`trufflehog`（必须，缺失即报错并给出官方安装链接，绝不自动安装）；至少一个可用引擎 CLI（`codex` 默认，`claude` v2.1.169+ / `pi` v0.79.0+ 可选）；引擎的凭据由对应 CLI 自带。
- **路径一次性设置**：`export AUTOREVIEW="skills/engineering/autoreview/scripts/autoreview"` 与 `AUTOREVIEW_HARNESS=".../test-review-harness"`（Windows 用 `.ps1` 变体）。

## 执行流程

1. **设路径**：一次性设置 `$AUTOREVIEW` 与 `$AUTOREVIEW_HARNESS`。
2. **选目标**：本地脏改动 `--mode local`；分支/PR `--mode branch --base origin/main`（或 `gh pr view` 取真实 base）；已落地的单提交 `--mode commit --commit HEAD`。不强制在已提交后用 dirty 模式，也不用 `--mode local` 硬套分支工作。
3. **打包并扫描**：helper 对精确新增/修改/删除内容跑 TruffleHog 密钥扫描（`verified,unknown` 低误报策略）。扫描不通过即中止；「整文件删除行中的疑似密钥且值仅出现在删除行」才就地打码；若该值也出现在新增/上下文/混合暂存内容中则 **fail closed** 拒绝审查。
4. **调引擎（隔离）**：Codex 在空工作区 + `exec --ignore-user-config --ignore-rules --skip-git-repo-check` + 只读沙箱；Claude `--safe-mode`（`v2.1.169+`）+ 禁文件/Shell 工具 + WebSearch；Pi `--no-approve --no-session --no-context-files ... --no-tools`。Droid / Copilot / Cursor / OpenCode **fail closed**。
5. **校验输出**：结构化结果校验通过后，逐条人工核验每个发现（读真实代码路径与相邻文件），按严重度分级；默认只报 P0（阻断当前变更的问题），`--max-priority P1/P2/P3` 仅在显式要求时放宽。
6. **处理发现**：in-scope blocker 修根因；follow-up 记入后续；需改协议/配置/存储/公共 API 契约或换 owner 边界的 stop-and-escalate。两条修复循环不收敛即暂停重分类。
7. **复跑**：修码后重跑聚焦测试并重跑 helper，直到无 accepted/actionable 发现。大 diff 自动分区（单次最多 8 个 bounded pass），全部报告合并后再判退出码。
8. **汇报**：给出使用的审查命令、跑的测试/证明、接受/拒绝的发现与理由、最终一次 clean 的审查结果。

## 交付结果

- **stdout 的审查报告**：按严重度分级的发现（默认 P0），以及 helper 的最终结论（`autoreview clean: no accepted/actionable findings reported` 或退出非零表示有可操作发现）。
- **不主动写文件**：默认只写 stdout；仅当 `--output` / `--json-output` / 流式引擎 stderr 开启才落盘。
- **不 push**：SKILL.md 明确「Do not push just to review」，只有用户要求 push / ship / PR update 才 push。
- 可作为最终报告的「clean review」证据。

## 默认边界

- **网络**：会调用外部模型引擎（Codex / Claude / Pi），把打包后的 diff 发到 OpenAI / Anthropic——这是 Skill 的核心用途。helper 自身不做远程执行、不下载远程脚本、无遥测。
- **读文件**：只读待审变更与其 repo 上下文；外部命令只从绝对 `PATH` 解析，不从被审仓库解析（防仓库内恶意可执行文件劫持）。
- **写文件**：默认不写；临时工作区与隔离测试 home 在系统 `/tmp`，`--parallel-tests` 用后即删。
- **执行命令**：会 `subprocess` 调用已安装的外部 CLI（`codex` / `claude` / `pi` / `trufflehog` / `gh` / `git`）。
- **凭据**：引擎调用前剥离 process-injection、Git override、带凭据的代理变量；`--parallel-tests` 的隔离 Testbox home 会 staged 凭据——这是**窄范围的 trusted-maintainer-code 例外**，绝不可用于不可信贡献者/分支代码。

### 风险提示

1. **代码出域**：打包后的 diff 文本会发送给 OpenAI / Anthropic。属 Skill 设计核心，但必须知晓。
2. **默认引擎是 Codex**：本仓库以 Claude Code 为主，若你不常跑 `codex` CLI，可用 `--engine claude`（这是显式换引擎，非静默降级；Claude 默认 `claude-fable-5`）。
3. **parallel-tests 凭据路径**：见上「凭据」项，不可信代码禁用。
4. **大 bundle 耗时**：结构化审查可达 30 分钟；心跳行 `review still running: ... elapsed=... pid=...` 表示健康运行，不是挂死。至少等 30 分钟或连续缺失多次心跳后再查。

## 与相邻 Skill 的区别

| Skill | 与 autoreview 的关系 |
| --- | --- |
| `engineering.code-review` | 同属「代码审查」，但机制不同：code-review 是主 Agent 与你协作的对话协议（请求审查 + 接收反馈 + 先验证再实现），autoreview 是**自动化门禁**（打包 diff + 密钥扫描 + 调外部引擎 + 分级输出）。分工：autoreview 管发布前外审+密钥扫描，code-review 管按需人工审查流程。autoreview **不是行为验证**——clean 结果不证明 UI/CLI/API/产物可用 |
| `backend.backend-review` / `web.frontend-review` | 领域化人工审查清单，无外部引擎、无密钥扫描，不冲突 |
| `engineering.code-review`（测试类） | autoreview 用 `--parallel-tests` 与聚焦测试并行，但验证行为、产物可用性交给测试类 Skill 与 smoke 测试，不混在一起 |

## 行为案例

### 案例 1：典型——发布前过一遍分支

用户说「发版前用 autoreview 过一下 `feature/x`」。设置好 `$AUTOREVIEW` 后运行 `"$AUTOREVIEW" --mode branch --base origin/main`：
- 先对精确新增/修改/删除内容跑 TruffleHog 扫描；
- 通过后调用默认 Codex 在空工作区审查，输出按严重度分级的发现；
- 主 Agent 逐条核验、只修 P0 根因，复跑聚焦测试与 helper 直到 clean；
- 整个过程不 push；最终报告给出命令、测试、接受/拒绝的发现与 clean 结论。

### 案例 2：边界——删除行疑似密钥撞上新增内容（fail closed）

扫描发现某整文件删除行中有疑似密钥，且该值同时出现在新增 / 上下文 / 混合暂存内容中。autoreview 必须**fail closed**——拒绝本次审查，而不是就地打码后继续。这是防绕过密钥扫描的保守设计，应如实报告而不是绕过。

### 案例 3：失败——引擎不可用

`codex` 未安装。helper 明确报错并给出安装指引，**绝不自动安装**；可按需换 `--engine claude` / `--engine pi`，或 `--no-engine` 离线模式。不会在你不知情时静默降级为无引擎审查。

## 版本与来源

- **版本**：0.1.0（beta）
- **来源**：内化自 `openclaw/openclaw` 的 `.agents/skills/autoreview`（revision `0dd8d3ea`，MIT，OpenClaw Foundation）。详见 `provenance.yaml` 与 `incubator/autoreview/`。
- **内化形态**：按仓库所有者「做减法」决定——保留约 1.2 万行 helper 脚本、三平台 smoke harness、测试与核心契约，剥离 OpenClaw 组织专属内容（clawsweeper / gitcrawl / Blacksmith / 发布流程 / 组织默认模型），并明确与 `engineering.code-review` 的分工。
