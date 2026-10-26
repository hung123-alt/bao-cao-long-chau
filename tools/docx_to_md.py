# -*- coding: utf-8 -*-
"""Chuyển đổi DOCX (báo cáo PTTKPM Long Châu) sang Markdown cho GitHub.

Giữ: tiêu đề, đoạn văn, bảng (Markdown table), hình ảnh nhúng (link tới
diagrams/png), chú thích Hình/Bảng, và danh sách.
"""
import io
import os
import re
import sys
import zipfile

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = r"C:\Users\Think P15\Downloads\bao-cao-long-chau"
DOCX = os.path.join(REPO, "docs", "BaoCao_LongChau_PTTKPM.docx")
OUT = os.path.join(REPO, "docs", "BaoCao_LongChau_PTTKPM.md")

# media file -> đường dẫn tương đối trong repo
MEDIA_MAP = {
    "image1.png": "00-logo-trang-bia.png",
    "image2.png": "01-phan-1-yeu-cau/hinh-1.1-use-case.png",
    "image3.png": "02-phan-2-phan-tich/hinh-2.1-kien-truc-muc-cao.png",
    "image4.png": "02-phan-2-phan-tich/hinh-2.2-danh-muc-san-pham.png",
    "image5.png": "02-phan-2-phan-tich/hinh-2.3-nguoi-dung-gio-hang.png",
    "image6.png": "02-phan-2-phan-tich/hinh-2.4-don-hang-thanh-toan.png",
    "image7.png": "02-phan-2-phan-tich/hinh-2.5-don-thuoc-tu-van-tra-cuu.png",
    "image8.png": "02-phan-2-phan-tich/hinh-2.6-trinh-tu-UC03.png",
    "image9.png": "02-phan-2-phan-tich/hinh-2.7-trinh-tu-UC04.png",
    "image10.png": "02-phan-2-phan-tich/hinh-2.8-trinh-tu-UC05.png",
    "image11.png": "02-phan-2-phan-tich/hinh-2.9-trinh-tu-UC06.png",
    "image12.png": "02-phan-2-phan-tich/hinh-2.10-trinh-tu-UC07.png",
    "image13.png": "02-phan-2-phan-tich/hinh-2.11-trinh-tu-UC11.png",
    "image14.png": "02-phan-2-phan-tich/hinh-2.12-trinh-tu-UC13.png",
    "image15.png": "02-phan-2-phan-tich/hinh-2.13-trinh-tu-UC22.png",
    "image16.png": "02-phan-2-phan-tich/hinh-2.14-trinh-tu-UC23.png",
    "image17.png": "02-phan-2-phan-tich/hinh-2.15-hoat-dong-UC03.png",
    "image18.png": "02-phan-2-phan-tich/hinh-2.16-hoat-dong-UC04.png",
    "image19.png": "02-phan-2-phan-tich/hinh-2.17-hoat-dong-UC05.png",
    "image20.png": "02-phan-2-phan-tich/hinh-2.18-hoat-dong-UC06.png",
    "image21.png": "02-phan-2-phan-tich/hinh-2.19-hoat-dong-UC07.png",
    "image22.png": "02-phan-2-phan-tich/hinh-2.20-hoat-dong-UC11.png",
    "image23.png": "02-phan-2-phan-tich/hinh-2.21-hoat-dong-UC22-them-sua.png",
    "image24.png": "02-phan-2-phan-tich/hinh-2.22-hoat-dong-UC22-xoa.png",
    "image25.png": "02-phan-2-phan-tich/hinh-2.23-hoat-dong-UC23-them-sua.png",
    "image26.png": "02-phan-2-phan-tich/hinh-2.24-hoat-dong-UC23-xoa.png",
    "image27.png": "02-phan-2-phan-tich/hinh-2.25-BCE-danh-muc.png",
    "image28.png": "02-phan-2-phan-tich/hinh-2.26-BCE-tim-kiem.png",
    "image29.png": "02-phan-2-phan-tich/hinh-2.27-BCE-dat-hang.png",
    "image30.png": "02-phan-2-phan-tich/hinh-2.28-BCE-quan-tri.png",
    "image31.png": "03-phan-3-thiet-ke/hinh-3.1-lop-thiet-ke-duyet-danh-muc-san-pham.png",
    "image32.png": "03-phan-3-thiet-ke/hinh-3.2-lop-thiet-ke-tim-kiem.png",
    "image33.png": "03-phan-3-thiet-ke/hinh-3.5-erd-phan-1-3-cum-a-b.png",
    "image34.png": "03-phan-3-thiet-ke/hinh-3.4-wireframe-giao-dien.png",
    "image35.png": "03-phan-3-thiet-ke/hinh-3.6-ui-dat-hang.png",
    "image36.png": "03-phan-3-thiet-ke/hinh-3.7-ui-thanh-toan.png",
}


def media_map():
    """Đọc relationship của DOCX để map rId -> tên media thật."""
    z = zipfile.ZipFile(DOCX)
    rels = z.read("word/_rels/document.xml.rels").decode("utf-8", "replace")
    return dict(re.findall(r'Id="([^"]+)"[^>]*Target="media/([^"]+)"', rels))


def esc(text):
    text = text.replace("|", "\\|")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def table_to_md(tbl):
    rows = []
    for row in tbl.rows:
        cells = []
        seen = set()
        for cell in row.cells:
            if id(cell._tc) in seen:
                cells.append("")
                continue
            seen.add(id(cell._tc))
            cells.append(esc(cell.text))
        rows.append(cells)
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |"]
    out.append("| " + " | ".join(["---"] * width) + " |")
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def iter_block_items(parent):
    from docx.oxml.ns import qn

    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def main():
    rmap = media_map()
    doc = Document(DOCX)
    parts = []
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            md = table_to_md(block)
            if md:
                parts.append(md)
                parts.append("")
            continue
        text = block.text.strip()
        # hình ảnh nhúng
        blips = block._p.findall(
            ".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip"
        )
        if blips:
            for blip in blips:
                rid = blip.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                )
                media = rmap.get(rid)
                if not media:
                    continue
                rel = MEDIA_MAP.get(media)
                if rel:
                    parts.append(f"![{media}](../diagrams/png/{rel})")
                    parts.append("")
        if not text:
            continue
        style = (block.style.name or "").lower()
        if style.startswith("heading"):
            m = re.search(r"(\d+)", style)
            level = int(m.group(1)) if m else 2
            level = max(1, min(level, 6))
            parts.append("#" * level + " " + text)
            parts.append("")
        elif re.match(r"^(Hình|Bảng)\s*\d", text):
            parts.append(f"**{text}**")
            parts.append("")
        elif re.match(r"^[-•]\s*|^\+\s*", text):
            parts.append("- " + re.sub(r"^[-•+]\s*", "", text))
        elif text.startswith("–") or text.startswith("—"):
            parts.append("- " + text.lstrip("–— "))
        else:
            parts.append(text)
        parts.append("")

    md = "\n".join(parts)
    md = re.sub(r"\n{3,}", "\n\n", md)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"DA_TAO_MD: {OUT}  ({len(md):,} ky tu, {md.count(chr(10))+1} dong)")
    print(f"  so bang: {md.count('| ---')}, so anh: {md.count('![')}")


if __name__ == "__main__":
    main()
