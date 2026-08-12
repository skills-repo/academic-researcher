---
name: paper-automation
description: 论文自动化：给定一篇论文（PDF/arXiv ID/DOI/URL/全文），产出可追溯的结构化精读报告，并维护带出处的标注式阅读库以加速综述与自动研究
source:
  type: derived
  repo: skills-repo/academic-researcher
  path: skills/paper-automation/SKILL.md
  url: https://skills.sh/orchestra-research/ai-research-skills/autoresearch
  version: 1.0.0
  updated: 2026-08-12
metadata:
  author: hope
  category: 研究
  platform: 通用
  difficulty: 进阶
  version: 1.0.0
  created: 2026-08-12
tags:
  - paper-reading
  - xray-paper
  - autoresearch
  - survey
  - comprehension
---

# Paper Automation — 论文自动化

> 把「读一篇论文」从手写笔记变成可复现、可追溯的流水线：精读报告一键成型，读过的论文自动沉淀为带出处的知识库，进而加速综述撰写与自动研究（autoresearch）。

本子技能与 `literature-review`（如何系统性检索与筛选大量文献）和 `paper-assembly`（如何写你自己的论文）**正交**：它解决的是**给定一篇具体论文，如何快速、准确地读懂并沉淀**。

## 能力

- **结构化精读（xray）**：输入一篇论文，产出 TL;DR、研究问题、方法解剖、claim–evidence 证据链、局限与威胁、可复现性清单。
- **出处可追溯**：每条结论标注「论文所述 / 代码已确认 / 报告推断 / 外部证据」，绝不把推断伪装成事实。
- **只读代码审计**：官方公开代码存在时，固定版本只读核对模块接口、张量形状、默认值、数据管线，不安装依赖、不跑训练。
- **阅读库沉淀**：多轮精读后把标注式笔记累积成带引用锚点的知识库，喂给综述与自动研究循环。
- **自动研究加速（autoresearch）**：从主题 + 种子论文出发，迭代扩展带出处的综述草稿，区分「语料观察到的趋势」与「作者预测」。

## 何时使用

- 「帮我快速看懂这篇论文」「精读这篇 arXiv 文章」「xray 一下这个方法」
- 给定 PDF/DOI，要产出可分享的精读笔记或 HTML 报告
- 读了一堆论文，需要一个带出处的标注库来写 Related Work
- 想从若干种子自动扩展出一篇带引用的综述草稿（autoresearch）

## 不使用本技能的场景

- 要从零设计检索策略、做 PRISMA 筛选 → 用 `literature-review`
- 要写你自己的论文章节 → 用 `paper-assembly`
- 只校验 BibTeX/引文字段 → 用 `academic-citation`

## 工作流

1. **定输出格式**：明确要 Markdown（轻量可编辑）还是 HTML（带阅读界面与静态公式）。格式未定时只问一次。
2. **锚定来源**：接受本地/远程 PDF、官方全文 HTML、或粘贴全文；记录来源哈希与出处，原始材料不可变。
3. **判论文类型**：Empirical / Theoretical / Survey / Systems，选主分支（不臆测为 empirical）。
4. **读完整论证**：连附录一起读，建立 claim–evidence–limitation 坐标；对承载性模块记录接口、输入/输出、关键参数。
5. **只读代码审计**：官方有公开代码时固定 revision 只读核对，否则显式写「未找到公开代码」，绝不静默替换。
6. **建证据脊柱**：每条实质结论落到精确论文/代码/一手来源锚点，推断显式标注。
7. **产出并校验**：Markdown 写 `summary.md`；HTML 用 `scripts/scaffold_paper_report.py` 起骨架后填占位、渲染静态公式、跑校验器直到通过。

## 边界（始终遵循）

- 不做复现实验、不跑训练/评测；精读报告与复现是两件事。
- 不臆造公式、指标、图表；无原始结果图时显式标记 `data-original-result-unavailable`。
- 不静默把推断写成事实；每处 `[推断]` 必须可见。
- 来源边界与代码审计状态要明确声明的，不夸大确定性。
- 脚本只生成报告骨架、出校验报告，**不改你的源论文、不替你下研究结论**。

## 与其他技能协作

- 精读后要做系统性筛选与综合 → 衔接 `literature-review`
- 读懂的方法要落到自己的论文 → 衔接 `paper-assembly` 与 `latex-writer`
- 引用的 BibTeX 字段要校验 → 衔接 `academic-citation` 与 `scripts/check_references.py`
