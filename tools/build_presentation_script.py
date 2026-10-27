"""
Sinh file Word "Kịch bản thuyết trình" cho đồ án PTTKPM Nhà thuốc FPT Long Châu.

Nguồn: slides/PROMPT_TAO_SLIDE_LONG_CHAU.md (30 slide, mỗi slide có phần
nội dung hiển thị + SPEAKER NOTES).

Đầu ra: docs/KICH_BAN_THUYET_TRINH.docx

Cách dùng:
    python tools/build_presentation_script.py
"""

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "slides" / "PROMPT_TAO_SLIDE_LONG_CHAU.md"
OUT = ROOT / "docs" / "KICH_BAN_THUYET_TRINH.docx"

NAVY = RGBColor(0x10, 0x36, 0x7A)
BLUE = RGBColor(0x0F, 0x62, 0xFE)
GRAY = RGBColor(0x5A, 0x64, 0x72)
ORANGE = RGBColor(0xFF, 0x8A, 0x00)

SLIDE_W = Cm(33.87)  # 16:9 khổ A4 ngang
SLIDE_H = Cm(19.05)


# --------------------------------------------------------------------------
# Parse
# --------------------------------------------------------------------------
def parse_prompt_file(text: str):
    """Tách file prompt thành danh sách slide: (num, title, body, notes)."""
    slides = []
    for chunk in re.split(r"\n#\s+", text):
        chunk = chunk.strip()
        m = re.match(r"PROMPT SLIDE\s+(\d+)\s*[–\-—]\s*(.+)", chunk)
        if not m:
            continue
        num = int(m.group(1))
        title = m.group(2).strip().strip("`").strip()

        # body = phần trong ```text ... ``` trước SPEAKER NOTES
        body, notes = "", ""
        code = re.search(r"```text\s*(.*?)```", chunk, re.S)
        block = code.group(1) if code else chunk
        mn = re.search(r"SPEAKER NOTES:\s*\n(.*)", block, re.S)
        if mn:
            body = block[: mn.start()].rstrip()
            notes = mn.group(1).strip().strip('"').strip()
        else:
            body = block.strip()

        slides.append((num, title, clean(body), clean(notes)))
    return slides


def clean(s: str) -> str:
    s = s.replace("\r", "")
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def strip_assets(paths_text: str):
    """Trả về (text đã thay đường dẫn, danh sách tên file ảnh)."""
    found = []

    def repl(m):
        found.append(m.group(0))
        return m.group(0).replace(
            "C:\\Users\\Think P15\\Downloads\\SlideAssets\\", "SlideAssets/"
        )

    text = re.sub(
        r"C:\\Users\\Think P15\\Downloads\\SlideAssets\\[^\s`\)]+", repl, paths_text
    )
    # bỏ dấu backtick thừa quanh đường dẫn
    text = text.replace("`SlideAssets/", "SlideAssets/").replace(".png`", ".png")
    return text, found


# --------------------------------------------------------------------------
# DOCX helpers
# --------------------------------------------------------------------------
def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


def style_run(run, size=11, bold=False, color=None, font="Segoe UI", italic=False):
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    rfonts.set(qn("w:ascii"), font)
    rfonts.set(qn("w:hAnsi"), font)
    return run


def add_para(doc, text="", size=11, bold=False, color=None, align=None,
             space_after=6, space_before=0, italic=False, indent=None,
             font="Segoe UI", line=1.35):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    pf.line_spacing = line
    if align is not None:
        p.alignment = align
    if indent is not None:
        pf.left_indent = Cm(indent)
    if text:
        style_run(p.add_run(text), size, bold, color, font, italic)
    return p


def add_rich(doc, segments, size=11, space_after=6, space_before=0, indent=None,
             line=1.35):
    """segments: list of (text, bold, color)"""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    pf.line_spacing = line
    if indent is not None:
        pf.left_indent = Cm(indent)
    for text, bold, color in segments:
        style_run(p.add_run(text), size, bold, color)
    return p


