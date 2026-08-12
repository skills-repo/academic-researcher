# 论文自动化 Playbook（增量方法论）

> 本 playbook 是 `skills/paper-automation/` 的深层指南：如何把「读一篇论文」变成可追溯、可复现的流水线，并把多轮精读沉淀为能喂给综述与自动研究的标注库。
> 它不重复子技能的能力描述，只给**决策树 + 命令 + 踩坑 + 检查清单**。

## 1. 决策树：先做哪一种

```
收到一篇论文 / 一个主题
│
├─ 输入是一篇具体论文（PDF / arXiv / DOI / URL / 全文）？
│   └─ 是 → 走【A. 单篇精读 xray】
│
├─ 输入是一个主题 + 若干种子论文，要扩展综述草稿？
│   └─ 是 → 走【B. 自动研究循环 autoresearch】
│
└─ 还不确定要什么？
    └─ 问一次：「精读这篇（出报告）」还是「围绕主题扩综述」？不要默认后者。
```

- **A. 单篇精读 xray**：目标是「准确读懂这一篇」，产物是一份可追溯报告。
- **B. 自动研究循环 autoresearch**：目标是「围绕主题累积带出处的知识」，产物是不断生长的综述骨架 + 标注库。

两者共用同一套 claim–evidence–limitation 坐标与出处规则；B 在 A 之上叠加「去重 + 归类 + 趋势辨析」。

## 2. 命令（输入锚定）

### 2.1 拿到论文文本

优先用 PDF（页码/图锚稳定），但不强制：

```bash
# 本地/远程 PDF → 抽取带页码锚的文本（按需，依赖 pymupdf4llm）
uv run --isolated --no-project --with pymupdf4llm==1.28.0 \
  python <skill-dir>/scripts/extract_paper.py PAPER.pdf EXTRACTED_DIR

# arXiv：直接取官方 HTML 或 PDF
#   https://arxiv.org/abs/<id>  →  https://arxiv.org/pdf/<id>
#   https://arxiv.org/html/<id>  （官方 HTML，锚更稳定）

# DOI / 出版页：用官方 full-text HTML；无则 PDF。记录链接与访问日期作出处。
```

**不可变原则**：原始材料只读不改；抽取产物另存目录，原始 PDF 不删。

### 2.2 起报告骨架（本仓库脚本，纯标准库）

```bash
python3 scripts/scaffold_paper_report.py \
  --title "论文标题" --paper-type empirical \
  --url "https://arxiv.org/abs/2401.12345" \
  --out reading-notes/2026-0812-<slug>.md
```

生成的结构化 Markdown 骨架含：基本信息、研究问题、方法解剖、claim–evidence–limitation 表、可复现性清单、出处声明。填空即可，不重复排版。

### 2.3 校验引文（复用现有脚本）

精读中引用的条目想顺手 lint：

```bash
python3 scripts/check_references.py bibtex --file refs.bib
```

## 3. 论文类型分支（先判再做）

| 类型 | 主分支关注 | 易错 |
|------|-----------|------|
| Empirical | 方法模块解剖、基线/消融、失败条件 | 把相关性当因果；漏掉失败 case |
| Theoretical | 定理/证明链条、假设边界 | 跳读证明直接信结论 |
| Survey | 分类法轴是否有意义、覆盖偏差 | 列论文清单而非机制家族 |
| Systems | 系统边界、实现、benchmark 协议 | 忽略部署/规模前提 |

跨类型论文只取**一个**主分支，必要时补一个同名次级模块；不要开 `hybrid` 第五类兜底。

## 4. 只读代码审计（有则必做）

官方有公开代码时，**固定一个 revision 只读核对**：模块接口、张量/数据形状、默认值、数据管线、训练 schedule、推理路径。

- 不安装依赖、不 import 项目、不跑训练/评测。
- 每条实现陈述标为：`论文所述` / `代码已确认` / `论文与代码不一致` / `报告推断`。
- 找不到权威实现 → 显式写「未找到公开代码」，绝不静默换成非官方仓库。

## 5. 踩坑清单（红线）

1. **把推断写成事实**：每处 `[推断]` 必须可见，且落到精确锚点。
2. **臆造公式/指标/图表**：无原始结果图时标记 `data-original-result-unavailable`，保留原表。
3. **跳过代码审计**：有公开代码却不核对，等于放弃一手证据。
4. **出处丢失**：报告里每句实质结论都要能回到论文/代码/一手来源。
5. **趋势与预测混谈**：autoresearch 中区分「语料观察到的趋势」与「作者预测」。
6. **复现当精读**：本工作流不跑复现实验；复现是另一件事。
7. **覆盖偏差无视**：survey 要检查 cutoff 日期、venue/语言选择是否 bias 了趋势。

## 6. 交付前检查清单

- [ ] 输出格式已定（Markdown / HTML），未默认选择
- [ ] 来源哈希/链接/访问日期已记录，原始材料未改
- [ ] 论文主类型已判定并有证据
- [ ] 完整论证（含相关附录）已读，claim–evidence–limitation 坐标齐
- [ ] 有公开代码时已完成只读审计并标注状态
- [ ] 每条实质结论可回溯到精确锚点，推断显式标注
- [ ] 局限与威胁和头条结论一样易查
- [ ] HTML：校验器通过、静态公式渲染、移动端可读
- [ ] autoresearch：种子去重、分类轴有意义、趋势/预测分离、出处锚点齐全
