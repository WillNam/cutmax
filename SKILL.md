---
name: cutmax
description: >
  Local-first video studio for AI agents. Route to ffmpeg/Pillow/Remotion recipes for photo→hand-drawn
  reveals, handdrawn diaries, stock B-roll, covers, and short-form assembly — with optional official
  platform elevation via Seedance, ChatCut, and Pireel. Use for 本地剪辑、照片成片、手绘动效、B-roll、
  短视频、封面、分镜、即梦/ChatCut/Pireel 平台剪辑.
---

# cutmax

**本地地基，官方加持。** Agent 视频工作室：默认本地跑通，需要更强成片时接入官方平台。

> 安装后读取 `references/skill-catalog.md` 路由子技能；配方细节见 `references/recipes.md`；平台选择见 `references/platform-guide.md`。

## Quick start

| User says | Agent does |
|-----------|------------|
| "把照片做成手绘动效成片" | Recipe A → `photo_draw_reveal.py` 或 Remotion |
| "手绘日记翻页视频" | Recipe C → `story-to-handdrawn-video` |
| "口播去废话加字幕" | Recipe F → `baocut`（需 BaoCut App） |
| "插空镜 B-roll" | Recipe D → Pexels + ffmpeg |
| "用即梦生成视频" | `platforms/seedance2` — **计费前确认** |
| "ChatCut 多轨精修" | `platforms/chatcut` — MCP 剪辑 |
| "竖版口播图文" | `platforms/pireel` — MCP 编排 |

## When to Use

- 用户要剪辑 / 成片 / 过程动效 / 风格对照，优先本地免费路径
- 有照片 / 手绘页 / 口播素材，需要组装成竖版或横版视频
- 需要 B-roll、封面、分镜、短视频脚本
- 用户明确要用 Seedance / ChatCut / Pireel 等官方能力

## When NOT to Use

- 纯文案策划、与视频无关的任务
- 用户只要静态 logo / 封面图（转 `gbro-cover-design`）

## Hard Rules

1. **本地保底**：未经确认不调用付费云 API（Seedance/Kling/Runway/Gemini video/ElevenLabs 等）。
2. **计费礼貌**：使用官方平台前，说明预计消耗并等用户确认。
3. **缺账号回退**：无平台账号时换本地配方或只交付 Prompt / 分镜，不静默失败。
4. **过程动效禁止「淡影成稿当白纸」**：白纸必须真白/近白，线稿与成稿肉眼可辨。
5. **成片前抽帧自检**：至少开场、过程中段、结尾三帧；不要只凭命令成功说「完成」。
6. **产物写入** `outputs/<slug>/`，附 `MANIFEST.md`；大视频不进 skill 目录。

## Router

| 用户意图 | 配方 / 技能 | 工具 |
|---|---|---|
| 实拍→手在画→成稿 | Recipe A | ffmpeg + Pillow |
| 手绘页翻页日记 | Recipe C | Remotion |
| 同图多风格对照 | Recipe B | ffmpeg grade |
| 口播整理 / 字幕 | Recipe F | BaoCut |
| 空镜插入 | Recipe D | Pexels + ffmpeg |
| 封面 / 换装提示词 | Recipe E | 提示词 skill |
| 数学 / 图表动画 | `manim-video` | Manim |
| 运镜 / 分镜 | `video-shotcraft` + `script-to-shootable-storyboard` | — |
| 即梦 AI 视频 | `platforms/seedance2` | Seedance API |
| 多轨精修 | `platforms/chatcut` | ChatCut MCP |
| 竖版口播图文 | `platforms/pireel` | Pireel MCP |

完整列表见 `references/skill-catalog.md`。

## Session Flow

1. **Intake**：素材路径、画幅（默认竖版 1080×1440 或 1080×1920）、时长、是否要过程手、是否用平台。
2. **Route**：按 Router 选 1 个主配方；需要时叠加 B-roll。
3. **Make assets**：本地变换 / 宿主生图 / Remotion 页。
4. **Assemble**：ffmpeg 或 Remotion 出静音片。
5. **Verify**：抽帧确认阶段差异（实拍 ≠ 白纸 ≠ 线稿 ≠ 成稿）。
6. **Deliver**：报告时长、分辨率、路径；更新 MANIFEST。

## Sub-skills 启用

本仓库含 19 个本地技能 + 4 个平台包。安装 cutmax 后运行：

```bash
bash scripts/link-skills.sh ~/.codex/skills    # 或 ~/.cursor/skills
bash scripts/link-platforms.sh ~/.codex/skills   # 可选：官方平台
```

## Key Scripts

过程动效（白纸起笔，手跟随擦除边缘）：

```bash
python3 skills/local-video-studio/scripts/photo_draw_reveal.py \
  --work-dir outputs/my-piece \
  --cycle photo.png draw.png art.png \
  --out outputs/my-piece/FINAL.mp4
```

手绘日记（Remotion）：

```bash
export STORY_VIDEO_PROJECT="$(pwd)/tools/story-to-handdrawn-video"
python3 "$STORY_VIDEO_PROJECT/scripts/run_story_video.py" \
  --images page1.png page2.png --title "标题" \
  --mode full --transition cut --page-duration 4.6 --layout full
```

## Common Mistakes

| 现象 | 原因 | 处理 |
|---|---|---|
| 「一张图一直放」 | 白纸是成稿淡影 | 真白纸起笔；线稿强对比 |
| 画面闪 | 每帧呼吸 zoom / 高光条 | 去掉 pulse；只保留手跟随 |
| 人物腰斩 | `layout=composite` | 改 `layout=full` |
| 卡住要 key | 误入付费 API | 改 Router 本地配方 |
| 静默扣费 | 未确认就调平台 | 计费前说明并等确认 |

## References

- `references/skill-catalog.md` — 全部技能索引
- `references/recipes.md` — 本地配方 A–F
- `references/platform-guide.md` — 平台选择与计费礼貌
- `references/brand-presets.md` — 腾讯/阿里/字节/B站/Apple 等品牌视频风格
- `references/free-stack.md` — 允许 / 禁止工具栈
- `examples/prompts.md` — 中英示例 Prompt
- `rules/stock-broll-workflow.md` — Pexels B-roll 自动工作流
