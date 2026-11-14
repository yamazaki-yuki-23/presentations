#!/usr/bin/env python3
"""Slides Artifact のソース（project/ フォルダ）が、デザインの決まりを守っているかを見る。

使い方: python3 scripts/check-deck.py <deck>/project
        python3 scripts/check-deck.py --selftest

見るもの（.claude/skills/slides/SKILL.md の 2 章）:
- deck.css の --base / --accent / --sub が白地（--paper）で 9:1 以上
- 本文に ul / li を使っていない
- 1 枚の本文の行（.line、.defs の .v、表の行）が 5 を超えない
- 文字の大きさを 28px 未満に下げていない
- 題（h2）がある。表紙（h1）と章の区切り（.toc）は除く
- 1 行が長すぎて語の途中で折り返しそう（48px で 36 字、44px で 40 字を目安）
- 出典の枚（id="sources"）がある
- 話す原稿（aside）が空の枚がない

終了コード: エラーがあれば 1。
"""

import json
import re
import sys
from pathlib import Path

MIN_CONTRAST = 9.0
MAX_LINES = 5
MIN_FONT_PX = 28
# 1760px 幅で折り返さずに入る字数の目安（全角で数える）
MAX_CHARS = {48: 36, 44: 40, 40: 44, 36: 48}


def luminance(hex_color: str) -> float:
    r, g, b = (int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5))

    def lin(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(fg: str, bg: str) -> float:
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html)


def width(text: str) -> float:
    """全角を 1、半角を 0.5 として数える。"""
    return sum(0.5 if ord(ch) < 0x3000 else 1 for ch in text.strip())


def check_css(css: str) -> list[str]:
    errors = []
    colors = dict(re.findall(r"--(\w+):\s*(#[0-9a-fA-F]{6})", css))
    paper = colors.get("paper", "#ffffff")
    for name in ("base", "accent", "sub"):
        if name not in colors:
            errors.append(f"deck.css: --{name} がない")
            continue
        ratio = contrast(colors[name], paper)
        if ratio < MIN_CONTRAST:
            errors.append(f"deck.css: --{name} {colors[name]} は白地で {ratio:.1f}:1（{MIN_CONTRAST:.0f}:1 以上にする）")
    return errors


def check_slide(path: Path, html: str) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    name = path.name
    body = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)
    aside = re.search(r"<aside>(.*?)</aside>", html, flags=re.S)

    if re.search(r"<(ul|ol|li)\b", body):
        errors.append(f"{name}: ul / ol / li を使っている。.line の行に番号の目印を付ける")

    is_cover = "<h1" in body
    is_divider = 'class="toc"' in body
    if not (is_cover or is_divider) and "<h2" not in body:
        errors.append(f"{name}: 題（h2）がない")

    h2 = re.search(r"<h2[^>]*>(.*?)</h2>", body, flags=re.S)
    if h2 and h2.group(1).count("<br>") >= 2:
        warnings.append(f"{name}: 題が 3 行になる。短くする")

    rows = re.findall(r'<p class="line[^"]*"[^>]*>(.*?)</p>', body, flags=re.S)
    rows += re.findall(r'<p class="v"[^>]*>(.*?)</p>', body, flags=re.S)
    rows += re.findall(r"<tr(?![^>]*head)[^>]*>", body)
    if len(rows) > MAX_LINES:
        errors.append(f"{name}: 本文が {len(rows)} 行（{MAX_LINES} 行まで。枚を分ける）")

    for size in re.findall(r"font-size:\s*(\d+)px", body):
        if int(size) < MIN_FONT_PX:
            errors.append(f"{name}: font-size {size}px は小さすぎる（{MIN_FONT_PX}px 以上）")

    for row in re.findall(r'<p class="line( tight)?"[^>]*>(.*?)</p>', body, flags=re.S):
        tight, inner = row
        size = 44 if tight else 48
        for piece in inner.split("<br>"):
            w = width(strip_tags(piece))
            if w > MAX_CHARS[size]:
                warnings.append(f"{name}: {size}px で {w:.0f} 字の行。折り返しの恐れ: 「{strip_tags(piece).strip()[:20]}…」")

    if aside is None or not aside.group(1).strip():
        warnings.append(f"{name}: 話す原稿（aside）が空")

    return errors, warnings


def check(project: Path) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    css = project / "deck.css"
    if css.exists():
        errors += check_css(css.read_text())
    else:
        errors.append("deck.css がない")

    deck = project / "deck.json"
    order: list[str] = []
    if deck.exists():
        order = json.loads(deck.read_text()).get("order", [])
        if "sources" not in order:
            errors.append("deck.json: 出典の枚（sources）が order にない")
        for sid in order:
            if not (project / "slides" / f"{sid}.html").exists():
                errors.append(f"deck.json: {sid}.html がない")
    else:
        errors.append("deck.json がない")

    for path in sorted((project / "slides").glob("*.html")):
        e, w = check_slide(path, path.read_text())
        errors += e
        warnings += w
    return errors, warnings


def selftest() -> None:
    assert round(contrast("#7c2d12", "#ffffff"), 1) == 9.4
    assert round(contrast("#9a3412", "#ffffff"), 1) == 7.3
    assert width("全角で 36") == 4.5  # 全角 3 字 + 半角 3 字（空白と数字）× 0.5
    bad = '<section><h2>a</h2><ul><li>x</li></ul><p style="font-size:20px">y</p></section>'
    e, _ = check_slide(Path("t.html"), bad)
    assert any("ul" in m for m in e) and any("20px" in m for m in e), e
    six = "<section><h2>a</h2>" + '<p class="line">x</p>' * 6 + "<aside>n</aside></section>"
    e, _ = check_slide(Path("t.html"), six)
    assert any("6 行" in m for m in e), e
    print("selftest ok")


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[1] == "--selftest":
        selftest()
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    project = Path(argv[1])
    errors, warnings = check(project)
    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"error {e}")
    print(f"エラー {len(errors)} 件、注意 {len(warnings)} 件")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
