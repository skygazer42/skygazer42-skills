# Review: ppt-agent

## 结论

**保留，直接晋级。** 端到端 PPT 生成技能：七阶段流水线（需求调研 → 大纲 → 资料检索 → 策划稿 → 整页 SVG 设计 → 预览出片 → 视觉 QA），两道人审关口（需求 + 大纲），最终产出 1280×720 整页 SVG + 原生可编辑 .pptx + 网页预览。与现有 `presentation.open-kimi-ppt` 互补。

## 保留理由

- **工作流成熟**：七阶段流水线固化"人类顶级 PPT 团队"的完整流程，每阶段有明确的输入/产出/落盘文件，可中断恢复。
- **人审关口设计**：在需求和大纲两处停下等用户确认，避免全自动跑偏。
- **内容优先理念**：先调研主题、确定听众/目的/场合，再构思内容和大纲，最后才是设计——这与现有 open-kimi-ppt 的"格式先行"互补。
- **原生可编辑 .pptx**：`build_pptx.py` 将 SVG 逐元素翻译为 PowerPoint 原生形状（矩形/圆/线条/文本框），打开即可改字改色，仅复杂图标走透明 PNG 叠层——这是区别于其他 PPT 工具的关键能力。
- **视觉 QA 关卡**：阶段 7 把 .pptx 渲染成图片逐页检查文字溢出、元素重叠、配色不一致等问题，修复后才交付。
- **自包含**：SKILL.md（瘦路由）+ 4 个提示词 + 2 个参考文件 + 2 个 Python 脚本，无外部 API 依赖。
- **与现有 Skill 互补**：
  - `presentation.open-kimi-ppt`：基于 PPTD DSL 格式，适合精确控制 OOXML 结构；ppt-agent 是"内容调研→策划→视觉设计"的内容驱动流水线。
  - 两者可互相衔接：ppt-agent 产出内容和大纲后，可选择用 open-kimi-ppt 的 PPTD 格式做精确排版。

## 安全与 License 检查

- **License**：MIT（Copyright 2026 joker-sxj），允许复制、修改、再分发。
- **脚本安全**：`build_pptx.py` 和 `build_preview.py` 是纯数据转换脚本，无网络访问、无 shell 注入风险。Chrome headless 渲染仅在本地运行。
- **依赖**：Python `python-pptx` + `lxml`；可选 SVG 渲染器（Chrome/Edge/rsvg-convert 等）——均为开发工具链常见组件。

## 与 open-kimi-ppt 的关键差异

| 维度 | open-kimi-ppt | ppt-agent |
|------|---------------|-----------|
| 技术路线 | PPTD YAML DSL → pptx | SVG → 逐元素翻译原生 pptx |
| 工作流 | 读内容 → 选场景 → 生成 PPTD → 导出 | 七阶段流水线（调研→大纲→检索→策划→设计→出片→QA） |
| 人审关口 | 无（一次性生成） | 2 道（需求 + 大纲） |
| 内容调研 | 不包含 | 阶段 1 联网调研 + 顾问式提问 |
| 设计方案 | PPTD 场景分类指南 | Bento Grid 版面方法论 + 风格令牌 |
| 质量保证 | 格式合规检查 | 渲染逐页 QA（溢出/重叠/配色一致性） |
| 网络需求 | 需要（编辑器连接 Kimi 远程服务） | 仅阶段 3 资料检索需要；出片全本地 |
| 脚本 | node 编辑器 + python3 导出 | 2 个 Python 脚本（preview + pptx builder） |

## 需要修改的内容

无。上游内容清洁，已直接晋级。

## 处理结果

**已晋级为 `skills/presentation/ppt-agent/`。**