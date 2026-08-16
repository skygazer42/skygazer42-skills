# 审核报告：gpt-image（GPT Image 2 生成/编辑 Skill）

- 候选来源：`incubator/gpt-image/candidate/`（上游 `wuyoscar/GPT-Image2-Skill`，revision `068dd9e2`）
- 审核日期：2026-08-16
- 审核人：skygazer42（由 AI 代审）
- 结论：**通过（带已记录的风险处置）**，可按 §8.3 规范化后进入 `skills/art/gpt-image`。

---

## 1. 是否解决个人工作流中的真实问题

是。GPT Image 2 的提示词质量差异极大，本 Skill 的价值核心是一个 162 条提示词的分类 Gallery
（`references/gallery.md` 路由 + 33 个分类文件）+ 19 节提示词工艺清单 `craft.md` +
OpenAI 官方指南存档 `openai-cookbook.md`。这不是一个裸 CLI 封装，而是一套「先检索范例再起草提示词」
的工作流。对个人日常「生成海报 / 图片 / UI 示意图 / 修图」的需求是真实且高频的。

## 2. 与现有 Skill 的重叠

| 现有 Skill | 与 gpt-image 的关系 |
| --- | --- |
| `art.photo-abstract-editorial` | 同标签 `image-generation`/`prompt-engineering`，但它是「单张照片→抽象编辑作品」的单一模式，内容源必须是用户上传照片；gpt-image 是通用生成/编辑 + 提示词库，两者边界清晰，需在 README 中写明 |
| `web.image-to-code` | 截图→前端代码，产出 HTML/CSS，方向相反（gpt-image 是文本→图像） |
| `web.frontend-design` / `web.interface-design` 等 | 交互/界面设计规范与流程，不负责出图 |

**结论**：无重复。`art` 分类下引入 gpt-image 是分类内的自然补充。

## 3. SKILL.md 的隐式写入 / 对外副作用

逐项核查 SKILL.md 与 `scripts/generate.py`：

- **无 git 提交/推送/建 PR/发消息/发布**。
- **写文件**：仅通过 CLI 写输出图像文件（`-f` 指定路径或 `cwd/fig/`），属生成器的正常职责。
- **写配置**：显式禁止——"do not reinstall, overwrite skill folders, create/modify `.env`, or write API keys unless the user explicitly requested setup"。
- **生产/远程写**：会调用 OpenAI API（产生账单），SKILL.md 的 "Key and cost rules" 已明确声明。

## 4. 密钥 / 个人数据 / 敏感信息

- 读取 `OPENAI_API_KEY`（env → `.env` → `~/.env`，不覆盖已有 env）。
- 有明确护栏：`Never print secret values`；未设置 key 时只报错不写入。
- 不读取其他个人数据、内部地址或敏感日志。`-i` 参考图是用户自己提供。

## 5. 远程执行 / 网络行为 / 遥测 —— 需要记录的风险点

- **`scripts/generate.py` 的最后一级回退**：`uvx --from git+https://github.com/wuyoscar/gpt_image_2_skill gpt-image`，
  会从作者 GitHub 临时安装并执行该 Python 包。**这是「下载并直接执行远程代码」**，属于必须记录的风险。
  - 性质：`uvx` 是标准临时安装器（同 pipx/npx），安装的是同一作者、同一 MIT 仓库发布的 CLI，不是任意第三方脚本。
  - 触发条件：仅当 repo 本地 src、已安装 `gpt_image_cli` 包、PATH 上的 `gpt-image` 都不存在时才会触发。
  - 无遥测/埋点代码；`cli.py` 仅用 `urllib.request` 从 OpenAI 自有域名拉取生成图字节。
  - 处置：**保留**，但在 README 与 `provenance.yaml` 中明确记录，Manifest 权限 `network: true`、`execute_commands: true`。
    若日后想收紧，可改为「仅提示用户手动 `uv tool install git+...` 安装」，作为可选项保留。
- CLI 调用 OpenAI API 是 Skill 的核心用途，属声明内行为。

## 6. 路径 / 命令 / 失败安全性

- `generate.py`：`subprocess.run` 委托给 `gpt-image`/`uvx`，失败时打印安装指引并返回退出码 2，无破坏性命令。
- `cli.py`：`-i`/`-m` 文件存在性检查；输出路径 `expanduser().resolve()`；不删除任何文件。
- 退出码语义明确：0 成功 / 1 API 或拒绝 / 2 参数或 key 缺失。

## 7. 平台绑定

- 依赖：Python 3.11+，`gpt-image`、`uv`、`uvx` 任一；`OPENAI_API_KEY`。均在 SKILL.md `compatibility` 声明。
- 上游 SKILL.md 前端带 `metadata.openclaw`（特定运行平台元数据）——规范化时移除，平台适配保留在 `agents/openai.yaml`（与本地 `art.photo-abstract-editorial` 的做法一致）。
- Gallery 与 craft 是纯文本知识，不依赖任何运行时，Skill 在无 CLI 环境下仍可作为提示词库使用。

## 8. 署名 / 外链 / 对外状态

- Gallery 条目保留 `Curated` / `Author + Source` 元数据——这是对**收集的提示词出处**的归属记录，不是强制用户署名。
- 无强制外链、无案例上传、无对外创建状态。

## 9. License

- **MIT**（Copyright (c) 2026 Wuyoscar），明确允许复制与修改，要求保留版权声明。`candidate/LICENSE` 已随附，正式 Skill 会保留该文件。

## 10. README 宣传是否属实

- Gallery 声称 162 条提示词：已核对 31 个分类文件 `### No.` 条目总和 = **162**，属实。
- SKILL.md 的操作循环、Flags、Endpoint routing 与 `cli.py` 实现一致；reference 加载路径（gallery.md / gallery-*.md / craft.md / openai-cookbook.md）全部存在。

---

## 规范化决定（对应 §8.3）

1. 归类 `art`，ID `art.gpt-image`，name `gpt-image`，version `0.1.0`，status `beta`。
2. **不引入上游 `docs/`（约 420MB 示例图）**：gallery-*.md 中的 `<img src>` 与 `- Image:` 行全部剥离，
   保留提示词 + 元数据（示例图是展示资产，非执行所需）。
3. 保留 `scripts/generate.py`、`agents/openai.yaml`、`references/` 全部文本、`LICENSE`（MIT）。
4. SKILL.md 前端适配本地约定：保留 `name`/`description`/`compatibility`，移除 `metadata.openclaw`。
5. Manifest 权限如实覆盖最坏路径：`network`/`read_files`/`write_files`/`execute_commands` 均为 true。
6. 依赖声明：命令 `gpt-image`/`uv`/`uvx`（任一，Python 3.11+），环境变量 `OPENAI_API_KEY`。

## 需仓库所有者知晓的风险提示

- `scripts/generate.py` 的 `uvx` 远程回退会临时安装并执行作者 GitHub 上的 CLI 包（第 5 节）。已记录，可后续收紧。
- Skill 调用 OpenAI API 会产生账单，且需要用户自己的 `OPENAI_API_KEY`。
