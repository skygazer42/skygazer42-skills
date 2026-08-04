# Skills 目录迁移到「类别/Skill」两层结构 — 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `skills/` 从扁平单层迁移至「类别/Skill」两层结构，同步全部工具、清单、文档与测试，并通过 `npx skills add . --list` 实测 CLI 发现。

**Architecture:** 先改工具（让它校验两层结构）→ 迁 backend（ID 不变，风险最低）→ `npx --list` 实测验证两层发现假设 → 迁 frontend（`frontend.*`→`web.*` 改名）→ 同步 pack / 清单 / registry → 根 README 重构为用户门面 → 其余文档与 AGENTS.md 同步 → 最终全量验证。任何阶段回滚即 `git mv` 逆操作。

**Tech Stack:** Python 3（PyYAML），bash / git，npx skills CLI（Node.js v22），Markdown

**Spec:** `docs/superpowers/specs/2026-08-04-skills-category-migration-design.md`

---

## Phase 1: 工具与测试改造（先让校验器认识两层）

### Task 1: 改造 `skill_directories()` 为两层遍历

**Files:**
- Modify: `tools/validate_repository.py:71-79`

- [ ] **Step 1: 改 `skill_directories()` 函数**

将单层 `iterdir()` 改为两层遍历（类别目录 → Skill 目录）。替换第 71-79 行：

```python
def skill_directories(root: Path) -> list[Path]:
    skills_root = root / "skills"
    if not skills_root.is_dir():
        return []
    result: list[Path] = []
    for category_dir in sorted(skills_root.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("."):
            continue
        for skill_dir in sorted(category_dir.iterdir()):
            if skill_dir.is_dir() and not skill_dir.name.startswith("."):
                result.append(skill_dir)
    return result
```

- [ ] **Step 2: 新增不变量 C — 父目录名 == category**

在 `validate_skill()` 函数中，读取 manifest 后、`id` 检查前插入。定位点：`validate_repository.py` 约第 150 行（`skill_id = manifest.get("id")` 之前）：

```python
    # 不变量 C：物理父目录名必须等于 manifest.category
    parent_category = skill_dir.parent.name
    if manifest.get("category") != parent_category:
        errors.append(
            f"{manifest_path}: category '{manifest.get('category')}' "
            f"must equal parent directory '{parent_category}' (不变量 C)"
        )
```

- [ ] **Step 3: 验证当前单层仓库被正确报错**

```bash
python tools/validate_repository.py
```

预期：报错——因为当前 `skills/` 下的 6 个目录不再被两层 `skill_directories()` 发现（它们的父目录是 `skills/`，不是 `skills/<category>/`）。**这是正确行为**——进入 Phase 2 迁移后就会解决。

- [ ] **Step 4: 提交工具改动**

确认当前没有无关改动：
```bash
git status --short
```

若只有本 task 的改动且用户已授权提交：
```bash
git add tools/validate_repository.py
git commit -m "feat: skill_directories() 改为两层遍历并新增父目录==category校验"
```

---

### Task 2: 改造 `build_registry.py` glob 为两层

**Files:**
- Modify: `tools/build_registry.py:31`

- [ ] **Step 1: 改 glob 模式**

替换第 31 行：

```python
# 旧：
for manifest_path in sorted((root / "skills").glob("*/manifest.yaml")):
# 新：
for manifest_path in sorted((root / "skills").glob("*/*/manifest.yaml")):
```

`path` 字段由 `skill_dir.relative_to(root)`（第 40 行）自动产出 `skills/<category>/<skill>`，无需额外改动。

- [ ] **Step 2: 验证 registry 生成逻辑**

```bash
python tools/build_registry.py --check
```

预期：registry 为空（`skills: []`）——因为当前单层结构不被两层 glob 扫到。同样正确行为。

- [ ] **Step 3: 提交**

```bash
git add tools/build_registry.py
git commit -m "feat: build_registry glob 改为两层扫描 skills/*/*/manifest.yaml"
```

---

### Task 3: 改造测试夹具与硬编码路径

**Files:**
- Modify: `tests/test_repository_tools.py`

- [ ] **Step 1: 改 `setUp` 夹具为两层**

