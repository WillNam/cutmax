# Recipes (local foundation)

## Recipe A — Photo → drawing hand → artwork (CLEAR)

Use when user wants vitality / 「正在画」 without paid I2V.

### Inputs per cycle

1. `photo.png` — real photo, padded to canvas
2. `draw.png` — process still with hands (optional but preferred)
3. `art.png` — finished handdrawn page

### Timing (~11–12s per cycle)

| Beat | Sec | Visual |
|---|---|---|
| Photo hold + mild Ken Burns | 2.2–2.6 | Real photo |
| Fade → process still | 0.3 | Hands on desk |
| Process hold | 0.5 | Static |
| Fade → **true blank page** | 0.25 | Near-white paper only |
| Pencil hand + L→R sketch reveal | 3.0–3.4 | Tip on wipe edge + stroke bob |
| Brush hand + L→R color reveal | 2.6–3.0 | Tip on wipe edge |
| Art hold + mild Ken Burns | 2.0 | Finished page |

### Anti-「一张图」rules

- Blank page = `#F8F6F2` (or similar), **not** a washed copy of `art.png`
- Sketch = strong B&W / edge-enhanced; must differ from color at a glance
- No per-frame pulse zoom; no full-height brush glow bars
- Hand sprite tip rides the reveal edge

### Script

```bash
python3 skills/local-video-studio/scripts/photo_draw_reveal.py \
  --work-dir outputs/my-draw \
  --cycle outputs/my-draw/photo.png outputs/my-draw/draw.png outputs/my-draw/art.png \
  --out outputs/my-draw/FINAL.mp4
```

---

## Recipe B — Style variants from one photo

Per variant: pad → grade (`eq`/`curves`/`colorbalance`) → Ken Burns 3–5s → concat. Default silent.

---

## Recipe C — Handdrawn diary (Remotion)

```bash
export STORY_VIDEO_PROJECT="$(pwd)/tools/story-to-handdrawn-video"
python3 "$STORY_VIDEO_PROJECT/scripts/run_story_video.py" \
  --images ... --title "..." --mode full --transition cut|page-flip \
  --page-duration 4.6 --layout full
```

Never use `layout=composite` for full-bleed portraits (waist-cut risk).

---

## Recipe D — Stock B-roll under A-roll

1. List beats from picture/script
2. Search [Pexels Videos](https://www.pexels.com/videos/); download to `outputs/broll-<slug>/`
3. Write `MANIFEST.md` (clip → beat → in/out)
4. Insert with ffmpeg overlay; mute B-roll; grade to match
5. Face-safe zones: top band / lower third / full cutaway

---

## Recipe E — Prompt-only (no render)

- Outfit carousel: `female-outfit-director`
- Cover: `gbro-cover-design`
- Collage / Vox planning: Gate1 markdown only; stop before paid APIs

---

## Recipe F — Talking-head cleanup (BaoCut)

Use `baocut` skill: transcribe → polish → filler/pause cuts → export.
If BaoCut missing, ask for SRT or do picture-only edit.

---

## Verify checklist

Before saying done:

- [ ] `ffprobe` duration / size match plan
- [ ] Frames at ≥3 timestamps show **different stages**
- [ ] No flicker on still holds
- [ ] Faces not cropped (prefer `contain` + pad)
- [ ] Output path reported; MANIFEST updated
