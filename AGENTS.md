# Academic Researcher — Agent 入口

> 本仓库是 skills-repo 组织下的学术研究者技能库。Agent 在处理论文撰写、LaTeX 排版、文献综述、引文管理等任务时加载本文件。采用 skills-repo 组织的 **superpower 架构**。

## 目录约定（superpower）

```
academic-researcher/
├── SKILL.md                     # L1 路由层：唯一入口，只做索引
├── references/                  # L2 深层 playbook
│   ├── literature-search-strategy.md
│   ├── reference-management-playbook.md
│   └── manuscript-assembly-checklist.md
├── skills/                      # L3 细粒度子技能
│   ├── paper-assembly/SKILL.md
│   ├── latex-writer/SKILL.md
│   ├── literature-review/SKILL.md
│   └── academic-citation/SKILL.md
├── scripts/                     # L4 确定性脚本：check_references.py
├── assets/                      # L5 模板资源：reference_rules.json 等
├── AGENTS.md / README.md / LICENSE / .gitignore
```

## 加载顺序（渐进式加载）

1. 先读 `SKILL.md` 路由表，判断任务属于哪一类。
2. **方法论决策**（检索策略 / 引文管理 / 论文组装验收）→ 读 `references/` 对应 playbook。
3. **落地具体动作**（综述 / 组装 / 排版 / 引文）→ 调 `skills/<name>/SKILL.md`。
4. **确定性自检**（BibTeX 字段/重复）→ 跑 `scripts/check_references.py`。
5. 套用 `assets/` 模板，不重复造轮子。

## 技能清单

| 环节 | 技能 | 文件 | 用途 |
|------|------|------|------|
| 写作 | paper-assembly | `skills/paper-assembly/SKILL.md` | 论文章节组装：从大纲到完整草稿 |
| 排版 | latex-writer | `skills/latex-writer/SKILL.md` | LaTeX 论文写作：编译修复、期刊格式、图表排版 |
| 综述 | literature-review | `skills/literature-review/SKILL.md` | 系统化文献综述：搜索、筛选、综合、撰写 |
| 引用 | academic-citation | `skills/academic-citation/SKILL.md` | 学术引文管理：格式校验、BibTeX 生成、完整性检查 |

## 适用场景

- 研究生/博士生撰写期刊或会议论文
- 独立研究者需要 LaTeX 排版和格式支持
- 需要进行系统化文献综述（Systematic Review / Meta-analysis）
- 管理学术引文和参考文献格式

## 技能来源

所有技能改编自 skills.sh 社区的成熟技能（安装量 ≥1K），包括 lingzhi227/agent-research-skills、bahayonghang/academic-writing-skills、affaan-m/everything-claude-code 和 yuan1z0825/nature-skills。详情见各 SKILL.md 的 source 字段。
