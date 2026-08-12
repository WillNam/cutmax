# cutmax

### 为创作者准备的本地视频工作室。  
给 Agent 用的剪辑与素材技能包。

---

**在你的电脑上完成。**  
不依赖付费云视频接口。  
打开即用，按需扩展。

cutmax 把已经验证过的视频剪辑、过程动效、分镜脚本与素材流程，整理成一套可被 Codex / Claude / Cursor 直接调用的 Skills。默认路径只走本地工具与免费素材；面向 Seedance、Kling 等产品的提示词，收在可选目录里，由你决定是否启用。

<br>

## 安静地强大。

少一些 key，多一些成品。

|  |  |
| --- | --- |
| **本地优先** | ffmpeg、Pillow、Remotion、BaoCut。算力与素材留在你这边。 |
| **结构清晰** | 一个枢纽 Skill 路由配方；其余按场景拆分，互不拖累。 |
| **边界分明** | 免费默认栈与付费模型提示词分开。不会默默把你带进计费接口。 |
| **为 Agent 设计** | 每个 Skill 都有明确触发条件与验收习惯，适合交给助手连续执行。 |

<br>

## 你想做的，它刚好会。

**照片变成有过程的成片。**  
实拍、手在画、线稿、上色、成稿——阶段分明，而不是一张图空转。

**手绘日记与翻页叙事。**  
本地 Remotion 渲染，竖版友好。

**口播整理。**  
在已安装 BaoCut 的 Mac 上，转写、去口癖、导出字幕与粗剪。

**产品镜头与图表。**  
Shotcraft 模板与 Manim 插槽，适合演示与讲解。

**脚本、分镜、封面、换装方案。**  
先写清，再决定在哪里渲染。

**免费 B-roll。**  
从画面计划到 Pexels 下载，再到时间轴清单。

<br>

## 两层设计。像开关一样简单。

**默认。** `skills/`  
本地剪辑、本地渲染、纯提示词脚本、免费素材流程。  
一条命令链接到你的 Agent Skills 目录。

**可选。** `opt-in/prompt-for-paid-models/`  
为即梦 / Seedance、Kling、Runway、Veo、Sora 等准备的提示词技能。  
不自动加载。启用后也只写提示词，不替你调用付费 API。

<br>

## 开始使用。

```bash
git clone https://github.com/WillNam/cutmax.git
cd cutmax

# 链接免费 / 本地 Skills
./scripts/link-skills.sh ~/.codex/skills

# 若需要付费模型提示词包（可选）
./scripts/link-opt-in-prompts.sh ~/.codex/skills
```

手绘渲染器（首次）：

```bash
cd tools/story-to-handdrawn-video
npm install
export STORY_VIDEO_PROJECT="$(pwd)"
```

建议环境：`ffmpeg` · `ffprobe` · Python 3 + Pillow

入口 Skill：[local-video-studio](skills/local-video-studio/SKILL.md)

<br>

## 目录一览。

|  |  |
| --- | --- |
| [skills/](skills/) | 默认技能包 |
| [opt-in/](opt-in/prompt-for-paid-models/) | 付费模型提示词（需显式启用） |
| [tools/](tools/story-to-handdrawn-video/) | 手绘 Remotion 工程 |
| [rules/](rules/stock-broll-workflow.md) | 免费 B-roll 工作流 |
| [CATALOG.md](CATALOG.md) | 完整收录表 |
| [EXCLUDED.md](EXCLUDED.md) | 刻意未收录项 |

<br>

## 设计原则。

1. **默认免费。** 缺 key 就换本地配方，不静默升级到付费云生成。  
2. **先看画面。** 成片前抽帧自检；阶段差异必须肉眼可辨。  
3. **少即是多。** 一个任务选一条主配方，再按需叠加 B-roll。  
4. **可选即可选。** 付费模型相关能力永不混入默认路由。

<br>

## License

各 Skill 保留其原有许可证。本仓库聚合说明（README、CATALOG、EXCLUDED）采用 MIT。

---

<p align="center">
  <sub>cutmax — Create more. Pay less for the path.</sub>
</p>
