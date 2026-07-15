# skygazer42-skills

个人与团队共用的 AI Skill 主仓库。所有平台读取同一份正式 Skill；从外部发现的内容先进入孵化区，完成来源核验、整理和测试后才能发布。

这个仓库当前支持：

- 通过原生插件机制安装到 Codex 和 Claude Code
- 作为 Extension 安装到 Gemini CLI
- 用统一的 `SKILL.md`、Manifest、来源记录和行为案例维护 Skill
- 用 Pack 组合 Skill，但不复制内容
- 自动生成 Registry，并在 CI 中检查结构、引用、权限、来源和常见密钥

> 当前状态：首批 6 个 Skill 以 `0.1.0 / beta` 发布，覆盖前端实现、审查、测试和后端实现、审查、排障；插件版本为 `0.2.0`。

## 当前 Skill

### Frontend Essentials

- [`frontend.frontend-implementation`](skills/frontend-implementation/)：实现页面、组件、表单、交互和客户端数据流
- [`frontend.frontend-review`](skills/frontend-review/)：审查正确性、无障碍、响应式、性能、安全和测试
- [`frontend.frontend-testing`](skills/frontend-testing/)：运行或添加测试，并验证浏览器、键盘和响应式行为

### Backend Essentials

- [`backend.backend-implementation`](skills/backend-implementation/)：实现 API、服务、任务、数据变更和集成
- [`backend.backend-review`](skills/backend-review/)：审查正确性、授权、安全、数据完整性和可靠性
- [`backend.backend-debugging`](skills/backend-debugging/)：复现故障、验证假设、定位根因和影响范围

原生插件当前安装全部 6 个 Skill；[`pack.frontend`](packs/frontend/) 和 [`pack.backend`](packs/backend/) 提供组合元数据。

## 快速安装

这个 GitHub 仓库本身同时是 Claude Code Marketplace、Codex Marketplace 和 Gemini CLI Extension，不需要手工复制 Skill。

> 发布状态：当前是 GitHub 自托管 Marketplace，尚未上架 Anthropic 的 `claude-plugins-official`。下面的命令是现在可以使用的安装方式。

### Claude Code — Skygazer42 Marketplace

注册 Marketplace：

```text
/plugin marketplace add skygazer42/skygazer42-skills
```

安装插件：

```text
/plugin install skygazer42-skills@skygazer42-skills
```

立即加载并确认：

```text
/reload-plugins
```

```bash
claude plugin list
```

插件中的 Skill 使用 `/skygazer42-skills:<skill-name>` 命名空间。

### Codex — Skygazer42 Marketplace

注册 Marketplace：

```bash
codex plugin marketplace add skygazer42/skygazer42-skills
```

安装插件：

```bash
codex plugin add skygazer42-skills@skygazer42-skills
```

确认安装：

```bash
codex plugin list
```

安装后开启新任务或新线程，让 Codex 重新加载 Skill。

### Gemini CLI — 直接从 GitHub 安装

```bash
gemini extensions install https://github.com/skygazer42/skygazer42-skills --auto-update
```

Gemini 会要求确认是否信任扩展源。先检查仓库内容，再确认安装，然后重启 Gemini CLI：

```bash
gemini extensions list
```

安装前需要 Git 和对应平台的 CLI。私有仓库还需要先配置 Git 凭据。

## 更新和卸载

Codex：

```bash
# 更新
codex plugin marketplace upgrade skygazer42-skills
codex plugin add skygazer42-skills@skygazer42-skills

# 卸载
codex plugin remove skygazer42-skills@skygazer42-skills
```

Claude Code：

```bash
# 更新
claude plugin update skygazer42-skills@skygazer42-skills

# 卸载
claude plugin uninstall skygazer42-skills@skygazer42-skills
```

Gemini CLI：

```bash
# 更新
gemini extensions update skygazer42-skills

# 卸载
gemini extensions uninstall skygazer42-skills
```

更新后按前文要求重新加载插件或重启对应会话。

## 其他 Agent Skills 工具

正式 Skill 使用通用目录：

```text
skills/<skill-name>/SKILL.md
```

其他支持 Agent Skills 的工具可以直接读取或同步 `skills/`。平台有额外 Manifest 要求时，只增加平台清单，不复制 Skill 正文。

## 为什么 `skills/` 不按分类嵌套

Codex、Claude Code 和 Gemini CLI 都原生发现 `skills/<skill-name>/SKILL.md`。因此正式目录保持扁平：

```text
skills/
├── review-pull-request/
├── source-verification/
└── decision-memo/
```

分类仍然保存在 `manifest.yaml` 和全局 ID 中：

```yaml
id: engineering.review-pull-request
category: engineering
```

这样既保留可搜索的分类，也不需要为每个平台生成重复副本。

## 仓库结构

```text
.
├── skills/                         # 已审核、可依赖的正式 Skill
├── packs/                          # Skill 引用组合，不复制正文
├── incubator/                      # 未审核的外部候选
├── templates/skill/                # 新 Skill 模板
├── tools/                          # Registry 与仓库校验工具
├── tests/                          # 仓库工具回归测试
├── registry.yaml                   # 根据 Manifest 自动生成
├── .codex-plugin/plugin.json       # Codex 插件清单
├── .agents/plugins/marketplace.json # Codex Marketplace
├── .claude-plugin/plugin.json      # Claude Code 插件清单
├── .claude-plugin/marketplace.json # Claude Code Marketplace
└── gemini-extension.json           # Gemini CLI Extension 清单
```