替换约第 51-52 行：
```python
# 旧：
skill = self.root / "skills/review-code"
(skill / "tests").mkdir(parents=True)
# 新：
skill = self.root / "skills/engineering/review-code"
(skill / "tests").mkdir(parents=True)
```

夹具 manifest 中 `category: engineering` / `id: engineering.review-code`，父目录须为 `engineering` 以满足不变量 C。

- [ ] **Step 2: 改 `test_external_skill_needs_exact_provenance`（约第 140 行）**

```python
# 旧：
(self.root / "skills/review-code/provenance.yaml").write_text(
# 新：
(self.root / "skills/engineering/review-code/provenance.yaml").write_text(
```

- [ ] **Step 3: 改 `test_skill_frontmatter_is_required`（约第 151 行）**

```python
# 旧：
(self.root / "skills/review-code/SKILL.md").write_text(
# 新：
(self.root / "skills/engineering/review-code/SKILL.md").write_text(
```

- [ ] **Step 4: 运行测试确认夹具自洽**

```bash
python -m unittest discover -s tests -v
```

预期：PASS（临时目录内夹具已是两层，`skill_directories()` 能发现，不变量 C 成立）。

- [ ] **Step 5: 提交**

```bash
git add tests/test_repository_tools.py
git commit -m "test: 夹具与硬编码路径适配两层 skills/<category>/<skill>/ 结构"
```

---

## Phase 2: 降险 — 先迁 backend + CLI 实测

### Task 4: Git mv backend 三个 Skill 到 skills/backend/

**Files:**
- Rename: `skills/backend-debugging/` → `skills/backend/backend-debugging/`
- Rename: `skills/backend-implementation/` → `skills/backend/backend-implementation/`
- Rename: `skills/backend-review/` → `skills/backend/backend-review/`

- [ ] **Step 1: 创建类别目录**

```bash
mkdir -p skills/backend
```

- [ ] **Step 2: 逐个 git mv**

```bash
git mv skills/backend-debugging skills/backend/backend-debugging
git mv skills/backend-implementation skills/backend/backend-implementation
git mv skills/backend-review skills/backend/backend-review
```

- [ ] **Step 3: 确认新结构**

```bash
ls skills/backend/
```

预期：`backend-debugging  backend-implementation  backend-review`

- [ ] **Step 4: 确认后端 manifest 不改、category/id 仍为 backend.***

```bash
grep -E '^(id|category):' skills/backend/*/manifest.yaml
```

预期：三个都是 `id: backend.*` / `category: backend`——与父目录 `backend` 一致，不变量 C 自然成立。

- [ ] **Step 5: 运行校验确认 backend 通过**

```bash
python tools/validate_repository.py
```

预期：仅报告 frontend 3 个 Skill 不在两层结构中（因为还在 `skills/frontend-*/`，`skill_directories()` 发现不了）。**没有 backend 相关错误**。registry 校验会因 skills: [] 报 stale，留到 Task 6 解决。

- [ ] **Step 6: 提交**

```bash
git add .
git commit -m "refactor: 迁移 backend 3 个 Skill 到 skills/backend/"
```

---

### Task 5: CLI 两层发现实测（关键假设验证）

**Files:**
- 无文件改动，纯验证。

- [ ] **Step 1: 确认当前工作区状态**

```bash
ls skills/backend/
```

预期：`skills/backend/` 下有 3 个目录，各有 `SKILL.md`。`skills/` 下还有 `frontend-*` 三个残留的单层目录。

- [ ] **Step 2: 运行 `npx skills add . --list`**

```bash
npx skills@latest add . --list
```

- 若发现 3 个 backend Skill → **假设成立**，两层结构被 CLI 正确发现。继续 Task 6。
- 若发现 0 个 → **假设不成立**，回滚 Phase 2（`git mv` 逆操作），回到设计层面重议。不继续前端迁移。

- [ ] **Step 3: （若通过）记录实测输出**

将 `npx skills add . --list` 的输出文本保存以便后续校对 README 安装命令措辞：

```bash
npx skills@latest add . --list 2>&1 | tee /tmp/skills-list-output.txt
```

- [ ] **Step 4: 提交 checkpoint**

```bash
# 无新文件，但可用空提交标 checkpoint
# 或跳过，因为 Task 4 已提交
```

---

## Phase 3: 迁移 frontend + ID 改名

