# drama — AI 短剧/漫剧创作九技能套件

本分类内化了 [worldwonderer/drama-skills](https://github.com/worldwonderer/drama-skills)
（MIT，revision `bc040191` = tag v0.3.0）的九个公开技能。它们不是互相独立的 skill，而是一个
**强耦合套件**：八个环节技能各带 `suite-ref.json`，经相对路径 `../short-drama/suite-manifest.json`
定位入口路由（`short-drama`）并核对 `core_manifest_sha256`；`scripts/suite_verify.py` 做字节级自检
（无清单外文件 + 内容 hash 一致 + 信任边界不变）。因此九个技能必须保持同级目录。

## 生产流水线

```
novel-analyze（原著抽样快评+分集候选）→ develop（改编契约/故事引擎/分集地图）
→ write（单集因果节拍+可拍剧本）→ assets（人物/场景/道具身份与连续性）
→ image-prompts（Lookdev 风格帧+资产参考图提示词）/ storyboard（分镜+冻结关键帧）
→ video-prompts（逐镜运动/表演/摄影/声音提示词）→ review（独立审查与修订路由）
```

`short-drama` 是入口路由：初始化/继续/恢复/交付项目、组织项目级 Look Development、提供面向创作者的
本地 Dashboard。套件内九个技能全程使用同一套创作者决策、来源引用与连续性契约衔接。

## 信任边界（suite_verify 强制校验）

- `host_text_inference: true`，仅文本推理；`media_generation: false`、`provider_api_calls: false`
  ——套件**刻意不生成图片/视频**，提示词先落文件由创作者确认后再进入生成环节。
- `suite_scripts_outbound_network: false`、`private_source_runtime_access: false`——脚本全部为
  Python 3.10+ **标准库**，无网络、无遥测、无 API key、无第三方依赖；Dashboard 仅绑定 IPv4 回环。
- 若 manifest 信任边界被改、出现清单外文件或内容 hash 不一致，`suite_verify.py` 直接停止。

## 仓库契约说明

- 每个技能目录含本仓契约文件（`manifest.yaml` / `README.md` / `provenance.yaml` / `tests/cases.yaml`
  / `LICENSE`）。按仓库所有者决策，这些元数据被**豁免**于套件字节清单（见 `suite_verify.py` 噪声集合
  与 `tools/update_suite_manifest.py`），169 个内容文件仍保持字节级固定。
- `tools/verify_suite.py` / `tools/update_suite_manifest.py` 随套件保留，用于开发期自检与清单重建；
  `tests/` 为上游 18 个 unittest 文件的落位；`demo/` 为上游《孤身入魔》样例摘录链。
- 内化详情与决策点见 `incubator/drama-skills/review.md`。

## 运行要求

- 套件自检、生命周期工具与 Dashboard 均要求 **Python 3.10+**（标准库，无第三方依赖）。
- Dashboard 仅支持 macOS/Linux（需要安全目录描述符）；Windows 支持套件安装与命令行生命周期工具，
  但拒绝启动 Dashboard——这是上游已声明的限制。
