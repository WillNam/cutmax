# Reference Style Spec

Use this file when reproducing the attached reference style or explaining how to make a similar image.

## Image Production Analysis

The reference is a vertical Chinese educational infographic titled "量化交易学习地图". It is not a decorative poster. It is a dense syllabus compressed into a long-form social card.

### 1. Information Architecture

The image follows this order:

1. Top category chip: narrow red-tinted label that frames the domain and era.
2. Large title: 6-8 Chinese characters plus "学习地图" structure.
3. Subtitle: one-sentence promise, defining the starting point and end state.
4. Core formula bar: a boxed equation that becomes the organizing thesis.
5. Main line label: describes the transformation arc.
6. Six numbered modules in a two-column grid.
7. Code practice strip: four compact cards for concrete exercises.
8. Toolbox panel: three-column resources/tools list.
9. Final discipline cards: three principles.
10. Small signature in lower right.

The content logic is:

`positioning -> thesis/formula -> learning path -> practice -> tools -> discipline`.

### 2. Module Card Pattern

Each main card uses:

- Small red top stroke as a section marker.
- Red circular number badge.
- Bold black module title.
- Red keyword line with 4-6 technical anchors.
- Two red-dot bullets explaining why the module matters.
- Pale inset homework box beginning with "课后：作业：".

Recommended module count: 4-8. Six is ideal for a two-column grid.

### 3. Visual System

Approximate visual parameters:

- Canvas: tall vertical, roughly 9:16.
- Background: warm off-white, not pure white.
- Accent: muted deep red.
- Body text: charcoal black.
- Secondary text: medium gray.
- Borders: light gray, 1px hairline.
- Card radius: 14-20px.
- Inner homework box: pale warm gray, rounded, inset.
- Grid gap: consistent vertical rhythm, no ornamental clutter.

### 4. Typography

- Title: high-contrast Chinese serif/Song-style face, very large, heavy.
- Body: clean sans-serif Chinese font.
- Emphasis: red for keywords, black bold for headings, gray for subtitles.
- Avoid negative letter spacing and overly compressed line height.

### 5. Copywriting Formula

Use this template:

```text
{领域/时代标签}

{主题}学习地图
从 {起点} 开始：{关键能力 1}、{关键能力 2}、{关键能力 3}、{落地能力}

核心公式：{结果} = {判断因子} × {更新机制} × {控制机制} × {执行系统}

主线：从 “{低阶方式}” 到 “{高阶方式}”

1 {模块名}
{关键词、公式、工具、概念}
- {洞察 1}
- {洞察 2}
课后：作业：{可执行任务}
```

### 6. Production Workflow

1. Research the domain.
   - Extract 20-40 domain concepts.
   - Separate foundations, methods, execution, tools, and risks.
2. Write the transformation thesis.
   - Define before/after states.
   - Write one formula that links the sections.
3. Create the six-card syllabus.
   - One card per learning milestone.
   - Force every card to include an exercise.
4. Build the poster in layout.
   - Start with exact text boxes before styling.
   - Use a two-column grid for the main modules.
   - Use compact bottom grids for tools and principles.
5. Polish visual hierarchy.
   - Red only for structure and technical anchors.
   - Keep whitespace between sections.
   - Ensure each card can be read independently.
6. Verify.
   - Zoom out: title/formula/mainline should remain clear.
   - Zoom in: every exercise should be understandable.
   - Remove weak generic wording.

### 7. Common Failure Modes

- Too many decorative elements: the reference works because it is restrained.
- Generic content: without formulas, tools, and exercises, it becomes a motivational poster.
- No learning sequence: modules must build toward implementation.
- Tiny text overload: dense is acceptable; unreadable is not.
- Weak ending: final principles should constrain behavior, not decorate the bottom.

### 8. Example Prompt

```text
Create a vertical Chinese learning-map infographic for {topic}.
Style: restrained off-white paper background, large Song-style Chinese title, muted red accents, rounded thin-border cards, two-column numbered module grid, bottom practice/toolbox/principle sections.
Structure: category chip, title, subtitle, core formula bar, mainline sentence, six numbered modules, four practice cards, three-column toolbox, three final discipline cards.
Content must include concrete formulas, tools, exercises, and implementation steps. Avoid generic motivational language.
```
