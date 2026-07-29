---
name: paper-assembly
description: 论文章节组装：从大纲到完整草稿的结构化写作，含论证链条和段落衔接
source:
  type: derived
  repo: skills-repo/academic-researcher
  path: skills/paper-assembly/SKILL.md
  url: https://skills.sh/lingzhi227/agent-research-skills/paper-assembly
  version: 1.0.0
  updated: 2026-07-30
metadata:
  author: hope
  category: 写作
  platform: 通用
  difficulty: 进阶
  version: 1.0.0
  created: 2026-07-30
tags:
  - academic-writing
  - paper
  - manuscript
  - research
---

# Paper Assembly — 论文章节组装

> 从大纲到完整论文草稿的结构化写作流程。不只帮你写段落，更帮你构建连贯的论证链条。

## 能力

- **章节结构化**：按 IMRaD（Intro-Methods-Results-Discussion）组织论文
- **论证链构建**：确保每个段落有清晰的主张-证据-推理链
- **段落衔接**：检查章节间过渡，避免断裂感
- **摘要精炼**：提炼核心贡献、方法和发现
- **一致性检查**：术语统一、时态一致、图表引用对应

## 使用方式

在 Claude Code 中使用 `/paper-assembly` 调用。

```
/paper-assembly 我有一个大纲和实验结果，帮我写 Discussion 章节
/paper-assembly 检查这篇论文的论证链条是否完整
/paper-assembly 从我的方法描述和实验数据开始，组装完整论文
```

## 工作流

1. **输入梳理** — 确认已有素材：大纲、实验数据、图表、参考文献
2. **章节规划** — 按目标期刊要求确定章节结构和页数分配
3. **逐章写作** — 按 IMRaD 顺序，每章先写骨架再填肉
4. **论证检查** — 每条主张有对应证据，每段有清晰主题句
5. **全局润色** — 统一术语、时态、缩写，检查图表引用

## IMRaD 结构指南

| 章节 | 核心问题 | 占全文比例 |
|------|---------|-----------|
| Introduction | 为什么这个问题重要？前人做了什么？本文贡献是什么？ | ~15% |
| Methods | 你怎么做的？别人能复现吗？ | ~20% |
| Results | 你发现了什么？ | ~25% |
| Discussion | 结果意味着什么？与已有工作如何关联？局限性？ | ~30% |
| Conclusion | 核心贡献和未来方向（一句话总结） | ~10% |

## 适用场景

- 从零开始撰写英文期刊/会议论文
- 已有实验结果和数据，需要组织成论文
- 论文被拒后需要重构论证链条
- 导师要求改写某个章节的逻辑结构

## 限制

- 不提供实验设计和数据分析（那是你自己的工作）
- 不替代领域专家对技术内容的判断
- 需要用户提供准确的数据和实验结果
- 不负责 LaTeX 排版（使用 latex-writer 技能）