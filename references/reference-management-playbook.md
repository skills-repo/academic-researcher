# 引文管理手册（Reference Management Playbook）

> 子技能 `academic-citation` 给了"格式校验、BibTeX 生成、完整性检查"，但没把**不同格式的字段完整性规则、重复条目怎么判定、DOI 必填性**量化成可机器检查的清单。本篇把引文质量固化，并直接对应 `scripts/check_references.py`。

## 1. 格式选型决策

| 场景 | 格式 | 字段组织 |
|------|------|----------|
| LaTeX 投稿 | BibTeX | `@article{key, field={val}}` |
| 社科/心理 | APA | Author (Year). Title. Journal. |
| 工程/电气 | IEEE | [1] Author, "Title," Journal, Year. |
| 综合 | Chicago | 脚注或作者-年 |

**决策树**：
```
用 LaTeX 写？ → BibTeX（本脚本重点校验）
投 APA 期刊？ → 检查 author-year-title 三元齐备
投 IEEE？ → 检查 numbered 引用的顺序与字段
```

## 2. BibTeX 字段完整性规则

按条目类型要求必填字段（与 `assets/reference_rules.json` 对齐）：

| 类型 | 必填字段 |
|------|----------|
| article | author, title, journal, year |
| inproceedings | author, title, booktitle, year |
| book | author, title, publisher, year |
| misc | author, title, year |

> `doi` 强烈建议必填（审稿人常核验），但本脚本归为建议项而非阻断项。

## 3. 重复检测

两种重复必须清除：
- **键重复**：两个条目 `@article{smith2020,...}` 同 key → 编译冲突，必改。
- **标题重复**：归一化（去括号/标点/大小写）后标题相同 → 同一文献多源混入。

脚本 `bibtex` 模式会同时报这两类重复。

## 4. 常见字段错误

| 错误 | 表现 | 修正 |
|------|------|------|
| 作者格式乱 | `Smith, J. and John Doe` 混用 | 统一 `Last, First and Last, First` |
| 标题带多余大括号 | `{A {Study}}` | 仅保留必要保护括号 |
| 年份非数字 | `year = {2020?}` | `year = {2020}` |
| 期刊名缩写不一致 | 有时全称有时缩写 | 统一（按期刊要求） |
| 缺 DOI | 无法核验 | 补全 doi 字段 |

## 5. 可执行的检查命令

```bash
# 校验 .bib：字段完整性 + 重复键 + 重复标题
python3 scripts/check_references.py bibtex --file refs.bib

# 自检：校验内置资产（规则+示例 .bib）应为 0 ERROR
python3 scripts/check_references.py selfcheck
```

## 6. 典型坑与规避

| 坑 | 表现 | 规避 |
|----|------|------|
| 缺必填字段 | 编译告警/审稿挑刺 | 跑脚本卡字段 |
| 键重复 | BibTeX 编译冲突 | 跑脚本查重键 |
| 标题重复 | 综述虚胖 | 跑脚本查重标题 |
| 作者格式混 |  bibliographic 乱 | 统一 Last, First |
| 缺 DOI | 不可核验 | 补全 doi |
| 手工改 .bib | 易错漏 | 用文献管理工具导出 |

## 7. 引文检查清单

- [ ] 已跑 `check_references.py bibtex` 且 0 ERROR
- [ ] 每类条目必填字段齐全
- [ ] 无重复键、无重复标题
- [ ] 作者格式统一
- [ ] 年份为纯数字
- [ ] 关键条目含 DOI
- [ ] 期刊名缩写/全称统一
