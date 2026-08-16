# 短剧资产拆解（drama.short-drama-assets）

从已接受剧本拆解并统筹角色/造型、场景/视图、道具/状态与可选的角色声音方向，维护跨场连续性与可追溯的资产表，供提示词、分镜与审查环节使用。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 短剧资产拆解 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
