# Excluded on purpose

These exist in local agent skill libraries but were **not** copied into cutmax because they require paid APIs, cloud video credits, or third-party billed ASR/I2V.

## Cloud video / I2V families

- `seedance`, `seedance2`, and all `seedance-*` variants
- `vox-director` (`ATLASCLOUD_API_KEY`)
- `gbro-collage-broll` video stage (`GEMINI_API_KEY`)
- `rachel-digital-human-production` (MiniMax / HeyGen)
- `longcat-video-avatar` (heavy model / non-free runtime assumptions)
- `classical-poem-silk-video` (Gemini / Docker paid path)
- `book-video`, `book-video-factory` (AI visuals / TTS cloud stages)

## Billed ASR / conversation editors tied to paid keys

- `video-use` (default ElevenLabs Scribe)
- `fivemedia-asr`, `yichen-asr`, `yichen-volc-asr`

## Credit / MCP generators

- `pireel` paid generation paths
- `qiaomu-cut-skill` vendor video-gen / TTS credit stack

## Prompt wrappers aimed at paid video models

Kept out of this pack to avoid “free skill → paid render” confusion:

- `vibe-creating-prompt` (Seedance / Sora / Kling / Veo / Runway)
- `fpv-immersive-video-prompting` (Seedance / Kling / Runway / Veo)
- `seedance-prompt-en` and related prompt packs

## Other

- `watch` (URL pipeline may pull third-party transcripts; not a cut pack core)
- Backup / `.bak` skill trees

If you explicitly want a **prompt-only** folder for paid models later, add it as an opt-in subdirectory — do not merge into the free default router.
