---
name: learning-map-infographic
description: >-
  Create, analyze, redesign, or implement dense vertical Chinese learning-map infographics for complex topics. Use when the user wants a polished long-form knowledge card, study roadmap, curriculum map, technical learning path, tool stack map, concept checklist, Xiaohongshu/WeChat-style educational poster, or asks to imitate/analyze a reference image like a structured "学习地图" with title, formula, numbered modules, practice cards, toolbox, and final principles.
---

# Learning Map Infographic

## Overview

Convert a complex domain into a readable vertical learning map. The output should feel like a compact expert syllabus: clear entry point, sequential modules, implementation exercises, tool stack, and final operating principles.

Use the reference image in `assets/reference-quant-map.png` as the style source when visual fidelity is required. For exact visual parameters and production analysis, read `references/style-spec.md`.

## Default Workflow

1. Define the audience, topic boundary, and promised transformation.
   - Example: "from instinctive trading to model-based trading" or "from messy SKU operation to data-driven ecommerce."
2. Compress the domain into one core formula.
   - Format: `核心公式：结果 = 因子 A × 因子 B × 因子 C × 执行系统`.
   - The formula must be specific enough to organize the rest of the poster.
3. Build the main path as 4-8 numbered modules.
   - Each module needs: short title, red keyword line, 2 bullet insights, one practice/homework block.
   - Order modules from foundation to execution, not from buzzword to buzzword.
4. Add a "code/practice" strip.
   - Use 3-5 compact cards for exercises, scripts, formulas, commands, or reproducible tasks.
5. Add a "toolbox" section.
   - Use 3 columns: core stack, data/source inputs, solvers/deployment/workflow.
6. End with 3 final principles.
   - These should be decision rules, not slogans.
7. Verify readability.
   - The poster should be skimmable in 10 seconds and useful in 3 minutes.

## Content Rules

- Prefer concrete nouns, equations, libraries, APIs, tools, datasets, and exercises.
- Avoid generic advice like "learn basics", "improve thinking", or "use AI well" unless tied to an observable task.
- Use Chinese headings for Chinese posters. English technical terms are acceptable inside keyword lines.
- Keep each module independent but sequential.
- Every "课后" or practice block must be actionable.
- If the domain is unfamiliar or current facts matter, research first and cite sources in the planning notes before designing.

## Visual Rules

- Canvas: vertical long poster, approximately 9:16 to 4:7; off-white paper background.
- Palette: black/charcoal text, muted red accent, light gray borders, warm pale red chips.
- Typography: large Song/Ming-style Chinese title; sans-serif body; strong weight contrast.
- Layout: generous margins, rounded cards, thin hairline borders, two-column main grid, bottom utility sections.
- Components: eyebrow chip, title, subtitle, formula bar, section labels, numbered module cards, practice strip, toolbox panel, principle cards, small signature.
- Decoration: keep minimal. Use subtle watermark text only if it does not compete with content.

## Production Modes

### Analyze Only

Return:

- Visual structure
- Content architecture
- Production steps
- Reusable prompt/template
- Risks in readability or accuracy

### Generate Copy Deck

Return a complete text blueprint with all poster sections filled in. Do not generate an image unless requested.

### Implement Poster

Create a real artifact: HTML/CSS, SVG, Figma-ready spec, or image-generation prompt. For HTML/SVG, use stable dimensions and verify the rendered output with screenshots when possible.

## Quality Bar

Before final delivery, check:

- The core formula actually explains the topic.
- The numbered path has a defensible learning sequence.
- The practice blocks are executable.
- There is enough domain specificity to avoid looking like a generic AI-generated poster.
- Text length fits card sizes; no module depends on tiny unreadable text.
- Visual hierarchy is clear: title, formula, main modules, practice/toolbox, principles.