def add_rule(doc, color="DDE3EA", size=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.space_before = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:color"), color)
    pbdr.append(bottom)
    pPr.append(pbdr)
    return p


def add_callout(doc, label, text, fill="F5F8FC", border="DDE3EA", label_color=NAVY):
    """Bảng 1 ô dùng như khung ghi chú."""
    t = doc.add_table(rows=1, cols=1)
    t.autofit = False
    t.columns[0].width = Cm(31.0)
    cell = t.cell(0, 0)
    cell.width = Cm(31.0)
    set_cell_bg(cell, fill)

    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "6")
        e.set(qn("w:color"), border)
        borders.append(e)
    tcPr.append(borders)

    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    style_run(p.add_run(label), 9, True, label_color)

    for line_text in text.split("\n"):
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_after = Pt(2)
        p2.paragraph_format.line_spacing = 1.3
        style_run(p2.add_run(line_text), 10, False, GRAY)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t


def speaker_words(text: str) -> int:
    return len(re.findall(r"\S+", text))


# --------------------------------------------------------------------------
# Build
# --------------------------------------------------------------------------
def build():
    text = SRC.read_text(encoding="utf-8")
    slides = parse_prompt_file(text)

    doc = Document()

    # --- thiết lập trang ngang, khổ 16:9 ---
    sec = doc.sections[0]
    sec.page_width = SLIDE_W
    sec.page_height = SLIDE_H
    sec.left_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)
    sec.top_margin = Cm(1.6)
    sec.bottom_margin = Cm(1.4)

    normal = doc.styles["Normal"]
    normal.font.name = "Segoe UI"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Segoe UI")

    total_words = sum(speaker_words(s[3]) for s in slides)
    minutes = total_words / 130  # tốc độ nói ~130 từ/phút

    # ================= BÌA =================
    add_para(doc, "ĐẠI HỌC PHENIKAA · TRƯỜNG CÔNG NGHỆ THÔNG TIN",
             11, True, RGBColor(0xFF, 0xFF, 0xFF), space_after=4)
    add_para(doc, "KỊCH BẢN THUYẾT TRÌNH", 34, True, RGBColor(0xFF, 0xFF, 0xFF),
             space_after=2)
    add_para(doc,
             "Đồ án Phân tích và Thiết kế Phần mềm (PTTKPM) — "
             "Hệ thống Website Nhà thuốc FPT Long Châu",
             17, False, RGBColor(0xFF, 0xFF, 0xFF), space_after=10)
    add_rule(doc, "FFFFFF", 8)
    add_para(doc,
             f"30 slide · {len(slides)} phần trình bày · "
             f"khoảng {minutes:.0f} phút nói + hỏi đáp",
             12, False, RGBColor(0xFF, 0xFF, 0xFF), space_after=4)
    add_para(doc, "Giảng viên hướng dẫn: TS. Trương Đức Phương",
             12, False, RGBColor(0xFF, 0xFF, 0xFF), space_after=2)
    add_para(doc, "Khảo sát thực tế: 10/2026 · Học kỳ 2026",
             12, False, RGBColor(0xFF, 0xFF, 0xFF), space_after=2)
    add_para(doc, "Kịch bản chi tiết theo từng slide — kèm nội dung hiển thị, "
                  "lời dẫn và gợi ý trả lời câu hỏi.",
             11, False, RGBColor(0xD8, 0xE2, 0xF2), space_before=8)

    # nền bìa xanh đậm
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), "10367A")
    doc.sections[0]._sectPr.append(shd)

    doc.add_page_break()

    # ================= MỤC LỤC =================
    add_para(doc, "MỤC LỤC TRÌNH BÀY", 20, True, NAVY, space_after=4)
    add_rule(doc, "0F62FE", 12)
    add_para(doc, "Tổng thời lượng dự kiến: "
                  f"{minutes:.0f} phút thuyết trình + 10–15 phút hỏi đáp.",
             11, False, GRAY, space_after=10)

    table = doc.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    widths = [Cm(1.6), Cm(11.5), Cm(13.0), Cm(4.9)]
    hdr = table.rows[0]
    for i, (txt, w) in enumerate(zip(
            ["#", "Tiêu đề slide", "Nội dung trọng tâm", "Thời lượng"], widths)):
        cell = hdr.cells[i]
        cell.width = w
        set_cell_bg(cell, "0F62FE")
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(2)
        style_run(p.add_run(txt), 10, True, RGBColor(0xFF, 0xFF, 0xFF))
    set_repeat_header(hdr)

    for num, title, body, notes in slides:
        row = table.add_row()
        words = speaker_words(notes)
        dur = max(1, round(words / 130))
        cells = row.cells
        for i, w in enumerate(widths):
            cells[i].width = w
        vals = [str(num), title, summary_of(body), f"{dur}′"]
        for i, v in enumerate(vals):
            p = cells[i].paragraphs[0]
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.space_before = Pt(1)
            style_run(p.add_run(v), 9.5, i == 1,
                      NAVY if i == 1 else GRAY)

    doc.add_page_break()

    # ================= CÁC SLIDE =================
    for idx, (num, title, body, notes) in enumerate(slides):
        body, assets = strip_assets(body)
        notes, _ = strip_assets(notes)

        # header dải
        add_para(doc, f"SLIDE {num:02d} / 30", 9, True, ORANGE, space_after=0)
        add_para(doc, title, 19, True, NAVY, space_after=2)
        add_rule(doc, "0F62FE", 12)

        words = speaker_words(notes)
        add_rich(doc, [
            ("Thời lượng ước tính: ", True, NAVY),
            (f"{max(1, round(words / 130))} phút  ", False, GRAY),
            (f"({words} từ)  ", False, GRAY),
            ("|  Mục tiêu: ", True, NAVY),
            (goal_of(body), False, GRAY),
        ], 10, space_after=8)

        # Nội dung hiển thị
        add_para(doc, "A. NỘI DUNG HIỂN THỊ TRÊN SLIDE", 11.5, True, NAVY,
                 space_after=4, space_before=2)
        add_rule(doc, "DDE3EA", 6)
        for line in body.split("\n"):
            line = line.rstrip()
            if not line.strip():
                add_para(doc, "", 9, space_after=2)
                continue
            if line.strip().startswith("```"):
                continue
            indent = 0.0
            txt = line
            if txt.startswith("  ") or txt.startswith("\t"):
                indent = 0.6
                txt = txt.lstrip()
            elif txt.startswith("- ") or txt.startswith("•"):
                indent = 0.4
                txt = txt[2:]
            add_para(doc, txt, 10, False, GRAY, indent=indent, space_after=2,
                     line=1.25)

        if assets:
            add_para(doc, "Ảnh sử dụng: " + ", ".join(sorted(set(assets))),
                     9.5, True, BLUE, space_before=4, space_after=6)

        # Lời thuyết trình
        add_para(doc, "B. LỜI THUYẾT TRÌNH (đọc tự nhiên, không cần đọc nguyên văn)",
                 11.5, True, NAVY, space_after=4, space_before=4)
        add_rule(doc, "DDE3EA", 6)
        para_text = " ".join(notes.split())
        # tách câu để dễ đọc
        sentences = re.split(r"(?<=[.!?])\s+", para_text)
        buf = ""
        for s in sentences:
            if len(buf) + len(s) < 260:
                buf = (buf + " " + s).strip()
            else:
                add_para(doc, buf, 10.5, False, RGBColor(0x22, 0x2A, 0x35),
                         space_after=5, line=1.4)
                buf = s
        if buf:
            add_para(doc, buf, 10.5, False, RGBColor(0x22, 0x2A, 0x35),
                     space_after=5, line=1.4)

        # Gợi ý chuyển slide
        nxt = slides[idx + 1] if idx + 1 < len(slides) else None
        if nxt:
            add_callout(doc, "→ CHUYỂN SLIDE",
                        f"Slide {nxt[0]:02d} — {nxt[1]}")

        doc.add_page_break()

    # ================= PHỤ LỤC =================
    add_para(doc, "PHỤ LỤC — CÂU HỎI THƯỜNG GẶP & GỢI Ý TRẢ LỜI",
             20, True, NAVY, space_after=4)
    add_rule(doc, "0F62FE", 12)

    qa = [
        ("Vì sao chọn kiến trúc monolith phân lớp mà không phải microservices?",
         "Độ phức tạp vận hành thấp, giao dịch đơn hàng – tồn kho cần tính nhất quán trong "
         "một CSDL (đáp ứng NFR-11), và phù hợp nguồn lực nhóm sinh viên. Ranh giới phân hệ "
         "vẫn giữ bằng interface công khai nên về sau có thể tách dần từng phân hệ."),
        ("ERD khác class diagram như thế nào?",
         "ERD mô hình hóa dữ liệu vật lý (bảng, cột, khóa, quan hệ bội số) và không có hành vi. "
         "Class diagram mô hình hóa cấu trúc hướng đối tượng khi chạy, có dữ liệu lẫn hành vi, "
         "kế thừa, giao diện và đa hình. Hai sơ đồ bổ sung cho nhau, không thay thế nhau."),
        ("33 đối tượng nghiệp vụ nhưng 35 bảng CSDL — giải thích thế nào?",
         "Ba lớp con KhachHang/DuocSi/QuanTriVien dùng chung khóa với bảng người dùng được tách "
         "thành 3 bảng con 1–1 (−3 bảng). Hai quan hệ N–M giữa thuốc với dược chất và dược liệu "
         "được giữ bằng 2 bảng nối (+2 bảng). Chênh lệch có chủ đích, xem reference/FACTS.md."),
        ("Tại sao không lưu số thẻ trong CSDL?",
         "Theo NFR-07 và nguyên tắc PCI-DSS, hệ thống không lưu số thẻ. Vì vậy Phần 3 thiết kế "
         "Adapter thanh toán (PaymentGatewayAdapter) đứng giữa hệ thống và cổng AC05; nếu đổi "
         "cổng chỉ thay Adapter, không sửa nghiệp vụ đặt hàng."),
        ("Làm sao bảo đảm không mất hoặc trùng đơn hàng (NFR-11)?",
         "Chỉ khi thanh toán thành công thì đơn hàng mới được tạo và tồn kho mới bị trừ. Nếu "
         "thanh toán thất bại, đơn không được xác nhận và khách được chọn lại phương thức. "
         "Nếu thanh toán quá thời gian, giao dịch chuyển sang trạng thái chờ đối soát chứ không xóa."),
        ("Vì sao gộp 3 cấp danh mục thành 1 bảng?",
         "Cây danh mục 4 cấp (nhóm sản phẩm – danh mục – danh mục con – sản phẩm) có cấu trúc đều, "
         "nên gộp thành bảng danh_muc với thuộc tính cap và quan hệ tự tham chiếu "
         "(danh_muc_cha_id) giúp tránh lặp lại và giữ được tính đệ quy."),
        ("Phần quản trị trong báo cáo có chắc đúng với hệ thống thật?",
         "Nhóm chỉ khảo sát được 8 màn hình từ phía người dùng. Các chức năng quản trị và cơ chế "
         "OTP đã được đánh dấu là đề xuất trong báo cáo và được giả định dựa trên kiến trúc đã phân tích."),
        ("Cơ sở dữ liệu có đạt chuẩn 3NF không?",
         "Có. Bảng thiết kế CSDL ở mục 3.3 đã chuẩn hóa 3NF: khóa chính id bigint tự tăng, "
         "khóa ngoại đặt theo bảng cha, quan hệ tùy chọn cho phép null, trạng thái dùng enum, "
         "và bảng chi tiết đơn lưu snapshot tên sản phẩm + đơn giá tại thời điểm đặt."),
        ("Vì sao dùng mẫu Repository, Adapter, Factory?",
         "Repository tách truy vấn khỏi nghiệp vụ, Adapter cô lập hệ thống ngoài để lỗi dịch vụ "
         "bên ngoài không làm ngừng chức năng khác, Factory tạo giao dịch theo phương thức thanh toán. "
         "Ba mẫu này trả lời trực tiếp cho NFR-15 về khả năng bảo trì."),
        ("Đồ án này còn hạn chế gì?",
         "Chỉ khảo sát được giao diện công khai (8 màn hình), nên phần quản trị chiều sâu và "
         "nghiệp vụ kho chuỗi cung ứng mang tính đề xuất. Hệ thống chưa được triển khai, mới dừng "
         "ở mức phân tích và thiết kế."),
    ]
    for i, (q, a) in enumerate(qa, 1):
        add_rich(doc, [(f"Câu {i}. ", True, ORANGE), (q, True, NAVY)],
                 11, space_after=2, space_before=6)
        add_para(doc, a, 10.5, False, RGBColor(0x22, 0x2A, 0x35),
                 space_after=4, line=1.35, indent=0.6)

    # ================= CHECKLIST =================
    add_para(doc, "CHECKLIST TRƯỚC KHI THUYẾT TRÌNH", 18, True, NAVY,
             space_before=12, space_after=4)
    add_rule(doc, "0F62FE", 12)
    checks = [
        "Mở app.diagrams.net và tải sẵn 13 file .drawio trong diagrams/drawio/ để trả lời câu hỏi về sơ đồ.",
        "Xuất PNG từ các file .drawio bằng Ctrl/Cmd + Shift + S nếu thầy yêu cầu hiển thị toàn màn hình.",
        "Kiểm tra tài khoản hiển thị đăng nhập: nhân viên Long Châu, dược sĩ tư vấn và quản trị viên.",
        "Chuẩn bị sẵn câu trả lời cho 10 câu hỏi thường gặp ở phụ lục.",
        "Mở link draw.io trực tiếp từ README nếu cần chỉnh sửa sơ đồ tại chỗ.",
        "Chuẩn bị bản in kịch bản này làm dự phòng khi máy trình chiếu lỗi.",
    ]
    for c in checks:
        add_rich(doc, [("[ ]  ", True, BLUE), (c, False, GRAY)],
                 10.5, space_after=3, indent=0.4)

    doc.save(OUT)
    print(f"OK -> {OUT}")
    print(f"slides={len(slides)}  words={total_words}  ~{minutes:.0f} phút")


def summary_of(body: str) -> str:
    """Tóm tắt nội dung hiển thị: ưu tiên các dòng có nội dung thật."""
    lines = [l.strip(" -•\t") for l in body.split("\n") if l.strip()]
    skip = ("Tạo slide", "BỐ CỤC", "NỘI DUNG", "BỐ CỤC:", "NỘI DUNG:")
    picked = []
    for l in lines:
        if l.startswith(skip):
            continue
        if l.startswith("```") or l.startswith("Logo") or l.startswith("Ảnh"):
            continue
        if len(l) < 12:
            continue
        picked.append(l)
    if not picked:
        picked = lines[:1]
    # ưu tiên dòng có dấu nháy kép (nội dung chữ hiển thị thật)
    quoted = [p for p in picked if '"' in p]
    if quoted:
        picked = quoted
    s = " · ".join(picked[:3])
    s = s.replace("`", "")
    if len(s) > 150:
        s = s[:147] + "…"
    return s


def goal_of(body: str) -> str:
    s = summary_of(body)
    return s if len(s) < 130 else s[:127] + "…"


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    build()