### Task 6: Git mv frontend 三个 Skill 到 skills/web/

**Files:**
- Rename: `skills/frontend-implementation/` → `skills/web/frontend-implementation/`
- Rename: `skills/frontend-review/` → `skills/web/frontend-review/`
- Rename: `skills/frontend-testing/` → `skills/web/frontend-testing/`

- [ ] **Step 1: 创建类别目录**

```bash
mkdir -p skills/web
```

- [ ] **Step 2: 逐个 git mv**

```bash
git mv skills/frontend-implementation skills/web/frontend-implementation
git mv skills/frontend-review skills/web/frontend-review
git mv skills/frontend-testing skills/web/frontend-testing
```

- [ ] **Step 3: 确认新结构**

```bash
ls skills/web/
```

预期：`frontend-implementation  frontend-review  frontend-testing`

- [ ] **Step 4: 提交**

```bash
git add .
git commit -m "refactor: 迁移 frontend 3 个 Skill 到 skills/web/"
```

---

### Task 7: 改 frontend 3 个 manifest（category → web，id → web.*）

**Files:**
- Modify: `skills/web/frontend-implementation/manifest.yaml`
- Modify: `skills/web/frontend-review/manifest.yaml`
- Modify: `skills/web/frontend-testing/manifest.yaml`

- [ ] **Step 1: 改 frontend-implementation manifest**

```bash
# 用 Edit 工具：
# old: "id: frontend.frontend-implementation"
# new: "id: web.frontend-implementation"
# old: "category: frontend"
# new: "category: web"
```

或用 `sed`（注意这两个字符串在各自文件里唯一）：
```bash
sed -i 's/^id: frontend\.frontend-implementation$/id: web.frontend-implementation/' skills/web/frontend-implementation/manifest.yaml
sed -i 's/^category: frontend$/category: web/' skills/web/frontend-implementation/manifest.yaml
```

- [ ] **Step 2: 改 frontend-review manifest**

```bash
sed -i 's/^id: frontend\.frontend-review$/id: web.frontend-review/' skills/web/frontend-review/manifest.yaml
sed -i 's/^category: frontend$/category: web/' skills/web/frontend-review/manifest.yaml
```

- [ ] **Step 3: 改 frontend-testing manifest**

```bash
sed -i 's/^id: frontend\.frontend-testing$/id: web.frontend-testing/' skills/web/frontend-testing/manifest.yaml
sed -i 's/^category: frontend$/category: web/' skills/web/frontend-testing/manifest.yaml
```

- [ ] **Step 4: 验证 manifest 一致性**

```bash
grep -E '^(id|category):' skills/*/*/manifest.yaml | sort
```

预期输出：
```
skills/backend/backend-debugging/manifest.yaml:id: backend.backend-debugging
skills/backend/backend-debugging/manifest.yaml:category: backend
skills/backend/backend-implementation/manifest.yaml:id: backend.backend-implementation
skills/backend/backend-implementation/manifest.yaml:category: backend
skills/backend/backend-review/manifest.yaml:id: backend.backend-review
skills/backend/backend-review/manifest.yaml:category: backend
skills/web/frontend-implementation/manifest.yaml:id: web.frontend-implementation
skills/web/frontend-implementation/manifest.yaml:category: web
skills/web/frontend-review/manifest.yaml:id: web.frontend-review
skills/web/frontend-review/manifest.yaml:category: web
skills/web/frontend-testing/manifest.yaml:id: web.frontend-testing
skills/web/frontend-testing/manifest.yaml:category: web
```

每个 id 都是 `<category>.<目录名>`，每个 category 都等于物理父目录名。

- [ ] **Step 5: 提交**

```bash
git add skills/web/*/manifest.yaml
git commit -m "feat: frontend 3 Skill 的 ID 与 category 改为 web.*"
```

---

## Phase 4: pack、清单、registry 同步

### Task 8: 更新 packs/frontend/pack.yaml

**Files:**
- Modify: `packs/frontend/pack.yaml`

- [ ] **Step 1: 改三处 ID 引用**

```bash
sed -i 's/frontend\.frontend-implementation/web.frontend-implementation/' packs/frontend/pack.yaml
sed -i 's/frontend\.frontend-review/web.frontend-review/' packs/frontend/pack.yaml
sed -i 's/frontend\.frontend-testing/web.frontend-testing/' packs/frontend/pack.yaml
```

