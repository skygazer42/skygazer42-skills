# skygazer42-skills

`skygazer42` 的个人 AI Skill 仓库。可通过官方 `npx skills` CLI 或平台插件安装。

完整的 Agent 维护规范见 [`AGENTS.md`](AGENTS.md)。

## 安装

### 一键配置（推荐）

```bash
git clone https://github.com/skygazer42/skygazer42-skills.git
cd skygazer42-skills
./scripts/setup.sh
```

这个脚本会自动安装 [FastCtx](https://github.com/yc-duan/fastctx)（高性能 MCP 文件/搜索工具运行时）和本仓库的 Skill。

FastCtx 用结构化的 `read`/`grep`/`glob`/`replace`/`run` 工具替代 shell 拼接，避免编码乱码、输出截断和转义错误，让 Agent 把更多上下文留给代码理解而不是跟工具较劲。单独安装：

```bash
npm install --global fastctx
fastctx   # 进入控制终端，Apply 后重启 AI 会话
```

### npx skills

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

共 **53** 个正式 Skill（`registry.yaml` 为唯一清单），分布在 15 个分类。详细行为以各 Skill 的 `SKILL.md`、中文 `README.md` 和 `tests/cases.yaml` 为准。

### 开发

#### web（已上线）— 前端设计、实现、审查与测试

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `web.frontend-design` | 营销/创意网页视觉设计，对标 Awwwards（定方向） | [→](skills/web/frontend-design/README.md) |
| `web.interface-design` | SaaS/产品界面，好用 + 品牌感（定方向） | [→](skills/web/interface-design/README.md) |
| `web.enterprise-design` | 企业内部系统，极致克制、功能第一（定方向） | [→](skills/web/enterprise-design/README.md) |
| `web.frontend-implementation` | 实现页面、组件、表单和前端交互（会修改文件） | [→](skills/web/frontend-implementation/README.md) |
| `web.frontend-review` | 审查前端正确性、无障碍、性能和安全（只读） | [→](skills/web/frontend-review/README.md) |
| `web.frontend-testing` | 用浏览器验证 UI 流程或补充回归测试 | [→](skills/web/frontend-testing/README.md) |
| `web.web-clone` | 1:1 复刻现有网站——镜像、逆向、溯源、验证 | [→](skills/web/web-clone/README.md) |
| `web.image-to-code` | 图片/截图→前端代码，先设计图再深度分析后忠实还原 | [→](skills/web/image-to-code/README.md) |
| `web.brandkit` | 品牌套件生成——Logo/色彩/字体/应用示例品牌指南板 | [→](skills/web/brandkit/README.md) |
| `web.agent-browser` | 浏览器自动化 CLI（Rust 原生）——导航/填表/点击/截图/数据提取 | [→](skills/web/agent-browser/README.md) |
| `web.ui-ux-pro-max` | UI/UX 设计智能参考库——84 风格/192 配色/74 字体配对/161 推理规则 | [→](skills/web/ui-ux-pro-max/README.md) |
| `web.design-system` | 设计系统构建——三层 token 架构/CSS 变量/组件规格/品牌合规 | [→](skills/web/design-system/README.md) |

#### backend（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `backend.backend-implementation` | 实现 API、服务、数据库和外部集成（会修改文件） | [→](skills/backend/backend-implementation/README.md) |
| `backend.backend-review` | 审查正确性、安全、并发和可靠性（只读） | [→](skills/backend/backend-review/README.md) |
| `backend.backend-debugging` | 定位根因、影响范围和修复建议（不改代码） | [→](skills/backend/backend-debugging/README.md) |

#### engineering（已上线）— 工程流程与编排（20 个）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `engineering.brainstorming` | 创意前先设计，一次一个问题厘清需求 | [→](skills/engineering/brainstorming/README.md) |
| `engineering.grilling` | 无情审问方案，压力测试思路（批判姿态） | [→](skills/engineering/grilling/README.md) |
| `engineering.grill-me` | 在干净对话中对任何想法启动审问式访谈（无状态入口） | [→](skills/engineering/grill-me/README.md) |
| `engineering.writing-plans` | 把设计规格拆成可执行实现计划 | [→](skills/engineering/writing-plans/README.md) |
| `engineering.architecture-review` | 找深化机会，浅模块变深模块（架构层审查） | [→](skills/engineering/architecture-review/README.md) |
| `engineering.test-driven-development` | 先写失败测试，Red-Green-Refactor 循环 | [→](skills/engineering/test-driven-development/README.md) |
| `engineering.systematic-debugging` | 四阶段根因调查，修根因不修症状 | [→](skills/engineering/systematic-debugging/README.md) |
| `engineering.verification-before-completion` | 声称完成前先跑验证拿证据 | [→](skills/engineering/verification-before-completion/README.md) |
| `engineering.subagent-driven-development` | 执行计划——子代理驱动（带审查）或内联执行 | [→](skills/engineering/subagent-driven-development/README.md) |
| `engineering.code-review` | 请求代码审查 + 接收反馈后先验证再实现 | [→](skills/engineering/code-review/README.md) |
| `engineering.finishing-a-development-branch` | 实现完成 → 验证测试 → 合并/PR/保持 + 更新规格 | [→](skills/engineering/finishing-a-development-branch/README.md) |
| `engineering.using-git-worktrees` | 为功能工作创建隔离工作区 | [→](skills/engineering/using-git-worktrees/README.md) |
| `engineering.writing-skills` | 用 TDD 创建/重构/评估 skill 的 skill（本仓创作规范） | [→](skills/engineering/writing-skills/README.md) |
| `engineering.handoff` | 将当前对话压缩为交接文档，供另一 Agent 继续工作 | [→](skills/engineering/handoff/README.md) |
| `engineering.teach` | 在结构化教学工作区中逐步教授新技能或概念 | [→](skills/engineering/teach/README.md) |
| `engineering.wizard` | 生成交互式 bash 向导，引导人类完成手动操作流程 | [→](skills/engineering/wizard/README.md) |
| `engineering.to-questionnaire` | 将无法自行回答的决策转化为结构化问卷，供他人异步填写 | [→](skills/engineering/to-questionnaire/README.md) |
| `engineering.mcp-builder` | MCP 服务器构建方法论——系统化构建生产级 MCP 工具 | [→](skills/engineering/mcp-builder/README.md) |
| `engineering.property-based-testing` | 属性化测试（PBT）指导——序列化/解析/校验/纯函数/智能合约的 roundtrip/幂等/不变量等属性验证 | [→](skills/engineering/property-based-testing/README.md) |
| `engineering.workflow-runner` | 在 Claude Code / Codex / Cursor 中直接运行 YAML 工作流 | [→](skills/engineering/workflow-runner/README.md) |

#### open-source（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `open-source.beautify-github-readme` | 美化 GitHub 个人主页——不改内容，纯视觉增强 | [→](skills/open-source/beautify-github-readme/README.md) |

#### security（已上线）— 授权安全测试与逆向

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `security.reverse-engineering` | 通用逆向：GDB/Frida/angr/Unicorn/Qiling，二进制/APK/WASM/固件 | [→](skills/security/reverse-engineering/README.md) |
| `security.apk-reverse` | Android APK 解包/jadx 反编译/smali 修改/Frida Hook/重打包 | [→](skills/security/apk-reverse/README.md) |
| `security.mobile-reverse` | Android+iOS：Frida/Objection/SSL Pinning/Root 检测绕过/OWASP MASTG | [→](skills/security/mobile-reverse/README.md) |
| `security.malware-analysis` | 恶意样本六阶段分析/YARA/Sigma/沙箱编排/IOC 提取 | [→](skills/security/malware-analysis/README.md) |
| `security.api-security` | REST/GraphQL/WebSocket 全协议：BOLA/IDOR/JWT/OAuth/10 阶段方法论 | [→](skills/security/api-security/README.md) |
| `security.code-audit` | 源码白盒审计：Semgrep/CodeQL/危险 API/鉴权审查/修复验证 | [→](skills/security/code-audit/README.md) |

### 运营

#### operations（已上线）— 事故响应

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `operations.incident-response` | 管理生产事故从检测到复盘的全生命周期——triage 严重级别/沟通草稿/缓解验证/无责备复盘，外部通知只生成草稿 | [→](skills/operations/incident-response/README.md) |

### 营销增长

#### marketing（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `marketing.seo` | 网站 SEO 审计/诊断/实施，证据优先不编造指标 | [→](skills/marketing/seo/README.md) |

### 调研

#### research（已上线）— 多源调研与信息搜集

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `research.last30days` | 多源调研引擎：并行搜索 Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub/Web，按用户互动排序，AI 融合成摘要 | [→](skills/research/last30days/README.md) |

### 写作

#### writing（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `writing.authentic-writing` | 去 AI 味写作——作者档案 + 多轮审稿 + 规则迭代 | [→](skills/writing/authentic-writing/README.md) |
| `writing.humanizer` | 识别并消除 AI 生成文本痕迹——基于 Wikipedia "Signs of AI writing" 指南 | [→](skills/writing/humanizer/README.md) |
| `writing.chinese-documentation` | 中文文档排版规范——中英文空格、全半角标点、术语保留 | [→](skills/writing/chinese-documentation/README.md) |
| `writing.qu-ai-wei` | 去 AI 味（中文）——51 类模式诊断 + 9 档语体矩阵 + 双重安全门检 | [→](skills/writing/qu-ai-wei/README.md) |

### 视觉创作

#### art（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `art.photo-abstract-editorial` | 把照片做成「摄影 + 抽象记忆面板 + 诗意标题」的竖向编辑作品（非滤镜/重画） | [→](skills/art/photo-abstract-editorial/README.md) |

#### presentation（已上线）— 演示文稿生成

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `presentation.open-kimi-ppt` | 基于 PPTD 格式创建/编辑/复刻/导出演示文稿，默认产出 PPTD 项目 + .pptx 文件 | [→](skills/presentation/open-kimi-ppt/README.md) |
| `presentation.ppt-agent` | 端到端 PPT 生成流水线——需求调研→大纲→资料检索→策划→SVG 设计→出片→视觉 QA | [→](skills/presentation/ppt-agent/README.md) |

### 数据分析

#### data（已上线）— 探索性分析

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| `data.exploratory-analysis` | 对本地数据文件做画像/质量审查/模式发现——缺失/基数/分布/可疑值/维度度量建议/分享前偏差审查 | [→](skills/data/exploratory-analysis/README.md) |

### 办公生产力（规划中）

`office.spreadsheet` 等，尚未内化。

## Pack

| Pack | 一句话 | 包含 |
| --- | --- | --- |
| `pack.backend` | 后端实现/审查/排障必备 | [→](packs/backend/pack.yaml) |
| `pack.frontend` | 前端实现/审查/测试必备 | [→](packs/frontend/pack.yaml) |

## 权限概览

权限来自各 Skill 的 `manifest.yaml`，覆盖其完整使用时可能需要的能力。

| Skill | 网络 | 读文件 | 写文件 | 执行命令 |
| --- | :---: | :---: | :---: | :---: |
| `web.frontend-design` | 否 | 是 | 是 | 是 |
| `web.interface-design` | 否 | 是 | 是 | 是 |
| `web.enterprise-design` | 否 | 是 | 是 | 是 |
| `web.frontend-implementation` | 否 | 是 | 是 | 是 |
| `web.frontend-review` | 否 | 是 | 否 | 是 |
| `web.frontend-testing` | 是 | 是 | 是 | 是 |
| `web.web-clone` | 是 | 是 | 是 | 是 |
| `web.image-to-code` | 否 | 是 | 是 | 否 |
| `web.brandkit` | 否 | 是 | 否 | 否 |
| `web.agent-browser` | 是 | 是 | 否 | 是 |
| `web.ui-ux-pro-max` | 否 | 是 | 是 | 是 |
| `web.design-system` | 是 | 是 | 是 | 是 |
| `backend.backend-implementation` | 否 | 是 | 是 | 是 |
| `backend.backend-review` | 否 | 是 | 否 | 是 |
| `backend.backend-debugging` | 否 | 是 | 否 | 是 |
| `engineering.*`（19 个，见上表） | 否 | 是 | 是/否 | 是/否 |
| `engineering.grill-me` | 否 | 否 | 否 | 否 |
| `open-source.beautify-github-readme` | 否 | 是 | 是 | 否 |
| `security.reverse-engineering` | 否 | 是 | 否 | 是 |
| `security.apk-reverse` | 否 | 是 | 否 | 是 |
| `security.mobile-reverse` | 否 | 是 | 否 | 是 |
| `security.malware-analysis` | 否 | 是 | 否 | 是 |
| `security.api-security` | 是 | 是 | 否 | 是 |
| `security.code-audit` | 否 | 是 | 否 | 是 |
| `marketing.seo` | 是 | 是 | 是 | 是 |
| `research.last30days` | 是 | 是 | 否 | 是 |
| `writing.authentic-writing` | 否 | 是 | 是 | 否 |
| `writing.humanizer` | 否 | 是 | 是 | 否 |
| `writing.chinese-documentation` | 否 | 是 | 是 | 否 |
| `writing.qu-ai-wei` | 否 | 是 | 否 | 否 |
| `art.photo-abstract-editorial` | 否 | 是 | 否 | 否 |
| `presentation.open-kimi-ppt` | 是 | 是 | 是 | 是 |
| `presentation.ppt-agent` | 是 | 是 | 是 | 是 |
| `data.exploratory-analysis` | 否 | 是 | 是 | 是 |
| `operations.incident-response` | 否 | 是 | 否 | 是 |

> 注：`engineering.*`（19 个）统一网络关闭、可读文件；写文件与执行命令因 Skill 职责而异。`engineering.grill-me` 是纯对话入口，四项全部为否。

## 仓库结构

```text
skills/
├── web/                  (12 个：设计/实现/审查/测试/复刻/浏览器自动化/设计系统)
├── backend/              (3 个：实现/审查/排障)
├── engineering/          (20 个：工程流程与编排)
├── data/                 (1 个：探索性数据分析)
├── operations/           (1 个：事故响应)
├── open-source/          (1 个：GitHub README 美化)
├── security/             (6 个：逆向/APK/移动端/恶意样本/API/源码审计)
├── marketing/            (1 个：SEO)
├── research/             (1 个：last30days 多源调研)
├── writing/              (4 个：去 AI 味/排版规范)
├── art/                  (1 个：照片抽象编辑)
└── presentation/         (2 个：PPT 生成)
```

## 贡献与维护

本仓库的维护规范、新增 / 导入 Skill 流程、版本与发布策略、安全边界，全部在 [`AGENTS.md`](AGENTS.md) 中定义。贡献前请先阅读。

## 当前已知限制

- 仓库自身尚未选择统一的开源许可证；原创 Skill 的来源记录当前使用 `NOASSERTION`。外部 Skill 仍必须独立保留并遵守其上游许可证。
- 行为案例目前是结构化期望，还不是自动评分系统。
- Pack 目前用于组织元数据，尚不负责选择性生成插件副本。
