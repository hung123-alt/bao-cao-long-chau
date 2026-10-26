# FACTS — Báo cáo PTTKPM "Nhà thuốc FPT Long Châu" (ĐÃ KIỂM CHỨNG TỪ FILE GỐC)

> Nguồn: `D:\dowload\BaoCao_LongChau_co_danh_dau_chen_anh (1).docx` (bản chính, có Kết luận + TLTK)
> và `D:\dowload\BaoCao_LongChau_Phan3.docx` (bản có 5 hình Phần 3: Hình 3.1–3.5).
> Mọi con số dưới đây đã đối chiếu trực tiếp với bảng gốc. TUYỆT ĐỐI KHÔNG BỊA SỐ LIỆU.

## 0. Thông tin chung
- Đồ án: **Phân tích và Thiết kế Phần mềm hệ thống Website Nhà thuốc FPT Long Châu** (`nhathuoclongchau.com.vn`)
- Trường: Công nghệ Thông tin Phenikaa — GV: TS. Trương Đức Phương — năm 2026
- Khảo sát thực tế: tháng 10/2026
- 5 nhóm sản phẩm: Thực phẩm chức năng, Dược mỹ phẩm, Thuốc, Chăm sóc cá nhân, Thiết bị y tế
- Cây danh mục: Nhóm sản phẩm (cấp 1) → Danh mục (cấp 2) → Danh mục con (cấp 3) → Sản phẩm
- Đặc thù: sản phẩm bán theo nhiều đơn vị tính (Hộp/Vỉ/Chai/Tuýp); thuốc kê đơn (Rx) cần tư vấn dược sĩ; miễn phí VC cho đơn ≥ 300.000đ; 2 hình thức nhận hàng (giao tận nơi / nhận tại nhà thuốc); 6 phương thức thanh toán.

## 1. PHẦN 1 — XÁC ĐỊNH YÊU CẦU
- **Bảng 1.3 Thuật ngữ (Glossary): 35 thuật ngữ.**
- **Bảng 1.4 Yêu cầu chức năng: 52 FR**, chia 9 module:
  | Module | FR | UC |
  |---|---|---|
  | 1 – Tài khoản | FR-01…FR-06 | UC01, UC02 |
  | 2 – Duyệt danh mục và sản phẩm | FR-07…FR-16 | UC03–UC06, UC10, UC19 |
  | 3 – Tìm kiếm và tra cứu | FR-17…FR-21 | UC07, UC08 |
  | 4 – Giỏ hàng, đặt hàng và thanh toán | FR-22…FR-32 | UC10–UC13 |
  | 5 – Đơn hàng và đánh giá | FR-33…FR-37 | UC14, UC15, UC16 |
  | 6 – Đơn thuốc và tư vấn | FR-38…FR-40 | UC17, UC18 |
  | 7 – Khuyến mãi | FR-41, FR-42 | UC09 |
  | 8 – Thông tin bổ trợ | FR-43…FR-45 | UC19, UC20, UC21 |
  | 9 – Quản trị (đề xuất) | FR-46…FR-52 | UC22–UC27 |
  - FR đáng nhớ: FR-25 miễn phí vận chuyển ≥300.000đ; FR-31 sáu phương thức thanh toán (tiền mặt khi nhận hàng, chuyển khoản QR, MoMo, ZaloPay, thẻ quốc tế/Apple Pay, NAPAS); FR-52 thống kê doanh thu, số đơn, sản phẩm bán chạy.
- **Bảng 1.5 Yêu cầu phi chức năng: 18 NFR**, mỗi NFR có tiêu chí đo lường:
  - Hiệu năng: NFR-01 tải trang ≤3s (95% lượt); NFR-02 tìm kiếm ≤2s, gợi ý ≤0,5s; NFR-03 ≥1.000 người dùng đồng thời.
  - Bảo mật: NFR-04 HTTPS TLS≥1.2; NFR-05 mã hóa dữ liệu nhạy cảm; NFR-06 phân quyền KH–DS–QTV, hết phiên 30′; NFR-07 không lưu số thẻ; NFR-08 chống SQLi/XSS/CSRF + giới hạn OTP.
  - Tin cậy: NFR-09 ≥99% uptime; NFR-10 sao lưu hằng ngày, khôi phục ≤4h; NFR-11 không mất/trùng đơn.
  - Dùng được: NFR-12 mua hàng ≤5 bước; NFR-13 tiếng Việt có dấu, tiền tệ `185.000đ`, ngày `dd/MM/yyyy`; NFR-14 Chrome/Edge/Firefox/Safari + responsive.
  - Bảo trì/mở rộng: NFR-15 thêm danh mục/pương thức thanh toán bằng cấu hình; NFR-16 ≥100.000 sản phẩm.
  - Tuân thủ: NFR-17 quy định kinh doanh dược, TMĐT, BV dữ liệu cá nhân.
  - Nhất quán: NFR-18 giá/khuyến mãi/tồn kho nhất quán giữa danh sách–chi tiết–giỏ–đơn.