- [ ] **Step 2: 验证**

```bash
grep 'id:' packs/frontend/pack.yaml
```

预期：三行都是 `web.frontend-*`。

- [ ] **Step 3: 提交**

```bash
git add packs/frontend/pack.yaml
git commit -m "feat: pack.frontend 引用更新为 web.*"
```

---

### Task 9: 平台清单版本 0.2.0 → 0.3.0

**Files:**
- Modify: `.claude-plugin/plugin.json`
- Modify: `.codex-plugin/plugin.json`
- Modify: `gemini-extension.json`

- [ ] **Step 1: 改三处 version**

```bash
# Claude Code
python3 -c "
import json
d=json.load(open('.claude-plugin/plugin.json'))
d['version']='0.3.0'
json.dump(d,open('.claude-plugin/plugin.json','w'),indent=2,ensure_ascii=False)
print(d['version'])
"

# Codex
python3 -c "
import json
d=json.load(open('.codex-plugin/plugin.json'))
d['version']='0.3.0'
json.dump(d,open('.codex-plugin/plugin.json','w'),indent=2,ensure_ascii=False)
print(d['version'])
"

# Gemini
python3 -c "
import json
d=json.load(open('gemini-extension.json'))
d['version']='0.3.0'
json.dump(d,open('gemini-extension.json','w'),indent=2,ensure_ascii=False)
print(d['version'])
"
```

- [ ] **Step 2: 验证三处版本一致**

```bash
grep '"version"' .claude-plugin/plugin.json .codex-plugin/plugin.json gemini-extension.json
```

预期：全部 `"version": "0.3.0"`。`skills` 字段仍为 `"./skills/"`（不改）。

- [ ] **Step 3: 提交**

```bash
git add .claude-plugin/plugin.json .codex-plugin/plugin.json gemini-extension.json
git commit -m "chore: 平台插件版本 0.2.0 → 0.3.0"
```

---

### Task 10: 重新生成 registry.yaml

**Files:**
- Regenerate: `registry.yaml`

- [ ] **Step 1: 运行 build_registry.py**

```bash
python tools/build_registry.py
```

预期：`wrote registry.yaml`

- [ ] **Step 2: 验证 registry 包含 6 个 Skill**

```bash
grep 'id:' registry.yaml
```

预期：
```
- id: backend.backend-debugging
- id: backend.backend-implementation
- id: backend.backend-review
- id: web.frontend-implementation
- id: web.frontend-review
- id: web.frontend-testing
```

- [ ] **Step 3: 运行校验确认全绿**

```bash
python tools/validate_repository.py
```

预期：`repository is valid`（全部 skill 被两层扫描发现、不变量 C 通过、pack 引用正确、registry 最新、密钥未检出）。

- [ ] **Step 4: 提交**

```bash
git add registry.yaml
git commit -m "chore: 重新生成 registry（两层结构 + web.* ID）"
```

---

## Phase 5: 文档同步

### Task 11: 根 README 重构为用户门面（~150 行）

**Files:**
- Rewrite: `README.md`

- [ ] **Step 1: 逐条核对 AGENTS.md 覆盖（零信息丢失保险）**

在删除根 README 任何段落前，确认对应信息已在 AGENTS.md 存在：

| 原根 README 章节 | 对应 AGENTS.md |
|---|---|
| 「我为什么维护这个仓库」+「维护原则」 | §1（仓库定位） |
| 「一个正式 Skill 包含什么」 | §3（信息唯一职责）、§4（目录契约）、§5（README 必须回答什么） |
| 「新增一个原创 Skill」 | §7（命名/分类/版本）、第 15 节（发布检查表）、模板 `templates/skill/` |
| 「导入一个外部 Skill」 | §8（外部 Skill 引入流程） |
| 「本地开发与校验」 | §12（验证要求） |
| 「版本与发布」 | §7（命名、分类、版本和状态） |
| 「安全边界」 | §13（外部状态与破坏性操作） |
| 「当前已知限制」 | 无对应——保留在根 README |

**若发现 AGENTS.md 缺失且有价值的内容，先补入 AGENTS.md 再从 README 删除。** 核实完毕后再继续 Step 2。

