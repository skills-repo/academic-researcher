---
name: latex-writer
description: LaTeX 论文排版：编译修复、期刊模板适配、图表排版、参考文献格式
source:
  type: derived
  repo: skills-repo/academic-researcher
  path: skills/latex-writer/SKILL.md
  url: https://skills.sh/bahayonghang/academic-writing-skills/latex-paper-en
  version: 1.0.0
  updated: 2026-07-30
metadata:
  author: hope
  category: 排版
  platform: 通用
  difficulty: 进阶
  version: 1.0.0
  created: 2026-07-30
tags:
  - latex
  - typesetting
  - journal-format
  - academic
---

# LaTeX Writer — 论文排版

> 专注于英文 LaTeX 论文的编译修复、期刊模板适配和排版优化。不从头写论文，而是让现有 .tex 文件达到投稿标准。

## 能力

- **编译修复**：诊断并修复 LaTeX 编译错误（缺失包、语法错误、环境不匹配）
- **期刊模板适配**：将论文适配到目标期刊/会议的模板（IEEE/ACM/Elsevier/Springer/Nature）
- **图表排版**：图片嵌入、表格格式化、子图排列、浮动体定位
- **参考文献格式**：BibTeX/BibLaTeX 配置、引用格式切换、DOI 校验
- **公式排版**：数学公式对齐、编号、多行公式拆分

## 使用方式

在 Claude Code 中使用 `/latex-writer` 调用。

```
/latex-writer 我的论文编译报错，帮我修复
/latex-writer 将这篇 IEEE 格式的论文转为 Elsevier 模板
/latex-writer 检查我的参考文献格式是否满足期刊要求
```

## 工作流

1. **现状诊断** — 读取 .tex 文件，检查编译错误和格式问题
2. **问题定位** — 按优先级排序：编译错误 > 格式不符 > 排版优化
3. **逐项修复** — 每个修复后验证编译通过
4. **模板适配** — 替换 documentclass、调整页边距/字体/章节样式
5. **最终检查** — 编译通过、参考文献完整、图表位置正确

## 常见 LaTeX 问题速查

| 问题 | 原因 | 修复 |
|------|------|------|
| `Undefined control sequence` | 未加载包或拼写错误 | 添加 `\usepackage{}` |
| `Missing $ inserted` | 数学符号在文本模式 | 用 `$...$` 包裹 |
| `Overfull hbox` | 内容超出页宽 | 调整断词或表格宽度 |
| 图片不显示 | 路径错误或格式不支持 | 检查路径，用 PDF 格式 |
| 引用 `[?]` | 未编译 BibTeX | 运行 pdflatex → bibtex → pdflatex ×2 |

## 适用场景

- 论文编译报错，不熟悉 LaTeX 调试
- 从 arXiv 下载的源码编译失败
- 投稿前需要转换期刊模板
- 图表排版不理想需要优化

## 限制

- 不处理中文 LaTeX（CTeX）排版
- 不提供 Overleaf 账号管理和协作功能
- 复杂的自定义模板（如学位论文格式）可能需要多轮交互