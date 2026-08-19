# Recipes (free / local)

## Recipe A — Photo → drawing hand → artwork (CLEAR)

Use when user wants vitality / 「正在画」 without paid I2V.

### Inputs per outfit

1. `photo.png` — real photo, padded to canvas
2. `draw.png` — process still with masculine hands (optional but preferred for hold beat)
3. `art.png` — finished handdrawn page

### Timing (per cycle, ~11–12s)

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
- Sketch = strong B&W / edge-enhanced from art; must differ from color at a glance
- No per-frame pulse zoom; no full-height brush glow bars (they flicker)
- Hand sprite tip must be calibrated; tip rides the reveal edge

### Script

```bash
python3 ~/.codex/skills/local-video-studio/scripts/photo_draw_reveal.py \
  --work-dir outputs/my-draw \
  --cycle outputs/my-draw/photo.png outputs/my-draw/draw.png outputs/my-draw/art.png \
  --out outputs/my-draw/FINAL.mp4
```

Proven output: `outputs/skill-trials-2026-08-06/handdrawn/conan-photo-draw-hand-motion-CLEAR.mp4`

---

## Recipe B — Style variants from one photo

Use when user wants fashion-clean / neo-noir / editorial looks without cloud models.

Per variant: pad to canvas → optional grade (`eq`/`curves`/`colorbalance`) → Ken Burns 3–5s → concat.

Keep titles as burned-in text only if user asks; default silent.

---

## Recipe C — Handdrawn diary (Remotion)

```bash
export STORY_VIDEO_PROJECT="${CUTMAX_ROOT:-.}/tools/story-to-handdrawn-video"
python3 "$STORY_VIDEO_PROJECT/scripts/run_story_video.py" \
  --images ... --title "..." --mode full --transition cut|page-flip \
  --page-duration 4.6 --layout full
```

Never use `layout=composite` for full-bleed portraits (waist-cut risk).

---

## Recipe D — Stock B-roll under A-roll

1. List beats from picture/script
2. Search Pexels; download to `outputs/broll-<slug>/`
3. Write `MANIFEST.md` (clip → beat → in/out)
4. Insert with ffmpeg overlay or editor MCP; mute B-roll; grade to match
5. Face-safe zones: top band / lower third / full cutaway

---

## Recipe E — Prompt-only (no render)

- Outfit carousel: `female-outfit-director`
- Cover: `gbro-cover-design`
- Collage / Vox **planning only**: write Gate1 markdown; stop before paid image/video APIs

---

## Recipe F — Talking-head cleanup (if BaoCut installed)

Use `baocut` skill: transcribe → polish → reversible filler/pause cuts → export.  
If BaoCut missing, ask for SRT or do picture-only edit.

---

## Verify checklist

Before saying done:

- [ ] `ffprobe` duration / size match plan
- [ ] Frames at ≥3 timestamps show **different stages**
- [ ] No flicker on still holds
- [ ] Faces not cropped (prefer `contain` + pad over aggressive `cover`)
- [ ] Output path reported; MANIFEST updated