- [ ] **Step 2: 写新版根 README（~150 行）**

结构：

```markdown
# skygazer42-skills

`skygazer42` 的个人 AI Skill 仓库。可通过官方 `npx skills` CLI 或平台插件安装。

完整的 Agent 维护规范见 [`AGENTS.md`](AGENTS.md)。

## 安装

### npx skills（推荐）

# 查看可用 Skill
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

### Codex / Claude Code / Gemini CLI（整包安装）

<!-- 保留现有原生安装命令，略作精简 -->

## 更新和卸载

<!-- 保留现有命令，并入安装节 -->

## 能力目录

### 开发

#### web（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| web.frontend-implementation | 实现页面、组件、表单和前端交互（会改文件） | [→](skills/web/frontend-implementation/README.md) |
| web.frontend-review | 审查前端正确性、无障碍、性能和安全（只读） | [→](skills/web/frontend-review/README.md) |
| web.frontend-testing | 用浏览器验证 UI 流程或补充回归测试 | [→](skills/web/frontend-testing/README.md) |

#### backend（已上线）

| Skill | 一句话 | 详情 |
| --- | --- | --- |
| backend.backend-implementation | 实现 API、服务、数据库和外部集成（会改文件） | [→](skills/backend/backend-implementation/README.md) |
| backend.backend-review | 审查正确性、安全、并发和可靠性（只读） | [→](skills/backend/backend-review/README.md) |
| backend.backend-debugging | 定位根因、影响范围和修复建议（不改代码） | [→](skills/backend/backend-debugging/README.md) |

### 视觉创作（规划中）
<!-- image / video / presentation 等 -->

### 视频（规划中）
### 办公生产力（规划中）
<!-- spreadsheet 等 -->

### 规划 / 任务拆解（规划中）
一个站在实现/审查/测试/排障之上的规划层 skill——接需求 → 技术决策 → 判断涉及前端/后端/设计等领域 → 拆解并路由到对应实现 skill。跨领域，最终类别/ID 待内化时敲定。

## 权限概览

| Skill | 网络 | 读文件 | 写文件 | 执行命令 |
| --- | :---: | :---: | :---: | :---: |
| web.frontend-implementation | 否 | 是 | 是 | 是 |
| web.frontend-review | 否 | 是 | 否 | 是 |
| web.frontend-testing | 是 | 是 | 是 | 是 |
| backend.backend-implementation | 否 | 是 | 是 | 是 |
| backend.backend-review | 否 | 是 | 否 | 是 |
| backend.backend-debugging | 否 | 是 | 否 | 是 |

## 仓库结构

skills/
├── web/
│   ├── frontend-implementation/
│   ├── frontend-review/
│   └── frontend-testing/
└── backend/
    ├── backend-implementation/
    ├── backend-review/
    └── backend-debugging/

## 贡献与维护

本仓库的维护规范、新增/导入 Skill 流程、版本与发布策略、安全边界，全部在 [`AGENTS.md`](AGENTS.md) 中定义。贡献前请先阅读。

## 当前已知限制

- 仓库自身尚未选择统一的开源许可证。
- 行为案例目前是结构化期望，还不是自动评分系统。
- Pack 目前用于组织元数据，尚不负责选择性生成插件副本。
```

- [ ] **Step 3: 验证新 README 中无残留 `frontend.*`**

```bash
grep -n 'frontend\.' README.md
```

预期：无匹配（全部已改为 `web.*` 或仅用于说明旧 ID 的历史文本）。

- [ ] **Step 4: 提交**

```bash
git add README.md
git commit -m "docs: 根 README 重构为用户门面（约150行），安装置顶，维护规范下沉 AGENTS.md"
```

---

### Task 12: 其余 6 个文档 `frontend.*` → `web.*` 同步

**Files:**
- Modify: `packs/frontend/README.md`
- Modify: `skills/web/frontend-implementation/README.md`
- Modify: `skills/web/frontend-review/README.md`
- Modify: `skills/web/frontend-testing/README.md`
- Modify: `skills/backend/backend-implementation/README.md`
- Modify: `skills/backend/backend-review/README.md`

- [ ] **Step 1: 批量改名**

