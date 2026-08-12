# Dr Chan workflow and QA

## 1. Plan the reel or series

For a long live recording:

1. Wait until transcription is complete before locking topic, specialty, reel count, hooks, or medical claims.
2. Read the full transcript and identify complete educational arcs: question/hook, explanation, practical implication, and safe conclusion.
3. Propose a reel map before batch editing. Keep each Facebook reel under two minutes and give every reel one promise only.
4. When the brief asks to condense the live into six reels, show the six-reel plan first and obtain approval before expanding beyond the first sample.
5. Use high-retention principles—strong first seconds, concrete stakes, visual proof, pattern changes, and a clear payoff—without sensationalising medical information.

### Stage map for Dr Chan edits

Keep the workflow explicitly separated into these phases:

1. `planning`: topic selection, reel map, hook, scope, and medical promise.
2. `rough-cut`: A-roll selection, transcript correction, pause trimming, and clause-safe structure.
3. `caption-lock`: approved-script comparison, Cantonese correction, subtitle segmentation, and disclaimer/CTA wording.
4. `packaging`: B-roll, face bubbles, chapter cards, mechanism/stat MG, Dr Chan attribution, music, and SFX.
5. `final-qa`: screenshot proof, continuity, safe-area checks, caption rerun, and delivery checkpoint.

Do not report a later phase complete when an earlier phase is still changing. If the user is only revising packaging, do not silently reopen rough-cut scope.

## 2. Protect versions and scope

- Duplicate the current timeline before broad reframing, B-roll replacement, transcript reconstruction, or audio replacement.
- Re-read the active timeline immediately before editing; the user may have made manual cuts.
- Write down the exact scope: target timeline, item/card/time range, expected item count, and properties allowed to change.
- Use a validate/dry-run operation before deleting or moving a batch.
- Do not ripple unless the user explicitly wants later content shifted or a gap closed.

### Local caption timing/editability

When only one caption needs independent timing or manual editing:

1. Read the viewer-facing caption pages and word keys.
2. Create or keep exactly one editable manual text/MG item for the named card.
3. Shift that item by the requested frames; at 30 fps, `0.1 s = 3 frames`.
4. Hide only the automatic-caption words under that card to prevent duplication.
5. Keep the automatic captions enabled for all later cards.
6. Verify the affected start, middle, end, the next automatic card, and a later control frame.

Never solve a one-card request by converting the whole video to manual text layers.

## 3. Transcript and A-roll

1. Preserve the original transcript evidence and create a corrected layer.
2. When Yiboh supplies an approved script, preserve its exact version and use it as the lexical and semantic source of truth for captions. Use the recorded audio as timing and spoken-evidence truth.
3. Correct Cantonese ASR, names, medical terms, numbers, and units before semantic editing.
4. Treat source-transcript wording as the durable caption layer. If Cantonese ASR is stored in Simplified Chinese, correct the source transcript to approved Hong Kong Traditional Chinese before relying on display overrides. Display-only Traditional Chinese can be replaced by Simplified source text whenever a trim, Script apply, clip split, or repagination creates new caption pages.
5. After every trim, Script apply, clip split, pause removal, or source-window change, refresh the viewer-facing captions and scan the affected point through the end for Simplified-character regression. Do not assume earlier display overrides still cover newly created item/word keys.
6. Compare the corrected transcript against the approved script before building final captions. If the script and audio materially disagree, preserve both readings and ask instead of silently changing medical meaning.
7. Let Dr Chan finish complete medical terms and clauses before cutting. Never cut into a key term such as `荷爾蒙`.
8. Remove failed takes, clear misstatements, and unnecessary pauses while preserving natural breathing and speaker personality.
9. When replacing a line with a new recording, align the new audio after the preceding sentence is complete, extend the visual if required, close any resulting gap, and update the matching subtitle only.
10. Review all subtitles after the replacement point; timing changes often expose downstream ASR or segmentation errors.

## 4. Captions

- Correct Hong Kong Cantonese rather than mechanically accepting homophones. Example: use `咁` when Dr Chan says the Cantonese connector; do not leave an ASR error such as `敢`.
- Preserve intended medical wording. Do not simplify a term into a different claim.
- Keep the project's approved font, size, outline, emphasis, two-line limit, and caption band.
- Check for doubled lines after adding manual text, face bubbles, B-roll, or source-audio replacements.
- When a manual text layer visually sits higher despite sharing the automatic-caption `top`, compare rendered glyph baselines and move only that layer's vertical position.

### Required approved-script comparison

Complete this pass before caption styling or review handoff:

