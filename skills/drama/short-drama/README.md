# 短剧创作路由（drama.short-drama）

基于文件系统初始化、继续、恢复和交付短剧/漫剧项目，提供面向创作者的本地 Dashboard，并组织项目级 Look Development 方向与授权生产观察校准；任务跨多个环节或意图不明时先判断当前状态再路由到对应子技能。
> 本技能是 drama 短剧/漫剧创作套件的**入口路由**，持有 `suite-manifest.json` 与 `scripts/suite_verify.py`，负责套件字节级自检与信任边界校验。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 短剧创作路由 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
