# UI/UX Pro Max（设计智能参考库）

## 一句话定位

UI/UX 设计智能参考库——可搜索的本地数据库，含 84 种风格、192 种配色、74 种字体配对、192 个产品类型推理规则、98 条 UX 准则、104 个图标条目、16 种动效预设和 25 种图表类型。

## 适用场景

- 设计新页面/组件时查询配色、字体、风格建议
- 按产品类型获取行业专属设计推理规则
- 审查 UI 实现是否遵循 UX 准则
- 选择图表类型进行数据可视化
- 跨 22 个技术栈的设计决策

## 不适用场景

- 具体代码实现（转 `web.frontend-implementation`）
- 品牌视觉体系生成（转 `web.brandkit`）
- 设计方向探索（转 `web.frontend-design`）

## 执行前需要的信息

- 产品类型（SaaS、电商、医疗、金融等）
- 设计目标（配色/字体/风格/动效/图表）
- 技术栈

## 执行流程

1. 根据产品类型查询推理规则
2. 匹配 UI 风格、配色方案、字体配对
3. 输出推荐设计系统（含反模式警告）
4. 可选：UX 准则检查清单

## 交付结果

- 推荐设计系统（风格 + 配色 + 字体 + 动效 + 图表）
- 反模式警告
- UX 检查清单

## 默认边界

- **读文件**：是（读取本 Skill 内 CSV 数据库）
- **写文件**：是（`--persist` 时把设计系统写入项目 `design-system/`）
- **执行命令**：是（运行 `scripts/search.py` 查询设计系统）
- **网络**：否（Google Fonts 链接为输出建议，不联网拉取）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `web.frontend-design` | 定设计方向，本 Skill 是设计知识库参考 |
| `web.design-system` | 设计 token 架构，本 Skill 是风格/配色/字体智能推荐 |
| `web.brandkit` | 品牌套件生成，本 Skill 是设计参数推荐 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)（MIT License），做本仓适配。
- **中文速查指南**：补充自 [bbylw/ui-ux-pro-max-skill-cn](https://github.com/bbylw/ui-ux-pro-max-skill-cn)（MIT），见 `references/zh-guide.md`。