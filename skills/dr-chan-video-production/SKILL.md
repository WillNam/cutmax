---
name: dr-chan-video-production
description: Produce, revise, and quality-check Dr Chan medical videos using the approved 202607 R4-V2 production rules. Use whenever the client, speaker, project, or request mentions Dr Chan, Dr. Chan, 陳醫生, Dr Delex Chan, 陳譽, 202607 R4-V2, or asks to reuse the established Hong Kong Cantonese medical-reel style for series planning, talking-head editing, captions, B-roll, face bubbles, vertical Motion Graphics, medical disclaimers, audio finishing, Facebook reels, or delivery QA.
---

# Dr Chan Video Production

Use this skill as the Dr Chan client layer. Keep the project genuinely editable in the chosen editor and protect medical accuracy, Cantonese authenticity, and Dr Chan's preferred framing.

## Canonical source and installation

This skill ships inside cutmax at `skills/dr-chan-video-production/`.

Install via cutmax:

```bash
bash scripts/link-skills.sh ~/.codex/skills
```

## Load the production context

1. Load `yiboh-video-editor` and follow its required universal, Cantonese, client, transcription, and finishing references.
2. When editing in ChatCut, also load the relevant `chatcut:*` skills for current schemas and supported operations.
3. Always read [production-style.md](references/production-style.md).
4. Read [workflow-and-qa.md](references/workflow-and-qa.md) before planning, editing, revising, or delivering a Dr Chan video.
5. Read [cantonese-medical-copy.md](references/cantonese-medical-copy.md) whenever speech, captions, visible copy, name tags, disclaimers, or CTAs are involved.

## Resolve instructions in this order

1. The user's explicit instruction for the current video.
2. The active project/timeline, approved reference, or current design style.
3. This Dr Chan skill.
4. `yiboh-video-editor` universal defaults.
5. Fresh editorial judgment from the actual footage.

Treat one-off deviations as project-only unless the user explicitly says they are the new Dr Chan default. Do not overwrite a good current timeline merely to force a historical convention.

## Default creative brief

Use these defaults only when the current brief does not say otherwise:

- Audience: Hong Kong viewers.
- Purpose: medical education and trust-building.
- Tone: credible and energetic; clear rather than sensational.
- Primary format: Facebook vertical reel, 1080×1920, under two minutes.
- CTA: save and share; optionally follow the Facebook page for future live updates.
- Default on-screen attribution: add `陳譽` / `Dr Delex Chan` unless the current project already shows identity clearly in the opening.
- Speaker treatment: favour confident head-and-shoulders framing, close crops, selected face bubbles, and useful B-roll over long full-body seated shots.
- Visual identity: dark navy, white, fluorescent yellow, and restrained warm-orange accents; `Noto Sans HK` ExtraBold when the renderer can prove the requested face/weight.

Do not infer a diagnosis, treatment promise, or guaranteed health outcome from a concise social-video title.

## Distinguish production stages

Treat different edit phases as separate deliverables with different goals:

1. `topic-planning`
   - Split the long live into clear educational arcs.
   - Define one promise per reel, target duration, and the safe medical takeaway.
2. `rough-cut`
   - Lock A-roll structure, remove failed takes, tighten pauses, and preserve clause integrity.
   - Do not spend time on final B-roll, MG, SFX, or colour polish before the spoken structure works.
3. `copy-and-captions`
   - Correct Cantonese, medical terms, numbers, and units.
   - Apply approved script comparison and establish the final viewer-facing subtitle wording.
4. `visual-packaging`
   - Add Dr Chan attribution, B-roll, talking-head bubbles, MG, chapter cards, disclaimers, and CTA.
   - Keep all packaging subordinate to the spoken medical point.
5. `final-qa`
   - Recheck captions, identity, disclaimer, CTA, pacing, overlay collisions, safe margins, and screenshot proof.

When the user asks for a change, first identify which stage it belongs to and avoid accidentally reopening later-stage polish when the earlier stage is still unsettled.

## Execute safely

1. Identify the live project, timeline/version, fps, canvas, target reel, and requested scope.
2. Duplicate the timeline before structural or batch revisions. For a small reversible property change, read the live item first and change only that item.
3. Finish transcript meaning and A-roll structure before captions, B-roll, Motion Graphics, music, or SFX.
4. Preserve natural Hong Kong Cantonese and verify medical terminology before designing visible copy.
5. Build vertical-first compositions around Dr Chan's face, gestures, caption band, and platform safe areas.
6. Keep every requested layer editable. Use baked media only for an explicit handoff, alpha overlay, reference, or final master.
7. Re-read structural state and inspect composed frames before saying an edit is complete.

## Script-led subtitle QC gate

When Yiboh provides an approved script, treat it as the lexical and semantic source of truth for captions. Use the recorded audio as timing and spoken-evidence truth.

