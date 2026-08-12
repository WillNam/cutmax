# cutmax

Local-first **video editing + media skills** pack for agent runtimes (Codex / Claude / Cursor).

**Hard rule:** this repo only ships skills that can run **without paid cloud video APIs** (no Seedance / Kling / Runway / Gemini video / Atlas Vox / ElevenLabs billing paths, no credit `submit_video`).

Start here: [`skills/local-video-studio/SKILL.md`](skills/local-video-studio/SKILL.md)

## Install

```bash
git clone https://github.com/WillNam/cutmax.git
cd cutmax

# Point your agent skills dir at this pack (example: Codex)
ln -sfn "$(pwd)/skills" ~/.codex/skills-cutmax
# Or copy / symlink individual skill folders into ~/.codex/skills/
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

## License

Each skill keeps its original license when present. Aggregator docs (README / CATALOG / EXCLUDED) are MIT.
