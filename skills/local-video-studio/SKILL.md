---
name: local-video-studio
description: >
  Use when the user wants local/free video editing, still-to-video assembly, photo→process→artwork
  reveals, style variants, stock B-roll cuts, handdrawn diary pages, outfit lookbooks, covers/prompts,
  or short silent picture tracks — and must avoid paid cloud video APIs, GEMINI/Atlas/Seedance/ElevenLabs
  keys, or credit-billed generation. Also use for 本地剪辑、免费出片、无 API、手绘过程、Ken Burns、
  素材生成、Pexels B-roll、照片成片.
---

# Local Video Studio（本地免费剪辑 + 素材）

## Overview

把「能本地跑通、不烧付费 API」的视频剪辑与素材生成收成一条工作室流程。默认工具栈：`ffmpeg` + `PIL` + 已安装的本地 Remotion 手绘项目 + 宿主免费生图（若可用）+ Pexels 免费素材。

**硬原则：本地保底；官方平台用于拔高。扣费云生成前必须说明并征得确认。缺平台账号时换本地配方或只交付提示词/分镜，不静默失败。**

## When to Use

- 用户要剪辑 / 成片 / 过程动效 / 风格对照片，但不要付费 API
- 有照片 / 手绘页 / 口播成片素材，需要本地组装
- 需要 B-roll、封面提示词、换装脚本，但不进入付费视频阶段
- 之前试过 `vox` / `gbro` 视频 / Seedance 等因缺 key 卡住，要免费替代

## When NOT to Use

- 用户明确要求 Seedance / Kling / Runway / Gemini video / Atlas Vox 等付费云生成
- 需要口播 ASR 且只能走 ElevenLabs 计费转写（改用本地/BaoCut，或先要用户提供字幕）
- 纯文案策划、与视频无关的任务

## Hard Rules

1. **未经确认不要擅自调用**：`GEMINI_API_KEY`、`ATLASCLOUD_API_KEY`、Seedance/Kling/Runway 付费接口、ElevenLabs 计费 ASR、任何按次扣费的 `submit_video` / 云端 I2V。
2. **允许**：`ffmpeg` / `ffprobe`、Pillow、本地 Remotion（`story-to-handdrawn-video`）、宿主内置免费生图（若环境提供）、Pexels 免费下载、纯提示词 Skill、已打开且不额外扣费的剪辑 MCP（仅用已有素材/免费库）。
3. **先问清楚画幅与时长**；默认竖版 `1080×1440`（3:4）或 `1080×1920`（9:16），静音 H.264，后期再配音。
4. **成片前必须抽帧自检**（至少：开场、过程中段、结尾）。不要只凭命令成功就说「完成」。
5. **过程动效禁止「淡影成稿当白纸」**：白纸必须是真白/近白，线稿与成稿必须肉眼可辨，否则用户会觉得「一张图一直放」。
6. **产物写入** `outputs/<slug>/`，附 `MANIFEST.md`（素材→时间轴映射）。不要把大视频塞进 skill 目录。

## Router（先选配方）

| 用户意图 | 免费配方 |  defer / 不走 |
|---|---|---|
| 照片序列翻页 / 手绘日记 | `story-to-handdrawn-video` + `layout=full` | composite 切半布局 |
| 实拍→手在画→成稿 | Recipe A（本 skill scripts） | 付费 I2V |
| 同图多风格对照 | Recipe B ffmpeg 调色/排版 | Seedance |
| 口播去废话 / 字幕 | BaoCut 本地 CLI（若已装）或用户给 SRT | ElevenLabs / 云 ASR |
| 纸拼贴 / Vox 讲解成片 | 只做 Gate1 方案 + 静帧；或改 Recipe A/B | gbro/vox 视频阶段（要 key） |
| 换装卡点 | `female-outfit-director` 提示词+脚本 | 自动云端渲染 |
| 封面 | `gbro-cover-design` 提示词 | 代扣费生图 API |
| 口播插空镜 | Pexels B-roll + ffmpeg / ChatCut 已有库 | 付费生成 B-roll |
| 数学/图表动画 | `video-use` 的 Manim 子 skill（本地） | 云 MG |

详细步骤见 `references/recipes.md`。免费栈边界见 `references/free-stack.md`。

## Session Flow

1. **Intake**：素材路径、画幅、目标时长、是否要过程手、是否要 B-roll、输出文件名。
2. **Route**：按上表选 1 个主配方；需要时叠加 Pexels B-roll。
3. **Make assets**：本地变换 / 宿主生图 / 手绘 Remotion 页；禁止「先去申请付费 key」。
4. **Assemble**：ffmpeg 或 Remotion 出静音片。
5. **Verify**：抽帧阅读；确认阶段差异明显（实拍 ≠ 白纸 ≠ 线稿 ≠ 成稿）。
6. **Deliver**：报告时长、分辨率、路径；可选同步飞书文档（若用户要）。

## Quick Commands

手绘日记（本地 Remotion）：

```bash
export STORY_VIDEO_PROJECT="/Users/minnan/Projects/conan-digital-human/tools/story-to-handdrawn-video"
cd "$STORY_VIDEO_PROJECT"
python3 scripts/run_story_video.py \
  --images /abs/01.png /abs/02.png /abs/03.png /abs/04.png \
  --title "标题" --mode full --transition cut \
  --page-duration 4.6 --layout full
```

过程动效（白纸起笔，防「一张图」）：

```bash
python3 ~/.codex/skills/local-video-studio/scripts/photo_draw_reveal.py \
  --work-dir /abs/outputs/my-piece \
  --cycle photo.png draw.png art.png \
  --out /abs/outputs/my-piece/FINAL.mp4
```

（`--cycle` 可重复多次；每组三张：实拍 / 作画过程静帧 / 成稿）

## Sibling Skills（免费可用部分）

- `story-to-handdrawn-video` — 本地手绘日记片
- `female-outfit-director` — 换装提示词与时间轴（不渲染）
- `gbro-cover-design` — 封面提示词（不调用付费 API）
- `baocut` — 本地转写/粗剪（需已装 BaoCut App）
- `video-use` / `manim-video` — 仅用本地 ffmpeg/Manim 部分；跳过需 ElevenLabs 的步骤或改用已有字幕
- 项目规则 `stock-broll-workflow` — Pexels 免费 B-roll

## Platforms（官方加持）

cutmax 的 `platforms/` 收录 Seedance、ChatCut、Pireel 等官方能力——为了成片更好，不是抵制。
本地配方保底；需要大模型画面或多轨精修时，读取并遵循对应 platform skill，**扣费生成前先确认用户**。
启用：`./scripts/link-platforms.sh`

## Proven Case Anchors（本仓库）

参考 `outputs/skill-trials-2026-08-06/`：

- 手绘 full 切页：`handdrawn/conan-outfit-diary-layout-full-preview-4imgs.mp4`
- 过程清晰版：`handdrawn/conan-photo-draw-hand-motion-CLEAR.mp4`
- 匹配手册：`FEISHU_MATCHING_GUIDE.md`

## Common Mistakes

| 现象 | 原因 | 处理 |
|---|---|---|
| 「一张图一直放」 | 白纸是成稿淡影 | 真白纸起笔；线稿强对比 |
| 人物腰斩 | `layout=composite` | 改 `layout=full` |
| 画面闪 | 每帧呼吸 zoom / 高光条 | 去掉 pulse；只保留笔尖/手跟随 |
| 卡住要 key | 误入 gbro/vox/Seedance | 改 Router 免费配方 |
| 说完成但没动 | 只看了命令成功 | 必须抽帧看阶段差异 |
