# Free stack vs paid (do not cross)

## Allowed (default)

| Tool | Role | Notes |
|---|---|---|
| ffmpeg / ffprobe | Cut, concat, Ken Burns, grade, xfade, export | Required |
| Pillow | Pads, sketch, chromakey, hand overlay, frames | Required |
| story-to-handdrawn-video (Remotion) | Diary pages / page-flip | Set `STORY_VIDEO_PROJECT` |
| Host GenerateImage | Stills, process-hand frames, covers | Only if host provides it free in-session |
| Pexels | Stock B-roll / stills | Free license; download then local import |
| female-outfit-director | Prompt + script only | User renders elsewhere if they want |
| gbro-cover-design | Cover prompts only | No API call from skill |
| BaoCut CLI | Local ASR / talking-head cleanup | Needs BaoCut Mac app |
| Manim (video-use subskill) | Chart / math slots | Local render |
| ChatCut / Pireel MCP | Edit with **already-local or free library** assets | Do not trigger paid `submit_*` generation |

## Forbidden unless user explicitly insists + accepts cost

| Tool / key | Why blocked here |
|---|---|
| `GEMINI_API_KEY` (gbro video stage) | Paid / quota cloud video |
| `ATLASCLOUD_API_KEY` (vox-director) | Paid cloud |
| Seedance / Kling / Runway / Luma I2V | Per-clip billing |
| ElevenLabs Scribe (video-use default ASR) | API billing |
| ChatCut/Pireel `submit_video` / paid MG | Credits |
| Any “just add the key and continue” silent upgrade | Violates this skill |

## If a sibling skill demands a key

1. Stop before the paid stage.
2. Tell the user what free substitute you will run instead.
3. Deliver Gate1 docs / prompts / local ffmpeg cut — never hang waiting for a key unless the user says they will add one.

## Minimal machine check

```bash
ffmpeg -version | head -1
ffprobe -version | head -1
python3 -c "from PIL import Image; print('pil ok')"
test -d "${STORY_VIDEO_PROJECT:-${CUTMAX_ROOT:-.}/tools/story-to-handdrawn-video}" && echo handdrawn_ok
```
