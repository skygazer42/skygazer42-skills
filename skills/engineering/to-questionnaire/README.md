# To Questionnaire（决策转问卷）

## 一句话定位

将无法自行回答的决策转化为结构化问卷，供他人异步填写。面向接收者撰写，按重要性排序。

## 适用场景

- 需要他人提供决策信息但无法当面沟通
- 跨团队协作中需要收集多方意见
- 技术决策需要业务方确认

## 不适用场景

- Agent 自己能回答的问题
- 可以当面沟通的简单决策

## 执行前需要的信息

- 接收者是谁（角色、专业领域、与用户的关系）
- 需要从接收者获得什么（具体决策或事实）

## 执行流程

1. 确定接收者身份和背景
2. 明确需要对方回答的具体决策点
3. 按重要性排序撰写问卷
4. 保存为 `to-questionnaire-<slug>.md`

## 交付结果

- 结构化的问卷文档（Markdown）

## 默认边界

- **读文件**：是
- **写文件**：是
- **执行命令**：否
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.grilling` | 批判性审问方案，本 Skill 是收集信息 |
| `engineering.brainstorming` | 设计探索，本 Skill 是信息收集 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `to-questionnaire`（MIT License），做本仓适配。