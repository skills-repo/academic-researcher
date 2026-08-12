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

## 架构说明（superpower）

本仓库采用 skills-repo 组织的 **superpower 架构**：

- `SKILL.md` — 唯一入口，只做能力路由（本文件）
- `references/` — 深层 playbook：检索策略、引文管理、论文组装验收、论文自动化
- `skills/` — 5 个细粒度子技能，可单独安装
- `scripts/` — `check_references.py` 参考文献格式自检、`scaffold_paper_report.py` 论文精读报告骨架生成（均纯标准库、可复现）
- `assets/` — 字段规则配置、合规 .bib 示例、论文结构清单模板

渐进式加载：Agent 先读路由表，按需读取 `references/` 或 `skills/`，重复任务交给脚本。

## 技能清单

| 环节 | 技能 | 描述 | 来源 |
|------|------|------|------|
| 写作 | `paper-assembly` | 论文章节组装与改写：从大纲到完整草稿的结构化写作 | [衍生](https://skills.sh/lingzhi227/agent-research-skills/paper-assembly) |
| 排版 | `latex-writer` | LaTeX 论文排版：编译修复、期刊模板、图表公式 | [衍生](https://skills.sh/bahayonghang/academic-writing-skills/latex-paper-en) |
| 综述 | `literature-review` | 系统化文献综述：搜索策略、筛选标准、综合分析 | [衍生](https://skills.sh/affaan-m/everything-claude-code/literature-review) |
| 引用 | `academic-citation` | 学术引文管理：格式校验、BibTeX 生成、完整性检查 | [衍生](https://skills.sh/yuan1z0825/nature-skills/nature-citation) |
| 自动化 | `paper-automation` | 论文自动化：给定一篇论文产出可追溯精读报告，并沉淀带出处的阅读库加速综述与自动研究 | [衍生](https://skills.sh/orchestra-research/ai-research-skills/autoresearch) |

## 安装

```bash
# 整库安装（推荐）—— 拿到路由层 + references + scripts + assets
npx skills add skills-repo/academic-researcher -g -y

# 单技能安装 —— 只要某一个细粒度能力
npx skills add skills-repo/academic-researcher@paper-assembly -g -y
npx skills add skills-repo/academic-researcher@latex-writer -g -y
npx skills add skills-repo/academic-researcher@literature-review -g -y
npx skills add skills-repo/academic-researcher@academic-citation -g -y
npx skills add skills-repo/academic-researcher@paper-automation -g -y
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