1. Read every viewer-facing caption card in timeline order and align it to the matching approved-script phrase.
2. Compare character by character after normalising only spacing and nonessential punctuation. Keep every different Chinese character visible as a mismatch.
3. For each mismatch, listen to the corresponding audio and classify it as an ASR homophone, Hong Kong orthography issue, medical-term error, name/acronym error, number/unit/negation error, punctuation/segmentation issue, or genuine script-versus-speech deviation.
4. Re-read the whole Cantonese phrase for grammar and meaning. Do not approve a character merely because it has the same sound.
5. Apply semantic checks explicitly:
   - Use `係` for the Cantonese copula; retain `系` only when the intended word genuinely means system, series, department, or another valid `系` usage.
   - Use `質` in `蛋白質` and other quality/substance terms; do not accept the homophone `汁`.
   - Use `咁` for the intended Cantonese connector or manner word; do not accept `敢`.
6. If the approved script and audio disagree in a way that changes a medical claim, condition, cause, certainty, number, unit, or negation, stop and flag the exact phrase for Yiboh instead of silently selecting one.
7. Lock wording first. Then perform line-break, punctuation, caption-band, duration, and karaoke-timing QC without changing the approved copy.
8. After an A-roll cut, replacement recording, transcript fix, or manual-caption insertion, rerun this comparison from the affected phrase through the end of the reel.
9. Record the approved-script version used, total caption cards checked, coverage percentage, mismatches corrected, and unresolved script/audio conflicts. Coverage must be `100%` before reporting subtitle completion.

### Caption-QC incident protocol

Use this whenever Yiboh finds a subtitle error after Codex has said the subtitles or QC are complete:

1. Withdraw the earlier caption-QC claim. Do not describe the problem as an isolated typo until the whole reel has been rechecked.
2. Read the complete viewer-facing caption text from the first card to the last card. A screenshot or a few rendered frames is visual evidence only, not copy coverage.
3. Build a card ledger and classify every card as `match`, `corrected ASR/orthography`, `acceptable spoken variation`, or `unresolved script/audio conflict`.
4. Compare the full ledger with the approved script, then listen to every mismatch in its complete phrase. Preserve actual spoken variants that do not change meaning; escalate any medical-meaning conflict.
5. Run a context-aware red-flag scan across the complete reel for `系／係`, `汁／質`, `食肉／食慾`, `信息／訊息`, `面／麵`, `噉／咁`, `敢／咁`, `余／餘`, names, acronyms, numbers, units, and negation.
6. Determine whether each mismatch exists in source transcript truth or only in the current display layer. Repair source transcript truth for durable orthography/medical-term errors; use display overrides only for intentional card-specific presentation. Preview source-word indices and preserve punctuation when the renderer stores a character and its punctuation in one token.
7. State the exact number of confirmed word or character edits before applying them. Change only those display words unless transcript truth itself must be repaired.
8. Re-read the full caption sequence after the batch. The corrected count must match the write result, and every red-flag occurrence must be resolved or explicitly justified.
9. Render the first affected frame, representative corrected frames across the reel, the last affected frame, and the next unaffected card. This visual pass checks line breaks, clipping, duplication, punctuation visibility, and karaoke timing only.
10. Do not accept punctuation from the data read alone. If required punctuation is stored but absent in the rendered karaoke frame, mark the card failed and use a manual text/MG fallback for that card only.
11. Treat every override test as provisional. Render both the edited moment and the next card; keep the change only when punctuation, pagination, wrapping, timing, and karaoke all pass. Revert a failed test immediately.
12. Report caption completion only with the approved-script version, total cards, `100%` card coverage, corrected mismatch count, acceptable spoken-variation count, and unresolved conflicts. If any field is missing, label the result `local correction checked`, not `full subtitle QC complete`.

## 5. B-roll, face bubbles, and MG

1. Inspect the target A-roll frame and the candidate B-roll frame before placement.
2. Protect face, gestures, captions, name tag, disclaimer, and platform UI.
3. Match stock literally to the spoken example whenever practical, then inspect the surrounding shots for subject, angle, colour, and motion variety. Never place identical or near-identical stock clips beside each other.
4. Treat each clean stock shot, including opening/title stock, as an automatic talking-head opportunity. Add a source-synchronised live Dr Chan circle or rounded rectangle when the background is simple, has no competing face/head, and offers safe negative space.
5. If a clean stock shot remains stock-only, record the specific reason: human-led or visually complex footage, or a medical/product detail that genuinely needs the full frame.
6. Prefer live face bubbles over full-body seated shots where it improves Dr Chan's comfort and viewer connection. Aim for about 3–5 live talking-head appearances in a finished reel and alternate circle and rounded-rectangle treatments.
7. Mute the overlay copy, keep it synchronised to the active spoken source, and keep the face centred. Use a real circle mask for circular bubbles and enlarge sparse layouts deliberately.
8. Keep a deliberate edge margin and protect MG information, products, logos, UI, and every person’s face/head. Move the talking-head occurrence instead of forcing it over busy or human-led stock.
9. Convert wide mechanism cards into transparent-overlay vertical compositions; do not merely squeeze a horizontal design or add an unexplained outer box, baked background, or decorative side line.
10. Use recognisable icons, images, or object cut-outs for concrete foods, drinks, organs, and objects when they improve comprehension.
11. Remove stock fades that reveal the underlying A-roll between clips.
12. Add SFX only after picture and MG timing are locked.

