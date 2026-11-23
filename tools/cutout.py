"""把 Gemini 生的綠幕（或洋紅幕）圖去背、裁切、縮圖，存成素材清單規格的透明 WebP。

用法：
  python tools/cutout.py 輸出資料夾 名稱=原圖.jpg [名稱=原圖.jpg ...]
  python tools/cutout.py 共用/圖 人-甲-笑+人-甲-愁=笑.jpg+愁.jpg     （換圖配對：用同一個裁切框，疊起來不會跳）
  加 --magenta：背景是 #FF00FF（主體本身是鮮綠色時用）

名稱以「人」開頭 → 高 1200px；其餘 → 長邊 800px。只保留最大的連通塊，雜點和分離的小東西會被清掉。
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def key(path, magenta):
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    d = np.minimum(r, b) - g if magenta else g - np.maximum(r, b)
    alpha = 1 - np.clip((d - 30) / 90, 0, 1)
    al = Image.fromarray((alpha * 255).astype("uint8"))
    al = al.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.7))
    # 只在邊緣附近去溢色，主體內部的顏色不動
    near = np.asarray(al.filter(ImageFilter.MinFilter(15))) < 250
    if magenta:
        spill = np.maximum(d, 0)
        r, b = np.where(near, r - spill, r), np.where(near, b - spill, b)
    else:
        g = np.where(near, np.minimum(g, np.maximum(r, b)), g)
    al = np.asarray(al).copy()
    al[al < 12] = 0
    al = np.minimum(al, biggest(al))
    return Image.fromarray(np.dstack([r, g, b, al]).clip(0, 255).astype("uint8"), "RGBA")


def biggest(al):
    """最大連通塊的遮罩（略微外擴，保留柔邊）。"""
    h, w = al.shape
    small = Image.fromarray(((al > 40) * 255).astype("uint8")).resize((w // 4, h // 4), Image.BOX)
    small = small.point(lambda v: 255 if v > 127 else 0)
    found = []
    for k in range(1, 255):
        ys, xs = np.where(np.asarray(small) == 255)
        if not len(xs):
            break
        ImageDraw.floodfill(small, (int(xs[0]), int(ys[0])), k)
        found.append((int((np.asarray(small) == k).sum()), k))
    keep = np.asarray(small) == max(found)[1]
    return np.asarray(Image.fromarray((keep * 255).astype("uint8")).resize((w, h), Image.NEAREST).filter(ImageFilter.MaxFilter(13)))


def shrink(im, size):
    """預乘透明度再縮圖，邊緣才不會帶到背景色。"""
    a = np.asarray(im).astype(np.float32)
    pm = np.dstack([a[..., :3] * a[..., 3:] / 255, a[..., 3:]]).round().astype("uint8")
    p = np.asarray(Image.fromarray(pm, "RGBA").resize(size, Image.LANCZOS)).astype(np.float32)
    pa = p[..., 3:] / 255
    rgb = np.where(pa > 0, p[..., :3] / np.maximum(pa, 1e-3), 0).clip(0, 255)
    return Image.fromarray(np.dstack([rgb, p[..., 3:]]).round().astype("uint8"), "RGBA")


def main(args):
    magenta = "--magenta" in args
    args = [x for x in args if x != "--magenta"]
    if len(args) < 2:
        sys.exit(__doc__)
    out = args[0]
    os.makedirs(out, exist_ok=True)
    for spec in args[1:]:
        names, files = (s.split("+") for s in spec.split("=", 1))
        assert len(names) == len(files), spec
        ims = [key(f, magenta) for f in files]
        boxes = [im.getchannel("A").point(lambda v: 255 if v > 60 else 0).getbbox() for im in ims]
        box = (min(b[0] for b in boxes) - 12, min(b[1] for b in boxes) - 12, max(b[2] for b in boxes) + 12, max(b[3] for b in boxes) + 12)
        for name, im, bx in zip(names, ims, boxes):
            im = im.crop(box)
            q = 1200 / im.height if name.startswith("人") else 800 / max(im.size)
            limit = 150 if name.startswith("人") else 80
            im = shrink(im, (round(im.width * q), round(im.height * q)))
            path = os.path.join(out, name + ".webp")
            for quality in (86, 80, 74, 66):
                im.save(path, quality=quality, method=6)
                kb = os.path.getsize(path) / 1024
                if kb <= limit:
                    break
            print(f"{path} {im.size} {kb:.0f} KB（上限 {limit}）外框 {bx}")


if __name__ == "__main__":
    main(sys.argv[1:])
