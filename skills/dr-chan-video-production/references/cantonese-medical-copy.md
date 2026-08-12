# Dr Chan Cantonese medical copy

## Language standard

- Use natural Hong Kong Cantonese and Traditional Chinese.
- Keep Dr Chan's credible, energetic speaking personality; do not rewrite him into formal written Mandarin.
- Correct ASR homophones from the audio and context, not from guesswork. Common connectors may include `咁`, `但係`, `所以`, `其實`, and `即係`; retain them when they carry logic or personality.
- Verify names, medical terminology, acronyms, numbers, percentages, units, and negation against the recording and approved references.

## Approved-script source of truth

- When Yiboh supplies an approved script, use it as the lexical and semantic source of truth for captions; use the recording to verify what was spoken and to determine timing.
- Compare the full reel card by card and character by character. Normalise only spacing and nonessential punctuation; never hide a character mismatch through normalisation.
- Resolve homophones through Cantonese grammar and sentence meaning, not sound alone. In particular:
  - Use `係` for the Cantonese copula; use `系` only when the intended word genuinely means system, series, department, or another valid `系` usage.
  - Use `質` in `蛋白質` and other substance/quality terms; do not accept `汁`.
  - Use `咁` for the intended Cantonese connector or manner word; do not accept `敢`.
  - Use `食慾` for appetite; reject ASR substitutions such as `食肉` when the phrase means appetite control.
  - Prefer Hong Kong `訊息` for signals or messages in this series; reject contextually wrong `信息`.
  - Use `麵` for noodles or bread-related `麵包`, and `面` only for a genuine face, surface, side, or other intended `面` meaning.
  - Use Traditional `餘` in `其餘`; do not leave Simplified `余`.
- If the approved script and recorded speech conflict on medical meaning, certainty, cause/effect, condition, number, unit, or negation, flag the exact phrase instead of silently rewriting it.
- Lock the approved wording before changing segmentation, styling, or karaoke timing. Rerun the comparison after any A-roll cut, replacement audio, transcript correction, or manual-caption insertion.

## Medical accuracy

- Separate transcript correction from editorial shortening and from caption layout.
- Visible titles may condense the spoken idea but must preserve conditions, uncertainty, cause/effect, and scope.
- Never turn `可能`, `較常見`, `有機會`, or a population statistic into certainty about an individual.
- Do not add treatment, medication, diagnosis, or prevention instructions unless Dr Chan states them and the current brief authorises the copy.
- Keep the disclaimer visible when discussing symptoms, medication, treatment changes, diagnosis, or health risk.

## Caption writing

- Use no more than two lines per card.
- Break at phrase boundaries and breaths. Keep names, acronyms, numbers plus units, negation, fixed medical terms, and verb-object phrases together.
- Use consistent punctuation across the reel. Social captions may omit nonessential final punctuation, but medical warnings and disclaimers should remain fully punctuated.
- Required internal punctuation such as `、` must be confirmed in the rendered output. Karaoke engines may retain it in caption data but suppress it visually; when that happens, use a card-specific manual text/MG fallback instead of claiming the caption passed.
- Highlight only the term carrying the current educational point; excessive yellow highlighting weakens hierarchy.

## Approved identity and closing copy

- Name: `陳譽`
- English name: `Dr Delex Chan`
- Disclaimer:
  - `⚠ 醫療資訊僅供參考。`
  - `如有不適，請諮詢專業醫生。請勿自行停藥或更改療程。`
- CTA:
  - `覺得有用？儲存＋分享`
  - `追蹤專頁｜唔好錯過下次 Live`

## Review checklist

- Record the approved-script version, total caption cards, `100%` comparison coverage, corrected mismatch count, and unresolved script/audio conflicts.
- Compare every viewer-facing caption card against the approved script; do not substitute spot checks.
- Listen to every corrected medical term.
- Check all Cantonese homophones and code-switching through full-phrase meaning, including context-correct `係／系`, `質／汁`, and `咁／敢`.
- Run the full-reel context-aware red-flag scan for `食肉／食慾`, `信息／訊息`, `面／麵`, `噉／咁`, and `余／餘`; do not rely on visual spot checks.
- If Yiboh finds an error after a QC claim, invalidate that claim and rerun the complete card-by-card comparison before reporting completion again.
- Check numbers and percentages against the source.
- Confirm no subtitle change alters medical meaning.
- Re-read captions after any audio replacement, cut, or timing change.
