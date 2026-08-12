# Catalog — included in cutmax

All entries are **free/local**, **prompt-only**, or **local-app** (no mandatory paid cloud video API).

## Hub

| Skill | Type | Notes |
|---|---|---|
| `local-video-studio` | hub + scripts | Routes free recipes; `photo_draw_reveal.py` |

## Local render / edit

| Skill | Type | Notes |
|---|---|---|
| `story-to-handdrawn-video` | Remotion wrapper | Needs `tools/story-to-handdrawn-video` + `npm install` |
| `video-shotcraft` | Remotion product shots | Local template; no Seedance |
| `baocut` | Local Mac app CLI | Transcribe / cleanup / export; CLI does not call paid LLM APIs |
| `manim-video` | Local Manim | Extracted free subskill (no ElevenLabs path) |

## Prompt / script (you render elsewhere if you want)

| Skill | Type | Notes |
|---|---|---|
| `female-outfit-director` | prompts + timeline | No cloud render |
| `gbro-cover-design` | cover prompts | No API call from skill |
| `script-to-shootable-storyboard` | shootable boards | Prompt/plan only in this pack |
| `self-media-short-video` | short-video scripts | Cuts only when user supplies footage |
| `xhs-visual-director-skill` | Xiaohongshu visual plan | Stills / carousel direction |
| `guizang-social-card-skill` | social cards | Image / Live Photo cards |
| `learning-map-infographic` | infographic | Dense vertical learning maps |

## Production / identity / publish helpers

| Skill | Type | Notes |
|---|---|---|
| `dr-chan-video-production` | production rules | Medical video QC rules |
| `conan-digital-human` | avatar library ops | Local identity workflow |
| `video-publisher` | draft upload helper | Ego Lite drafts; not cloud video gen |

## Content workflow (pre-cut)

| Skill | Type |
|---|---|
| `self-media-content-workflow` | router |
| `self-media-content-brief` | brief |
| `self-media-content-delivery` | delivery pack |
| `self-media-platform-copywriting` | platform copy |

## Rules

| File | Notes |
|---|---|
| `rules/stock-broll-workflow.md` | Plan → Pexels → MANIFEST → cut |

## Tools

| Path | Notes |
|---|---|
| `tools/story-to-handdrawn-video/` | Remotion sources + fonts (no `node_modules`, no generated plates) |

## Opt-in (paid-model prompts only)

Not linked by `link-skills.sh`. See `opt-in/prompt-for-paid-models/README.md`.

| Path | Notes |
|---|---|
| `opt-in/prompt-for-paid-models/` | Seedance / Kling / Runway / Veo / Sora **prompt** skills; no API calls from cutmax |