- **Bảng 1.6 Tác nhân: 6** (4 người + 2 hệ thống ngoài)
  - AC01 Khách vãng lai (UC01, UC03–UC09, UC19–UC21)
  - AC02 Khách hàng (kế thừa AC01) — UC02, UC10–UC18
  - AC03 Dược sĩ — UC01, UC17, UC18
  - AC04 Quản trị viên — UC01, UC22–UC27
  - AC05 Cổng thanh toán (ngoài) — UC13
  - AC06 Dịch vụ xác thực bên ngoài (ngoài) — UC01
- **Bảng 1.7 Use Case: 27** chia 3 mức + 4 nhóm chức năng
  - Nhóm Tài khoản: UC01 (Hỗ trợ), UC02 (Đơn giản)
  - Nhóm Mua sắm sản phẩm: UC03, UC04, UC05, UC06, UC07 (Trọng tâm); UC08 (Hỗ trợ); UC09 (Đơn giản); UC10 (Hỗ trợ); UC11 (Trọng tâm); UC12 (Đơn giản); UC13 (Hỗ trợ); UC14 (Hỗ trợ); UC15 (Đơn giản); UC16 (Đơn giản)
  - Nhóm Thông tin bổ trợ: UC19, UC20, UC21 (Đơn giản)
  - Nhóm Quản trị hệ thống: UC22, UC23, UC24, UC25, UC26, UC27 (Đơn giản)
  - **Trọng tâm = 6 Use Case: UC03, UC04, UC05, UC06, UC07, UC11.**
- **Bảng 1.1 Phạm vi**: 4 mức — Trọng tâm / Hỗ trợ / Đơn giản / Ngoài phạm vi (app di động; quản lý nhập hàng–kho–chuỗi cung ứng; nghiệp vụ tiêm chủng chi tiết; tích hợp kỹ thuật cổng thanh toán & vận chuyển; chương trình KH thân thiết).
- **Hình 1.1** — Biểu đồ Use Case tổng quát.

## 2. PHẦN 2 — PHÂN TÍCH HỆ THỐNG
- **Kiến trúc mức cao (Hình 2.1): 4 tầng** — Trình bày / Nghiệp vụ / Truy cập dữ liệu / Dữ liệu + thành phần xuyên suốt + 2 adapter hệ thống ngoài.
- **Quyết định kiến trúc:** monolith phân lớp theo phân hệ (có bảng so sánh với microservices).
- **Bảng 2.4: 9 phân hệ nghiệp vụ PH01–PH09**
  | Mã | Phân hệ | UC | FR |
  |---|---|---|---|
  | PH01 | Tài khoản & Xác thực | UC01, UC02, UC26 | FR-01–FR-06, FR-51 |
  | PH02 | Danh mục & Sản phẩm | UC03–UC06, UC16, UC22, UC23 | FR-07–FR-16, FR-37, FR-46–FR-48 |
  | PH03 | Tìm kiếm & Tra cứu | UC07, UC08 | FR-17–FR-21 |
  | PH04 | Giỏ hàng & Đơn hàng | UC10, UC11, UC14, UC15, UC24 | FR-22–FR-27, FR-29, FR-30, FR-32–FR-36, FR-49 |
  | PH05 | Thanh toán | UC13 | FR-31 |
  | PH06 | Khuyến mãi | UC09, UC12, UC25 | FR-28, FR-41, FR-42, FR-50 |
  | PH07 | Đơn thuốc & Tư vấn | UC17, UC18 | FR-38–FR-40 |
  | PH08 | Thông tin bổ trợ | UC19, UC20, UC21 | FR-43–FR-45 |
  | PH09 | Thống kê báo cáo | UC27 | FR-52 |
  - Ghi chú đối chiếu: Phân hệ ≠ Module. UC22–UC23 → PH02; UC24 → PH04; UC25 → PH06; UC26 → PH01; UC27 → PH09. FR-15, FR-16 bắt đầu PH02 rồi gọi PH04/PH08.
