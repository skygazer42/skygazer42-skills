# 短剧独立审查（drama.short-drama-review）

独立校验与审查文件系统短剧项目中的原著分析、故事、剧本、资产、连续性、资产图片提示词、分镜、关键帧与视频提示词，消费有界授权生产观察做当前项目校准，输出带证据的审查记录与修订路由。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 短剧独立审查 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
