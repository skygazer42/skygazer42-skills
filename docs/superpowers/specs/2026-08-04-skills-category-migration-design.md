# skills 目录迁移到「类别/Skill」两层结构 — 设计文档

- 日期：2026-08-04
- 状态：设计已获用户批准，待写实现计划
- 范围：`skygazer42-skills` 仓库结构迁移（不含新增 Skill）

## 1. 背景与问题

当前 `skills/` 是扁平单层结构（`skills/<skill-name>/`）。目标是让本仓库成为一个「可直接安装的个人 Skill 仓库」，而不仅是文档化的注册表：

- 保留标准 `SKILL.md`。
- 支持官方 `npx skills` CLI 从 GitHub 仓库发现并选择性安装。
- 保留 Claude / Codex 整包安装（`.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`、`.agents/plugins/marketplace.json`）与 Gemini Extension（`gemini-extension.json`）。
- 根 README 既是安装说明，也是完整能力目录。

**待确认假设**：官方 CLI 默认支持两种物理结构——`skills/<skill-name>/SKILL.md` 与 `skills/<category>/<skill-name>/SKILL.md`（单层类别嵌套，无需 `--full-depth`）。整个两层方案的成立**依赖此假设**。本次 WebFetch 官方 README 遇 429 未取到（见 §9），因此该假设必须在任何 `git mv` 扩大改动之前，由 §8 步骤 4 的 `npx skills@latest add . --list` 实测确认；若两层结构未被正确发现，则回到设计层面重议，不强行迁移。采用两层「类别/Skill」结构的目的：既能按用户可理解的能力类别组织，又能被 CLI 正确发现。

## 2. 目标

1. `skills/` 改为「类别/Skill」两层结构。
2. 现有 6 个 Skill 迁移到 `web/` 与 `backend/` 两个类别下，保留 git 历史。
3. Registry 生成与仓库校验工具支持两层结构。
4. 同步 pack、平台清单、`registry.yaml`、根 README 与 `AGENTS.md`。
5. README 首屏加入 `npx skills add`。
6. 用本地路径 `npx skills add . --list` 实测真实发现结果，并据此校对 README 的安装命令。

## 3. 非目标（范围边界）

- 不新增任何 Skill；`beautify-github-readme`、image / video / presentation / spreadsheet / mobile 等类别下的 Skill，以及新构想的「规划 / 任务拆解」skill（详见 §5.4 路线图），均后续各自单独一轮内化。
- 不创建空的类别目录；未来类别只在 README 路线图中列出，等真正内化第一个 Skill 时才建目录（遵循 `AGENTS.md`「一次一个」「不加占位目录」）。
- 不改动任何 Skill 的行为内容（`SKILL.md` 正文、`tests/cases.yaml`、权限声明均不变）。
- 不做与本次迁移无关的重构。

## 4. 关键决策

### 4.1 ID 与分类：采用「类别即分类」

物理父目录名 = `manifest.category` = 全局 ID 前缀，三者严格对齐。

| Skill（目录名不变） | 旧 ID | 新 ID | category | 新物理路径 |
| --- | --- | --- | --- | --- |
| frontend-implementation | `frontend.frontend-implementation` | `web.frontend-implementation` | `frontend`→`web` | `skills/web/frontend-implementation/` |
| frontend-review | `frontend.frontend-review` | `web.frontend-review` | `frontend`→`web` | `skills/web/frontend-review/` |
| frontend-testing | `frontend.frontend-testing` | `web.frontend-testing` | `frontend`→`web` | `skills/web/frontend-testing/` |
| backend-implementation | `backend.backend-implementation` | 不变 | `backend` | `skills/backend/backend-implementation/` |
| backend-review | `backend.backend-review` | 不变 | `backend` | `skills/backend/backend-review/` |
| backend-debugging | `backend.backend-debugging` | 不变 | `backend` | `skills/backend/backend-debugging/` |

理由：最贴合仓库既有纪律「目录 = 分类 = ID 一致」；校验器 `validate_repository.py:151` 的 `id == <category>.<最内层目录名>` 规则天然成立；beta 阶段改 ID 成本最低。前端 3 个 ID 变更是破坏性的，但仅影响本仓 pack/registry，无外部依赖。

`SKILL.md` 的 `name` 字段不变：校验器用**最内层目录名**（如 `frontend-implementation`）与之比对，目录名迁移后不变。已确认 `web.frontend-implementation` 匹配校验器的 `IDENTIFIER` 正则。

### 4.2 三项已确认默认

- **A**：不建空类别目录，未来类别只写入 README 路线图。
- **B**：三处平台清单版本 `0.2.0` → `0.3.0`（ID 破坏性变更，升 minor）。
- **C**：校验器强制两层结构，并新增不变量「物理父目录名 == `manifest.category`」，使「类别即分类」由工具兜底、防止漂移。

## 5. 详细改动清单

### 5.1 目录迁移（`git mv`，保留历史）

