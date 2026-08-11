# Review: html-ppt

## 结论

**有保留地晋级。** 交互式 HTML PPT 生成技能：用户提供配色方案、主题和逐页内容，生成单个自包含 `.html` 演示文稿（粒子背景、毛玻璃、键盘/触摸/滚轮导航、缩略图、全屏、帮助、首次气泡指引、进度条）。

为上游仓库为 README 宣称 MIT 但未提供 LICENSE 文件，引入时以声明的 MIT 记录，同时在本仓 README 与 provenance 中明示该事实。其余审核项全部通过，属安全的自包含技能。

## 真实需求

- 用户明确指定要从 ModelScope 内化此技能（页面跳转到 GitHub 镜像源）。
- 这是直给式"给出内容 → 出一个能播的演示"的场景：不需要内容调研，不需要人审关口，不像 ppt-agent 七阶段流水线那样重；也不需要 .pptx 可编辑导出，不像 open-kimi-ppt 那样依赖 PPTD 格式和远程服务。
- 输出是浏览器即开即用的单文件 `.html`，零依赖，适合快速看效果、本地演示、发给他人即点即看。

## 与现有 Skill 的重复分析

| 维度 | presentation.open-kimi-ppt | presentation.ppt-agent | presentation.html-ppt（本次） |
|------|---------------------------|------------------------|-------------------------------|
| 技术路线 | PPTD YAML DSL → .pptx | SVG → 逐元素翻译原生 .pptx | 内联 CSS/JS → 单文件 .html |
| 输出产物 | .pptd 项目 + .pptx | 1280×720 SVG + .pptx + preview.html | 单个 .html，浏览器打开即播 |
| 工作流 | 读内容 → 选场景 → 生成 → 导出 | 七阶段流水线（调研→大纲→检索→策划→设计→出片→QA） | 确认需求 → 初级框架 → 渲染 → 检查 |
| 依赖 | node 编辑器（需网络访问 Kimi 远程服务）+ python3 | python-pptx + lxml + 可选 SVG 渲染器 | 无（纯提示词 + 静态模板） |
| 可编辑性 | .pptx 原生可编辑 | .pptx 原生可编辑 | 无 .pptx，HTML 需改代码/重新生成 |
| 网络需求 | 是 | 阶段 3 检索需要 | 否 |

三者输出物不重叠（.pptx/SVG 流水线 vs 纯 HTML 单文件）、依赖栈不重叠、触发场景不重叠。`web.design-system` 的 Brand 视觉规范是"给产品页面定 token"，不产出可交互的整页演示，也不冲突。**不合并、不补强现有 Skill，独立引入。**

## 安全与平台检查

- **隐式提交/推送/发消息/PR/发布/删除/生产写入**：SKILL.md 全文为生成提示词和 CSS/JS 代码规范，无任何此类指令。逐行扫描通过。
- **密钥/敏感数据**：无密钥、个人数据、内部地址或敏感日志读写。`find_secrets`（validate_repository.py）通过。
- **远程脚本/未声明网络行为**：技能运行时不执行任何脚本、不下载、不调用远程服务。唯一"指针"是 README 中一句"建议同时安装 frontend-design 技能"的软推广，不构成强制。生成物 base_template.html 只有一个空的 `<img id="lightboxImg" src="">`（src 为空，无外部引用），无 `<script src>`、`<link>` 外链。
- **本地行为**：无脚本目录；模板是纯静态内容。生成的是自包含 HTML，不写系统路径。
- **平台绑定**：不绑定特定平台/工具/环境变量；仅作为创作型技能接受人类输入。
- **署名/外链/上传/对外状态**：无强制署名，无强制外链，无案例上传，无对外状态创建。

## License 检查

- 上游 `README.md` / `README_EN.md` 均写明 "MIT License"，但仓库中**没有 LICENSE 文件**，git 历史中也从未添加过。
- 严苛的 SPDX 视角下这属于"声明未物料化"；但作者明确声明 MIT，且仓库开放复制/修改（本身就是给 Claude Code 使用的技能分发）。
- 处理方案：`licence.identifier: MIT`、`license.file: LICENSE`（由本仓依据上游声明生成一份 MIT 许可证文本随副本保存），并在 provenance 的 local_modifications 中明确注明"上游未提供 LICENSE 文件，依 README 声明复制 MIT"，避免读者误以为上游附带该文件。
- 不进入 `NOASSERTION`：README 是作者本人写的持续声明，可信度高于完全无声明；本仓 README 的已知限制页也说明外部技能需独立遵守上游许可证。

## 需要修改的内容

1. 适配 `SKILL.md`：仅新增"生成的文件必须只写用户指定目录、不得触碰其他路径"这一条明确边界（原本靠第 493 行注释暗含），其余内容保持不过度改写。
2. 补全仓库契约文件：manifest.yaml / 中文 README.md / provenance.yaml / tests/cases.yaml。
3. 模板与配色文件按 `references/` 挂入（内容量大且执行时按需读取，不是每次都要内联到 SKILL.md）。
4. 上游两处 README（`README.md`/`README_EN.md`）属于安装/宣传页，规范化时不带入正式技能目录。

## 处理结果

**晋级为 `skills/presentation/html-ppt/`。**