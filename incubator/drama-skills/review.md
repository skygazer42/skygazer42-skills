# 审核报告：drama-skills（AI 短剧/漫剧创作九技能套件）

- 候选来源：`incubator/drama-skills/candidate/`（上游 `worldwonderer/drama-skills`，revision `bc040191` = tag `v0.3.0`，repo 根）
- 审核日期：2026-08-16
- 审核人：skygazer42（由 AI 代审）
- 结论：**有条件通过**——工程扎实、安全面干净（纯文本产出、无网络无遥测、stdlib-only）、与仓库现有 skill 几乎无重叠，直接填补「AI 短剧/漫剧生产」空缺。引入形态用户已选**全链路（9 技能）**。内化前需解决套件自检与仓库契约文件的调和，见文末三个决策点。

---

## 1. 是否解决个人工作流中的真实问题

是，且独特。用户明确问过「有没有做 AI 漫剧的 skill」，本仓此前无此类能力。drama-skills 把点子或长篇原著一路做成可拍分镜、资产设定、图片提示词、视频提示词与独立审查记录：

```
novel-analyze（原著抽样快评+分集候选）→ develop（改编契约/故事引擎/分集地图）
→ write（单集因果节拍+可拍剧本）→ assets（人物/场景/道具身份与连续性）
→ image-prompts（Lookdev 风格帧+资产参考图提示词）/ storyboard（分镜+冻结关键帧）
→ video-prompts（逐镜运动/表演/摄影/声音提示词）→ review（独立审查与修订路由）
```

`short-drama` 是入口路由（初始化/状态/接受/恢复/交付/Look Development/Dashboard），9 技能全程用同一套创作者决策、来源引用与连续性契约衔接。来自真实漫剧工作室产线（README 自述上千项目），方法论密度远超仓库内多数写作类 skill。

## 2. 与现有 Skill 的重叠

| 现有 Skill | 与 drama-skills 的关系 |
| --- | --- |
| `writing.qu-ai-wei` / `writing.humanizer` / `writing.authentic-writing` | 通用「去 AI 味 / 人声」文本清理，面向任意中文/英文散文；drama 的 `short-drama-review` 内 `anti-template-repair` 是**短剧生产循环内**的模板感诊断（绑定 fresh reviewer + 修订路由），只服务于短剧链，不替代通用去味 skill |
| `art.gpt-image` | 实际**调用 OpenAI API 生成图片**；drama 的 `image-prompts` 只写**提示词文本、不生成媒体**（套件 trust_boundary 明示 `media_generation: false`）。分层互补：drama 出提示词 → gpt-image 出图，非重复 |
| `art.photo-abstract-editorial` | 摄影抽象编辑风格，与短剧生产无关 |

**结论**：无重复。最接近的相邻 skill 均为互补层（文本生成 vs 文本去味；提示词创作 vs 图片生成）。

## 3. SKILL.md 与脚本的隐式写入 / 对外副作用

- 全部写入集中在项目工作区内（`short-drama.json`、`.short-drama/`、`剧集/`、`设定集/`、`项目开发/`）。
- `project_tool.py` 的 `publish` 是**本地文件系统发布**（预写日志 WAL 原子提交 candidate），不附带 git push/commit、不发消息、不建 PR、不发布到远端。全仓脚本扫描**无 `git`/`gh` 调用**。
- Dashboard（`dashboard_server.py`）读写项目文本文件；保存不等于采用（创作者在对话中显式接受版本）。
- 无隐式删除：修订只把依赖的旧产物标 `stale`，不静默覆盖创作者文件；外部编辑冲突提供 `adopt/restore/merge` 三选，不静默修复。

## 4. 密钥 / 个人数据 / 敏感信息

- 无 API key、无环境变量读取、无凭据（`secrets`/`getenv`/`API_KEY`/`TOKEN` 扫描仅命中 Dashboard 的 `secrets.token_urlsafe(32)` 会话令牌与 `project_tool` 的 JSON-pointer 路径令牌）。
- Dashboard 安全设计扎实：**仅绑定 IPv4 回环**（非 loopback 直接 `raise ValueError`）、每次启动生成独立会话令牌与随机 API 路径、浏览器用地址片段换 `HttpOnly` 本机会话、`_security_ok` 用 `hmac.compare_digest` 校验、Host/Origin 校验、路径包含与 symlink 拒绝。
- `knowhow`（维护者技能）只在维护者明确授权、会话已提供只读访问时读非公开来源，把凭据/源名留在隔离工作区，公开产物去标识——不把私有观察带入公开技能树。
- 交付包排除凭据、绝对路径、非公开来源材料、机器状态。

## 5. 远程执行 / 网络行为 / 遥测

