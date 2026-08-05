# skygazer42-skills

`skygazer42` 的个人 AI Skill 仓库。可通过官方 `npx skills` CLI 或平台插件安装。

完整的 Agent 维护规范见 [`AGENTS.md`](AGENTS.md)。

## 安装

### npx skills（推荐）

```bash
# 查看仓库里有哪些 Skill
npx skills@latest add skygazer42/skygazer42-skills --list

# 交互式选择并安装
npx skills@latest add skygazer42/skygazer42-skills

# 只安装某一个
npx skills@latest add skygazer42/skygazer42-skills \
  --skill <skill-name>

# 全局安装到指定 agent
npx skills@latest add skygazer42/skygazer42-skills \
  --skill <skill-name> \
  --agent codex --global --yes
```

### Codex

```bash
codex plugin marketplace add skygazer42/skygazer42-skills
codex plugin add skygazer42-skills@skygazer42-skills
codex plugin list
```

### Claude Code

```text
/plugin marketplace add skygazer42/skygazer42-skills
/plugin install skygazer42-skills@skygazer42-skills
/reload-plugins
```

### Gemini CLI

```bash
gemini extensions install https://github.com/skygazer42/skygazer42-skills --auto-update
gemini extensions list
```

### 更新和卸载

```bash
# Codex
codex plugin marketplace upgrade skygazer42-skills
codex plugin remove skygazer42-skills@skygazer42-skills

# Claude Code
claude plugin update skygazer42-skills@skygazer42-skills
claude plugin uninstall skygazer42-skills@skygazer42-skills

# Gemini CLI
gemini extensions update skygazer42-skills
gemini extensions uninstall skygazer42-skills
```

## 能力目录

### 开发

#### web（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `web.frontend-design` | 营销/创意网页视觉设计，对标 Awwwards（定方向） | [→](skills/web/frontend-design/README.md) |
| `web.interface-design` | SaaS/产品界面，好用 + 品牌感（定方向） | [→](skills/web/interface-design/README.md) |
| `web.enterprise-design` | 企业内部系统，极致克制、功能第一（定方向） | [→](skills/web/enterprise-design/README.md) |
| `web.frontend-implementation` | 实现页面、组件、表单和前端交互（会修改文件） | [→](skills/web/frontend-implementation/README.md) |
| `web.frontend-review` | 审查前端正确性、无障碍、性能和安全（只读） | [→](skills/web/frontend-review/README.md) |
| `web.frontend-testing` | 用浏览器验证 UI 流程或补充回归测试 | [→](skills/web/frontend-testing/README.md) |
| `web.web-clone` | 1:1 复刻现有网站——镜像、逆向、溯源、验证 | [→](skills/web/web-clone/README.md) |

#### backend（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `backend.backend-implementation` | 实现 API、服务、数据库和外部集成（会修改文件） | [→](skills/backend/backend-implementation/README.md) |
| `backend.backend-review` | 审查正确性、安全、并发和可靠性（只读） | [→](skills/backend/backend-review/README.md) |
| `backend.backend-debugging` | 定位根因、影响范围和修复建议（不改代码） | [→](skills/backend/backend-debugging/README.md) |

#### engineering（已上线）— 工程流程与编排

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `engineering.brainstorming` | 创意前先设计，一次一个问题厘清需求 | [→](skills/engineering/brainstorming/README.md) |
| `engineering.grilling` | 无情审问方案，压力测试思路（批判姿态） | [→](skills/engineering/grilling/README.md) |
| `engineering.writing-plans` | 把设计规格拆成可执行实现计划 | [→](skills/engineering/writing-plans/README.md) |
| `engineering.architecture-review` | 找深化机会，浅模块变深模块（架构层审查） | [→](skills/engineering/architecture-review/README.md) |
| `engineering.test-driven-development` | 先写失败测试，Red-Green-Refactor 循环 | [→](skills/engineering/test-driven-development/README.md) |
| `engineering.systematic-debugging` | 四阶段根因调查，修根因不修症状 | [→](skills/engineering/systematic-debugging/README.md) |
| `engineering.verification-before-completion` | 声称完成前先跑验证拿证据 | [→](skills/engineering/verification-before-completion/README.md) |
| `engineering.subagent-driven-development` | 执行计划——子代理驱动（带审查）或内联执行 | [→](skills/engineering/subagent-driven-development/README.md) |
| `engineering.code-review` | 请求代码审查 + 接收反馈后先验证再实现 | [→](skills/engineering/code-review/README.md) |
| `engineering.finishing-a-development-branch` | 实现完成 → 验证测试 → 合并/PR/保持 + 更新规格 | [→](skills/engineering/finishing-a-development-branch/README.md) |
| `engineering.using-git-worktrees` | 为功能工作创建隔离工作区 | [→](skills/engineering/using-git-worktrees/README.md) |
| `engineering.skill-authoring` | 创建/重构/评估 skill 的 skill（本仓创作规范） | [→](skills/engineering/skill-authoring/README.md) |

#### open-source（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `open-source.beautify-github-readme` | 美化 GitHub 个人主页——不改内容，纯视觉增强 | [→](skills/open-source/beautify-github-readme/README.md) |

### 营销增长

#### marketing（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `marketing.seo` | 网站 SEO 审计/诊断/实施，证据优先不编造指标 | [→](skills/marketing/seo/README.md) |

### 写作

#### writing（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `writing.authentic-writing` | 去 AI 味写作——作者档案 + 多轮审稿 + 规则迭代 | [→](skills/writing/authentic-writing/README.md) |

### 视觉创作（规划中）

image / video / presentation 等。

### 办公生产力（规划中）

spreadsheet 等。

## 权限概览

| Skill | 网络 | 读文件 | 写文件 | 执行命令 |
| --- | :---: | :---: | :---: | :---: |
| `web.frontend-implementation` | 否 | 是 | 是 | 是 |
| `web.frontend-review` | 否 | 是 | 否 | 是 |
| `web.frontend-testing` | 是 | 是 | 是 | 是 |
| `backend.backend-implementation` | 否 | 是 | 是 | 是 |
| `backend.backend-review` | 否 | 是 | 否 | 是 |
| `backend.backend-debugging` | 否 | 是 | 否 | 是 |
| engineering 类全部 Skill | 否 | 是 | 是/否 | 是/否 |
| `open-source.beautify-github-readme` | 否 | 是 | 是 | 否 |

## 仓库结构

```text
skills/
├── web/
│   ├── frontend-implementation/
│   ├── frontend-review/
│   └── frontend-testing/
├── backend/
│   ├── backend-implementation/
│   ├── backend-review/
│   └── backend-debugging/
├── engineering/           (13 个工程流程 Skill)
└── open-source/
    └── beautify-github-readme/
```

## 贡献与维护

本仓库的维护规范、新增 / 导入 Skill 流程、版本与发布策略、安全边界，全部在 [`AGENTS.md`](AGENTS.md) 中定义。贡献前请先阅读。

## 当前已知限制

- 仓库自身尚未选择统一的开源许可证；原创 Skill 的来源记录当前使用 `NOASSERTION`。外部 Skill 仍必须独立保留并遵守其上游许可证。
- 行为案例目前是结构化期望，还不是自动评分系统。
- Pack 目前用于组织元数据，尚不负责选择性生成插件副本。