```
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

前端 3 个 `manifest.yaml`：仅改 `category`（→ `web`）与 `id`（→ `web.*`）。后端 3 个：仅移动，manifest 不变。

个体 Skill 版本保持 `0.1.0`（不升 major）：本仓 ID 前缀是仓库内部命名空间、而非 Skill 对外的公开 API，且当前处于 `0.x` / beta——`AGENTS.md` §7 的语义化版本在 `0.x` 阶段允许此类调整，「破坏性升 major」在 `1.0.0` 之后才严格适用。插件包版本另按默认 B 升 minor（§4.2）。

### 5.2 工具

- `tools/build_registry.py`：`registry_data()` 的 `(root / "skills").glob("*/manifest.yaml")` → `glob("*/*/manifest.yaml")`。`path` 字段由 `skill_dir.relative_to(root)` 自动产出 `skills/<category>/<skill>`，无需额外改动。
- `tools/validate_repository.py`：
  - `skill_directories()`：由「遍历 `skills/` 直接子目录」改为「遍历 `skills/<category>/<skill>/`」（两层）。
  - 新增校验：每个 Skill 的物理父目录名必须等于其 `manifest.category`（不变量 C）。
  - 保留 `:151` 的 `id == <category>.<目录名>` 规则不变。
  - 保留平台清单 `skills` 必须指向 `./skills/` 的检查不变。

### 5.3 pack / 平台清单 / registry

- `packs/frontend/pack.yaml`：3 处 `frontend.*` → `web.*`（否则校验器报 `unknown skill reference`）。
- `.claude-plugin/plugin.json`、`.codex-plugin/plugin.json`、`gemini-extension.json`：`version` `0.2.0` → `0.3.0`；`skills` 仍为 `./skills/`（校验器强制，CLI 递归发现），不改。
- `registry.yaml`：重新用 `build_registry.py` 生成。

### 5.4 README 重构为用户门面 + 其余文档同步

本次把根 `README.md` 从「用户向 + 维护向混排的约 500 行」重构为**纯用户门面**（约 150 行）。这既服务「可直接安装的个人 Skill 仓库」定位，也顺带消除它与 `AGENTS.md` 的信息重复——正是本仓「文档唯一职责」纪律（`AGENTS.md` §3）的应用。

**(a) 根 README 目标结构（门面）：**

1. 一句话定位。
2. 安装：`npx skills@latest add skygazer42/skygazer42-skills`（`--list` / 交互式 / `--skill <name>` / `--agent codex --global --yes`）**置顶**；Codex / Claude / Gemini 原生 marketplace 安装随后。
3. 能力目录：大分组（开发 / 视觉创作 / 视频 / 办公生产力）呈现，物理类别（web/backend/…）作二级；现有 6 个标「已上线」、未来方向标「规划中」；含选择表与权限表；每个 skill 只给一句话摘要 + 链接到 `skills/<category>/<skill>/README.md`（详解下沉到各 skill 自己的 README，不在根 README 展开）。
4. 贡献 / 维护：一句话指向 `AGENTS.md`，不再在根 README 复述规范。

**(b) 从根 README 删除、改为指向 `AGENTS.md` 的章节**（信息不丢失——`AGENTS.md` 已覆盖）：

- 「我为什么维护这个仓库」「维护原则」→ `AGENTS.md` §1。
- 「一个正式 Skill 包含什么」（SKILL/manifest/README/provenance/tests 详解）→ `AGENTS.md` §3/§4/§5。
- 「新增一个原创 Skill」「导入一个外部 Skill」→ `AGENTS.md` §8 及第 15 节发布检查表。
- 「本地开发与校验」→ 根 README 保留一条极简校验命令指针，规范正文归 `AGENTS.md` §12。
- 「版本与发布」→ `AGENTS.md` §7。
- 「安全边界」→ `AGENTS.md` §13。
- **删除前逐条核对**：确认该内容确已在 `AGENTS.md` 覆盖；若有 AGENTS 尚未含而有价值者，先补入 `AGENTS.md`（见 §5.5）再从 README 删除，保证零信息丢失。

**(c) 保留并前置的用户向内容**（不删，仅重排）：原生安装命令、更新 / 卸载命令（并入安装节）、「当前已知限制」（诚实披露，留在根 README）。

**(d) 路线图**含「规划 / 任务拆解」方向（**规划中**，本轮不实现、不建目录、不定最终类别/ID）：一个站在 implementation / review / testing / debugging **之上**的规划层 skill——接需求 → 技术决策 → 判断涉及前端 / 后端 / 设计等领域 → 拆解并路由到对应实现 skill。它跨领域、不归属 web/backend；本轮它在本 spec 的唯一交付触点就是这条 README 路线图。

**(e) `frontend.* → web.*` 同步**（README 类文档不被 `build_registry.py` / `validate_repository.py` 解析，故第 8 节自动校验会全绿却与 manifest/registry 矛盾，必须人工同步；依 `AGENTS.md` §11/§3）：

- 根 README 在上述重构中一并把所有 `frontend.*` 改写为 `web.*`；重构会重排/删除原含 ID 的章节，故不再逐行对应旧行号（原出现处：选择表、各 Skill「ID」展示行、`id:` 代码示例块）。
- 其余 6 个文档仍逐一同步（行号为迁移前当前工作区位置）：
  - `packs/frontend/README.md`（第 5-7 行，三个 ID）
  - `skills/web/frontend-implementation/README.md`（第 7 行「全局 ID」；第 36-37 行交叉引用）
  - `skills/web/frontend-review/README.md`（第 7 行；第 36-37 行交叉引用）
  - `skills/web/frontend-testing/README.md`（第 7 行；第 35-36 行交叉引用）
  - `skills/backend/backend-implementation/README.md`（第 36 行交叉引用）
  - `skills/backend/backend-review/README.md`（第 36 行交叉引用）
  - （`skills/backend/backend-debugging/README.md` 经 grep 核实无 `frontend.*` 引用，无需改。）
- 仓库结构树与 `skills/` 目录示例更新为两层。

### 5.5 AGENTS.md

- 第 4 节目录契约与结构示例更新为 `skills/<category>/<skill>/`。
- 第 7 节命名/分类表述更新，明确写入新不变量「物理类别目录名 = `manifest.category` = 全局 ID 前缀」。
- 接收从根 README 下沉、且 AGENTS 尚未覆盖的维护内容（若 §5.4(b) 核对时发现），以保证 README 瘦身零信息丢失。

### 5.6 测试

- `tests/test_repository_tools.py`：
  - `setUp` 夹具由单层 `skills/review-code` 改为两层 `skills/<category>/review-code`（强制两层后单层夹具会失败）。夹具 manifest 现为 `category: engineering` / `id: engineering.review-code`，故父目录名须取 `engineering` 以满足新不变量 C，`category`/`id` 保持自洽。
  - 另有**两个方法硬编码单层路径**，须一并改为两层：`test_external_skill_needs_exact_provenance`（写 `skills/review-code/provenance.yaml`，当前第 140 行）与 `test_skill_frontmatter_is_required`（写 `skills/review-code/SKILL.md`，当前第 151 行）。否则它们注入的路径不再被两层 `skill_directories()` 发现，断言失败。

## 6. CLI 发现数据流

```
npx skills add <repo|.>  →  递归扫描 skills/
                         →  发现 skills/<category>/<skill>/SKILL.md
