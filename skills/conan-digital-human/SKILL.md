---
name: conan-digital-human
description: "Build, organize, and operate Conan's personal digital-human system: identity-preserved avatar portraits, role libraries, voice recordings, voice-clone test preparation, and short talking-head samples. Use when the user asks about Conan's 数字人, 声音库, 音色克隆, 角色库, 数字人口播, or wants to update the associated Feishu documentation."
---

# Conan Digital Human

## Scope

Maintain one consistent personal digital human for Conan. Preserve identity, archive raw source assets, generate role-specific portraits, prepare voice references, and produce sample-video specifications.

## Consent Gate

1. Confirm that the voice and portrait belong to Conan or that Conan has explicit authorization.
2. Keep raw voice and portrait files local by default.
3. Do not upload voice or portrait assets to an external cloning or generation service until Conan explicitly confirms the exact action.
4. Before an external voice-generation request, summarize source clip, test text, output format, estimated cost when available, and wait for explicit confirmation.

## Asset Intake

Use this project structure when available:

```text
outputs/digital-avatar/
  avatar-master.jpg
  avatar-master-v*.png
  role-library.md
  voice-library/raw/
  voice-library/prepared/
  digital-human-profile.md
```

For a new source image, require a clear, unobstructed face with even lighting. Use the original portrait as the identity anchor for every edited or generated avatar.

For a new voice recording, archive the original file first. Check format, sample rate, duration, clipping, and loudness locally. Keep voice-reference clips under 30 seconds. Create a non-destructive normalized WAV only when a test reference is needed; never overwrite the raw recording.

## Avatar Rules

- Preserve face shape, cheek and jaw width, eyes, eyelids, eyebrows, nose, lips, ears, skin tone, hair, age, ethnicity, and natural asymmetry.
- Prefer 9:16 chest-up framing for talking-head content: full head and shoulders visible, direct eye contact, mouth unobstructed, eyes near the upper third.
- For Douyin-style vertical talking-head portraits, use an eye-level 70–85 mm look. Keep the hair top about 7–9% below the frame edge, eyes near the upper third, both shoulders fully visible with comfortable side margins, and crop between the chest and upper waist. The head should occupy no more than about 30% of the vertical frame; hands stay below the chest or outside the frame.
- Keep dark-studio portraits readable: preserve both eyes, natural skin tone, and clothing separation from the black background. Use restrained blue, amber, or red edge light without letting colored light contaminate the whole face.
- For 16:9 scene portraits, keep a believable adult head-to-body ratio near 1:7.5 in full-body views. The head, neck, trapezius, shoulders, chest, arms, and legs must share one coherent lens perspective and anatomy.
- Reject any result with an oversized or pasted-on head, narrow shoulders, shortened torso, long or disconnected neck, uneven shoulder line, undersized limbs, slouching, or an abrupt face-to-body skin or lighting seam.
- Use a natural 70–85 mm editorial perspective for medium-full and full-body scenes. Keep shoulders broad but believable, chest open, spine upright, and muscle tension appropriate to the activity.
- Keep skin texture, individual hair strands, catchlights, natural blinking, slight breathing, and small head movement.
- Avoid face slimming, beauty filtering, waxy skin, enlarged eyes, altered nose, exaggerated smiles, large turns, or strong hand gestures.
- Vary long-term expressions and actions within identity limits: calm half-smile, genuine smile, focused mid-sentence expression, thoughtful gaze, natural walking, open-hand explanation, or activity-specific movement. Do not reuse an identical face and pose across the library.
- Use contemporary premium menswear with clean fit, natural fabric drape, and no forced logo exposure. Spring/summer defaults include fitted crew-neck T-shirts, fine-gauge polos, poplin shirts, linen shirts, and modern camp-collar shirts in navy, forest green, ivory, white, pale blue, taupe, charcoal, and espresso.
- For tennis scenes, prefer a dark crew-neck professional performance T-shirt and authentic athletic anatomy. Avoid dated contrast-collar polos unless Conan explicitly requests one.
- Save every accepted portrait as a versioned sibling; never overwrite a prior master unless Conan explicitly requests replacement.

## Core Role Library

Use the existing role-library document when it exists. Default role mapping:

| Role | Best for | Visual direction |
| --- | --- | --- |
| 创始人 / 商务代表 | 公司介绍、合作、商业观点 | 深蓝或深色利落商务休闲 |
| 科技操盘手 | AI、创业、效率、工作流 | 现代办公室、克制深色 |
| 知识讲师 | 课程、教程、方法论 | 暖色、干净、易亲近 |
| 深度访谈主持人 | 播客、访谈、深度观点 | 深色针织、低照度暖背景 |
| 生活方式主理人 | 创意工作、个人日常、审美内容 | 柔和自然光、低饱和休闲造型 |
| 极简观点表达者 | 短视频观点、答疑、产品口播 | 正面棚拍、极简深色上装 |

Create new roles only when they have a distinct content purpose, not merely a small wardrobe change.

## Voice Library

Use six short recordings to cover natural baseline, professional explanation, warm support, energetic delivery, numbers/rhythm, and English/tool names. Use the natural-baseline clip as the first test candidate unless its technical quality is worse than another clip.

Report audio checks succinctly: duration, format, clipping status, and whether the clip is suitable for a first test. Recommend a higher-fidelity re-record only when quality materially limits the intended result.

## Talking-Head Sample

Start with a 10–15 second vertical sample. Use the default portrait and natural voice. Keep the camera locked or use only an imperceptible slow push-in; use one or two natural blinks and no background music for the first acceptance test.

Suggested initial script:

> 大家好，我是 Conan。我会用简单、清楚的方式，分享关于工作、创造和成长的真实观察。我们一起把复杂的问题，变成可以行动的下一步。

Verify identity consistency, lip readability, voice similarity, natural timing, and absence of visual artifacts before expanding to longer content.

## Feishu Documentation

When asked to synchronize this system to Feishu, require the exact document link or an accessible Feishu connector. Add or update these sections:

1. 默认数字人：主视觉、主声音、画幅与构图。
2. 角色库：角色、用途、画面与语气。
3. 声音库：录音编号、技术验收、测试母带。
4. 样片流程：首条文案、镜头规则、验收标准。
5. 授权边界：仅代表 Conan；外部上传或克隆前需明确确认。

If Feishu is unavailable, save the same content as Markdown in the current project's `outputs/digital-avatar/` directory and report the exact blocker without inventing a sync result.