```bash
# 所有 Markdown 文件中的 frontend.frontend-* → web.frontend-*
find skills/web packs/frontend skills/backend -name '*.md' -exec sed -i 's/frontend\.frontend-/web.frontend-/g' {} +
```

- [ ] **Step 2: 验证无残留**

```bash
grep -rn 'frontend\.' skills/ packs/ README.md
```

预期：无匹配（`skills/backend/backend-debugging/README.md` 经核实不含 `frontend.`，其余已全改）。

- [ ] **Step 3: 抽查关键文件**

```bash
# 确认 packs/frontend/README.md 第 5-7 行已改
head -10 packs/frontend/README.md | grep 'web\.'

# 确认各 skill README 第 7 行「全局 ID」已改
for f in skills/web/frontend-*/README.md; do
  echo "=== $f ==="
  sed -n '7p' "$f"
done

# 确认 backend 交叉引用已改
grep 'web\.frontend' skills/backend/backend-{implementation,review}/README.md
```

- [ ] **Step 4: 更新各 skill README 中的路径引用**

`frontend-*` 3 个 skill README 中若有「详细说明：[`skills/frontend-xxx/...`](skills/frontend-xxx/...)」这类链接，需把路径改为 `skills/web/frontend-xxx/...`：

```bash
find skills -name 'README.md' -exec sed -i 's|skills/frontend-|skills/web/frontend-|g' {} +
```

- [ ] **Step 5: 提交**

```bash
git add skills/ packs/
git commit -m "docs: 全部文档 frontend.* → web.* 同步，含交叉引用与路径"
```

---

### Task 13: 更新 AGENTS.md

**Files:**
- Modify: `AGENTS.md`

- [ ] **Step 1: 第 4 节目录契约更新**

替换约第 50 行的目录示例：

```text
skills/<category>/<skill-name>/
├── SKILL.md
├── manifest.yaml
├── README.md
├── provenance.yaml
└── tests/
    └── cases.yaml
```

- [ ] **Step 2: 第 7 节新增不变量**

在命名/分类/版本表述中加入：

```markdown
- 物理类别目录名（`skills/<category>/<skill>/` 的 `<category>`）必须等于 `manifest.category` 和全局 ID 前缀。三者严格对齐：`<manifest.category> = <物理父目录名> = <id 的第一段>`。
```

- [ ] **Step 3: 核实 §5.4(b) 核对结果**

若 Task 11 Step 1 核对时发现 AGENTS.md 缺失有价值内容，本步补入。

- [ ] **Step 4: 提交**

```bash
git add AGENTS.md
git commit -m "docs: AGENTS.md 同步两层目录契约与新不变量"
```

---

## Phase 6: 最终验证

### Task 14: 全量校验

**Files:**
- 无文件改动。

- [ ] **Step 1: 运行三条校验命令**

```bash
python tools/build_registry.py --check
```

预期：`registry.yaml is current`

```bash
python tools/validate_repository.py
```

预期：`repository is valid`

```bash
python -m unittest discover -s tests -v
```

预期：全部 PASS

- [ ] **Step 2: CLI 实测（6 个 Skill 完整发现）**

```bash
npx skills@latest add . --list
```

预期：发现全部 6 个 Skill（3 个 `backend.*` + 3 个 `web.*`）。

- [ ] **Step 3: 与 Phase 2 的实测输出对比**

若两次 `--list` 输出格式一致 → README 安装命令措辞已对。

- [ ] **Step 4: 确认 Git 历史完整**

```bash
git log --oneline --follow skills/backend/backend-implementation/manifest.yaml | head -5
git log --oneline --follow skills/web/frontend-implementation/manifest.yaml | head -5
```

预期：`git mv` 保留了迁移前的提交历史（`--follow` 能跟踪到旧路径的提交）。

- [ ] **Step 5: 汇总报告**

记录：
- 改了什么文件（列表）
- 三条自动校验的结果
- `npx skills add . --list` 的发现数量
- 任何未验证项

---

## 提交与授权提示

每步最后的 `git commit` 步骤**仅在用户明确授权后执行**。若用户未授权提交，则所有改动停留在工作区，后续步骤继续累积。最终由用户决定如何提交（单次 squash？或逐笔保留？）。

依据 `AGENTS.md` §13：「任何提交、推送和发布都作为独立授权处理」。
