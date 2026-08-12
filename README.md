# cutmax

### 为创作者准备的视频工作室。  
本地地基，官方加持。给 Agent 用的剪辑与素材技能包。

---

**本地把事做稳。平台把事做漂亮。**

cutmax 整理已验证的剪辑、动效、分镜与素材流程，供 Codex / Claude / Cursor 直接调用。  
默认能力跑在你的电脑上；需要更强成片时，正式接入 **Seedance（即梦）、ChatCut、Pireel** 等官方能力——不是抵制，是为了做得更好。

<br>

## 安静地强大。

少折腾，多成品。

|  |  |
| --- | --- |
| **本地优先** | ffmpeg、Pillow、Remotion、BaoCut。随时可剪，不卡在登录墙外。 |
| **官方加持** | Seedance / ChatCut / Pireel 一等公民。该用大模型与专业时间线时，就用。 |
| **结构清晰** | 本地包与平台包分层。链接清晰，计费先确认。 |
| **为 Agent 设计** | 触发条件明确，适合连续执行到可验收成片。 |

<br>

## 你想做的，它刚好会。

**照片变成有过程的成片。**  
实拍、手在画、线稿、上色、成稿——阶段分明。

**手绘日记与翻页叙事。**  
本地 Remotion，竖版友好。

**口播精修。**  
BaoCut 本地整理，或 ChatCut / Pireel 多轨精修与图文编排。

**即梦级画面。**  
Seedance 提示词与创意工作台，把想法推到可生成。

**产品镜头与图表。**  
Shotcraft 与 Manim，讲清楚就好。

**脚本、分镜、封面、换装。**  
先写清，再选本地渲染或官方生成。

<br>

## 两层结构。像开关一样清楚。

**地基。** `skills/`  
本地剪辑、本地渲染、脚本与免费素材流程。

**平台。** `platforms/`  
Seedance、ChatCut、Pireel，以及官方提示词族。  
为质量服务；花积分前先问你一声。

<br>

## 开始使用。

```bash
git clone https://github.com/WillNam/cutmax.git
cd cutmax

# 本地地基
./scripts/link-skills.sh ~/.codex/skills

# 官方平台（推荐一并启用）
./scripts/link-platforms.sh ~/.codex/skills
```

手绘渲染器（首次）：

```bash
cd tools/story-to-handdrawn-video
npm install
export STORY_VIDEO_PROJECT="$(pwd)"
```

建议环境：`ffmpeg` · `ffprobe` · Python 3 + Pillow  
平台能力另需对应账号 / MCP（ChatCut、Pireel、即梦等）。

入口 Skill：[local-video-studio](skills/local-video-studio/SKILL.md) · 平台说明：[platforms/README.md](platforms/README.md)

<br>

## 目录一览。

|  |  |
| --- | --- |
| [skills/](skills/) | 本地地基技能包 |
| [platforms/](platforms/) | 官方平台与大模型工作流 |
| [tools/](tools/story-to-handdrawn-video/) | 手绘 Remotion 工程 |
| [rules/](rules/stock-broll-workflow.md) | 免费 B-roll 工作流 |
| [CATALOG.md](CATALOG.md) | 完整收录表 |
| [SCOPE.md](SCOPE.md) | 收录边界与暂缓项 |

<br>

## 设计原则。

1. **本地保底，平台拔高。** 能本地完成的先本地；要更好就上官方工具。  
2. **花积分先确认。** 批量云生成、付费 ASR、扣费 MG 前说明并征得同意。  
3. **先看画面。** 成片前抽帧或时间线预览，再谈完成。  
4. **一层一件事。** 本地路由与平台路由分开，Agent 不混淆。

<br>

## License

各 Skill 保留其原有许可证。本仓库聚合说明采用 MIT。

---

<p align="center">
  <sub>cutmax — Local foundation. Official power. Better films.</sub>
</p>
