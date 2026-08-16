# 长篇原著分析（drama.short-drama-novel-analyze）

把长篇小说、连载网文或多集散稿拆成可追溯的原著分析：章节索引、改编价值快评、逐章功能提取、剧情单元与节奏聚合、人物与设定归并，最后给出改编价值判定与分集候选，交给开发环节。

本技能来自 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)（MIT），
经规范化后归入本仓 `drama` 分类，与另外八个短剧环节技能保持同级目录以通过套件自检。详见
`incubator/drama-skills/review.md` 与 `provenance.yaml`。

## 使用场景

- 长篇原著分析 面向短剧/漫剧创作产线，与套件内其他技能按契约衔接。
- 所有写入集中在项目工作区内；纯文本产出，无网络、无遥测、无媒体生成。

## 运行要求

- Python 3.10+（标准库，无第三方依赖）。