--list                   →  列出发现的 Skill 供查看
（交互式）               →  勾选安装
--skill <name>           →  只安装指定 Skill
--agent <codex|claude|…> →  写入对应 agent 的 skill 目录
--global / --yes         →  全局安装 / 跳过确认
```

以本机 `npx skills@latest add . --list` 的真实输出为准，校对上述行为与 README 命令措辞。

## 7. 校验器新不变量（错误处理）

- 每个 Skill 必须恰好位于 `skills/<category>/<skill>/`（两层）。
- `manifest.category` 必须等于其物理父目录名。
- `id` 必须等于 `<category>.<最内层目录名>`（既有规则）。
- 违反任一 → 输出明确 error 并使校验失败。

## 8. 验证计划

1. `python tools/build_registry.py`（重新生成 registry）。
2. `python tools/validate_repository.py`（结构、ID、父目录==category、密钥、清单、registry 一致性）。
3. `python -m unittest discover -s tests`（含改造后的两层夹具）。
4. `npx skills@latest add . --list`（本机 node v22 / npx 11 可用且能连通 npm；确认 6 个 Skill 被正确发现）。此步验证 §1 的两层发现假设，应**尽早执行**：实现计划宜先迁移风险最低的 `backend`（ID 不变）并立即 `--list` 验证两层被正确发现，确认后再迁前端（带 ID 改名）；任何阶段失败即回滚（`git mv` 可逆）。
5. 可选：`claude plugin validate .`、`gemini extensions validate .`（若本机 CLI 可用）。

报告时区分「自动校验通过」与「CLI 实测发现」，不混为一谈。

## 9. 风险与回滚

- **ID 破坏性变更**：仅影响本仓 `pack.frontend` 与 `registry.yaml`，beta 阶段无外部消费者；`git mv` 与 manifest 改动均可回滚。
- **不建空类别目录**：未来内化 Skill 时补建对应类别目录，无遗留；README 路线图保持类别可见。
- **官方 CLI 行为与预期不符**：以 `--list` 实测为准；若发现两层结构未被正确发现，回到设计层面重新澄清，不强行发布。
- **本次 429 未取到官方 README**：实现阶段重试 WebFetch，或直接以本机 CLI 实测替代作为权威依据。

## 10. 提交与授权

依据 `AGENTS.md` 第 13 节，本设计文档写入后**不自动提交**；所有 `git commit` / `git mv` 的实际执行、以及最终提交，均作为独立授权项，由仓库所有者在实现阶段明确确认。
