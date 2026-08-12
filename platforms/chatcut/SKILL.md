---
name: chatcut
description: >
  Use when the user wants to edit video in ChatCut — import media, cut talking-head footage,
  captions, B-roll, motion graphics, timeline proof, or open the live ChatCut editor via MCP.
  Also for Chinese requests such as ChatCut剪辑、多轨时间线、口播粗剪、加字幕、加B-roll、MG动效.
---

# ChatCut

ChatCut is a multi-track NLE. In Cursor / compatible hosts, drive it through the **ChatCut MCP** (`user-chatcut`). Official product surface — embraced by cutmax to ship stronger edits than local ffmpeg alone.

## Philosophy in cutmax

Local tools are the foundation. **ChatCut is a first-class platform** when you need a real timeline, captions, overlays, and live preview. Prefer it for talking-head polish and layered edits; fall back to ffmpeg recipes when offline or when the job is a simple silent picture track.

## Before spending credits

- Reuse library / stock / builtins before paid `submit_*` generation.
- Confirm model, count, duration, and aspect when a paid generation is needed.
- Never silently replace the user’s recorded speech with TTS.

## Essentials

1. **Show the editor early** — create/target a project, present the editor URL, use `show_preview` when available.
2. **Discover before mutate** — `read_project` / `browse_assets`; do not invent item ids.
3. **Speech edits** — prefer `read_script` → edit → `apply_script` (restorable) over destructive clip deletes.
4. **Verify** — tool success ≠ visual proof; use timeline frames / preview before claiming done.
5. **Hard cuts** on locked-off talking heads — avoid cross-dissolves that ghost the face.

## Routing

| Task | Approach |
|---|---|
| Import local files | `import_media` session + upload helper |
| Cleanup fillers / silence | `clean_script` / script edit |
| Captions | `edit_captions` (do not fake as V2 video track) |
| B-roll | Stock / library first; place on upper video tracks |
| MG | Design Style presets / `create_motion_graphic_from_code` |
| Export proof | Preview + frame inspection |

Read host MCP tool schemas before calling. Keep the user’s visible ChatCut surface aligned with the project you edit.

## Related cutmax skills

- `baocut` — local Mac ASR / cleanup when ChatCut is unavailable
- `local-video-studio` — silent local picture tracks / draw-process recipes
- `pireel` — talking-head studio alternative via Pireel MCP
