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

Moved to **opt-in** (not free default):

- `opt-in/prompt-for-paid-models/` — Seedance family prompt packs, `vibe-creating-prompt`, `fpv-immersive-video-prompting`
- Enable with `./scripts/link-opt-in-prompts.sh`

Still fully excluded (API / credit callers):

- `seedance2` (即梦 API 工作台，会走付费接口)

## Other

- `watch` (URL pipeline may pull third-party transcripts; not a cut pack core)
- Backup / `.bak` skill trees
