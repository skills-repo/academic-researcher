# 文献检索策略手册（Literature Search Strategy）

> 子技能 `literature-review` 给了"搜索策略模板"和 PRISMA 流程，但没回答**数据库怎么选、布尔式怎么搭、什么时候该停、重复文献怎么去**。本篇把检索从"随便搜搜"变成可复现、可审计的策略。

## 1. 数据库选型矩阵

| 研究方向 | 首选库 | 补充库 | 理由 |
|----------|--------|--------|------|
| 医学/生物 | PubMed / MEDLINE | Cochrane, Web of Science | 学科权威、循证强 |
| 综合/理工 | Web of Science / Scopus | Google Scholar | 引文网络全 |
| 计算机 | DBLP / arXiv / ACM DL | Google Scholar | 预印本快、覆盖全 |
| 社科 | Scopus / SSRN | Google Scholar | 工作论文多 |

> 不要只用一个库——单一库漏检率高。至少 2 个互补库交叉。

## 2. 布尔式搭建（PICO 驱动）

用 PICO 把研究问题拆成维度，再映射布尔：

```
P (Population)  →  (adolescent OR teenager OR "young adult")
I (Intervention)→  AND (CBT OR "cognitive behavioral")
C (Comparison)  →  AND (medication OR "treatment as usual")
O (Outcome)     →  AND (relapse OR remission)
```

规则：
- OR 用于同义/近义扩展，用括号分组：`(A OR B)`
- AND 用于维度连接
- NOT 慎用——会误删相关文献（如排除 "children" 可能漏掉 "adolescents"）
- 短语用引号 `"cognitive behavioral"` 避免词序错位

## 3. 滚雪球（Snowballing）

检索饱和后做两层滚雪球：
- **向后滚雪球**：读入选文献的参考文献列表，找被引的关键文献
- **向前滚雪球**：用引文追踪（Google Scholar "被引用"）找后续引用文献

停止条件：连续两轮滚雪球无新增高相关文献 → 检索饱和。

## 4. 去重决策

同文献可能以不同元数据出现在多库。判定重复：
- 强信号：DOI 相同 → 必重
- 中信号：作者+标题归一化相同 → 必重
- 弱信号：仅年份/卷期不同 → 人工核对

去重在导入文献管理工具（Zotero/EndNote）后做，或用脚本（见 `reference-management-playbook.md` 的重复检测）。

## 5. 可执行的检索辅助命令

```bash
# 导出检索结果后统计各库命中数（评估覆盖）
for db in pubmed scopus; do echo "$db: $(wc -l < $db.ris)"; done

# 用本仓库脚本检测 .bib 中的重复条目
python3 scripts/check_references.py bibtex --file refs.bib
```

## 6. 典型坑与规避

| 坑 | 表现 | 规避 |
|----|------|------|
| 只用 Google Scholar | 漏检、重复多 | ≥2 互补库交叉 |
| 滥用 NOT | 误删相关文献 | 仅在明确排除时用 |
| 布尔不分括号 | 逻辑错乱 | 每个 OR 组加括号 |
| 不滚雪球 | 关键文献缺失 | 饱和后向后+向前滚 |
| 检索无时间窗 | 噪声大 | 设合理年限（如 2018-2026） |
| 重复文献混入选集 | 综述虚胖 | 导入后去重 |

## 7. 检索策略检查清单

- [ ] 已按领域选 ≥2 个互补数据库
- [ ] 布尔式按 PICO 搭建，OR 组加括号
- [ ] 设了时间窗与文献类型过滤
- [ ] 已跑检索并导出结果
- [ ] 已去重（DOI/标题归一化）
- [ ] 已滚雪球至饱和（连续两轮无新增）
- [ ] 已跑 `check_references.py bibtex` 查重与字段完整性
