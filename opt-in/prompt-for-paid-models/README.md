# Opt-in: prompts for paid video models

This folder is **not** part of the free default cutmax router.

It contains **prompt-only** skills that help you write better prompts for third-party paid video generators (Seedance / 即梦, Kling, Runway, Veo, Sora, etc.).

## What this is

- Prompt engineering, shot design, scene packs
- No API keys required to *use the skill text*
- You paste prompts into the paid product yourself

## What this is not

- Not a free local renderer
- Does **not** call Seedance/Kling/Runway APIs from this repo
- `seedance2` (API workstation) stays **excluded** — see root `EXCLUDED.md`

## Skills included

| Skill | Focus |
|---|---|
| `seedance` | Seedance 2.0 中文提示词核心 |
| `seedance-prompt-en` | English Seedance prompting (+ zh) |
| `seedance-shot-design` | 分镜 / 运镜 / 导演风格库 |
| `seedance-viral-hook` | 开头钩子 |
| `seedance-ai-avatar` | AI 数字人口播提示 |
| `seedance-before-after` | 前后对比转化 |
| `seedance-course-promo` | 课程推广 |
| `seedance-faceless-channel` | 无出镜频道 |
| `seedance-luxury-aesthetic` | 奢侈美学 |
| `seedance-personal-brand` | 个人品牌 |
| `seedance-podcast-visual` | 播客可视化 |
| `seedance-saas-launch` | SaaS 发布 |
| `seedance-testimonial-story` | 客户证言 |
| `vibe-creating-prompt` | 跨模型 vibe 提示改写 |
| `fpv-immersive-video-prompting` | FPV / 路线控制沉浸提示 |

## Enable (explicit)

Default `scripts/link-skills.sh` **does not** link this folder.

```bash
# link opt-in prompts into your agent skills dir
./scripts/link-opt-in-prompts.sh ~/.codex/skills
```

Or symlink a single skill:

```bash
ln -sfn "$(pwd)/opt-in/prompt-for-paid-models/seedance-shot-design" \
  ~/.codex/skills/seedance-shot-design
```

## Cost reminder

Rendering on Seedance / Kling / Runway / Veo / Sora consumes **their** credits. cutmax only ships the prompt skills.
