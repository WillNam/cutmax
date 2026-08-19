# Platform Guide

cutmax 不抵制官方大模型与专业剪辑平台。  
**本地是地基；官方能力是放大器。**

## 怎么选

| 场景 | 建议 |
|---|---|
| 静音图文轨、过程动效、免费 B-roll | 默认 `skills/`（本地） |
| 多轨口播、字幕、MG、实时预览 | **ChatCut** |
| 口播图文块、主题化讲解轨 | **Pireel** |
| 即梦 / Seedance 创意与 API 出片 | **Seedance 系列** + `seedance2` |
| 只要提示词、自己到网页生成 | `seedance-and-prompts/` |

## 计费礼貌

1. **先说清楚**会用哪个平台、大概消耗什么。
2. **用户确认后再花积分**（尤其是批量生成）。
3. **能 BYO / 本地 / 免费库存就先用**，付费生成作增强，不作默认。

## 目录

| Path | 内容 |
|---|---|
| `platforms/chatcut/` | ChatCut MCP 剪辑技能 |
| `platforms/pireel/` | Pireel Studio MCP 技能 |
| `platforms/seedance2/` | 即梦 Seedance 创意工作台 |
| `platforms/seedance-and-prompts/` | Seedance 提示词族 |

## 启用

```bash
bash scripts/link-platforms.sh ~/.codex/skills
```
