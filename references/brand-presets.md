# Brand Style Presets for Video Content

Use these presets as **visual direction anchors** when the user references a company, asks for a recognizable brand vibe, or wants video content "in the spirit of" a famous brand.

> **Legal note:** Presets describe *category aesthetics* — pacing, color, typography mood, B-roll tone. Do not reproduce trademarked logos, exact brand marks, or registered visual identity in rendered output unless the user owns the brand.

## How to apply

1. Match user input to preset `aliases`.
2. Copy `visual_cue`, `palette`, `pacing`, `typography` into shot design / cover prompt.
3. Enforce `do_not_copy` during QA.
4. Route to local recipe (A–F) or platform (Seedance / ChatCut / Pireel) as needed.

---

## 中国互联网 & 科技

### Tencent 腾讯

| Field | Value |
|-------|-------|
| **aliases** | 腾讯, Tencent, QQ, 企鹅 |
| **visual_cue** | Tech blue gradients, rounded UI cards, social/community warmth, clean sans-serif |
| **palette** | Tech blue `#0052D9`, white, muted orange accent |
| **pacing** | Medium, friendly; 2–3s holds on key messages |
| **typography** | Clean sans, generous line spacing |
| **do_not_copy** | QQ penguin logo, Tencent wordmark |

### Alibaba 阿里巴巴

| Field | Value |
|-------|-------|
| **aliases** | 阿里, Alibaba, 淘宝, Taobao |
| **visual_cue** | Warm orange energy, commerce/product showcase, optimistic motion |
| **palette** | Orange `#FF6A00`, cream, charcoal |
| **pacing** | Upbeat, product-forward; quick cuts on features |
| **do_not_copy** | Alibaba smile logo, Taobao cat |

### ByteDance 字节跳动

| Field | Value |
|-------|-------|
| **aliases** | 字节, ByteDance, 抖音, TikTok, 今日头条 |
| **visual_cue** | Dynamic vertical rhythm, bold captions, youth energy, dark + accent split |
| **palette** | Near-black, red/cyan accent, deep navy bg |
| **pacing** | Fast hook (≤3s), beat-synced cuts, 9:16 native |
| **do_not_copy** | TikTok note, Douyin logo |

### Bilibili B站

| Field | Value |
|-------|-------|
| **aliases** | B站, bilibili, 哔哩哔哩, 小电视 |
| **visual_cue** | ACG pink/cyan, playful overlays, community/subtitle culture, danmaku energy |
| **palette** | Pink `#FB7299`, sky blue `#00A1D6`, white |
| **pacing** | Casual, meme-aware; longer holds OK for explainers |
| **do_not_copy** | 22/33 characters, TV logo |

### Meituan 美团

| Field | Value |
|-------|-------|
| **aliases** | 美团, Meituan |
| **visual_cue** | Sunny yellow, local-life everyday scenes, delivery/convenience metaphors |
| **palette** | Yellow `#FFC300`, charcoal, sage green bg |
| **pacing** | Practical, fast utility demo |
| **do_not_copy** | Meituan kangaroo exact pose |

---

## 全球品牌

### Apple

| Field | Value |
|-------|-------|
| **aliases** | Apple, 苹果, iPhone, Mac |
| **visual_cue** | Extreme minimalism, product hero on white/gray, slow Ken Burns, no clutter |
| **palette** | `#F5F5F7`, white, charcoal `#1D1D1F` |
| **pacing** | Slow, deliberate; 3–5s product holds |
| **do_not_copy** | Apple logo, product silhouette exact match |

### Spotify

| Field | Value |
|-------|-------|
| **aliases** | Spotify, 音乐, 播客 |
| **visual_cue** | Bold color blocks, rhythm/wave metaphors, dark bg + green accent |
| **palette** | Green `#1DB954`, black, white type |
| **pacing** | Beat-synced, audio-visual lock |
| **do_not_copy** | Spotify circle logo |

### Nike

| Field | Value |
|-------|-------|
| **aliases** | Nike, 耐克, 运动 |
| **visual_cue** | High contrast, athletic motion, bold typography, kinetic energy |
| **palette** | Black, white, single accent (red or volt) |
| **pacing** | Fast, impactful; slam cuts on key words |
| **do_not_copy** | Swoosh logo |

---

## Quick reference

| Prompt snippet | Loads preset |
|----------------|--------------|
| "腾讯风格短视频" | Tencent |
| "阿里电商感" | Alibaba |
| "抖音感竖版" | ByteDance |
| "B站二次元" | Bilibili |
| "Apple 产品发布风" | Apple |
| "Spotify 节奏感" | Spotify |
| "Nike 运动广告" | Nike |

Agent: read this file when user names a brand; combine with `references/recipes.md` for local render path.
