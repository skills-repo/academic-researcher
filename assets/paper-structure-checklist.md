# 论文结构清单模板（Paper Structure Checklist Template）

> 复制本模板，按 IMRaD 组织你的论文章节，并在每章完成后勾选硬检查项。配合 `scripts/check_references.py` 做引文验收。

## 1. Introduction（引言）
- [ ] 痛点：研究领域为什么重要
- [ ] 空白：现有工作还差什么（research gap）
- [ ] 贡献：可数的 3 条左右具体增量（非"本文研究了…"）

## 2. Methods（方法）
- [ ] 可复现：数据 / 参数 / 环境齐全
- [ ] 伦理声明（如适用）

## 3. Results（结果）
- [ ] 只报发现，不解释意义
- [ ] 每图每表被正文引用，编号连续

## 4. Discussion（讨论）
- [ ] 回扣引言提出的问题
- [ ] 关联已有工作
- [ ] 明确局限性

## 5. Conclusion（结论）
- [ ] 一句话核心贡献
- [ ] 未来方向

## 6. 全文一致性
- [ ] 术语统一、时态统一（已完成→过去时，普适→现在时）
- [ ] 缩写首次出现写全称
- [ ] 所有 `\cite` 在 .bib 中有对应且字段完整

## 7. 引文验收

```bash
python3 scripts/check_references.py bibtex --file refs.bib
```