## 每个正式 Skill 的结构

```text
skills/<skill-name>/
├── SKILL.md
├── manifest.yaml
├── README.md
├── provenance.yaml
└── tests/
    └── cases.yaml
```

只有确实需要时才增加 `examples/`、`references/` 或 `scripts/`。

### `SKILL.md`

`SKILL.md` 是 Agent 执行的指令。它必须以 YAML frontmatter 开头：

```markdown
---
name: review-pull-request
description: Review pull request changes for correctness, regressions, security, and tests.
---
```

规则：

- `name` 必须与目录名一致
- `description` 必须说明能力以及何时触发
- 正文只保留输入、执行步骤、输出契约、约束和失败处理
- 不得编造缺失的输入或证据

### `manifest.yaml`

Manifest 是仓库内部协议，至少明确：

- 全仓唯一且稳定的 `id`
- 语义化 `version`
- `category` 和 `entrypoint`
- Skill、命令和环境变量依赖
- 网络、文件和命令权限
- 测试案例与来源文件位置

目录、ID 和分类必须满足：

```text
目录：skills/review-pull-request/
分类：engineering
ID：  engineering.review-pull-request
```

`skills/` 中不允许 `draft`。正式发布前必须更新状态；`stable` Skill 至少需要一个行为案例。

### `provenance.yaml`

外部 Skill 必须记录：

- 原仓库地址
- 精确 commit 或 release
- 原文件路径和作者
- License 标识和文件位置
- 导入时间、导入者和改造记录

只记录仓库首页或默认分支不够，因为无法稳定检查上游变化。

### `tests/cases.yaml`

第一阶段只描述输入和预期行为，不做复杂的模型自动评分。案例至少要明确 Skill 必须做到什么、不得做什么，以及输入不足时如何处理。

## 新建一个原创 Skill

1. 复制模板：

```bash
cp -R templates/skill skills/my-skill
```

2. 修改以下内容：

- `SKILL.md` 的 `name`、`description` 和正文
- `manifest.yaml` 的 ID、版本、状态、分类、依赖和权限
- `README.md` 的人类使用说明
- `provenance.yaml` 的作者与 License
- `tests/cases.yaml` 的行为案例

3. 正式提交前生成 Registry 并验证：

```bash
python tools/build_registry.py
python tools/validate_repository.py
python -m unittest discover -s tests
```

模板默认是 `draft`，所以未完成内容不会通过正式仓库校验。

## 导入外部 Skill

不要直接复制到 `skills/`。先建立：

```text
incubator/<candidate-name>/
├── source.yaml
├── review.md
└── candidate/
```

处理顺序：

```text
Discover -> Incubator -> Review -> Normalize -> Test -> Publish -> Package
```

审核至少覆盖来源、License、密钥、内部地址、危险写操作、网络权限和平台专属逻辑。完整字段见 [`incubator/README.md`](incubator/README.md)。

## Skill Pack

Pack 只引用 Skill ID 和版本范围：

```yaml
skills:
  - id: engineering.review-pull-request
    version: ">=1.0.0 <2.0.0"
```

当前原生插件安装会加载仓库中的全部正式 Skill；Pack 目前用于组合、检索和未来的选择性安装，不会生成 Skill 副本。Pack 格式见 [`packs/README.md`](packs/README.md)。

## 本地开发与校验

安装 Python 依赖：

```bash
python -m pip install -r requirements.txt
```

修改 Skill、Pack 或 Manifest 后：

```bash
python tools/build_registry.py
python tools/validate_repository.py
python -m unittest discover -s tests
```

只检查 Registry 是否已同步：

```bash
python tools/build_registry.py --check
```

如果本机安装了对应 CLI，还可以执行平台原生校验：

```bash
claude plugin validate .
gemini extensions validate .
```

GitHub Actions 会自动执行仓库校验、单测和 Registry 一致性检查。

## 发布版本

仓库插件版本同时保存在：

- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `gemini-extension.json`

发布时三个版本必须一致；仓库校验器会阻止版本漂移。单个 Skill 仍在自己的 `manifest.yaml` 中独立维护版本。

## 安全边界

- 安装第三方插件前先检查源码和权限
- `manifest.yaml` 的权限是审核声明，不替代平台自身的沙箱和确认机制
- 不提交密钥、本机路径、私有地址或生成产物
- 外部 Skill 未完成来源与 License 检查前不得晋级
- Pack 不会扩大单个 Skill 已声明的权限

## 常见问题

### 安装时找不到 Marketplace 或插件

确认仓库可访问，并且 `.agents/plugins/marketplace.json`、`.claude-plugin/marketplace.json` 和对应插件清单已经推送到目标 Git 分支。

### 安装成功但看不到 Skill

检查目录是否为 `skills/<skill-name>/SKILL.md`，frontmatter 的 `name` 是否与目录一致。Claude Code 执行 `/reload-plugins`；Codex 开启新线程；Gemini CLI 重启会话。

### 校验提示 `registry.yaml is stale`

```bash
python tools/build_registry.py
```

生成后重新执行仓库校验。

### 校验提示 `draft skills belong in incubator`

完成正文、来源、权限和行为案例，再将 Manifest 状态改为正式状态；未完成的外部候选继续留在 `incubator/`。