- **Bảng 2.6: 33 đối tượng nghiệp vụ, 7 cụm** (KHÔNG phải 41/4)
  | Cụm | Mã | Đối tượng |
  |---|---|---|
  | 1 – Người dùng & tài khoản (Hình 2.3) | EN01–EN06 | NguoiDung, KhachHang, DuocSi, QuanTriVien, LienKetDangNhap, DiaChi |
  | 2 – Danh mục & sản phẩm (Hình 2.2) | EN07–EN12 | DanhMuc, SanPham, DonViTinh, ThuongHieu, ThuocTinhSanPham, DanhGia |
  | 3 – Tra cứu thuốc (Hình 2.5) | EN13–EN16 | NhomThuoc, Thuoc, DuocChat, DuocLieu |
  | 4 – Giỏ hàng, đơn hàng, thanh toán (Hình 2.3, 2.4) | EN17–EN23 | GioHang, MucGioHang, DonHang, ChiTietDonHang, YeuCauHuyTra, GiaoDichThanhToan, HoaDonDienTu |
  | 5 – Khuyến mãi (Hình 2.2, 2.4) | EN24–EN27 | Voucher, FlashSale, SanPhamFlashSale, Banner |
  | 6 – Đơn thuốc & tư vấn (Hình 2.5) | EN28–EN30 | DonThuoc, PhienTuVan, TinNhan |
  | 7 – Thông tin bổ trợ (Hình 2.2, 2.4) | EN31–EN33 | NhaThuoc, VacXin, BaiViet |
  - Tên lớp viết PascalCase không dấu (SanPham). Quy tắc xác định đối tượng: (1) có dữ liệu riêng cần lưu, (2) có thuộc tính/quan hệ riêng, (3) tham gia ≥1 UC.
- **Hình 2.6–2.14: 9 biểu đồ trình tự** (UC03, UC04, UC05, UC06, UC07, UC11, UC13, UC22, UC23)
- **Hình 2.15–2.24: 10 biểu đồ hoạt động** (UC03, UC04, UC05, UC06, UC07, UC11, UC22 thêm/sửa, UC22 xóa, UC23 thêm/sửa, UC23 xóa)
- **Hình 2.25–2.28: 4 biểu đồ lớp phân tích BCE**
  - 2.25 Duyệt danh mục & sản phẩm (UC03–UC06) — 3 Boundary, 4 Control, 4 Entity
  - 2.26 Tìm kiếm sản phẩm (UC07) — 1 Boundary, 1 Control, 1 Entity
  - 2.27 Đặt hàng & thanh toán (UC11, UC13) — DatHangControl gọi ThanhToanControl (nét đứt), ThanhToanControl ↔ Cổng thanh toán AC05
  - 2.28 Quản trị danh mục & sản phẩm (UC22, UC23) — 2 màn hình quản trị dùng chung mẫu thao tác
  - **Tổng 17 lớp Boundary/Control** (Bảng 2.9) + 33 lớp Entity = lớp BCE.
- Mũi tên: solid = gọi phương thức, dashed = kết quả/nội dung hiển thị.

