# cutmax

Local-first **video editing + media skills** pack for agent runtimes (Codex / Claude / Cursor).

**Hard rule:** the default `skills/` pack runs **without paid cloud video APIs**. Prompt packs for Seedance/Kling/etc. live under `opt-in/` and are **not** linked unless you opt in.

Start here: [`skills/local-video-studio/SKILL.md`](skills/local-video-studio/SKILL.md)

## Install

```bash
git clone https://github.com/WillNam/cutmax.git
cd cutmax

# Free/local skills (recommended)
./scripts/link-skills.sh ~/.codex/skills

# Optional: prompt packs for paid video products (Seedance/Kling/…)
./scripts/link-opt-in-prompts.sh ~/.codex/skills
```

For the Remotion handdrawn renderer:

```bash
cd tools/story-to-handdrawn-video
npm install
export STORY_VIDEO_PROJECT="$(pwd)"
```

Machine basics: `ffmpeg`, `ffprobe`, Python 3 + Pillow.

## What's inside

| Path | Role |
|---|---|
| `skills/` | Agent skills (free / local / prompt-only) |
| `opt-in/prompt-for-paid-models/` | **Opt-in** prompt packs for Seedance/Kling/etc. (not auto-linked) |
| `tools/story-to-handdrawn-video/` | Remotion project used by handdrawn skill |
| `rules/stock-broll-workflow.md` | Pexels B-roll intake rule |
| `CATALOG.md` | Full include list |
| `EXCLUDED.md` | Paid / third-party API skills deliberately left out |

## Quick router

| You want… | Use |
|---|---|
| Local still→video / draw process / free cut hub | `local-video-studio` |
| Hand-drawn diary / page flip | `story-to-handdrawn-video` + `tools/` |
| Talking-head cleanup + captions (Mac app) | `baocut` |
| Product shot Remotion template | `video-shotcraft` |
| Outfit carousel prompts (no cloud render) | `female-outfit-director` |
| Cover prompts | `gbro-cover-design` |
| Short-video script / storyboard | `self-media-short-video`, `script-to-shootable-storyboard` |
| Charts / math slots | `manim-video` |
| Stock B-roll | `rules/stock-broll-workflow.md` |
| Seedance/Kling **prompts** (opt-in) | `opt-in/prompt-for-paid-models/` |

## License

Each skill keeps its original license when present. Aggregator docs (README / CATALOG / EXCLUDED) are MIT.
