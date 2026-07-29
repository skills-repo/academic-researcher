---
name: academic-citation
description: 学术引文管理：格式校验、BibTeX 生成、完整性检查、高影响力期刊引文适配
source:
  type: derived
  repo: skills-repo/academic-researcher
  path: skills/academic-citation/SKILL.md
  url: https://skills.sh/yuan1z0825/nature-skills/nature-citation
  version: 1.0.0
  updated: 2026-07-30
metadata:
  author: hope
  category: 引用
  platform: 通用
  difficulty: 入门
  version: 1.0.0
  created: 2026-07-30
tags:
  - citation
  - bibtex
  - references
  - bibliography
---

# Academic Citation — 学术引文管理

> 引文是论文的信用记录。本技能帮你校验格式、生成 BibTeX、检查完整性，确保每条引用都经得起审稿人推敲。

## 能力

- **引文格式校验**：检查 APA/IEEE/MLA/Chicago/Nature 等格式一致性
- **BibTeX 生成**：从 DOI、标题或 URL 自动生成准确的 BibTeX 条目
- **完整性检查**：正文引用与参考文献列表交叉比对，发现缺失或多余引用
- **高影响力期刊适配**：Nature/CNS 等顶刊的严格引文要求
- **引文长句拆分**：将长段落拆分为可引用的独立主张，确保每句话引用到位

## 使用方式

在 Claude Code 中使用 `/academic-citation` 调用。

```
/academic-citation 检查这篇论文的引用格式是否符合 IEEE 标准
/academic-citation 从 DOI 列表生成 BibTeX 文件
/academic-citation 找出正文中引用但参考文献中缺失的条目
```

## 工作流

1. **收集输入** — 正文 .tex/.docx + 参考文献列表或 .bib 文件
2. **交叉比对** — 逐一核对正文中的 `\cite{}` 与 .bib 条目
3. **格式检查** — 按目标期刊/会议标准逐字段检查
4. **DOI 补全** — 对缺失 DOI 的条目搜索并补全
5. **输出报告** — 问题列表 + 修复建议 + 修正后的 .bib 文件

## 引文检查清单

```
[ ] 正文中所有 \cite{} 在 .bib 中有对应条目
[ ] .bib 中所有条目在正文中被引用
[ ] 作者名格式一致（First Last vs Last, First）
[ ] 期刊名缩写/全称统一
[ ] DOI 字段存在且可解析
[ ] 卷/期/页码完整
[ ] 出版年份与正文引用一致
[ ] URL 访问日期（如有）在合理范围内
```

## 适用场景

- 投稿前做最后的引文检查
- 从 Word 转到 LaTeX 需要生成 .bib 文件
- 导师要求引用高影响力期刊论文
- 参考文献格式被审稿人挑过毛病

## 限制

- 不替代 Zotero/EndNote/Mendeley 等文献管理工具
- DOI 解析依赖 Crossref API，非 Crossref 注册的 DOI 可能无法解析
- 不处理专利、标准文档等非论文类型的引用
- 不提供查重和剽窃检测