## 3. PHẦN 3 — THIẾT KẾ HỆ THỐNG
### 3.1.1 Bảng 3.1 — 21 nhóm lớp thiết kế (kèm PK/FK/UQ + phương thức)
| STT | Lớp | Loại | Thuộc tính & phương thức chính | UC |
|---|---|---|---|---|
| 1 | DanhMuc | Entity (PH02) | +id bigint {PK}, +ma varchar(30) {UQ}, +ten, +cap, +danhMucChaId {FK}, +thuTuHienThi, +trangThai; +themCon(), +sua(), +an()/hien(), +xoaKiemTraRangBuoc() | UC03,04,22 |
| 2 | SanPham | Entity (PH02) | +id {PK}, +ma {UQ}, +ten, +danhMucId {FK}, +thuongHieuId {FK}, +thuocKeDon, +canTuVan, +trangThai; +sua(), +ngungBan(), +kiemTraKeDon() | UC03–06,22,23 |
| 3 | DonViTinh | Entity (PH02, PH04) | +id {PK}, +sanPhamId {FK}, +tenDonVi, +giaBan, +giaGoc, +tonKho; +truTonKho(sl), +kiemTraTon(sl) | UC04–06,11,23 |
| 4 | DanhGia | Entity (PH02) | +id {PK}, +sanPhamId {FK}, +khachHangId {FK}, +soSao, +noiDung, +trangThaiDuyet; +duyet(), +tuChoi() | UC06 |
| 5 | ThuocTinhSanPham | Entity (PH02) | +id {PK}, +sanPhamId {FK}, +tenThuocTinh, +giaTri; +sua(), +xoa() | UC23 |
| 6 | GioHang | Entity (PH04) | +id {PK}, +khachHangId {FK,UQ}, +ngayCapNhat; +themMuc(), +capNhatSoLuong(), +xoaMuc(), +tinhTamTinh() | UC10,11 |
| 7 | DiaChi | Entity (PH04) | +id {PK}, +khachHangId {FK}, +hoTen/sdtNguoiNhan, +tinhThanh/quanHuyen/phuongXa, +macDinh; +datMacDinh(), +kiemTraHopLe() | UC11 |
| 8 | DonHang | Entity (PH04) | +id {PK}, +maDon {UQ}, +khachHangId {FK}, +trangThai, +hinhThucNhanHang, +voucherId {FK}, +donThuocId {FK}, +tongTien/giamGia/phiVC/thanhTien, +anTenSanPham; +xacNhan(), +huy(), +yeuCauTraHang(), +tinhThanhTien() | UC11,14,15 |
| 9 | ChiTietDonHang | Entity (PH04) | +id {PK}, +donHangId {FK}, +tenSanPham/tenDonVi {SNAP}, +soLuong, +donGia {SNAP}; +tinhThanhTien() | UC11 |
| 10 | GiaoDichThanhToan | Entity (PH05) | +id {PK}, +maGiaoDich {UQ}, +donHangId {FK}, +phuongThuc, +soTien, +trangThai; +taoGiaoDich(), +capNhatKetQua(), +doiSoat() | UC13 |
| 11 | DanhMucControl, DanhSachControl, BoLocControl, ChiTietControl | Control (PH02) | Điều phối UC03–UC06: lấy cây danh mục, danh sách/giá sản phẩm, lọc-sắp xếp, chi tiết-đánh giá | UC03–06 |
| 12 | TimKiemControl | Control (PH03) | goiYKhiGo(), timKiem(), xepHangKetQua(), giongNoiThanhVanBan(), nhanDienAnh() | UC07 |
| 13 | DatHangControl | Control (PH04) | moTrangDatHang(), tinhTien(), apDungVoucher(ma), datHang(), taoDon(), truTonKho() | UC11 |
| 14 | ThanhToanControl | Control (PH05) | thanhToan(), taoGiaoDich(), guiYeuCau(), nhanKetQua(), capNhatGiaoDich(), xuLyTimeout() | UC13 |
| 15 | QLDanhMucControl, QLSanPhamControl | Control (PH02) | layCayDanhMuc()/layDanhSach(), luuDanhMuc()/luuSanPham(), kiemTraDuLieu(), xoaDanhMuc()/xoaSanPham()/anSanPham(), capNhatTonKho() | UC22,23 |
| 16 | ManHinhMenu, ManHinhDanhSach, ManHinhChiTiet | Boundary (PH02) | Hiển thị menu cây, danh sách + bộ lọc, chi tiết + đơn vị tính + cảnh báo kê đơn | UC03–06 |
| 17 | ManHinhTimKiem | Boundary (PH03) | nhapTuKhoa(), noiVaoMicro(), taiAnh(), hienThiGoiY()/hienThiKetQua()/hienThiLichSu() | UC07 |
| 18 | ManHinhDatHang, ManHinhThanhToan | Boundary (PH04, PH05) | Hiển thị trang đặt hàng (nhận hàng, địa chỉ, thanh toán, voucher, đơn thuốc), mã QR/chuyển cổng | UC11,13 |
| 19 | ManHinhQLDanhMuc, ManHinhQLSanPham | Boundary (PH02) | Hiển thị cây danh mục, danh sách sản phẩm; nhập/luu/xóa, nhập tồn kho | UC22,23 |
| 20 | DanhMucRepository, SanPhamRepository, DonHangRepository, GiaoDichRepository | Repository (PH02, PH04, PH05) | findCap2(), findCon(idCha), findByDanhMuc(), findBanChayNhat(), searchFullText(tuKhoa), save(), softDelete()/ngungBan(), capNhatTon(), capNhatTrangThai() | UC03–07,11,13,22,23 |
| 21 | ICongThanhToan, ITimKiemNangCao | Interface (PH05, PH03) | +taoYeuCau(tt):url, +kiemTraKetQua(maGD); +nhanDienAnh(anh), +speechToText(amThanh) | UC07,13 |
- **Nguyên tắc thiết kế (3.1.1):** (i) mỗi phân hệ chỉ giao tiếp qua interface công khai, không đọc trực tiếp dữ liệu nhau; (ii) mọi truy xuất đi qua Repository, lớp nghiệp vụ không chứa SQL; (iii) hệ thống ngoài (Cổng thanh toán AC05, Dịch vụ xác thực AC06) được cô lập sau Adapter.
### 3.1.2 Bảng 3.2 — 9 phân hệ + giao diện cung cấp
| Mã | Hệ thống con | UC | FR | Giao diện / lớp cung cấp |
|---|---|---|---|---|
| PH01 | Tài khoản & Xác thực | UC01,02,26 | FR-01–06,51 | INguoiDung (dangNhap, dangKy, doiMatKhau); Adapter xác thực (OTP/định danh/MXH) |
| PH02 | Danh mục & Sản phẩm | UC03–06,16,22,23 | FR-07–16,37,46–48 | IDanhMuc (layCayDanhMuc, layDanhMucCap2), ISanPham (xemDanhSach, xemChiTiet, locVaSapXep); DanhMucRepository, SanPhamRepository |
| PH03 | Tìm kiếm & Tra cứu | UC07,08 | FR-17–21 | ITimKiem (timKiem, goiY, xepHangKetQua), ITimKiemNangCao (nhanDienAnh, speechToText) |
| PH04 | Giỏ hàng & Đơn hàng | UC10,11,14,15,24 | FR-22–27,29,30,32–36,49 | IDatHang (tinhTien, datHang, taoDon), IGioHang; DonHangRepository; gọi PH02 (giá/tồn), PH06 (giảm giá), PH05 (thanh toán) |
| PH05 | Thanh toán | UC13 | FR-31 | IThanhToan (thanhToan, capNhatGiaoDich); ICongThanhToan + Adapter thanh toán; GiaoDichRepository; không lưu số thẻ (NFR) |
| PH06 | Khuyến mãi | UC09,12,25 | FR-28,41,42,50 | IVoucher (kiemTraDieuKien, tinhGiamGia), IFlashSale |
| PH07 | Đơn thuốc & Tư vấn | UC17,18 | FR-38–40 | IDonThuoc (taiLen, xacNhan, tuChoi), ITuVan (moPhien, guiTinNhan) |
| PH08 | Thông tin bổ trợ | UC19,20,21 | FR-43–45 | INhaThuoc, ITiemChung, IBaiViet |
| PH09 | Thống kê báo cáo | UC27 | FR-52 | IThongKe (tongHopDoanhThu, sanPhamBanChay); chỉ đọc |
- Quy tắc giao tiếp: PH04 → PH02 (giá/tồn), PH04 → PH06 (voucher), PH04 → PH05 (thanh toán); PH05 ↔ AC05 qua ICongThanhToan + Adapter; PH01 ↔ AC06 qua Adapter xác thực; PH09 chỉ đọc.
### 3.2 Hình 3.1–3.4 — 4 biểu đồ lớp thiết kế
- Hình 3.1 Duyệt danh mục & sản phẩm (UC03–UC06)
- Hình 3.2 Tìm kiếm sản phẩm (UC07)
- Hình 3.3 Đặt hàng & Thanh toán (UC11, UC13)
- Hình 3.4 Quản trị danh mục & sản phẩm (UC22, UC23)
### 3.3 Bảng 3.3 — 35 bảng CSDL / 7 cụm (PK, FK, mô tả)
Quy ước chung: PK `id` BIGINT tự tăng; FK đặt tên `<bang>_id`, cho phép NULL khi quan hệ tuỳ chọn (`voucher_id`, `don_thuoc_id`, `nha_thuoc_id` của `don_hang`; `don_hang_id` của `giao_dich_thanh_toan` khi COD); ENUM cho trạng thái/phân loại cố định; TEXT cho mô tả/nội dung.
| STT | Bảng | Khóa chính | Khóa ngoại | Mô tả |
|---|---|---|---|---|
| 1 | nguoi_dung | id | – | Tài khoản dùng chung: sdt(UQ), hoTen, email, matKhauBam, vaiTro, trangThai, ngayTao |
| 2 | khach_hang | nguoi_dung_id (PK,FK) | → nguoi_dung.id | Hồ sơ KH (1-1): ngaySinh, gioiTinh |
| 3 | duoc_si | nguoi_dung_id (PK,FK) | → nguoi_dung.id | Dược sĩ (1-1): soChungChiHanhNghề |
| 4 | quan_tri_vien | nguoi_dung_id (PK,FK) | → nguoi_dung.id | Quản trị viên (1-1) |
| 5 | dia_chi | id | khach_hang_id → khach_hang.nguoi_dung_id | Sổ địa chỉ: người nhận, sdt, tỉnh/quận/phường, chi tiết, mặc định |
| 6 | lien_ket_dang_nhap | id | nguoi_dung_id → nguoi_dung.id | Liên kết đăng nhập ngoài (OTP/định danh/FB/Google/Apple) |
| 7 | danh_muc | id | danh_muc_cha_id → danh_muc.id (tự tham chiếu) | Cây nhiều cấp: ma(UQ), ten, cap, bieuTuong, thuTu, trangThai |
| 8 | san_pham | id | danh_muc_id → danh_muc.id; thuong_hieu_id → thuong_hieu.id | ma(UQ), ten, noiSX, moTa, quyCach, thanhPhan, thuocKeDon, canTuVan, trangThai |
| 9 | thuong_hieu | id | – | ma(UQ), ten |
| 10 | don_vi_tinh | id | san_pham_id → san_pham.id | Đơn vị tính + giá/tồn kho: tenDonVi, giaBan, giaGoc, %giam, tonKho |
| 11 | thuoc_tinh_san_pham | id | san_pham_id → san_pham.id | Thuộc tính dạng cặp tên–giá trị |
| 12 | danh_gia | id | san_pham_id → san_pham.id; khach_hang_id → khach_hang.nguoi_dung_id | soSao, noiDung, ngayGui, trangThaiDuyet |
| 13 | nhom_thuoc | id | – | ma(UQ), ten |
| 14 | thuoc | id | nhom_thuoc_id → nhom_thuoc.id | ma(UQ), ten, chiDinh, cachDung, luuY |
| 15 | duoc_chat | id | – | ma(UQ), ten, moTaDuocLy, chiDinh |
| 16 | duoc_lieu | id | – | ma(UQ), ten, tenKhoaHoc, congDung, luuY |
| 17 | thuoc_duoc_chat | thuoc_id + duoc_chat_id (PK kép) | → thuoc.id; → duoc_chat.id | Bảng nối N-M thuốc–dược chất |
| 18 | thuoc_duoc_lieu | thuoc_id + duoc_lieu_id (PK kép) | → thuoc.id; → duoc_lieu.id | Bảng nối N-M thuốc–dược liệu |
| 19 | gio_hang | id | khach_hang_id → khach_hang.nguoi_dung_id (UQ) | Giỏ hàng (1-1 với KH): ngayCapNhat |
| 20 | muc_gio_hang | id | gio_hang_id → gio_hang.id; don_vi_tinh_id → don_vi_tinh.id | Dòng giỏ: soLuong, daChon |
| 21 | don_hang | id | khach_hang_id; nha_thuoc_id (nullable); voucher_id (nullable); don_thuoc_id (nullable) | maDon(UQ), ngayDat, trangThai, hinhThucNhan, snapshot người nhận, các mục tiền, anTenSP |
| 22 | chi_tiet_don_hang | id | don_hang_id → don_hang.id | Dòng đơn (snapshot): tenSP, tenDonVi, soLuong, donGia, thanhTien |
| 23 | giao_dich_thanh_toan | id | don_hang_id → don_hang.id (nullable khi COD) | maGD(UQ), phuongThuc, soTien, trangThai, maGDCong, thoiDiem |
| 24 | hoa_don_dien_tu | id | don_hang_id → don_hang.id | tenNguoiMua, mst, diaChi, emailNhan |
| 25 | yeu_cau_huy_tra | id | don_hang_id → don_hang.id | ma(UQ), loai, lyDo, ngayGui, trangThaiXuLy |
| 26 | flash_sale | id | – | ma(UQ), ten, gioBatDau/ketThuc, trangThai |
| 27 | san_pham_flash_sale | id | flash_sale_id → flash_sale.id; don_vi_tinh_id → don_vi_tinh.id | mucGiam, slGioiHan, daBan |
| 28 | voucher | id | – | ma(UQ), loaiGiam, giaTri, donToiThieu, hanDung, phamVi, trangThai |
| 29 | banner | id | – | anh, duongDan, thuTu, trangThai |
| 30 | don_thuoc | id | khach_hang_id; duoc_si_id → duoc_si | tepURL, ngayTai, trangThai, lyDoTuChoi |
| 31 | phien_tu_van | id | khach_hang_id; duoc_si_id → duoc_si | ma(UQ), thoiGianBatDau/ketThuc, trangThai |
| 32 | tin_nhan | id | phien_tu_van_id → phien_tu_van.id; san_pham_goi_y_id → san_pham.id (nullable) | nguoiGui, noiDung, thoiDiem, spGoiY |
| 33 | nha_thuoc | id | – | ma(UQ), ten, diaChi, tinhQuan, gioMoCua |
| 34 | bai_viet | id | – | tieuDe, chuyenMuc, noiDung, ngayDang |
| 35 | vac_xin | id | – | ten, phongBenh, gia, thongTinChiTiet |
- So với 33 đối tượng Bảng 2.6: số bảng giảm do **gộp 3 lớp con dùng chung khóa** (KhachHang/DuocSi/QuanTriVien → bảng con 1-1 với PK/FK = nguoi_dung_id) và giữ nguyên **2 bảng nối N-M** (thuoc_duoc_chat, thuoc_duoc_lieu).
### 3.3.2 Hình 3.5 — ERD vật lý (35 bảng, 7 cụm), chia 3 phần: 1/3 (cụm A,B), 2/3 (cụm C,D), 3/3 (cụm E,F,G). Ký hiệu Crow's Foot.
### 3.4 Thiết kế giao diện — **CHƯA LÀM** (cần ảnh UI). Trong báo cáo còn placeholder `[CHÈN ẢNH: ...]`.

