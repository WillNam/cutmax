# cutmax

**WillNam 出品的 Agent 视频工作室。**

本地地基，官方加持。为 Codex / Cursor 设计的剪辑与素材技能包——照片→手绘动效、翻页日记、B-roll 插入、口播整理，内置 **19 个本地技能 + 4 个官方平台**（Seedance、ChatCut、Pireel），一条链路从本地保底到平台拔高。

**仓库：** https://github.com/WillNam/cutmax

遵循开放 Agent Skills 格式，兼容 Codex、Cursor 等 Agent 环境。

![cutmax showcase](assets/cutmax-hero-dark.png)

## 核心能力

| 能力 | 说明 |
|------|------|
| 统一路由 | 根 `SKILL.md` 一键分发全部视频任务 |
| 照片→手在画→成稿 | Recipe A 脚本 + 反「一张图」规则 |
| 手绘翻页日记 | 内置 Remotion 工程 |
| 平台集成 | Seedance / ChatCut / Pireel 一等公民 |
| 计费礼貌 | 扣费前说明并确认 |
| B-roll 工作流 | Pexels 规则 + MANIFEST |
| 示例 Prompt | 中英双语 |
| 品牌视觉 | 明亮创作者风封面 + 架构图 |
| 品牌风格预设 | 腾讯 / 阿里 / 字节 / B站 / Apple / Spotify 等 |

> **原则：** 本地把事做稳，平台把事做漂亮。

## 安装

```bash
npx skills@latest add WillNam/cutmax
```

全局安装：

```bash
npx skills@latest add WillNam/cutmax --global
```

安装后链接子技能（本地 + 平台）：

```bash
cd ~/.codex/skills/cutmax   # 或 ~/.cursor/skills/cutmax
bash scripts/link-skills.sh ~/.codex/skills
bash scripts/link-platforms.sh ~/.codex/skills   # 可选
```

或手动克隆：

```bash
git clone https://github.com/WillNam/cutmax.git
bash cutmax/scripts/link-skills.sh ~/.codex/skills
```

## 使用

### 照片 → 手绘动效

```text
把这三张图做成手绘过程视频：photo.png / draw.png / art.png
要求白纸起笔、手跟随擦除边缘。竖版 1080×1440。
```

Agent 会读取 `references/recipes.md` 的 Recipe A，调用 `photo_draw_reveal.py` 出片。

### 手绘日记翻页

```text
把这 4 张手绘页做成翻页日记，标题「夏日穿搭」，layout=full。
```

### 平台增强

```text
本地 cut 已完成，用 ChatCut 加字幕和 MG。计费前告诉我消耗。
```

Agent 读取 `references/platform-guide.md`，确认后再调 MCP。

## 内置技能（部分）

**本地地基：** local-video-studio · story-to-handdrawn-video · baocut · manim-video · video-shotcraft · gbro-cover-design · self-media-short-video · …

**官方加持：** Seedance 即梦 · ChatCut · Pireel · seedance-and-prompts

完整列表见 [`references/skill-catalog.md`](references/skill-catalog.md)。

## 仓库结构

```text
SKILL.md                          # 主 Skill 路由中枢
references/
  skill-catalog.md                # 全部技能索引
  recipes.md                      # 本地配方 A–F
  platform-guide.md               # 平台选择与计费礼貌
  brand-presets.md                # 知名品牌视频风格预设
  free-stack.md                   # 允许 / 禁止工具栈
examples/
  prompts.md                      # 中英示例 Prompt
assets/
  cutmax-hero-dark.png            # 品牌封面
  cutmax-architecture.png         # 架构分类图
  cutmax-feature-draw.png         # 功能流程图
skills/                           # 19 个本地子技能
platforms/                        # 4 个官方平台包
tools/                            # Remotion 工程源码
scripts/                          # link-skills / link-platforms
README.md
LICENSE
```

## 核心规范（摘要）

- 默认竖版 1080×1440 或 1080×1920，静音 H.264
- 过程动效：真白纸 → 线稿 → 上色 → 成稿，四阶段肉眼可辨
- 成片前抽帧自检 ≥3 帧；产物写入 `outputs/<slug>/` + MANIFEST
- 付费平台：先说清楚 → 用户确认 → 再调用
- B-roll：Pexels 优先，脸区安全，MANIFEST 映射时间轴

## 展示

<img src="assets/cutmax-feature-draw.png" alt="照片变成有过程的成片" width="100%" />

<img src="assets/cutmax-architecture.png" alt="skills 本地地基 + platforms 官方加持" width="100%" />

## 作者

Copyright © 2026 [WillNam](https://github.com/WillNam)

MIT License — 见 [LICENSE](LICENSE)
