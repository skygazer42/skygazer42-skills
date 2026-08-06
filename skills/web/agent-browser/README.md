# Agent Browser（浏览器自动化）

## 一句话定位

浏览器自动化 CLI（Rust 原生），让 AI Agent 能操控浏览器——导航、填表、点击、截图、提取数据、测试 Web 应用。

## 适用场景

- 需要 AI Agent 操作网页（填表/点击/导航）
- Web 应用截图和数据提取
- 自动化浏览器测试
- Electron 桌面应用自动化（VS Code/Slack/Discord/Figma）

## 不适用场景

- 不需要浏览器交互的纯 API 测试（转 `security.api-security`）
- 前端组件测试（转 `web.frontend-testing`）
- 未安装 agent-browser CLI 的环境

## 执行前需要的信息

- 已安装 `agent-browser` CLI（`npm i -g agent-browser && agent-browser install`）
- 目标 URL 或操作描述

## 执行流程

1. 确保 agent-browser CLI 已安装
2. 加载核心技能内容：`agent-browser skills get core`
3. 按需加载专项技能（electron/slack/dogfood 等）
4. 执行浏览器操作

## 交付结果

- 浏览器操作结果（截图/数据/页面状态）

## 默认边界

- **读文件**：是
- **写文件**：否
- **执行命令**：是（agent-browser CLI）
- **网络**：是（浏览器操作需要网络）

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `web.frontend-testing` | 用浏览器验证 UI 流程，本 Skill 是底层浏览器自动化 |
| `web.web-clone` | 复刻网站，本 Skill 是操控浏览器 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)（Apache 2.0 License），做本仓适配。