## 4. PHẦN 4 — KẾT LUẬN
**4.1 Tổng kết kết quả đạt được**
- **1. Khảo sát & Xác định yêu cầu**: khảo sát thực tế website Long Châu; xây dựng Glossary; phân loại 52 FR + 18 NFR có tiêu chí đo lường; mô hình hóa bằng sơ đồ Use Case, xác định 6 tác nhân + 27 UC phân 3 mức.
- **2. Phân tích hệ thống (Chương 2)**: kiến trúc mức cao theo mô hình phân lớp (Layered Architecture) kết hợp phân hệ monolith, tách biệt 4 tầng Trình bày/Nghiệp vụ/Truy cập dữ liệu/Dữ liệu; xác định **33 đối tượng nghiệp vụ / 7 cụm**; hiện thực hóa UC trọng tâm qua biểu đồ trình tự, hoạt động và biểu đồ lớp phân tích BCE.
- **3. Thiết kế hệ thống (Chương 3)**: mô hình thiết kế kiến trúc hệ thống con, giao diện, biểu đồ lớp thiết kế chi tiết; thiết kế CSDL quan hệ hoàn chỉnh với danh sách bảng chi tiết và ERD; xây dựng quy chuẩn giao diện (UI/UX Guidelines) và sơ đồ luồng màn hình (Screen Flow) + wireframe.
**4.2 Ưu điểm**
- Tính thực tiễn cao — phản ánh sát nghiệp vụ chuỗi nhà thuốc lớn, xử lý tốt đặc thù: quản lý đa đơn vị tính, phân loại thuốc kê đơn (Rx) cần tư vấn dược sĩ, kiểm soát…
- Tính mở rộng và bảo trì tốt — kiến trúc phân hệ rõ ràng giúp dễ bổ sung nhóm sản phẩm mới, phương thức thanh toán mới, hoặc nâng cấp thành microservices mà không ảnh hưởng hiện trạng.
- Bảo mật và an toàn dữ liệu — HTTPS, phân quyền theo vai trò, mã hóa thông tin nhạy cảm, tích hợp cổng thanh toán không lưu số thẻ.
**4.3 Hạn chế**
- Giới hạn về dữ liệu và quyền tiếp cận thực tế — chỉ khảo sát qua giao diện công khai.
- Thời gian và nguồn lực có hạn — một số phân hệ phụ trợ còn giới hạn.

