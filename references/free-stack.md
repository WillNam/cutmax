# Local foundation + official platforms

## Local (foundation)

| Tool | Role | Notes |
|---|---|---|
| ffmpeg / ffprobe | Cut, concat, Ken Burns, grade, xfade, export | Required |
| Pillow | Pads, sketch, chromakey, hand overlay, frames | Required |
| story-to-handdrawn-video (Remotion) | Diary pages / page-flip | Set `STORY_VIDEO_PROJECT` |
| Host GenerateImage | Stills, process-hand frames, covers | Only if host provides it free |
| Pexels | Stock B-roll / stills | Free license; download then local import |
| female-outfit-director | Prompt + script only | User renders elsewhere |
| gbro-cover-design | Cover prompts only | No API call from skill |
| BaoCut CLI | Local ASR / talking-head cleanup | Needs BaoCut Mac app |
| Manim (manim-video) | Chart / math slots | Local render |
| ChatCut / Pireel MCP | Edit with **already-local or free library** assets | Do not trigger paid `submit_*` without confirm |

## Official platforms (confirm before spend)

| Tool / key | Why confirm first |
|---|---|
| `GEMINI_API_KEY` (gbro video stage) | Paid / quota cloud video |
| `ATLASCLOUD_API_KEY` (vox-director) | Paid cloud |
| Seedance / Kling / Runway / Luma I2V | Per-clip billing |
| ElevenLabs Scribe | API billing |
| ChatCut/Pireel `submit_video` / paid MG | Credits |

## If a platform needs login or credits

1. Stop before the paid stage.
2. Tell the user what free substitute you will run instead.
3. Deliver Gate1 docs / prompts / local ffmpeg cut — never hang waiting for a key unless the user says they will add one.

## Minimal machine check

```bash
ffmpeg -version | head -1
ffprobe -version | head -1
python3 -c "from PIL import Image; print('pil ok')"
test -d "${STORY_VIDEO_PROJECT:-./tools/story-to-handdrawn-video}" && echo handdrawn_ok
```
