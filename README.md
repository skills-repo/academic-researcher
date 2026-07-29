# 学术研究者技能库

> AI Agent Skills for Academic Researchers —— 论文撰写、LaTeX 排版、文献综述、引文管理

## 定位

为研究生、博士后和独立研究者提供一套 AI 驱动的学术写作技能，覆盖从文献检索到论文排版的全流程。特别适合需要撰写英文期刊/会议论文的华人研究者。

## 核心理念

> 好论文不只是写出来的，更是改出来的——引用要准、格式要对、论证要严密。

- **写作与排版分离** — 先专注内容，再处理格式
- **文献综述是研究的基本功** — 系统化搜索、筛选、综合
- **引文准确性是第一道关卡** — 一篇论文的参考文献就是它的信用记录
- **LaTeX 不是障碍，是工具** — 掌握模板和自动化命令

## 技能清单

| 环节 | 技能 | 描述 | 来源 |
|------|------|------|------|
| 写作 | `paper-assembly` | 论文章节组装与改写：从大纲到完整草稿的结构化写作 | [衍生](https://skills.sh/lingzhi227/agent-research-skills/paper-assembly) |
| 排版 | `latex-writer` | LaTeX 论文排版：编译修复、期刊模板、图表公式 | [衍生](https://skills.sh/bahayonghang/academic-writing-skills/latex-paper-en) |
| 综述 | `literature-review` | 系统化文献综述：搜索策略、筛选标准、综合分析 | [衍生](https://skills.sh/affaan-m/everything-claude-code/literature-review) |
| 引用 | `academic-citation` | 学术引文管理：格式校验、BibTeX 生成、完整性检查 | [衍生](https://skills.sh/yuan1z0825/nature-skills/nature-citation) |

## 快速开始

```bash
npx skills add skills-repo/academic-researcher@paper-assembly -g -y
npx skills add skills-repo/academic-researcher@latex-writer -g -y
npx skills add skills-repo/academic-researcher@literature-review -g -y
npx skills add skills-repo/academic-researcher@academic-citation -g -y
```

## 推荐工作流

```
文献检索 → 综述撰写 → 论文写作 → 排版提交
literature-  paper-     latex-
review      assembly   writer
            academic-
            citation
```

## 许可

MIT