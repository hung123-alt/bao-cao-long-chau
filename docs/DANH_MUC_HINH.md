# Danh mục hình vẽ (Diagram Index)

Toàn bộ hình trong báo cáo đều có **2 bản**:

| Bản | Vị trí | Dùng để |
|---|---|---|
| `.drawio` (nguồn) | [`diagrams/drawio/`](../diagrams/drawio/) | Chỉnh sửa, mở trên [app.diagrams.net](https://app.diagrams.net/) |
| `.png` (đã xuất) | [`diagrams/png/`](../diagrams/png/) | Nhúng vào báo cáo / slide / README |

> **Cách mở file `.drawio` trực tiếp trên web:** vào [app.diagrams.net](https://app.diagrams.net/) → **File → Open From → Device**, chọn file trong thư mục `diagrams/drawio/`.
> Link công khai tới từng file `.drawio` được liệt kê ở bảng dưới (mở được trực tiếp từ README trên GitHub).

---

## Phần 1 — Xác định yêu cầu

| Hình | Nội dung | File nguồn | Ảnh |
|---|---|---|---|
| **Hình 1.1** | Biểu đồ Use Case tổng quát — 6 tác nhân, 27 UC, 6 nhóm trang | [`Hinh_1_1_Bieu_do_Use_Case.drawio`](../diagrams/drawio/Hinh_1_1_Bieu_do_Use_Case.drawio) | [xem](../diagrams/png/01-phan-1-yeu-cau/hinh-1.1-use-case.png) |

## Phần 2 — Phân tích hệ thống

### Kiến trúc & mô hình đối tượng

| Hình | Nội dung | File nguồn | Ảnh |
|---|---|---|---|
| **Hình 2.1** | Kiến trúc mức cao — 4 tầng, thành phần xuyên suốt, 2 adapter ngoài | [`Hinh_2_1_Kien_truc_muc_cao.drawio`](../diagrams/drawio/Hinh_2_1_Kien_truc_muc_cao.drawio) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.1-kien-truc-muc-cao.png) |
| **Hình 2.2** | Mô hình đối tượng cụm Danh mục, Sản phẩm và Khuyến mãi | [`Hinh_2_2_Danh_muc_San_pham.drawio`](../diagrams/drawio/Hinh_2_2_Danh_muc_San_pham.drawio) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.2-danh-muc-san-pham.png) |
| **Hình 2.3** | Mô hình đối tượng cụm Người dùng và Giỏ hàng | [`Hinh_2_3_Nguoi_dung_Gio_hang.drawio`](../diagrams/drawio/Hinh_2_3_Nguoi_dung_Gio_hang.drawio) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.3-nguoi-dung-gio-hang.png) |
| **Hình 2.4** | Mô hình đối tượng cụm Đơn hàng và Thanh toán | [`Hinh_2_4_Don_hang_Thanh_toan.drawio`](../diagrams/drawio/Hinh_2_4_Don_hang_Thanh_toan.drawio) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.4-don-hang-thanh-toan.png) |
| **Hình 2.5** | Mô hình đối tượng cụm Đơn thuốc, Tư vấn và Tra cứu thuốc | [`Hinh_2_5_Don_thuoc_Tu_van_Tra_cuu.drawio`](../diagrams/drawio/Hinh_2_5_Don_thuoc_Tu_van_Tra_cuu.drawio) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.5-don-thuoc-tu-van-tra-cuu.png) |

### Biểu đồ trình tự (Sequence) — Hình 2.6 → 2.14

Tất cả nằm trong **1 file** [`Hinh_2_6-2_14_Bieu_do_trinh_tu.drawio`](../diagrams/drawio/Hinh_2_6-2_14_Bieu_do_trinh_tu.drawio) (9 trang).

| Hình | Use Case | Ảnh |
|---|---|---|
| 2.6 | UC03 – Xem danh mục sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.6-trinh-tu-UC03.png) |
| 2.7 | UC04 – Xem danh sách sản phẩm theo danh mục | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.7-trinh-tu-UC04.png) |
| 2.8 | UC05 – Lọc và sắp xếp sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.8-trinh-tu-UC05.png) |
| 2.9 | UC06 – Xem chi tiết sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.9-trinh-tu-UC06.png) |
| 2.10 | UC07 – Tìm kiếm sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.10-trinh-tu-UC07.png) |
| 2.11 | UC11 – Đặt hàng | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.11-trinh-tu-UC11.png) |
| 2.12 | UC13 – Thanh toán | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.12-trinh-tu-UC13.png) |
| 2.13 | UC22 – Quản lý danh mục | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.13-trinh-tu-UC22.png) |
| 2.14 | UC23 – Quản lý sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.14-trinh-tu-UC23.png) |

### Biểu đồ hoạt động (Activity) — Hình 2.15 → 2.24

10 hình, được xuất từ các file `.drawio` cùng họ (UC03, UC04, UC05, UC06, UC07, UC11, UC22 ×2, UC23 ×2).

| Hình | Use Case | Ảnh |
|---|---|---|
| 2.15 | UC03 – Xem danh mục sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.15-hoat-dong-UC03.png) |
| 2.16 | UC04 – Xem danh sách sản phẩm theo danh mục | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.16-hoat-dong-UC04.png) |
| 2.17 | UC05 – Lọc và sắp xếp sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.17-hoat-dong-UC05.png) |
| 2.18 | UC06 – Xem chi tiết sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.18-hoat-dong-UC06.png) |
| 2.19 | UC07 – Tìm kiếm sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.19-hoat-dong-UC07.png) |
| 2.20 | UC11 – Đặt hàng | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.20-hoat-dong-UC11.png) |
| 2.21 | UC22 – Thêm / sửa / ẩn-hiện / sắp xếp danh mục | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.21-hoat-dong-UC22-them-sua.png) |
| 2.22 | UC22 – Xóa danh mục | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.22-hoat-dong-UC22-xoa.png) |
| 2.23 | UC23 – Thêm / sửa / ẩn-hiện sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.23-hoat-dong-UC23-them-sua.png) |
| 2.24 | UC23 – Xóa sản phẩm | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.24-hoat-dong-UC23-xoa.png) |

