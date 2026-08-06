# Open Kimi PPT（演示文稿生成）

## 一句话定位

基于 Moonshot AI 的 PPTD 格式（YAML 中间 DSL）创建、编辑、复刻和导出演示文稿，默认产出 PPTD 项目目录 + 本地 .pptx 文件。

## 适用场景

- 从零创建演示文稿（PPT/PPTX）
- 从已有 PPTX 模板生成新演示
- 将图片/PDF 复刻为可编辑的 PPTD
- 编辑已有 PPT 的特定页面
- 信息图/海报等单页高视觉设计
- 任何需要"做 PPT"的请求

## 不适用场景

- 不需要 PPT/PPTX 格式的纯文档（转 `writing.*` 系列）
- 品牌视觉体系设计（转 `web.brandkit`）
- 页面级前端实现（转 `web.frontend-implementation`）
- 视频/动画演示（本 Skill 专注静态幻灯片）

## 执行前需要的信息

- PPT 主题/内容/文档
- 设计方向（自主设计/设计系统/模板/风格迁移）
- 输入类型（仅主题/完整文档/页级大纲）
- 页数需求（如无要求则根据内容自行决定）

## 执行流程

1. 阅读所有用户上传文件和 PPTD 格式规范 `references/pptd.md`
2. 确定目的（新建/编辑/复刻）+ 设计方向 + 输入类型 + 页数
3. 按场景分类读取对应设计指南 `references/slides_categories/`
4. 生成 PPTD 项目（`.pptd` + `pages/` + `media/`）
5. 导出为 .pptx（嵌入字体 + fade 转场）
6. 验证：检查 PPTD 格式合规、PPTX 结构完整性

## 交付结果

- 完整的可编辑 PPTD 项目目录
- 本地生成的 .pptx 文件（嵌入字体，fade 转场）

## 默认边界

- **读文件**：是
- **写文件**：是（生成 PPTD 项目 + PPTX）
- **执行命令**：是（python3 导出脚本、node 编辑器）
- **网络**：是（编辑器需网络访问 Kimi 远程服务）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `web.brandkit` | 品牌视觉板生成，本 Skill 是完整多页 PPT 生成 |
| `web.frontend-design` | 网页设计，本 Skill 是幻灯片设计 |
| `writing.authentic-writing` | 文本写作，本 Skill 是演示文稿 |

本 Skill 是本仓库唯一的 PPT/演示文稿生成能力。

## 行为案例

### 案例 1：典型 PPT 创建

**输入**：用户提供一份产品发布新闻稿，要求"做成 10 页的发布 PPT"。

**预期行为**：
1. 读取新闻稿全文
2. 读取 `references/pptd.md` 和场景设计指南
3. 确定设计方向，生成 PPTD 项目
4. 导出为 .pptx
5. 产出 PPTD 目录 + PPTX 文件

### 案例 2：复刻 PPT

**输入**：用户上传竞品 PPT 截图，要求"复刻这个风格做我们的版本"。

**预期行为**：
1. 分析图片中的元素位置、字体、大小
2. 1:1 复刻为 PPTD 格式
3. 替换为用户的品牌内容
4. 产出可编辑的 PPTD 项目

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [Binaryify/open-kimi-ppt-skill](https://github.com/Binaryify/open-kimi-ppt-skill)（MIT License），做本仓适配（见 `provenance.yaml`）。