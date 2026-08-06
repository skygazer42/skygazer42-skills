# Teach（教学）

## 一句话定位

在结构化教学工作区中逐步教授新技能或概念，包含 MISSION、学习记录、参考资料和课程。

## 适用场景

- 用户想学习新技能或概念
- 需要多会话持续学习的长期教学
- 需要高质量参考资料和交互式课程

## 不适用场景

- 一次性快速答疑（直接回答即可）
- 纯代码审查或实现任务

## 执行前需要的信息

- 用户想学什么
- 学习动机（MISSION）

## 执行流程

1. 建立教学工作区（MISSION.md、RESOURCES.md、learning-records/、lessons/）
2. 寻找高质量参考资料
3. 基于资料设计交互式课程
4. 记录学习心得和关键洞察
5. 根据学习记录调整后续课程

## 交付结果

- 教学工作区（含 MISSION、RESOURCES、学习记录、课程）

## 默认边界

- **读文件**：是
- **写文件**：是
- **执行命令**：否
- **网络**：否

## 与相邻 Skill 的区别

| Skill | 区别 |
| --- | --- |
| `engineering.brainstorming` | 设计探索，本 Skill 是结构化教学 |
| `engineering.writing-for-agents` | 为 Agent 写文档，本 Skill 是为人教学 |

## 版本与来源

- **版本**：`0.1.0` / `beta`
- **来源**：基于 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `teach`（MIT License），做本仓适配。