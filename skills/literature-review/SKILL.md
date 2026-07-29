---
name: literature-review
description: 系统化文献综述：搜索策略、筛选标准、质量评估、综合分析，产出结构化的综述章节
source:
  type: derived
  repo: skills-repo/academic-researcher
  path: skills/literature-review/SKILL.md
  url: https://skills.sh/affaan-m/everything-claude-code/literature-review
  version: 1.0.0
  updated: 2026-07-30
metadata:
  author: hope
  category: 研究
  platform: 通用
  difficulty: 进阶
  version: 1.0.0
  created: 2026-07-30
tags:
  - literature-review
  - systematic-review
  - research-method
  - synthesis
---

# Literature Review — 文献综述

> 从搜索策略到综合分析，系统化地完成学术文献综述。不只是罗列文献，而是建立知识图谱、识别研究空白。

## 能力

- **搜索策略设计**：关键词组合、数据库选择、时间范围设定
- **文献筛选**：按纳入/排除标准筛选，PRISMA 流程图
- **质量评估**：对关键文献做方法论评估和偏倚风险分析
- **主题综合**：识别研究主题聚类，建立概念关联
- **综述撰写**：按主题组织综述章节，突出研究空白

## 使用方式

在 Claude Code 中使用 `/literature-review` 调用。

```
/literature-review 帮我做 transformer 模型压缩方向的文献综述
/literature-review 设计一个关于联邦学习隐私保护的搜索策略
/literature-review 从这 30 篇论文中提取研究主题和趋势
```

## 工作流

1. **定义范围** — 研究问题、PICO 框架、综述类型（系统/范围/叙事）
2. **设计搜索** — 关键词+布尔运算符、数据库列表、时间/语言限制
3. **执行筛选** — 标题摘要初筛 → 全文精筛 → 记录排除理由
4. **数据提取** — 从入选文献中提取关键信息（方法、发现、局限）
5. **综合分析** — 按主题聚类、识别一致与矛盾、画知识图谱
6. **撰写综述** — 引言→方法→结果→讨论，突出 research gap

## 搜索策略模板

```
("keyword A" OR "synonym A") AND ("keyword B" OR "synonym B")
Databases: PubMed / Scopus / Web of Science / Google Scholar
Filter: 2018-2026, English, peer-reviewed
```

## 适用场景

- 开题前需要了解领域研究现状
- 撰写论文的 Related Work 章节
- 做系统化文献综述（Systematic Review / Meta-analysis）
- 写基金申请时需要论证研究创新性

## 限制

- 不能替代人工全文阅读和深度理解
- 文献搜索受限于公开数据库访问权限
- 不提供文献管理软件（Zotero/EndNote）的直接集成
- 对非英文文献的处理能力有限