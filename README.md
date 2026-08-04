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
| `web.frontend-implementation` | 实现页面、组件、表单和前端交互（会修改文件） | [→](skills/web/frontend-implementation/README.md) |
| `web.frontend-review` | 审查前端正确性、无障碍、性能和安全（只读） | [→](skills/web/frontend-review/README.md) |
| `web.frontend-testing` | 用浏览器验证 UI 流程或补充回归测试 | [→](skills/web/frontend-testing/README.md) |

#### backend（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `backend.backend-implementation` | 实现 API、服务、数据库和外部集成（会修改文件） | [→](skills/backend/backend-implementation/README.md) |
| `backend.backend-review` | 审查正确性、安全、并发和可靠性（只读） | [→](skills/backend/backend-review/README.md) |
| `backend.backend-debugging` | 定位根因、影响范围和修复建议（不改代码） | [→](skills/backend/backend-debugging/README.md) |

### 视觉创作（规划中）

image / video / presentation 等。

### 办公生产力（规划中）

spreadsheet 等。

### 规划 / 任务拆解（规划中）

一个站在实现 / 审查 / 测试 / 排障之上的规划层 skill——接需求 → 技术决策 → 判断涉及前端 / 后端 / 设计等领域 → 拆解并路由到对应实现 skill。跨领域，最终类别名与 ID 留待单独内化时敲定。

## 权限概览

| Skill | 网络 | 读文件 | 写文件 | 执行命令 |
| --- | :---: | :---: | :---: | :---: |
| `web.frontend-implementation` | 否 | 是 | 是 | 是 |
| `web.frontend-review` | 否 | 是 | 否 | 是 |
| `web.frontend-testing` | 是 | 是 | 是 | 是 |
| `backend.backend-implementation` | 否 | 是 | 是 | 是 |
| `backend.backend-review` | 否 | 是 | 否 | 是 |
| `backend.backend-debugging` | 否 | 是 | 否 | 是 |

## 仓库结构

```text
skills/
├── web/
│   ├── frontend-implementation/
│   ├── frontend-review/
│   └── frontend-testing/
└── backend/
    ├── backend-implementation/
    ├── backend-review/
    └── backend-debugging/
```

## 贡献与维护

本仓库的维护规范、新增 / 导入 Skill 流程、版本与发布策略、安全边界，全部在 [`AGENTS.md`](AGENTS.md) 中定义。贡献前请先阅读。

## 当前已知限制

- 仓库自身尚未选择统一的开源许可证；原创 Skill 的来源记录当前使用 `NOASSERTION`。外部 Skill 仍必须独立保留并遵守其上游许可证。
- 行为案例目前是结构化期望，还不是自动评分系统。
- Pack 目前用于组织元数据，尚不负责选择性生成插件副本。
