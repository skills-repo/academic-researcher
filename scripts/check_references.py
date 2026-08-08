#!/usr/bin/env python3
"""check_references.py — 参考文献格式检查器（纯标准库，零依赖）

检查 BibTeX 文献库（.bib）的字段完整性与重复条目：
  bibtex   校验每类条目的必填字段、重复键、重复标题
  selfcheck 校验内置资产（规则配置 + 示例 .bib）应为 0 ERROR

规则来源：assets/reference_rules.json（配置驱动）。以 `_` 开头的键为注释，加载时跳过。

特性：纯标准库、带 --help、确定性可复现、不联网、只读不修改被检文件。

用法:
  python3 check_references.py bibtex --file refs.bib
  python3 check_references.py selfcheck
  python3 check_references.py --help
"""
import argparse
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_RULES = os.path.join(_HERE, "..", "assets", "reference_rules.json")
_DEFAULT_EXAMPLE = os.path.join(_HERE, "..", "assets", "sample_references.bib")


def _load_rules(path):
    errors = []
    if not os.path.isfile(path):
        return {}, [f"规则配置不存在: {path}"]
    try:
        with open(path, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return {}, [f"规则配置解析失败: {exc}"]
    if not isinstance(raw, dict):
        return {}, ["规则配置根必须是 JSON 对象"]
    rules = {k: v for k, v in raw.items() if not k.startswith("_")}
    rf = rules.get("required_fields_by_type")
    if not isinstance(rf, dict) or not rf:
        errors.append("required_fields_by_type 必须是非空对象")
    else:
        for t, fs in rf.items():
            if not isinstance(fs, list):
                errors.append(f"类型 {t} 的必填字段必须是数组")
    if not isinstance(rules.get("detect_duplicate_title"), bool):
        errors.append("detect_duplicate_title 必须是布尔")
    return rules, errors


def _parse_bib(text):
    entries = []
    i, n = 0, len(text)
    while i < n:
        if text[i] == "@":
            j = i + 1
            while j < n and text[j] not in " \t\n{":
                j += 1
            etype = text[i + 1:j].strip().lower()
            if j < n and text[j] == "{":
                k = j + 1
                while k < n and text[k] not in ",}":
                    k += 1
                key = text[j + 1:k].strip()
                if text[k] == "}":
                    body, close = "", k
                else:
                    depth, p = 1, k
                    while p < n and depth > 0:
                        if text[p] == "{":
                            depth += 1
                        elif text[p] == "}":
                            depth -= 1
                        p += 1
                    close = p - 1
                    body = text[k + 1:close]
                entries.append({"type": etype, "key": key, "fields": _parse_fields(body)})
                i = close + 1
                continue
        i += 1
    return entries


def _parse_fields(body):
    fields, depth, cur, parts = {}, 0, "", []
    for ch in body:
        if ch == "{":
            depth += 1
            cur += ch
        elif ch == "}":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    for part in parts:
        if "=" in part:
            name, _, val = part.partition("=")
            name = name.strip().lower()
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "{}":
                val = val[1:-1]
            fields[name] = val
    return fields


def _norm(s):
    s = s.lower().replace("{", "").replace("}", "")
    s = re.sub(r"[^a-z0-9 ]", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _check_bib(text, rules):
    errors = []
    rf = rules.get("required_fields_by_type", {})
    detect_dup = rules.get("detect_duplicate_title", True)
    entries = _parse_bib(text)
    seen_keys, seen_titles = {}, {}
    for e in entries:
        label = f"@{e['type']}{{{e['key']}}}"
        if e["key"] in seen_keys:
            errors.append(f"重复键: {label}（首次出现在 {seen_keys[e['key']]}）")
        else:
            seen_keys[e["key"]] = label
        req = rf.get(e["type"], [])
        for f in req:
            val = e["fields"].get(f, "")
            if not val.strip():
                errors.append(f"字段缺失: {label} 缺必填字段 '{f}'")
        title = e["fields"].get("title", "")
        if detect_dup and title.strip():
            nt = _norm(title)
            if nt in seen_titles:
                errors.append(f"重复标题: {label} 与 {seen_titles[nt]} 标题归一化相同")
            else:
                seen_titles[nt] = label
    return errors


def _read_file_or_die(path):
    if not os.path.isfile(path):
        sys.stderr.write(f"[ERROR] 文件不存在: {path}\n")
        sys.exit(2)
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def main(argv=None):
    ap = argparse.ArgumentParser(description="参考文献格式检查器（bibtex / selfcheck）")
    ap.add_argument("--rules", default=_DEFAULT_RULES, help="规则配置 JSON 路径")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_b = sub.add_parser("bibtex", help="校验 BibTeX 文献库")
    p_b.add_argument("--file", required=True, help=".bib 文件路径")

    sub.add_parser("selfcheck", help="校验内置资产（规则+示例 .bib）应为 0 ERROR")

    args = ap.parse_args(argv)

    if args.cmd == "selfcheck":
        rules, rerr = _load_rules(args.rules)
        print(f"[selfcheck] 规则 {os.path.relpath(args.rules)} : "
              f"{'OK' if not rerr else rerr}")
        ex_err = _check_bib(_read_file_or_die(_DEFAULT_EXAMPLE), rules) if os.path.isfile(_DEFAULT_EXAMPLE) else ["示例 .bib 缺失"]
        print(f"[selfcheck] 示例 .bib {os.path.relpath(_DEFAULT_EXAMPLE)} : "
              f"{'0 ERROR' if not ex_err else ex_err}")
        total = len(rerr) + len(ex_err)
        if total == 0:
            print("[selfcheck] PASS — 资产与脚本互相验证通过（0 ERROR）")
            return 0
        print(f"[selfcheck] FAIL — 共 {total} 项错误")
        return 1

    rules, rerr = _load_rules(args.rules)
    if rerr:
        for e in rerr:
            sys.stderr.write(f"[ERROR] {e}\n")
        return 2

    if args.cmd == "bibtex":
        errs = _check_bib(_read_file_or_die(args.file), rules)
        if errs:
            for e in errs:
                print(f"ERROR: {e}")
            print(f"\n参考文献检查未通过：{len(errs)} 项")
            return 1
        print("参考文献检查通过：0 ERROR")
        return 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