## 6. Audio and colour

1. Match replacement audio tone and loudness to Dr Chan's main track.
2. Set speech as the anchor and music as the follower/ducked bed when the editor supports it.
3. Check voice clarity, peaks, music balance, and every SFX in context—not solo.
4. Match exposure, white balance, skin tone, and suit colour across A-roll and replacement shots.

## 7. Opening, captions, and pacing

1. Make the first frame immediately readable as a Facebook thumbnail. Keep the series label and main title visually joined.
2. On A-roll, place the main title around the tie/chest region when it clears the face and caption band. On clean opening stock, place Dr Chan in unused upper or side negative space without weakening the title.
3. Do not place routine dialogue subtitles in the first `0.1 s`.
4. Keep captions in the approved lower-chest/lower-third band with white primary text, dark outline/shadow, and fluorescent-yellow emphasis only on the word or short phrase currently spoken.
5. Keep captions to one or two lines and break at complete Cantonese phrases. Never split a fixed medical term, number plus unit, negation, or verb-object phrase.
6. Scan the full reel for uninterrupted pure-A-roll spans. At or before roughly 15 seconds, add relevant stock, stock plus a live Dr Chan window, or a context-specific vertical MG.
7. Do not count subtitle highlighting, a routine punch-in, minor reframing, or colour correction as a pacing reset.

## 8. Screenshot before review

After every completed visible modification:

1. Capture fresh screenshots from the actual composed timeline before asking Yiboh to watch, review, or approve the edit.
2. Inspect the first affected frame, a settled representative frame, the last affected frame, and the first unaffected control frame when relevant. Include source-cut boundaries for overlays or stock replacements.
3. Complete the first-round QC yourself: check scale, position, crop, face centring, safe margins, title/subtitle clearance, MG collisions, and stock-subject protection.
4. Fix every visible defect, then capture fresh proof and repeat the QC until the composed result passes. Yiboh must not be the first-pass QC reviewer.
5. Attach at least one representative composed-timeline screenshot to the review handoff.

If screenshot capture is blocked, state the blocker and do not claim visual completion.

## 9. Completion gate

Do not report completion until all applicable checks pass:

- Correct active timeline and version.
- No unintended item, track, caption, or asset changes.
- No black gaps, audio gaps, flash frames, stock-transition leaks, or clipped words.
- Dr Chan finishes every intended clause before a replacement or cut.
- The first frame has a joined, readable title and no routine dialogue subtitle in the first `0.1 s`.
- Every caption card has been compared in sequence against the approved script with `100%` recorded coverage; all character mismatches were resolved by audio and semantic review, or the exact script/audio conflict was escalated.
- Any prior caption-QC claim was invalidated and fully rerun if Yiboh subsequently found an error; a local screenshot check was never substituted for full copy coverage.
- Captions are correct Hong Kong Traditional Chinese, including context-correct `係／系`, `質／汁`, and `咁／敢`; there are no duplicates, missing cards, or timing drift, and karaoke emphasis follows only the current spoken word or short phrase.
- Manual and automatic caption baselines match visually.
- B-roll and MG do not cover face, essential gestures, subtitle band, disclaimer, CTA, products, logos, UI, stock subjects, or another person's face/head.
- Every clean stock-only shot has been scanned; Dr Chan was added where safe or a specific full-screen reason was recorded.
- Talking-head overlays use moving, source-synchronised footage, stay silent as overlays, keep the face centred, and appear in a deliberate mix of circle and rounded-rectangle treatments.
- Circular face bubbles are truly circular with no square corners visible.
- No identical or near-identical stock clips sit beside each other; literal examples and surrounding shot variety have been checked.
- Vertical MG remains readable at phone size, uses the approved transparent-overlay treatment, does not resemble a squeezed horizontal layout, and has no unexplained outer box, baked background, or decorative side line.
- No uninterrupted pure-A-roll span runs roughly 15 seconds without a meaningful relevant intervention.
- Name tag, medical disclaimer, and CTA use approved copy and safe placement.
- Dr Chan attribution is present unless the user explicitly approved an unsigned variant for that specific deliverable.
- Voice remains clearly dominant; music and SFX support rather than compete.
- The first affected frame, settled frame, source-cut boundaries, last affected frame, first unaffected frame, opening, middle, replacement-audio area, and ending have composed-frame proof where applicable.
- First-pass visual QC is complete, visible defects were fixed, and the review handoff includes at least one representative screenshot from the actual composed timeline.

Report the exact changed items/properties, the preserved scope, the frames or sections checked, and the attached representative screenshot. Stop at an editable review checkpoint unless export was explicitly requested.
