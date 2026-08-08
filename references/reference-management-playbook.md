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

## 7. BibTeX 结构错误示例

```bibtex
% 错误：缺 journal（article 必填）
@article{smith2020, author={Smith, J.}, title={A Study}, year={2020}}

% 错误：键重复 → 编译冲突
@article{smith2020, ...}
@article{smith2020, ...}

% 错误：作者格式混用
author = {Smith, J. and John Doe}   % 后者缺 Last, First

% 正确
@article{smith2020,
  author = {Smith, John and Doe, Jane},
  title = {A Study of Attention},
  journal = {JMLR},
  year = {2020},
  doi = {10.1234/jmlr.2020.020}
}
```

## 8. 多格式对照与 DOI

| 格式 | 作者呈现 | 年份位置 | 标题 |
|------|----------|----------|------|
| BibTeX | `Last, First` | `year={}` | `title={}` |
| APA | `Last, F. (Year).` | 紧跟作者 | 句号结尾 |
| IEEE | `[n] F. Last,` | 末尾 | 引号包裹 |

DOI：关键条目必填，可用 Crossref 按标题检索补全；非 Crossref 注册的 DOI 工具无法解析属正常。

## 9. 实战：从 Zotero 到投稿级 BibTeX

1. Zotero 导入 PubMed/Scopus 的 RIS，自动去重。
2. 选中 62 篇，右键"导出 BibTeX" → `refs.bib`。
3. 跑校验：`python3 scripts/check_references.py bibtex --file refs.bib`。
4. 修复报出的缺失字段（补 journal/booktitle、补 doi）。
5. 去重：脚本报重复键/标题 → 回 Zotero 合并后再导出。
6. 终检：0 ERROR 后接入 LaTeX 的 `\bibliography{refs}`。

> 不要在 LaTeX 里手敲 `.bib`——既慢又易错，工具导出 + 脚本校验最稳。

## 10. 引文反模式（扩展）

| 反模式 | 后果 | 修正 |
|--------|------|------|
| 缺必填字段 | 编译告警/审稿挑刺 | 跑脚本卡字段 |
| 键重复 | 编译冲突 | 查重键 |
| 标题重复 | 综述虚胖 | 查重标题 |
| 作者格式混 | 著录乱 | 统一 Last, First |
| 缺 DOI | 不可核验 | 补全 |
| 手工改 .bib | 易错漏 | 工具导出 |
| 期刊名缩写乱 | 不统一 | 按刊要求 |
| 年份非数字 | 告警 | 纯数字 |
| 多余大括号 | 排版怪 | 仅必要保护 |
| 引用未列入 | 审稿质疑 | 正文与 .bib 交叉比对 |

## 11. 引文检查清单

- [ ] 已跑 `check_references.py bibtex` 且 0 ERROR
- [ ] 每类条目必填字段齐全
- [ ] 无重复键、无重复标题
- [ ] 作者格式统一
- [ ] 年份为纯数字
- [ ] 关键条目含 DOI
- [ ] 期刊名缩写/全称统一

## 12. Zotero/EndNote 实战工作流

工具导出 + 脚本校验是最稳的组合，推荐标准工作流：

1. **导入**：把各库 RIS 导入 Zotero，开启"自动去重"，先清掉跨库重复。
2. **补全**：用 Zotero 的 DOI 检索（DOI Manager）补全缺失字段（journal/booktitle/doi）。
3. **校正**：人工核对作者格式、期刊名缩写是否统一。
4. **导出**：选中目标文献，导出 BibTeX（选 UTF-8，避免中文/特殊字符乱码）。
5. **校验**：跑 `check_references.py bibtex`，修字段缺失与重复。
6. **回归**：每次新增文献后重跑校验，不让缺陷累积到投稿前才爆。

```bash
python3 scripts/check_references.py bibtex --file refs.bib
```

## 13. 字段完整性实战对照表

不同条目类型的易错字段与修正：

| 类型 | 易错/易漏字段 | 典型错误 | 修正 |
|------|--------------|----------|------|
| article | journal | 漏 journal 或写简称 | 写全称或按期刊要求缩写 |
| inproceedings | booktitle | 错写成 journal | 用会议名 |
| book | publisher | 漏出版社 | 补全 |
| misc | 无强制，但建议 author/title/year | 用 misc 逃避必填 | 尽量归到具体类型 |
| techreport | institution | 漏机构 | 补全 |
| phdthesis | school | 漏学校 | 补全 |

## 14. 多工具对比与选型

| 工具 | 强项 | 弱项 | 适用 |
|------|------|------|------|
| Zotero | 免费、跨平台、浏览器抓取 | 大体量略慢 | 多数场景首选 |
| EndNote | 期刊样式全、Word 集成好 | 贵、闭源 | 机构已购 |
| JabRef | 纯 BibTeX、轻量 | 无云同步 | LaTeX 重度用户 |
| Paperpile | 谷歌生态、协作 | 订阅制 | 团队云协作 |

选型原则：**用的人多、能导出标准 BibTeX/RIS** 优先；避免用只能导出私有格式的工具，迁移成本极高。

## 15. 引文常见误判与修正（扩展）

| 误判 | 后果 | 修正 |
|------|------|------|
| 手工敲 .bib 快 | 易错漏 | 工具导出 |
| DOI 不重要 | 不可核验 | 补全 doi |
| 缩写全称混用 | 不统一 | 按刊要求 |
| 键重复无所谓 | 编译冲突 | 脚本查重键 |
| 标题重复无所谓 | 综述虚胖 | 脚本查重标题 |
| 年份写范围 | 告警 | 纯数字年 |
| 多余大括号 | 排版怪 | 仅必要保护 |
| 引用未列入 .bib | 审稿质疑 | 正文↔.bib 交叉比对 |

## 16. 引文工作流自检清单（扩展）

- [ ] 已用文献管理工具导入并自动去重
- [ ] 已补全关键字段（journal/booktitle/doi）
- [ ] 已导出 BibTeX（UTF-8 编码）
- [ ] 已跑 `check_references.py bibtex` 且 0 ERROR
- [ ] 每类条目必填字段齐全
- [ ] 无重复键、无重复标题
- [ ] 作者格式统一（Last, First）
- [ ] 年份为纯数字
- [ ] 期刊名缩写/全称统一（按刊要求）
- [ ] 正文 `\cite` 与 .bib 交叉比对无遗漏
