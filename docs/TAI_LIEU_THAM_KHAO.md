# Tài liệu tham khảo

## 1. Giáo trình

- **Bài giảng môn Phân tích và Thiết kế Phần mềm** — TS. Trương Đức Phương, Trường Công nghệ Thông tin Phenikaa, năm 2026.
  Nguồn chính cho toàn bộ phương pháp luận: mô hình phân lớp (Layered Architecture), mẫu BCE, ký hiệu UML, quy trình xác định yêu cầu.

## 2. Hệ thống được khảo sát

- **FPT Long Châu** — Website chính thức của hệ thống Nhà thuốc FPT Long Châu.
  Khảo sát tháng 10/2026 tại [nhathuoclongchau.com.vn](https://nhathuoclongchau.com.vn/).
  Nguồn cho: mô hình nghiệp vụ, danh mục 5 nhóm sản phẩm, quy trình đặt hàng, 6 phương thức thanh toán, điều kiện miễn phí vận chuyển, và giao diện thực tế dùng cho mục 3.4.

## 3. An toàn & bảo mật

- **OWASP Foundation** — *OWASP Top 10 Web Application Security Risks*.
  [owasp.org](https://owasp.org/) — Nguồn cho nhóm yêu cầu phi chức năng về bảo mật (NFR-04 → NFR-08): HTTPS/TLS, mã hóa dữ liệu nhạy cảm, phân quyền theo vai trò, chống SQLi/XSS/CSRF, không lưu số thẻ thanh toán.

## 4. Pháp luật & tuân thủ

- **Bộ Y tế** — *Luật Dược số 105/2016/QH13* quy định về hoạt động kinh doanh dược và thương mại điện tử dược phẩm.
  Nguồn cho yêu cầu tuân thủ NFR-17 (kinh doanh dược, thương mại điện tử) và nghiệp vụ đơn thuốc (UC17, UC18, PH07).

## 5. Công cụ

| Công cụ | Vai trò trong đồ án |
|---|---|
| [draw.io / diagrams.net](https://app.diagrams.net/) | Vẽ toàn bộ sơ đồ UML (Use Case, Sequence, Activity, Class, ERD) và wireframe UI |
| Microsoft Word | Soạn thảo báo cáo, xuất bản PDF |
| Python (`python-docx`) | Tự động hoá bước trích ảnh & chuyển đổi báo cáo sang Markdown cho GitHub |
| [Gamma](https://gamma.app/) / ChatGPT / Claude | Sinh slide trình bày từ đặc tả nội dung trong [`slides/`](../slides/) |

## 6. Liên kết nội bộ

- [`../reference/FACTS.md`](../reference/FACTS.md) — nguồn sự thật đã kiểm chứng: toàn bộ số liệu, bảng, mapping hình ↔ caption.
- [`../slides/PROMPT_TAO_SLIDE_LONG_CHAU.md`](../slides/PROMPT_TAO_SLIDE_LONG_CHAU.md) — đặc tả 30 slide kèm lời thuyết trình.
- [`BaoCao_LongChau_PTTKPM.md`](BaoCao_LongChau_PTTKPM.md) — bản Markdown của báo cáo (đọc trực tiếp trên GitHub).
