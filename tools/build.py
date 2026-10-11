"""把 src/index.src.html 建成可離線使用的單一 index.html。

1. 「字[ㄓㄨㄛˊ]」標記 → 字 + IVS 選擇子（依字咍注音標楷的讀音順序）。
2. 列出沒有標記、但字型有多個讀音的字，方便人工確認預設讀音。
3. 只取用到的字，裁出字型子集，以 base64 WOFF 內嵌。

用法：python tools/build.py [來源.src.html 輸出.html]
"""
import base64
import io
import re
import sys
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 2 else ROOT / "src" / "index.src.html"
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "index.html"
FONT = ROOT / "fonts" / "BpmfZihiKaiStd-Regular.ttf"
TABLE = ROOT / "fonts" / "phonic_table.txt"

CREDIT = (
    "<!--\n"
    "  字型：字嗨注音標楷 BpmfZihiKaiStd（But Ko，https://github.com/ButTaiwan/bpmfvs）\n"
    "  漢字部分 CC BY 4.0；漢字以外 SIL OFL 1.1；注音 IVS 規格 Apache 2.0。\n"
    "  內含全字庫正楷體：國家發展委員會 2018 CNS11643中文標準交換碼全字庫 Ver 103.1。\n"
    "  本檔僅內嵌此頁用到的字（子集化）。\n"
    "-->\n"
)


def load_readings():
    readings = {}
    for line in TABLE.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) >= 4:
            readings.setdefault(parts[0], parts[3:])
    return readings


def is_han(ch):
    cp = ord(ch)
    return 0x3400 <= cp <= 0x9FFF or 0x20000 <= cp <= 0x2FFFF or 0xF900 <= cp <= 0xFAFF


def main():
    readings = load_readings()
    # Windows 終端機預設 cp950，印不出注音 IVS 選擇子，統一改用 UTF-8 輸出
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    src = SRC.read_text(encoding="utf-8")
    errors = []

    def mark(m):
        ch, zy = m.group(1), m.group(2)
        opts = readings.get(ch)
        if not opts or zy not in opts:
            errors.append(f"{ch}[{zy}] 不在讀音表中：{opts}")
            return ch
        idx = opts.index(zy)
        return ch if idx == 0 else ch + chr(0xE01E0 + idx)

    html = re.sub(r"(.)\[([ㄅ-ㄩˊˇˋ˙]+)\]", mark, src)
    if errors:
        sys.exit("\n".join(errors))

    # 只看畫面文字：拿掉 <style>/<script> 內容與標籤本身（屬性值保留，aria-label 也要有字形）
    visible = re.sub(r"<(style|script)\b.*?</\1>", "", html, flags=re.S)
    visible = re.sub(r"<!--.*?-->", "", visible, flags=re.S)
    script_text = "".join(re.findall(r"<script\b.*?</script>", html, flags=re.S))
    text = visible + "".join(re.findall(r'"([^"\n]*)"', script_text))

    chars = sorted({c for c in text if ord(c) > 0x7F and not 0xE0100 <= ord(c) <= 0xE01EF})
    poly = []
    for i, c in enumerate(text):
        if is_han(c) and len(readings.get(c, [])) > 1:
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if not 0xE01E0 <= ord(nxt or " ") <= 0xE01EF:
                poly.append((c, readings[c][0], text[max(0, i - 4): i + 5].replace("\n", " ")))
    seen = set()
    print("== 未標記的多音字（使用預設讀音） ==")
    for c, zy, ctx in poly:
        key = (c, ctx)
        if key not in seen:
            seen.add(key)
            print(f"  {c} {zy:<6} …{ctx}…")

    # 字型子集
    font = TTFont(FONT)
    opts = subset.Options()
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    opts.flavor = "woff"
    opts.with_zopfli = False
    unicodes = {ord(c) for c in chars} | set(range(0x20, 0x7F)) | set(range(0xE01E0, 0xE01F0))
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=unicodes)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff"
    font.save(buf)
    data = base64.b64encode(buf.getvalue()).decode("ascii")

    missing = [c for c in chars if ord(c) not in TTFont(FONT).getBestCmap()]
    if missing:
        print("== 字型沒有的字 ==", "".join(missing))

    html = html.replace("/*FONT_DATA*/", data, 1)
    html = html.replace("<!doctype html>\n", "<!doctype html>\n" + CREDIT, 1)
    OUT.write_text(html, encoding="utf-8", newline="\n")
    print(f"字數 {len(chars)}，字型 {len(buf.getvalue()) // 1024} KB，輸出 {OUT.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