### Biểu đồ lớp phân tích BCE — Hình 2.25 → 2.28

Tất cả nằm trong **1 file** [`Hinh_2_25-2_28_Bieu_do_lop_phan_tich_BCE.drawio`](../diagrams/drawio/Hinh_2_25-2_28_Bieu_do_lop_phan_tich_BCE.drawio) (4 trang).

| Hình | Phạm vi | Ảnh |
|---|---|---|
| 2.25 | Duyệt danh mục và sản phẩm (UC03–UC06) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.25-BCE-danh-muc.png) |
| 2.26 | Tìm kiếm sản phẩm (UC07) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.26-BCE-tim-kiem.png) |
| 2.27 | Đặt hàng và thanh toán (UC11, UC13) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.27-BCE-dat-hang.png) |
| 2.28 | Quản trị danh mục và sản phẩm (UC22, UC23) | [xem](../diagrams/png/02-phan-2-phan-tich/hinh-2.28-BCE-quan-tri.png) |

## Phần 3 — Thiết kế hệ thống

| Hình | Nội dung | File nguồn | Ảnh |
|---|---|---|---|
| **Hình 3.1** | Lớp thiết kế – Duyệt danh mục & sản phẩm (UC03–UC06) | [`Hinh_3_1_Lop_thiet_ke_Duyet_danh_muc_San_pham.drawio`](../diagrams/drawio/Hinh_3_1_Lop_thiet_ke_Duyet_danh_muc_San_pham.drawio) | [xem](../diagrams/png/03-phan-3-thiet-ke/hinh-3.1-lop-thiet-ke-duyet-danh-muc-san-pham.png) |
| **Hình 3.2** | Lớp thiết kế – Tìm kiếm sản phẩm (UC07) | [`Hinh_3_2_Lop_thiet_ke_Tim_kiem.drawio`](../diagrams/drawio/Hinh_3_2_Lop_thiet_ke_Tim_kiem.drawio) | [xem](../diagrams/png/03-phan-3-thiet-ke/hinh-3.2-lop-thiet-ke-tim-kiem.png) |
| **Hình 3.3** | Lớp thiết kế – Đặt hàng & Thanh toán (UC11, UC13) | [`Hinh_3_3_Lop_thiet_ke_Dat_hang_Thanh_toan.drawio`](../diagrams/drawio/Hinh_3_3_Lop_thiet_ke_Dat_hang_Thanh_toan.drawio) | [xem](../diagrams/png/03-phan-3-thiet-ke/hinh-3.3-lop-thiet-ke-dat-hang-thanh-toan.png) |
| **Hình 3.4** | Lớp thiết kế – Quản trị danh mục & sản phẩm (UC22, UC23) | [`Hinh_3_4_Lop_thiet_ke_Quan_tri.drawio`](../diagrams/drawio/Hinh_3_4_Lop_thiet_ke_Quan_tri.drawio) | [xem](../diagrams/png/03-phan-3-thiet-ke/hinh-3.4-lop-thiet-ke-quan-tri.png) |
| **Hình 3.5** | ERD vật lý – 35 bảng / 7 cụm (3 phần) | [`Hinh_3_5_ERD.drawio`](../diagrams/drawio/Hinh_3_5_ERD.drawio) | [1/3](../diagrams/png/03-phan-3-thiet-ke/hinh-3.5-erd-phan-1-3-cum-a-b.png) · [2/3](../diagrams/png/03-phan-3-thiet-ke/hinh-3.5-erd-phan-2-3-cum-c-d.png) · [3/3](../diagrams/png/03-phan-3-thiet-ke/hinh-3.5-erd-phan-3-3-cum-e-f-g.png) |

### Giao diện (mục 3.4)

| Ảnh | Nội dung |
|---|---|
| [Wireframe giao diện](../diagrams/png/03-phan-3-thiet-ke/hinh-3.4-wireframe-giao-dien.png) | Khung bố cục màn hình theo quy chuẩn UI/UX đã đề xuất |
| [UI màn hình đặt hàng](../diagrams/png/03-phan-3-thiet-ke/hinh-3.6-ui-dat-hang.png) | Giao diện thực tế trang Checkout (UC11) |
| [UI màn hình thanh toán](../diagrams/png/03-phan-3-thiet-ke/hinh-3.7-ui-thanh-toan.png) | Giao diện thực tế trang Thanh toán (UC13) |

---

## Quy ước ký hiệu

| Ký hiệu | Ý nghĩa |
|---|---|
| Mũi tên liền | Gọi phương thức / quan hệ phụ thuộc |
| Mũi tên đứt | Trả kết quả / luồng dữ liệu về |
| `«interface»` | Interface công khai giữa các phân hệ |
| `«repository»` | Lớp truy cập dữ liệu (chỉ Entity mới truy xuất CSDL) |
| `«adapter»` | Lớp cô lập hệ thống bên ngoài (AC05 cổng thanh toán, AC06 xác thực) |
| Khóa `PK` | Primary Key · `FK` Foreign Key · `UQ` Unique |
