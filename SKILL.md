---
name: academic-researcher
description: >-
  把 AI 变成学术研究搭档：从文献检索、综述撰写、论文组装到 LaTeX 排版与引文管理。
  覆盖检索策略、参考文献字段完整性与重复检测、IMRaD 论证链验收。
  触发词："文献综述"、"BibTeX 校验"、"论文结构"、"LaTeX 排版"、"引文格式"、"查重重复"。
agent_created: true
metadata:
  version: 1.0.0
  category: 学术研究
  difficulty: 进阶
  architecture: superpower
---

# 学术研究者

> 让 AI 帮你把研究想法变成可投稿的论文——检索、综述、写作、排版、引文，全链路护航。

本技能采用 **superpower 架构**：`SKILL.md` 只做路由，深层 playbook 放 `references/` 按需加载，
细粒度能力放 `skills/` 子技能，确定性 lint 交给 `scripts/`，结构模板放 `assets/`。

## 何时使用

- 要设计可复现、可审计的文献检索策略
- 写综述前需要搜索/筛选/综合的方法论
- 汇编论文章节，需要 IMRaD 验收与论证链检查
- LaTeX 排版报错或要适配期刊模板
- 给定一篇论文（PDF/arXiv/DOI），需要快速、可追溯的精读报告与阅读库沉淀
- 需要校验 BibTeX/引文字段完整性与重复条目

## 能力索引（超级技能路由）

| 任务 | 读取 / 调用 | 关键词（grep 线索） |
|------|------------|---------------------|
| 文献检索策略：库选型/布尔/PICO/滚雪球 | `references/literature-search-strategy.md` | 文献检索 数据库 布尔 PICO 滚雪球 去重 饱和 |
| 引文管理：格式选型/字段完整/重复检测 | `references/reference-management-playbook.md` | 引文 BibTeX APA IEEE 字段 重复 去重 DOI |
| 论文章节组装验收：IMRaD/论证链/一致性 | `references/manuscript-assembly-checklist.md` | 论文组装 IMRaD 论证链 一致性 图表引用 术语 |
| 系统化文献综述：搜索/筛选/综合 | `skills/literature-review/SKILL.md` | 文献综述 systematic review PRISMA 筛选 综合 |
| 论文章节组装：大纲到草稿的结构化写作 | `skills/paper-assembly/SKILL.md` | 论文组装 章节 大纲 论证 摘要 一致性 |
| LaTeX 排版：编译修复/期刊模板/图表 | `skills/latex-writer/SKILL.md` | LaTeX 排版 编译修复 期刊模板 图表 公式 |
| 学术引文管理：格式校验/BibTeX/完整性 | `skills/academic-citation/SKILL.md` | 学术引文 格式校验 BibTeX 完整性 DOI |
| 论文自动化：精读报告/证据链/阅读库沉淀 | `skills/paper-automation/SKILL.md` | 论文自动化 精读 xray 证据链 综述 autoresearch 阅读库 |
| 论文自动化方法论：决策树/命令/坑/清单 | `references/paper-automation-playbook.md` | 精读 自动研究 分类 代码审计 出处 检查清单 |

## 内置脚本（确定性、可重复执行）

放在 `scripts/`，把引文质量变成可复现的机器检查：

- `scripts/check_references.py bibtex --file <refs.bib>` — 校验字段完整性/重复键/重复标题
- `scripts/check_references.py selfcheck` — 校验内置资产（规则+示例 .bib）0 ERROR
- `scripts/scaffold_paper_report.py --title "..." --paper-type empirical --url <arXiv> --out note.md` — 生成可追溯的论文精读报告骨架

运行示例：

```bash
python3 scripts/check_references.py bibtex --file refs.bib
python3 scripts/scaffold_paper_report.py --title "论文标题" --paper-type empirical \
  --url "https://arxiv.org/abs/2401.00001" --out reading-notes/note.md
```

## 模板资源

`assets/` 提供可直接套用的规范与模板：

- `assets/reference_rules.json` — 必填字段规则（脚本 `bibtex` 的规则来源，可自定义）
- `assets/sample_references.bib` — 合规 .bib 示例（脚本 selfcheck 回检 0 ERROR）
- `assets/paper-structure-checklist.md` — 论文结构清单模板

## 核心原则（始终遵循）

1. **检索可复现**：≥2 互补库、布尔带括号、滚雪球至饱和。
2. **引文即信用**：每条引用字段完整、无重复，用脚本 lint 而非肉眼。
3. **一主张一证据**：每条主张配证据与推理，无 [unsupported]。
4. **渐进式加载**：先读路由表与对应 `references/`，再动手。
5. **明确边界**：脚本只做引文规范自检、出报告，不替你拍板研究结论、不改你的源文件。
6. **写作与排版分离**：先内容后格式，LaTeX 是工具不是障碍。

## 与其他技能协作

- 引文需接入文献管理工具 → 配合 Zotero/EndNote（子技能侧重校验而非替代）
- 数据可视化与图表 → 参考 `figma-master` 的视觉设计原则
- 需要英文润色与学术表达 → `skills-repo/writer-studio`
