#!/usr/bin/env python3
"""scaffold_paper_report.py — 论文精读报告骨架生成器（纯标准库）。

把「读一篇论文要产出的结构化报告」固化成可复现模板：给定标题/类型/来源，
生成含 claim-evidence-limitation 坐标、可复现性清单与出处声明的 Markdown 骨架。
不与源论文交互、不替你下结论，只保证每次精读落盘结构一致、可追溯。

用法:
    python3 scaffold_paper_report.py --title "..." --paper-type empirical \
        --url "https://arxiv.org/abs/2401.00001" --out note.md
    python3 scaffold_paper_report.py --title "..." --strict --json
    python3 scaffold_paper_report.py --help
"""

import argparse
import datetime as _dt
import json
import os
import sys

VALID_TYPES = ("empirical", "theoretical", "survey", "systems")
TODAY = _dt.date.today().isoformat()


def build_report(title: str, paper_type: str, url: str, authors: str) -> str:
    t = title.strip() or "(待填：论文标题)"
    a = authors.strip() or "(待填：作者 / 机构)"
    u = url.strip() or "(待填：来源链接)"
    return f"""# 精读报告：{t}

> 由 `scripts/scaffold_paper_report.py` 生成骨架（{TODAY}）。填空即可，不要删结构。
> 红线：每条实质结论落到精确锚点（论文/代码/一手来源）；推断显式标 `[推断]`。

## 基本信息
- 标题：{t}
- 作者 / 机构：{a}
- 来源：{u}
- 论文类型：`{paper_type}`
- 访问日期：{TODAY}
- 来源哈希 / 提取目录：(只读锚定，原始材料不可变)

## 研究问题
- 动机 / 待解问题：
- 核心假设 / 使能洞察：
- 与最相近工作的差异：

## 方法解剖（按承载性模块拆分）
- 模块 1：目的 / 输入 / 输出 / 关键参数 / 训练·推理角色 / 代码锚点
- 模块 2：...
> 对每个承载性模块给出 input → transform → output 的显式数据流。

## 证据脊柱（claim–evidence–limitation）
| ID | Claim（主张） | Evidence（证据/锚点） | Limitation（局限/威胁） | 标注 |
|----|--------------|----------------------|------------------------|------|
| C1 |  |  |  | 论文所述/代码已确认/推断 |

## 局限与威胁
- 失败条件 / 结果反转前提：
- 公开代码审计状态：(已确认 / 未找到公开代码 / 论文与代码不一致)

## 可复现性清单
- [ ] 环境 / 依赖声明
- [ ] 数据可用性 / 许可
- [ ] 代码仓库与版本（pinned revision）
- [ ] 超参 / 随机种子
- [ ] 评测协议与基线对齐

## 出处声明
- 本报告为结构化精读，非复现实验；未运行训练/评测。
- 所有 `[推断]` 标记处均为报告推断，非论文明示。
- 来源边界与代码审计状态如上，确定性不夸大。
"""


def validate(title: str, paper_type: str, out: str) -> list[str]:
    errors: list[str] = []
    if not title.strip():
        errors.append("title 为空")
    if paper_type not in VALID_TYPES:
        errors.append(f"paper-type 必须是 {VALID_TYPES} 之一，收到 {paper_type!r}")
    if out:
        parent = os.path.dirname(os.path.abspath(out))
        if not os.path.isdir(parent):
            errors.append(f"输出目录不存在: {parent}")
    return errors


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="scaffold_paper_report.py",
        description="生成论文精读报告的 Markdown 骨架（可追溯、结构化）。",
    )
    p.add_argument("--title", default="", help="论文标题")
    p.add_argument(
        "--paper-type",
        default="empirical",
        choices=VALID_TYPES,
        help="论文类型：empirical/theoretical/survey/systems",
    )
    p.add_argument("--url", default="", help="来源链接（arXiv/DOI/出版页）")
    p.add_argument("--authors", default="", help="作者 / 机构")
    p.add_argument("--out", default="", help="输出 Markdown 路径（默认打印到 stdout）")
    p.add_argument("--json", action="store_true", help="以 JSON 输出校验结果")
    p.add_argument(
        "--strict",
        action="store_true",
        help="校验失败时退出码 1（可做 CI 门禁）",
    )
    args = p.parse_args(argv)

    errors = validate(args.title, args.paper_type, args.out)
    if errors:
        if args.json:
            print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False))
        else:
            for e in errors:
                print(f"ERROR: {e}", file=sys.stderr)
        return 1

    report = build_report(args.title, args.paper_type, args.url, args.authors)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report)
        msg = f"已生成报告骨架: {args.out}"
        if args.json:
            print(json.dumps({"ok": True, "path": args.out}, ensure_ascii=False))
        else:
            print(msg)
    else:
        if args.json:
            print(json.dumps({"ok": True, "report": report}, ensure_ascii=False))
        else:
            sys.stdout.write(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
