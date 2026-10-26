# -*- coding: utf-8 -*-
"""Sinh lại toàn bộ ảnh PNG trong diagrams/png từ nguồn .drawio.

Yêu cầu:
  - draw.io Desktop hoặc `drawio` CLI trong PATH
  - Python 3.9+

Cách dùng:
  python tools/export_drawio_to_png.py            # xuất toàn bộ
  python tools/export_drawio_to_png.py --check    # chỉ kiểm tra drawio CLI có sẵn

Ghi chú:
  File .drawio nhiều trang (multi-page) sẽ được xuất thành nhiều PNG,
  đặt tên theo thứ tự trang: <ten-file>__trang-1.png, ... .
"""
import argparse
import io
import json
import os
import shutil
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAWIO_DIR = os.path.join(REPO, "diagrams", "drawio")
PNG_DIR = os.path.join(REPO, "diagrams", "png")

# drawio CLI sẽ tìm ở các đường dẫn phổ biến trên Windows
CANDIDATES = [
    shutil.which("drawio"),
    shutil.which("draw.io"),
    r"C:\Program Files\draw.io\draw.io.exe",
    r"C:\Program Files (x86)\draw.io\draw.io.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Programs\draw.io\draw.io.exe"),
]


def find_drawio():
    for c in CANDIDATES:
        if c and os.path.exists(c):
            return c
    return None


def page_count(path):
    """Đếm số trang trong file .drawio (mxfile chứa nhiều <diagram>)."""
    import re

    with open(path, encoding="utf-8", errors="replace") as f:
        data = f.read()
    return max(1, len(re.findall(r"<diagram\b", data)))


def export_one(exe, drawio, out_png, page=0, crop=True):
    args = [
        exe,
        "--export",
        "--format",
        "png",
        "--scale",
        "2",
        "--border",
        "10",
        "--page-index",
        str(page),
        "-o",
        out_png,
    ]
    if crop:
        args.append("--crop")
    args.append(drawio)
    proc = subprocess.run(args, capture_output=True, text=True, timeout=180)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"exit={proc.returncode}")
    if not os.path.exists(out_png):
        raise RuntimeError("khong tao duoc file PNG")
    return os.path.getsize(out_png)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="chi kiem tra drawio CLI")
    ap.add_argument("--only", default=None, help="chi xuat file .drawio chua ten substring nay")
    args = ap.parse_args()

    exe = find_drawio()
    if not exe:
        print("KHONG_TIM_THAY_DRAWIO_CLI")
        print("Hay cai dat draw.io Desktop: https://www.drawio.com")
        print("Hoac them draw.io.exe vao PATH.")
        return 1
    print("drawio CLI:", exe)

    if args.check:
        return 0

    os.makedirs(PNG_DIR, exist_ok=True)
    files = sorted(f for f in os.listdir(DRAWIO_DIR) if f.endswith(".drawio"))
    if args.only:
        files = [f for f in files if args.only in f]

    ok = fail = 0
    for f in files:
        src = os.path.join(DRAWIO_DIR, f)
        base = os.path.splitext(f)[0]
        pages = page_count(src)
        for p in range(pages):
            if pages == 1:
                out = os.path.join(PNG_DIR, base + ".png")
            else:
                out = os.path.join(PNG_DIR, f"{base}__trang-{p + 1}.png")
            try:
                size = export_one(exe, src, out, page=p)
                print(f"  OK   {os.path.relpath(out, REPO)}  ({size:,} bytes)")
                ok += 1
            except Exception as e:
                print(f"  FAIL {os.path.basename(out)}: {e}")
                fail += 1

    print(f"\nXong: {ok} thanh cong, {fail} that bai")
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
