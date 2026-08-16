# 短剧视频提示词（drama.short-drama-video-prompts）

为已接受的短剧镜头与关键帧编写或修改可复制的通用视频提示词与运动规格，覆盖动作、表演过程、运镜、对白口型、环境运动、镜头时长与节奏。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 短剧视频提示词 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