## 5. PHẦN 5 — TÀI LIỆU THAM KHẢO
1. **Giáo trình**: Bài giảng môn Phân tích và Thiết kế Phần mềm, TS. Trương Đức Phương, Trường Công nghệ Thông tin Phenikaa, 2026.
2. **FPT Long Châu**, Website chính thức của hệ thống Nhà thuốc FPT Long Châu, truy cập tháng 10/2026 tại `nhathuoclongchau.com.vn`.
3. **OWASP Foundation**, *OWASP Top 10 Web Application Security Risks*, truy cập tại `owasp.org`.
4. **Bộ Y tế**, *Luật Dược số 105/2016/QH13* quy định về hoạt động kinh doanh dược và thương mại điện tử dược phẩm.

## 6. PHÂN BIỆT ERD vs CLASS DIAGRAM (slide bắt buộc)
| Tiêu chí | ERD (mục 3.3) | Class Diagram (mục 3.2) |
|---|---|---|
| Mục đích | Mô hình **dữ liệu vật lý** lưu trữ | Mô hình **cấu trúc hướng đối tượng** khi chạy |
| Thành phần | Bảng, cột, kiểu dữ liệu, PK, FK, UQ, index | Lớp, thuộc tính, phương thức, visibility `+ - #` |
| Quan hệ | Bội số quan hệ 1:1 / 1:N / N:M, ký hiệu Crow's Foot | Kế thừa, giao diện, đa hình, điều hướng (navigation) |
| Hành vi | **KHÔNG** có phương thức | **CÓ** phương thức, quy tắc nghiệp vụ |
| Mẫu thiết kế | Chuẩn hóa 3NF, ràng buộc, index | Repository, Adapter, Factory |
| Ánh xạ | 33 đối tượng Bảng 2.6 → 35 bảng (gộp lớp con 1-1, giữ 2 bảng nối N-M) | 17 lớp BCE (Bảng 2.9) → 21 nhóm lớp thiết kế (Bảng 3.1) |

