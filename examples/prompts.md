# Example Prompts

Copy-ready examples for agents and users. Replace `<path>` / `<title>` with actual values.

---

## 中文示例

### 照片 → 手绘动效（本地）

```text
把这三张图做成手绘过程视频：
- 实拍：/path/photo.png
- 作画过程：/path/draw.png
- 成稿：/path/art.png
要求：白纸起笔、手跟随擦除边缘、线稿与成稿肉眼可辨。竖版 1080×1440，输出到 outputs/my-piece/
```

```text
用 cutmax Recipe A 做过程动效，不要付费 API。
每组 cycle 三张图，手在画的感觉要明显，禁止「一张图一直放」。
```

### 手绘日记翻页

```text
把这 4 张手绘页做成翻页日记视频：
/path/01.png /path/02.png /path/03.png /path/04.png
标题「<title>」，layout=full，transition=cut，每页 4.6 秒。
```

### B-roll 插入

```text
给这段口播加空镜 B-roll。
先读 rules/stock-broll-workflow.md，从 Pexels 搜素材，下载到 outputs/broll-<slug>/，写 MANIFEST.md 再剪入。
脸不要被遮挡。
```

### 平台增强（需确认计费）

```text
本地配方已经 OK，现在用 ChatCut 做多轨精修：加字幕、MG、转场。
先告诉我大概消耗什么，我确认后再操作。
```

```text
用即梦 Seedance 把这张分镜图生成 5 秒视频。
走 platforms/seedance2，计费前说明积分消耗。
```

### 短视频全流程

```text
/cutmax 帮我做一条 60 秒竖版短视频：
1. 用 self-media-short-video 写脚本
2. 用 video-shotcraft 设计运镜
3. 本地 Remotion 或 ffmpeg 组装
4. gbro-cover-design 出封面提示词
```

---

## English examples

### Photo → hand-drawn reveal (local)

```text
Use cutmax Recipe A to create a drawing-process video from:
photo.png, draw.png, art.png
True blank page start, hand follows reveal edge, sketch and color must be visually distinct.
Portrait 1080×1440, output to outputs/my-piece/FINAL.mp4
```

### Handdrawn diary

```text
Turn these 4 handdrawn pages into a page-flip diary video.
Title "<title>", layout=full, transition=cut, 4.6s per page.
Use story-to-handdrawn-video Remotion project.
```

### Platform elevation (confirm billing)

```text
Local cut is done. Now use ChatCut MCP for multi-track polish: captions, MG, transitions.
Tell me estimated cost before proceeding.
```

---

## Quick reference

| Prompt snippet | Routes to |
|----------------|-----------|
| "照片做成手绘" | Recipe A |
| "翻页日记" | Recipe C |
| "加空镜" | Recipe D + stock-broll-workflow |
| "口播去废话" | Recipe F / baocut |
| "即梦生成" | platforms/seedance2 |
| "ChatCut 精修" | platforms/chatcut |
| "竖版口播图文" | platforms/pireel |
| "腾讯/Apple 风格短视频" | references/brand-presets.md |
| "封面设计" | gbro-cover-design |
| "数学动画" | manim-video |

Agent: always read `references/skill-catalog.md` for full routing and `references/recipes.md` for timing details.
