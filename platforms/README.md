# Platforms

cutmax 不抵制官方大模型与专业剪辑平台。  
**本地是地基；官方能力是放大器。**

我们收录 Seedance（即梦）、ChatCut、Pireel 等官方工作流，是为了把成片做得更好——在需要电影级生成、多轨精修、口播图文编排时，用对的工具，而不是为了「纯本地」而牺牲质量。

## 怎么选

| 场景 | 建议 |
|---|---|
| 静音图文轨、过程动效、免费 B-roll | 默认 `skills/`（本地） |
| 多轨口播、字幕、MG、实时预览 | **ChatCut** |
| 口播图文块、主题化讲解轨 | **Pireel** |
| 即梦 / Seedance 创意与提示词 / API 出片 | **Seedance 系列** + `seedance2` |
| 只要提示词、自己到网页生成 | `seedance-and-prompts/` |

## 计费礼貌

官方平台可能消耗积分或订阅。cutmax 的约定是：

1. **先说清楚**会用哪个平台、大概消耗什么。  
2. **用户确认后再花积分**（尤其是批量生成）。  
3. **能 BYO / 本地 / 免费库存就先用**，付费生成作增强，不作默认。

## 目录

| Path | 内容 |
|---|---|
| `chatcut/` | ChatCut MCP 剪辑技能 |
| `pireel/` | Pireel Studio MCP 技能 |
| `seedance2/` | 即梦 Seedance 创意工作台（含 API 生成路径） |
| `seedance-and-prompts/` | Seedance 提示词族 + vibe / FPV 等提示技能 |

## 启用

```bash
# 推荐：本地地基 + 官方平台一起链接
./scripts/link-skills.sh ~/.codex/skills
./scripts/link-platforms.sh ~/.codex/skills
```

`link-skills.sh` 只链默认本地包。  
`link-platforms.sh` 链本目录下全部官方平台技能（含提示词子包）。