## 7. MAP HÌNH → FIGURE (dùng đúng, đừng đoán)
| File | Figure trong báo cáo | Tỉ lệ |
|---|---|---|
| image_001.png | ảnh minh họa đầu báo cáo (có thể bỏ) | 1.46 |
| image_002.png | **Hình 1.1** Biểu đồ Use Case tổng quát | 0.66 (dọc) |
| image_003.png | **Hình 2.1** Kiến trúc mức cao | 0.99 |
| image_004.png | Hình 2.2 Đối tượng cụm Danh mục/Sản phẩm/Khuyến mãi | 0.98 |
| image_005.png | Hình 2.3 Đối tượng cụm Người dùng/Giỏ hàng | 1.12 |
| image_006.png | Hình 2.4 Đối tượng cụm Đơn hàng/Thanh toán | 1.24 |
| image_007.png | Hình 2.5 Đối tượng cụm Đơn thuốc/Tư vấn/Tra cứu | 0.96 |
| image_008–016.png | Hình 2.6–2.14 biểu đồ trình tự (008=UC03, 009=UC04, 010=UC05, 011=UC06, 012=UC07, 013=UC11, 014=UC13, 015=UC22, 016=UC23) | |
| image_017–026.png | Hình 2.15–2.24 biểu đồ hoạt động (017=UC03, 018=UC04, 019=UC05, 020=UC06, 021=UC07, 022=UC11, 023=UC22 thêm/sửa, 024=UC22 xóa, 025=UC23 thêm/sửa, 026=UC23 xóa) | |
| image_027.png | Hình 2.25 BCE UC03–UC06 | |
| image_028.png | Hình 2.26 BCE UC07 | |
| image_029.png | Hình 2.27 BCE UC11+UC13 | |
| image_030.png | Hình 2.28 BCE UC22+UC23 | |
| image_031.png | **Hình 3.5** ERD phần 3/3 (cụm E,F,G) | |
| image_032.png | **Hình 3.5** ERD phần 2/3 (cụm C,D) | |
| image_033.png | **Hình 3.5** ERD phần 1/3 (cụm A,B) | |
| image_034.png | **Hình 3.4** Lớp thiết kế – Quản trị danh mục & sản phẩm | |
| image_035.png | **Hình 3.3** Lớp thiết kế – Đặt hàng & Thanh toán | |
| image_036.png | **Hình 3.2** Lớp thiết kế – Tìm kiếm sản phẩm | |
| image_037.png | **Hình 3.1** Lớp thiết kế – Duyệt danh mục & sản phẩm | |