- **无**：trust_boundary 显式声明 `host_text_inference` 仅文本推理、`suite_scripts_outbound_network: false`、`provider_api_calls: false`、`media_generation: false`、`private_source_runtime_access: false`，`suite_verify.py` 还会**拒绝任何违反该边界的 manifest**。
- 技能脚本全为 Python 3.10+ **标准库**（`project_tool.py` 4965 行 / `dashboard_server.py` 1153 行 / novel_index / screenplay_index / storyboard_check / motion_timing_check / container_check / voice_sheet_check），无第三方依赖，无 `urllib.request`/`socket`/`requests`/`httpx`/`subprocess`/`os.system`/`eval`/`exec`/`curl`/`wget`。`subprocess` 仅出现在测试夹具（用子进程跑 CLI）。
- 不下载、不执行远程脚本，无遥测。

## 6. 路径 / 命令 / 失败安全性

- `project_tool.py` 职责定位「只拥有文件系统完整性」：五轴生命周期、可恢复多文件发布、原子保存、事务恢复必须先读后写、可重复运行；来源漂移（source drift）用 `content_sha256` 校验，改过原文就报错。
- Dashboard 对每次请求做路径包含（path containment）与 `PurePosixPath` 规约，拒绝 symlink，原子保存，防并发编辑。
- 各校验脚本（storyboard_check / motion_timing_check / container_check）只做**算术与结构比对**，不评价质量；报错先修产物再继续，不靠措辞掩盖。
- 失败安全：候选预览必须标 `provisional` / `authority:candidate`，未接受版本不进入交付；交付前 `verify` 用校验和复核。

## 7. 平台绑定与可移植性

- 要求 **Python 3.10+**（stdlib），macOS 自带 3.9 不够——README 明确写明。
- Dashboard 仅 macOS/Linux（安全目录描述符要求），Windows 支持套件安装与命令行生命周期工具但拒绝启动 Dashboard——这是**已声明限制**，非隐藏绑定。
- 不依赖专属 CLI、未安装工具或不存在的环境变量。`agents/openai.yaml` 提供跨运行时（Claude Code / Codex）的展示接口。
- 套件强耦合（见决策点 2）：9 技能必须同级安装，`suite-ref.json` 经相对路径 `../short-drama/suite-manifest.json` 定位核心并核对 `core_manifest_sha256`。

## 8. 署名 / 外链 / 对外状态

- 无强制署名、无外链植入、无案例上传、无对外创建状态。运行时只读本地项目文件。
- 上游 README 的致谢（LINUX DO 社区）与宣传语为上游促销内容，规范化时按 §8.3 移除。

## 9. License

- **MIT**（Copyright (c) 2026 drama-skills contributors），允许复制与修改，需保留版权声明（`candidate/LICENSE` 已随附）。无第三方 notices 依赖。规范化时 LICENSE 随正式 skill 保留。

## 10. README 宣传是否属实

抽查全部属实：9 个技能确实存在且职责与 README 表格一致；`suite-manifest.json` 固定 169 文件 SHA-256 + trust_boundary，`suite_verify.py` 会拒绝清单外文件、hash 不一致、信任边界被改；`demo/` 确有《孤身入魔》剧本→资产→分镜→视频提示词摘录链；Dashboard 的 loopback-only 与 stdlib-only 与源码一致；「刻意不含生图生视频、提示词先落文件由人确认」与 trust_boundary 一致；18 个 unittest 文件覆盖生命周期/索引/时账/交付边界等，工程可信度高。

---

## 结论与需仓库所有者决策的点

**核心判断**：这是目前见过的安全面最干净、契约最完备的外部 skill 套件之一——纯文本产出、stdlib-only、无网络无遥测、无隐式提交，且 `suite_verify` 自带「清单外文件/内容篡改/越权信任边界 → 停止」的字节级完整性校验。引入价值真实（填补 AI 短剧/漫剧空缺，用户已确认全链路形态），可**有条件通过**。

三个决策点（仓库所有者已确认，2026-08-16）：

1. **分类落位**：**新建 `drama` 分类**——`skills/drama/short-drama/` … `short-drama-review/` 9 技能同级，与 `writing`/`art` 平级。
2. **套件自检与仓库契约的调和**：**豁免仓库元数据**——在 `suite_verify.py` + `tools/update_suite_manifest.py` 的噪声集合里显式登记本仓契约元数据（`manifest.yaml`/`README.md`/`provenance.yaml`/`LICENSE`/`tests/cases.yaml`），保留 169 个内容文件的字节完整性，「可执行文件永不被视为噪声」的安全属性不变。
3. **规范化取舍**：**保留 Dashboard 与 demo**；剥离 `maintainers/skills/short-drama-knowhow`、README 宣传语/README_EN、`docs/` 截图。套件自检工具（`suite-manifest.json` / 8 个 `suite-ref.json` / `suite_verify.py` / `tools/verify_suite.py` / `update_suite_manifest.py`）随 9 技能保留。