- Compare every subtitle card against the approved script in sequence; do not rely on raw ASR, spot checks, or screenshots alone.
- Diff characters after normalising only spacing and nonessential punctuation. Never normalise away different Chinese characters.
- Resolve every mismatch by listening to the matching audio and reading the full phrase for meaning. Check Hong Kong Cantonese usage, homophones, medical terms, names, acronyms, numbers, units, and negation.
- Treat errors such as `系／係`, `汁／質`, and `敢／咁` as mandatory semantic-review failures, not cosmetic typos. Use `係` for the Cantonese copula, while retaining `系` only when it genuinely means system, series, department, or another intended `系` word; use `質` in terms such as `蛋白質`.
- If the approved script and recorded speech differ in a way that changes medical meaning, do not silently choose one. Preserve the evidence, flag the exact phrase, and obtain direction.
- Lock caption wording before final line breaks, styling, and karaoke timing. After any A-roll cut, replacement audio, or caption correction, rerun the comparison for the affected point through the end.
- Keep copy QC and visual QC separate. Rendered screenshots prove layout, visibility, and karaoke behaviour; they do not prove that the wording matches the approved script. A copy pass must read the complete viewer-facing caption text in sequence.
- Treat punctuation as passed only when it is visible in a rendered frame, not merely present in caption data. If karaoke rendering suppresses required punctuation, fail visual QC and replace only that affected card with a manual text/MG layer after preserving the original timing and approved copy.
- Any experimental caption override must be rendered at the affected frame and the following card. Keep it only if text, punctuation, pagination, line breaks, and karaoke remain correct; otherwise revert it before continuing.
- Maintain a caption audit ledger with every card accounted for as `match`, `corrected ASR/orthography`, `acceptable spoken variation`, or `unresolved script/audio conflict`. Spot checks are never full-reel copy QC.
- Run a context-aware red-flag scan across the complete reel for known Cantonese and medical confusions, including `系／係`, `汁／質`, `食肉／食慾`, `信息／訊息`, `面／麵`, `噉／咁`, `敢／咁`, and `余／餘`. Do not replace blindly where the first form is contextually correct.
- If Yiboh finds any subtitle error after a QC claim, invalidate the previous caption-QC status. Fix the confirmed target, then rerun the approved-script comparison and red-flag scan from the first card through the last card before making another completion claim.
- Do not report captions complete without recording `100%` card coverage, the number of mismatches corrected, and any unresolved script/audio conflicts.

## Visual pacing gate

- Treat uninterrupted A-roll as a timed retention risk. At or before roughly 15 seconds of continuous A-roll, introduce an editorially relevant visual change: contextual stock B-roll, stock B-roll with a live Dr Chan talking-head window, or a context-specific Motion Graphic.
- Each finished reel should normally show Dr Chan as a synced live talking-head bubble or rounded-rectangle window about 3–5 times. Prefer alternating the two shapes instead of repeating one treatment throughout.
- Treat every clean stock shot as an automatic talking-head opportunity, including opening/title stock. If the background is simple, has no competing face/head, and has safe negative space, add a source-synchronised live Dr Chan window. Leave a clean stock shot full-screen only for a specific visual reason that is recorded during QA.
- Size talking-head windows for clear facial presence, not corner decoration. On clean stock, default to a horizontally centred upper-frame placement and make a rounded-rectangle window roughly 50–60% of the 1080-pixel canvas width unless the stock composition or MG requires another safe area. Do not shrink the window into a corner. Preserve the source aspect ratio, keep Dr Chan's face centred inside the mask, and move the window lower when needed for title-safe margins.
- Place these talking-head windows only over simple stock footage or in genuine negative space beside Motion Graphics. Keep a deliberate safe margin from every canvas edge, and never cover subtitles, MG information, products, logos, UI, or a person’s face/head in the stock shot. If the available background is visually busy or human-led, move the talking-head occurrence to a cleaner moment instead of forcing the overlay.
- Keep the overlay copy muted so programme audio never doubles. Use moving source video, keep the face comfortably centred, and make circular treatments genuinely circular with no visible square corners.
- If one spoken sentence or explanation runs longer than roughly 15 seconds, place the visual change at the nearest natural clause or sentence beat no later than that threshold; do not wait until the long explanation finishes.
- Reset the 15-second count only after a meaningful visual intervention. Automatic subtitles, karaoke highlighting, a routine punch-in, minor reframing, or colour adjustment alone do not count.
- Keep the intervention long and clear enough to register, and match it to the exact idea being spoken. Do not insert unrelated stock merely to satisfy the clock.
- During timeline QA, scan every reel for continuous pure-A-roll spans approaching or exceeding 15 seconds and fix them before delivery. Any deliberate exception requires the user's explicit approval for that specific moment.

## Screenshot before review

After every completed visible modification:

1. Capture fresh screenshot proof from the actual composed timeline before asking Yiboh to watch or approve it.
2. Inspect the first affected frame, a settled representative frame, the last affected frame, and the first unaffected control frame when relevant.
3. Complete the first-round visual QC yourself, checking scale, position, crop, face centring, safe margins, title/subtitle clearance, MG collisions, and stock-subject protection.
4. Fix every visible defect and capture fresh proof again before handoff. Never use Yiboh as the first-pass QC reviewer.
5. Include at least one representative composed-timeline screenshot in the review handoff.

If screenshot capture is blocked, state the blocker and do not claim visual completion.

## Non-negotiable correction rule

Apply the smallest possible edit.

- If the user names one line, one card, one word, one clip, one time range, or one graphic, modify only that target.
- Never convert all automatic captions to manual text merely because one caption needs independent timing or editability.
- For a single independently timed caption card, create or retain one manual text/MG item for that card only, hide only the matching automatic-caption words, and leave every later automatic caption intact.
- Before committing a batch, state the exact number of items affected. If the requested scope and planned scope differ, stop and ask.
- After a correction, verify the first affected frame, settled frame, last affected frame, first unaffected frame, and a later control frame.

## Deliver the review checkpoint

Report only what changed, what remained untouched, what was visually verified, and which representative screenshot is attached. Do not export unless the user asks for export or final delivery.