**Bộ hình nên dùng (~8–10 hình)**: image_002 (Use Case), image_003 (Kiến trúc mức cao), image_004 (Mô hình đối tượng cụm 2), image_013 (Trình tự UC11), image_022 (Hoạt động UC11), image_029 (BCE đặt hàng), image_037 (Lớp thiết kế duyệt SP), image_035 (Lớp thiết kế đặt hàng), image_033 (ERD 1/3), image_032 (ERD 2/3). Bỏ phần còn lại — user nói rõ "không cần bê tất cả sơ đồ hình".

## 8. GỢI Ý ROSTER SLIDE (~28 slide)
1. Bìa · 2. Agenda · 3. Bối cảnh & vấn đề · 4. Mục tiêu & phạm vi · **Divider Phần 1** · 5. 35 thuật ngữ · 6. 52 FR / 9 module · 7. 18 NFR có tiêu chí đo · 8. 6 tác nhân · 9. 27 UC / 3 mức (Hình 1.1) · **Divider Phần 2** · 10. Kiến trúc mức cao 4 tầng (Hình 2.1) · 11. Monolith phân lớp vs microservices · 12. 9 phân hệ PH01–PH09 · 13. 33 đối tượng / 7 cụm (Hình 2.4) · 14. Trình tự UC11 đặt hàng (Hình 2.13→image_013) · 15. Hoạt động UC11 (image_022) · 16. BCE UC11+UC13 (image_029) · **Divider Phần 3** · 17. Thiết kế cấu trúc: 21 nhóm lớp (Bảng 3.1) · 18. 9 phân hệ + interface (Bảng 3.2) · 19. Mẫu Repository/Adapter/Factory · 20. Lớp thiết kế duyệt SP (image_037) · 21. Lớp thiết kế đặt hàng (image_035) · 22. **ERD vs Class Diagram** (bảng so sánh) · 23. 35 bảng CSDL / 7 cụm (Bảng 3.3) · 24. ERD phần 1/3 (image_033) · 25. ERD phần 2/3 (image_032) · 26. Quy ước đặt tên & chuẩn 3NF · 27. 3.4 Thiết kế giao diện (placeholder) · **Divider Kết luận** · 28. Ưu điểm & hạn chế · 29. Tài liệu tham khảo · 30. Cảm ơn / Q&A

## 9. RÀNG BUỘC KỸ THUẬT
- Font phải hỗ trợ đầy đủ dấu tiếng Việt. **Đã kiểm chứng tồn tại trên máy**: `Segoe UI` (segoeui.ttf), `Arial`, `Calibri`, `Times New Roman`, `Tahoma`, `Verdana`, `Trebuchet MS`, `Consolas`. Dùng **Segoe UI** cho Title+Body (hỗ trợ tốt nhất, có sẵn). TUYỆT ĐỐI không dùng font không cài (Inter, Roboto, Be Vietnam Pro...).
- Nội dung tiếng Việt có dấu phải render đúng, không tofu, không tràn khung.
- Dùng `python` (KHÔNG `python3`) — Windows này `python3` trỏ shim Store rỗng.
- Đường dẫn project có khoảng trắng → luôn quote path.
- `svg_quality_checker.py --canonical-authoring --stage early --stage final --json` phải **0 error**.
- PPTX export phải tồn tại, size > 0, mở được; đếm slide bằng `python-pptx`.
- Speaker notes BẬT (notes là lời thuyết trình tiếng Việt cụ thể, không phải placeholder).
