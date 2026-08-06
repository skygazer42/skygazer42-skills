# Design System（设计系统）

## 一句话定位

设计系统构建方法论——三层 token 架构（primitive→semantic→component）、CSS 变量、间距/排版尺度、组件规格和品牌合规展示。

## 适用场景

- 为新项目建立设计 token 体系
- 从零构建组件库规格
- 生成品牌合规的策略性幻灯片
- 系统性设计（非一次性页面设计）

## 不适用场景

- 一次性营销页面设计（转 `web.frontend-design`）
- 品牌视觉板生成（转 `web.brandkit`）
- 风格/配色推荐（转 `web.ui-ux-pro-max`）

## 执行前需要的信息

- 品牌或产品名称
- 设计 token 需求（颜色/间距/排版/组件）
- 技术栈

## 执行流程

1. 定义 primitive token（颜色/间距/字号/圆角）
2. 定义 semantic token（主题/用途映射）
3. 定义 component token（组件级变量）
4. 输出 CSS 变量或平台特定 token 文件
5. 可选：生成策略性幻灯片展示

## 交付结果

- 三层 token 定义
- CSS 变量文件或平台特定 token 配置

## 默认边界

- **读文件**：是
- **写文件**：否
- **执行命令**：否
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `web.ui-ux-pro-max` | 设计参数推荐，本 Skill 是 token 架构和组件规格 |
| `web.frontend-design` | 页面级视觉设计，本 Skill 是系统级设计基础设施 |
| `web.brandkit` | 品牌视觉板，本 Skill 是设计 token 体系 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)（MIT License），做本仓适配。