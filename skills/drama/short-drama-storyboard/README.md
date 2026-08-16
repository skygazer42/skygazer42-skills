# 短剧分镜与冻结关键帧（drama.short-drama-storyboard）

把已接受的中文短剧剧本和资产转成原文落实表、有戏剧动机的镜头、连续性边界与冻结关键帧提示词；关键场次可先做场次视觉计划或 Coverage Audition 比较再定稿。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 短剧分镜与冻结关键帧 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
