# PROMPT TẠO SLIDE — ĐỒ ÁN PTTKPM "NHÀ THUỐC FPT LONG CHÂU"

> Bộ prompt này được viết sau khi đọc toàn bộ file `C:\Users\Think P15\Downloads\BaoCao_LongChau.docx`.
> Mọi số liệu trong prompt đều lấy từ báo cáo gốc — **không có số liệu bịa**.
> Thư mục ảnh: `C:\Users\Think P15\Downloads\SlideAssets\` (36 ảnh, đã đặt tên theo số Hình).

---

## CÁCH DÙNG

1. Mở AI khác (ChatGPT / Claude / Gemini / Copilot) — bất kỳ công cụ nào tạo được slide đẹp.
2. **Bước 1:** dán nguyên khối **SYSTEM PROMPT** bên dưới vào đầu cuộc trò chuyện (chỉ dán 1 lần).
3. **Bước 2:** dán lần lượt từng khối **PROMPT SLIDE 01 → 30**. Yêu cầu AI **vẽ ra 1 slide duy nhất** mỗi lần, không vẽ cả bộ.
4. **Bước 3:** nếu AI không xuất được file, bảo nó trả về **SVG hoặc HTML** để bạn dán vào PowerPoint.

---

# SYSTEM PROMPT (dán 1 lần đầu)

```text
Bạn là chuyên gia thiết kế slide trình bày học thuật bằng HTML/SVG, chuyên nghiệp cho đồ án
môn Phân tích và Thiết kế Phần mềm (PTTKPM) của trường Công nghệ Thông tin Phenikaa,
giảng viên hướng dẫn TS. Trương Đức Phương.

NGUYÊN TẮC TUYỆT ĐỐI
1. CHỈ dùng số liệu và nội dung có trong prompt được giao. TUYỆT ĐỐI KHÔNG tự bịa thêm
   con số, mã FR/NFR/UC, tên bảng, tên lớp hay tên hình. Nếu thiếu dữ liệu thì ghi rõ
   "[CẦN BỔ SUNG]" thay vì đoán.
2. Tiếng Việt có dấu đầy đủ. Dùng font "Segoe UI" (đã cài trên máy, hỗ trợ dấu tốt nhất).
   Tuyệt đối không dùng font không cài như Inter, Roboto, Be Vietnam Pro.
3. Tỷ lệ slide 16:9, cỡ 1920×1080. Lề an toàn 80px mọi cạnh.
4. KHÔNG dùng emoji. KHÔNG dùng clipart/ảnh minh họa stock. KHÔNG dùng gradient.
   KHÔNG dùng box-shadow. KHÔNG đổ màu khác nhau cho từng phần tử.
5. Bảng màu cố định cho cả bộ slide:
   - Nền: #FFFFFF
   - Xanh thương hiệu (điểm nhấn chính): #0F62FE
   - Xanh đậm (tiêu đề, dải phân cách): #10367A
   - Cam CTA (nút, mốc nhấn): #FF8A00
   - Xám văn bản phụ: #5A6472
   - Xám đường kẻ bảng: #DDE3EA
   - Nền bảng xen kẽ: #F5F8FC
6. Cấu trúc slide chuẩn:
   - Dải tiêu đề trên cùng: khối xanh đậm #10367A cao 96px, chữ trắng, tiêu đề 40px bold,
     bên phải ghi "Phần 1 · Xác định yêu cầu" bằng chữ trắng 60% 20px.
   - Số trang góc phải dưới: 16px màu #5A6472.
   - Logo trường (nếu prompt có yêu cầu): Ảnh `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png`,
     cao 56px, đặt ở góc trên phải dải tiêu đề hoặc góc dưới trái.
   - Chữ thân: 22–26px, dòng cách 1.45. Tiêu đề phụ trong slide: 28px bold #10367A.
7. Với slide có sơ đồ/hình: đặt ảnh vào khung có viền 1px #DDE3EA, canh giữa, giữ tỷ lệ gốc,
   KHÔNG méo kéo ảnh, không thêm khung đẹp rối rắm. Ảnh phải đủ lớn để đọc được chữ
   (chiếm tối thiểu 60% chiều cao vùng nội dung nếu là sơ đồ chính).
8. Slide bảng: dùng bảng thật (<table>), header nền #0F62FE chữ trắng, xen kẽ #F5F8FC,
   viền 1px #DDE3EA, cỡ chữ 18–20px, cột số căn phải, không dùng markdown pipe.
9. Slide thống kê: dùng 3–4 ô số liệu lớn, số 48px bold #0F62FE, nhãn 18px #5A6472,
   nền #F5F8FC bo góc 12px, viền 1px #DDE3EA. Không thêm icon vào ô số.
10. Speaker notes (ghi vào ô Notes của slide): 100–160 từ tiếng Việt, viết như lời nói
    tự nhiên để sinh viên đọc/thuyết trình, có câu mở và câu chuyển ý. Không viết placeholder.
11. Đầu ra: một file .html hoặc .svg duy nhất cho slide đó + đoạn notes riêng.
    Nếu xuất được PPTX thì xuất 1 slide trong file đó.
12. Kiểm tra trước khi trả về: chữ không tràn khung, không đè lên nhau, không có tofu
    (ô vuông thay chữ tiếng Việt), tất cả ảnh trỏ đúng đường dẫn trong SlideAssets.
```

---

# PROMPT SLIDE 01 — BÌA

```text
Tạo slide BÌA cho bộ slide đồ án PTTKPM "Nhà thuốc FPT Long Châu".

NỘI DUNG:
- Dải xanh đậm #10367A phủ toàn bộ chiều cao slide (full-bleed background).
- Canh giữa theo chiều ngang, nội dung canh giữa từ trên xuống:
  - Dòng nhỏ 20px chữ trắng 70% độ đậm, letter-spacing rộng: "ĐẠI HỌC PHENIKAA · TRƯỜNG CÔNG NGHỆ THÔNG TIN PHENIKAA"
  - Tiêu đề lớn 54px bold trắng, 2 dòng: "PHÂN TÍCH VÀ THIẾT KẾ PHẦN MỀM"
  - Tên đề tài 34px trắng, 2 dòng: "Hệ thống Website Nhà thuốc FPT Long Châu" / "(nhathuoclongchau.com.vn)"
  - Đường kẻ ngang 1px trắng 40%, rộng 220px
  - Khối thông tin 18px trắng 85%, căn trái trong khung 760px, 5 dòng:
      "Giảng viên hướng dẫn: TS. Trương Đức Phương"
      "Khảo sát thực tế: 10/2026"
      "Lớp: …………………"
      "Nhóm: …………………"
      "Thành viên: …………………"
  - Dòng cuối: "Hà Nội, 2026" 18px trắng 70%
- Logo trường: `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png`, cao 72px,
  đặt giữa ở trên cùng (cách mép trên 70px). Nếu logo nền đen, đặt trong hộp trắng bo góc 8px.
- KHÔNG đánh số trang slide này.

SPEAKER NOTES:
"Chào thầy và các bạn. Nhóm em trình bày đồ án Phân tích và Thiết kế Phần mềm hệ thống
Website Nhà thuốc FPT Long Châu. Nhóm khảo sát trực tiếp website vào tháng 10 năm 2026.
Đồ án bám theo môn học của thầy với 5 chương: xác định yêu cầu, phân tích hệ thống,
thiết kế hệ thống, kết luận và tài liệu tham khảo. Hôm nay nhóm tập trung trình bày
toàn bộ quá trình từ yêu cầu đến thiết kế cơ sở dữ liệu."
```

---

# PROMPT SLIDE 02 — NỘI DUNG TRÌNH BÀY

```text
Tạo slide "NỘI DUNG TRÌNH BÀY" (dải tiêu đề nền #10367A, tiêu đề trắng 40px bold,
bên phải ghi "Mở đầu" 20px trắng 70%).

NỘI DUNG:
Dùng bống bốn khối ngang (4 cột bằng nhau, cách nhau 20px), mỗi khối cao 380px,
nền #F5F8FC, viền 1px #DDE3EA, bo góc 12px, padding 24px.
Mỗi khối có:
  - Số thứ tự lớn 40px bold #0F62FE ở góc trên
  - Tên phần 26px bold #10367A
  - Danh sách nội dung 18px #5A6472, giãn dòng 1.5, có gạch đầu dòng mảnh
KHỐI 1 — số "1", tên "Xác định yêu cầu"
  • Bối cảnh và mục tiêu
  • Phạm vi theo 4 mức
  • 35 thuật ngữ
  • 52 yêu cầu chức năng (FR)
  • 18 yêu cầu phi chức năng (NFR)
  • 6 tác nhân · 27 Use Case

KHỐI 2 — số "2", tên "Phân tích hệ thống"
  • Kiến trúc mức cao 4 tầng
  • 9 phân hệ nghiệp vụ PH01–PH09
  • 33 đối tượng nghiệp vụ / 7 cụm
  • 9 biểu đồ trình tự
  • 10 biểu đồ hoạt động
  • 4 biểu đồ lớp phân tích BCE

KHỐI 3 — số "3", tên "Thiết kế hệ thống"
  • 21 nhóm lớp thiết kế (Bảng 3.1)
  • 9 phân hệ và giao diện (Bảng 3.2)
  • Biểu đồ lớp thiết kế (Hình 3.1, 3.2)
  • 35 bảng cơ sở dữ liệu (Bảng 3.3)
  • ERD vật lý (Hình 3.3)
  • Thiết kế giao diện (mục 3.4)

KHỐI 4 — số "4", tên "Kết luận"
  • Tổng kết kết quả đạt được
  • Ưu điểm của hệ thống thiết kế
  • Hạn chế và hướng phát triển
  • Tài liệu tham khảo

Dưới cùng, một dòng chữ 18px #5A6472 căn giữa:
"Nhóm đã hoàn thành Phần 1 và Phần 2; Phần 3 đã hoàn thành thiết kế lớp và thiết kế CSDL."

SPEAKER NOTES:
"Bài trình bày chia làm bốn phần. Phần một xác định yêu cầu với 52 yêu cầu chức năng,
18 yêu cầu phi chức năng và 27 use case. Phần hai phân tích hệ thống với kiến trúc
4 tầng, 9 phân hệ và 33 đối tượng nghiệp vụ, được hiện thực hóa bằng 9 biểu đồ trình tự,
10 biểu đồ hoạt động và 4 biểu đồ lớp phân tích BCE. Phần ba là thiết kế: 21 nhóm lớp
thiết kế, biểu đồ lớp chi tiết và thiết kế cơ sở dữ liệu 35 bảng với ERD vật lý.
Cuối cùng là kết luận, ưu điểm, hạn chế và tài liệu tham khảo."
```

# PROMPT SLIDE 03 — BỐI CẢNH KHẢO SÁT

```text
Tạo slide "BỐI CẢNH KHẢO SÁT HỆ THỐNG" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC: hai cột — cột trái 58% nội dung chữ, cột phải 42% khối "đặc thù nghiệp vụ".

CỘT TRÁI:
- Đoạn dẫn 24px: "Nhà thuốc FPT Long Châu là chuỗi nhà thuốc bán lẻ có kênh bán hàng
  trực tuyến tại nhathuoclongchau.com.vn, bán thuốc, thực phẩm chức năng, dược mỹ phẩm,
  sản phẩm chăm sóc cá nhân và thiết bị y tế; đồng thời hỗ trợ tư vấn với dược sĩ,
  tìm nhà thuốc gần nhất và thông tin tiêm chủng."
- Tiêu đề phụ "5 nhóm sản phẩm" 24px bold #10367A, dưới là 5 pill ngang (mỗi pill
  nền #F5F8FC viền #DDE3EA bo góc 20px, chữ 18px): "Thực phẩm chức năng" · "Dược mỹ phẩm" ·
  "Thuốc" · "Chăm sóc cá nhân" · "Thiết bị y tế"
- Tiêu đề phụ "Cấu trúc danh mục 4 cấp" 24px bold #10367A, dưới là một sơ đồ ngang
  4 hộp nối bằng mũi tên, mỗi hộp nền trắng viền #0F62FE 1.5px bo góc 10px, chữ 18px
  #10367A, cao 72px:
  "Nhóm sản phẩm" → "Danh mục" → "Danh mục con" → "Sản phẩm"
  (ghi chú nhỏ 16px #5A6472 dưới: "Cây nhiều cấp, mỗi nút có thể ẩn/hiện và sắp xếp thứ tự")
- Tiêu đề phụ "Phương pháp thu thập yêu cầu" 24px bold #10367A, nội dung 20px:
  "Khảo sát trực tiếp 8 màn hình: trang chủ, menu 5 nhóm sản phẩm, trang danh sách sản phẩm,
  trang chi tiết sản phẩm, giỏ hàng, trang đặt hàng, cửa sổ đăng nhập, trang Đơn hàng của tôi.
  Chức năng không quan sát được từ phía người dùng được đánh dấu (đề xuất) trong báo cáo."

CỘT PHẢI:
- Khối nền #10367A bo góc 12px, padding 28px, chữ trắng.
- Đầu khối 22px bold "Đặc thù nghiệp vụ cần lưu ý"
- 5 mục 19px, giãn dòng 1.55, mỗi mục có một gạch đầu dòng màu #FF8A00:
  1. "Thuốc kê đơn (Rx) và một số sản phẩm cần dược sĩ tư vấn"
  2. "Một sản phẩm bán theo nhiều đơn vị tính — Hộp, Vỉ, Chai, Tuýp — mỗi đơn vị có giá và tồn kho riêng"
  3. "Mỗi sản phẩm hiển thị thương hiệu, nước sản xuất, quy cách và nhãn khuyến mãi"
  4. "Đơn hàng có 2 hình thức nhận hàng, miễn phí vận chuyển từ 300.000đ, có tùy chọn ẩn tên sản phẩm"
  5. "6 phương thức thanh toán: tiền mặt, chuyển khoản QR, MoMo, ZaloPay, thẻ quốc tế/Apple Pay, NAPAS"

SPEAKER NOTES:
"Nhóm khảo sát trực tiếp website Long Châu trong tháng 10 năm 2026. Hệ thống có năm nhóm
sản phẩm với cây danh mục bốn cấp: nhóm sản phẩm, danh mục, danh mục con và sản phẩm.
Khác biệt lớn so với thương mại điện tử thông thường là thuốc kê đơn bắt buộc phải có
tư vấn dược sĩ, và một sản phẩm được bán theo nhiều đơn vị tính với giá cùng tồn kho
riêng cho từng đơn vị. Nhóm chỉ khảo sát được tám màn hình từ phía người dùng, nên các
chức năng phía quản trị và cơ chế xác thực OTP được đánh dấu là đề xuất."
```

---

# PROMPT SLIDE 04 — VẤN ĐỀ & MỤC TIÊU

```text
Tạo slide "VẤN ĐỀ CẦN GIẢI QUYẾT VÀ MỤC TIÊU" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC: hai cột bằng nhau, cách nhau 32px. Mỗi cột có tiêu đề phụ 26px bold.
Cột trái nền #F5F8FC viền #DDE3EA bo góc 12px; cột phải nền trắng viền #0F62FE 2px
bo góc 12px.

CỘT TRÁI — tiêu đề "Vấn đề cần giải quyết", 5 mục dạng danh sách có số tròn đỏ:
  1. "Số lượng sản phẩm rất lớn, chia nhiều nhóm và nhiều cấp danh mục — cần cách duyệt,
     lọc và tìm kiếm nhanh để tìm đúng sản phẩm"
  2. "Thông tin sản phẩm mang tính chuyên môn (thành phần, dạng bào chế, quy cách, nước sản xuất)
     và khác nhau giữa các nhóm — cần tổ chức, hiển thị nhất quán"
  3. "Một số sản phẩm, đặc biệt là thuốc kê đơn, cần dược sĩ tư vấn — hệ thống phải hỗ trợ
     liên hệ dược sĩ và quản lý đơn thuốc"
  4. "Quy trình mua hàng phải thuận tiện: giỏ hàng, nhiều hình thức nhận hàng, nhiều phương thức
     thanh toán, mã giảm giá và theo dõi đơn hàng"
  5. "Phía quản trị cần quản lý tập trung danh mục, sản phẩm, giá, tồn kho, đơn hàng
     và các chương trình khuyến mãi"

CỘT PHẢI — tiêu đề "Mục tiêu của hệ thống", 4 mục có dấu kiểm màu #0F62FE:
  1. "Cung cấp cho khách hàng một kênh trực tuyến để xem, tìm, lựa chọn và mua sản phẩm
     y tế – sức khỏe một cách nhanh chóng, rõ ràng"
  2. "Hỗ trợ khách hàng tra cứu thông tin thuốc và được dược sĩ tư vấn"
  3. "Giúp quản trị viên và dược sĩ quản lý danh mục, sản phẩm, đơn hàng, đơn thuốc
     và khuyến mãi hiệu quả"
  4. "Bảo đảm an toàn thông tin cá nhân và dữ liệu giao dịch của người dùng"

Dưới cùng, dải cam #FF8A00 4px cao, trên nền #10367A, chữ trắng 21px, padding 16px 24px,
bo góc 8px, căn giữa:
"Đối tượng sử dụng: 4 nhóm người dùng — Khách vãng lai, Khách hàng, Dược sĩ, Quản trị viên;
  cộng 2 hệ thống bên ngoài — Cổng thanh toán và Dịch vụ xác thực."

SPEAKER NOTES:
"Từ khảo sát, nhóm rút ra năm vấn đề cốt lõi. Vấn đề lớn nhất là quy mô dữ liệu lớn với
cây danh mục bốn cấp khiến người dùng khó tìm sản phẩm. Vấn đề đặc thù nhất về nghiệp vụ
là thuốc kê đơn cần dược sĩ tư vấn. Bên cạnh đó là yêu cầu đồng nhất thông tin hiển thị
vì mỗi nhóm sản phẩm có đặc thù riêng. Bốn mục tiêu ở bên phải là mục tiêu thiết kế mà
toàn bộ Phần 2 và Phần 3 sẽ phục vụ. Lưu ý hệ thống có bốn nhóm người dùng và hai tác nhân
là hệ thống bên ngoài."
```

---

# PROMPT SLIDE 05 — PHẠM VI 4 MỨC

```text
Tạo slide "PHẠM VI HỆ THỐNG — 4 MỨC CHI TIẾT" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

NỘI DUNG: bảng 4 dòng, 3 cột (Mức | Nội dung | Cách trình bày trong báo cáo),
chiều cao hàng 100px, cỡ chữ 20px, header nền #0F62FE chữ trắng, xen kẽ #F5F8FC.

DÒNG 1 — Mức: "TRỌNG TÂM" (chữ đậm, màu #0F62FE)
  Nội dung: "Duyệt danh mục, danh sách, lọc – sắp xếp, tìm kiếm và xem chi tiết sản phẩm
  của 5 nhóm: Thực phẩm chức năng, Dược mỹ phẩm, Thuốc, Chăm sóc cá nhân, Thiết bị y tế;
  đặt hàng; quản lý danh mục và sản phẩm (quản trị)."
  Cách trình bày: "Mô tả Use Case đầy đủ — luồng chính, luồng thay thế, luồng ngoại lệ."

DÒNG 2 — Mức: "HỖ TRỢ"
  Nội dung: "Đăng nhập; giỏ hàng; thanh toán; theo dõi đơn hàng; tra cứu thuốc, dược chất,
  dược liệu; quản lý đơn thuốc."
  Cách trình bày: "Mô tả Use Case gọn, đủ luồng chính và ngoại lệ quan trọng."

DÒNG 3 — Mức: "ĐƠN GIẢN"
  Nội dung: "Hồ sơ và sổ địa chỉ; Flash Sale và khuyến mãi; voucher; hủy/trả hàng;
  đánh giá và bình luận; tư vấn dược sĩ; tìm nhà thuốc; tiêm chủng; bài viết sức khỏe;
  quản lý đơn hàng, khuyến mãi, người dùng và thống kê."
  Cách trình bày: "Chỉ nêu và mô tả tóm tắt trong một bảng tổng hợp."

DÒNG 4 — Mức: "NGOÀI PHẠM VI" (chữ #5A6472)
  Nội dung: "Ứng dụng di động; quản lý nhập hàng – kho – chuỗi cung ứng tại các nhà thuốc;
  nghiệp vụ tiêm chủng chi tiết (đặt lịch, đơn hàng tiêm chủng); tích hợp kỹ thuật thực tế
  với cổng thanh toán và đơn vị vận chuyển; chương trình khách hàng thân thiết."
  Cách trình bày: "Chỉ nhắc đến, không phân tích."

Dưới bảng, dòng chữ 20px #10367A đậm căn giữa:
"6 Use Case trọng tâm: UC03, UC04, UC05, UC06, UC07, UC11"

SPEAKER NOTES:
"Do quy mô lớn của website, nhóm chia phạm vi thành bốn mức để tập trung phân tích sâu.
Mức trọng tâm là toàn bộ luồng mua sắm cùng phần quản trị danh mục sản phẩm — sáu use case
trọng tâm là UC03 duyệt danh mục, UC04 xem danh sách, UC05 lọc sắp xếp, UC06 xem chi tiết,
UC07 tìm kiếm và UC11 đặt hàng. Mức hỗ trợ gồm đăng nhập, giỏ hàng, thanh toán, theo dõi
đơn và tra cứu thuốc. Mức đơn giản là những chức năng nhỏ. Ngoài phạm vi nhóm chủ động loại
app di động và nghiệp vụ kho chuỗi cung ứng vì vượt quá năng lực một đồ án môn học."
```

---

# PROMPT SLIDE 06 — THUẬT NGỮ (35)

```text
Tạo slide "THUẬT NGỮ — GLOSSARY 35 MỤC" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC: lưới 3 cột × 4 hàng = 12 thẻ thuật ngữ, mỗi thẻ cao 96px, nền #F5F8FC,
viền 1px #DDE3EA, bo góc 10px, padding 16px 20px.
Mỗi thẻ: tên thuật ngữ 20px bold #10367A, mô tả 16px #5A6472, giãn dòng 1.35.
Dùng đúng 12 thuật ngữ sau (nhóm theo vùng nghiệp vụ để dễ đọc):

NHÓM "Sản phẩm & Danh mục":
 1. Nhóm sản phẩm — "Danh mục cấp 1 trên thanh menu: 5 nhóm hàng của Long Châu."
 2. Danh mục — "Danh mục cấp 2 nằm trong một nhóm sản phẩm."
 3. Danh mục con — "Danh mục cấp 3 nằm trong một danh mục; trang danh sách hiển thị theo danh mục con."
 4. Đơn vị tính — "Đơn vị bán của sản phẩm (Hộp, Vỉ, Chai, Tuýp); mỗi đơn vị có giá riêng."
 5. Sản phẩm — "Mặt hàng được bán hoặc tra cứu, thuộc đúng một danh mục con."

NHÓM "Thuốc & Tư vấn":
 6. Thuốc kê đơn (Rx) — "Chỉ được bán khi có chỉ định của bác sĩ và cần dược sĩ tư vấn."
 7. Dược chất — "Hoạt chất có tác dụng dược lý trong thuốc."
 8. Dược liệu — "Nguyên liệu nguồn gốc tự nhiên dùng làm thuốc."
 9. Đơn thuốc — "Chỉ định dùng thuốc của bác sĩ do khách hàng cung cấp để dược sĩ xem xét."
 10. Nhóm thuốc — "Cách phân loại thuốc theo tác dụng điều trị."

NHÓM "Mua sắm & Thanh toán":
 11. Giỏ hàng — "Danh sách tạm các sản phẩm khách hàng đã chọn mua trước khi đặt hàng."
 12. Voucher — "Mã ưu đãi giảm giá áp dụng khi đặt hàng nếu thỏa điều kiện."
 13. Đơn hàng — "Yêu cầu mua hàng đã xác nhận, có mã đơn và trạng thái."
 14. Cổng thanh toán — "Dịch vụ bên ngoài xử lý giao dịch thanh toán trực tuyến."
 15. OTP — "Mã xác thực dùng một lần gửi tới số điện thoại để xác nhận người dùng."

Dưới lưới, dải xanh #0F62FE nền #EAF1FE bo góc 10px padding 18px 24px, chữ 20px #10367A:
"Tổng cộng 35 thuật ngữ — bảng 1.3 của báo cáo. Nhóm sử dụng bảng này để thống nhất ngôn ngữ
giữa các thành viên và với giảng viên."

SPEAKER NOTES:
"Nhóm xây dựng bảng 35 thuật ngữ ở bảng 1.3 để thống nhất ngôn ngữ khi phân tích và thiết kế.
Slide này trình bày 12 thuật ngữ đại diện theo ba nhóm. Điểm cần lưu ý là phân biệt rõ
ba cấp danh mục: nhóm sản phẩm là cấp một, danh mục là cấp hai, danh mục con là cấp ba —
sau này khi thiết kế CSDL, nhóm gộp ba cấp này thành một bảng danh muc có thuộc tính cap.
Thuật ngữ đơn vị tính cũng quyết định việc phải có bảng don_vi_tinh riêng vì mỗi đơn vị
có giá và tồn kho riêng."
```

# PROMPT SLIDE 07 — 52 YÊU CẦU CHỨC NĂNG

```text
Tạo slide "52 YÊU CẦU CHỨC NĂNG — 9 MODULE" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC: bảng 3 cột (Module | Mã FR | Use Case liên quan), 10 dòng (1 dòng header +
9 dòng module), cỡ chữ 20px, header #0F62FE chữ trắng, xen kẽ #F5F8FC.
Cột Module rộng 44%, cột FR 24%, cột UC 32%.

  1 – Tài khoản                    | FR-01…FR-06  | UC01, UC02
  2 – Duyệt danh mục và sản phẩm   | FR-07…FR-16  | UC03–UC06, UC10, UC19
  3 – Tìm kiếm và tra cứu          | FR-17…FR-21  | UC07, UC08
  4 – Giỏ hàng, đặt hàng, thanh toán | FR-22…FR-32 | UC10–UC13
  5 – Đơn hàng và đánh giá         | FR-33…FR-37  | UC14–UC16
  6 – Đơn thuốc và tư vấn          | FR-38…FR-40  | UC17, UC18
  7 – Khuyến mãi                   | FR-41, FR-42 | UC09
  8 – Thông tin bổ trợ              | FR-43…FR-45  | UC19–UC21
  9 – Quản trị (đề xuất)           | FR-46…FR-52  | UC22–UC27

Dưới bảng, ba ô số liệu nhỏ nằm ngang, nền #F5F8FC viền #DDE3EA bo góc 10px,
số 34px bold #0F62FE, nhãn 17px #5A6472:
  - "FR-25" / "Miễn phí vận chuyển đơn từ 300.000đ"
  - "FR-31" / "6 phương thức thanh toán: COD, QR, MoMo, ZaloPay, thẻ quốc tế/Apple Pay, NAPAS"
  - "FR-52" / "Thống kê doanh thu, số đơn hàng, sản phẩm bán chạy"

SPEAKER NOTES:
"52 yêu cầu chức năng được đánh mã FR và chia theo 9 module, mỗi yêu cầu đều được đối chiếu
với use case tương ứng ở mục 1.5. Ba yêu cầu đáng nhớ nhất là FR-25 miễn phí vận chuyển
cho đơn từ ba trăm nghìn đồng, FR-31 hỗ trợ sáu phương thức thanh toán, và FR-52 thống kê
doanh thu, số đơn và sản phẩm bán chạy cho quản trị viên. Lưu ý module 9 là quản trị
được nhóm đánh dấu là đề xuất, vì không quan sát được từ phía người dùng."
```

---

# PROMPT SLIDE 08 — 18 YÊU CẦU PHI CHỨC NĂNG

```text
Tạo slide "18 YÊU CẦU PHI CHỨC NĂNG — ĐỀU CÓ TIÊU CHÍ ĐO" (dải tiêu đề nền #10367A,
bên phải ghi "Phần 1 · Xác định yêu cầu").

BỐ CỤC:
Hàng 1: bốn ô số liệu nằm ngang, nền #F5F8FC viền #DDE3EA bo góc 12px, số 44px bold
#0F62FE, nhãn 17px #5A6472:
  - "≤ 3 giây" / "Tải đầy đủ trang chủ và trang danh sách (95% lượt truy cập)"
  - "≤ 2 giây" / "Kết quả tìm kiếm; gợi ý khi gõ ≤ 0,5 giây"
  - "≥ 1.000" / "Người dùng đồng thời khi có Flash Sale"
  - "≥ 99%" / "Sẵn sàng hoạt động trong tháng"

Hàng 2: bảng 4 cột (Mã | Nhóm | Yêu cầu | Tiêu chí đo), 18 dòng, cỡ chữ 15px,
header #0F62FE chữ trắng, xen kẽ #F5F8FC, cột Mã rộng 8%, Nhóm 13%, Yêu cầu 44%,
Tiêu chí đo 35%. Chiều cao hàng 34px.

DÙNG ĐÚNG 18 DÒNG SAU:
NFR-01 | Hiệu năng | Trang chủ và trang danh sách tải nhanh | Thời gian tải đầy đủ ≤ 3 giây với 95% lượt truy cập
NFR-02 | Hiệu năng | Tìm kiếm phản hồi nhanh | Kết quả ≤ 2 giây; từ khóa gợi ý ≤ 0,5 giây
NFR-03 | Hiệu năng | Chịu tải khi có Flash Sale | Phục vụ ≥ 1.000 người dùng đồng thời, không lỗi hệ thống
NFR-04 | Bảo mật | Mã hóa dữ liệu khi truyền tải | Toàn bộ website dùng HTTPS, TLS 1.2 trở lên
NFR-05 | Bảo mật | Bảo vệ dữ liệu cá nhân và đơn thuốc | Mã hóa số điện thoại, địa chỉ, đơn thuốc; chỉ chủ tài khoản và dược sĩ phụ trách xem đơn thuốc
NFR-06 | Bảo mật | Xác thực và phân quyền theo vai trò | Phân quyền Khách hàng – Dược sĩ – Quản trị viên; phiên hết hạn sau 30 phút không hoạt động
NFR-07 | Bảo mật | Thanh toán an toàn | Hệ thống không lưu số thẻ; giao dịch trực tuyến qua cổng thanh toán
NFR-08 | Bảo mật | Chống tấn công phổ biến | Chống SQL Injection, XSS, CSRF; giới hạn số lần yêu cầu mã xác thực và đăng nhập sai
NFR-09 | Sẵn sàng | Hoạt động liên tục | Sẵn sàng ≥ 99% thời gian trong tháng, không tính bảo trì có báo trước
NFR-10 | Độ tin cậy | Sao lưu và khôi phục dữ liệu | Sao lưu CSDL hằng ngày; khôi phục được trong ≤ 4 giờ
NFR-11 | Độ tin cậy | Toàn vẹn dữ liệu đơn hàng và tồn kho | Không mất hoặc trùng đơn khi lỗi thanh toán; tồn kho cập nhật nhất quán
NFR-12 | Sử dụng | Giao diện dễ dùng, phù hợp mọi lứa tuổi | Hoàn tất mua hàng từ giỏ hàng trong ≤ 5 bước; chữ rõ, đủ tương phản
NFR-13 | Sử dụng | Ngôn ngữ và định dạng hiển thị | Tiếng Việt có dấu; tiền tệ dạng 185.000đ; ngày dạng dd/MM/yyyy
NFR-14 | Tương thích | Chạy trên nhiều trình duyệt và thiết bị | Chrome, Edge, Firefox, Safari bản mới; giao diện co giãn máy tính – tablet – điện thoại
NFR-15 | Bảo trì | Dễ bổ sung danh mục và phương thức thanh toán | Thêm bằng cấu hình/module, không phải sửa lõi hệ thống
NFR-16 | Mở rộng | Mở rộng theo lượng dữ liệu | Hỗ trợ ≥ 100.000 sản phẩm mà thời gian phản hồi không suy giảm đáng kể
NFR-17 | Tuân thủ | Tuân thủ quy định pháp luật | Tuân thủ quy định kinh doanh dược, thương mại điện tử, bảo vệ dữ liệu cá nhân; cảnh báo thuốc kê đơn
NFR-18 | Nhất quán | Thông tin sản phẩm đồng nhất | Giá, khuyến mãi, tồn kho nhất quán giữa danh sách – chi tiết – giỏ hàng – đơn hàng

Dưới bảng, dòng 17px #5A6472:
"Điểm khác biệt của nhóm: mỗi NFR đều gắn với một tiêu chí đo được, phục vụ kiểm thử sau này."

SPEAKER NOTES:
"Điểm nhấn mạnh của bảng 1.5 là mỗi yêu cầu phi chức năng đều có tiêu chí đo lường cụ thể,
không ghi chung chung kiểu hệ thống phải nhanh. Về hiệu năng có ba yêu cầu: tải trang, tìm
kiếm và chịu tải. Về bảo mật có năm yêu cầu, trong đó NFR-07 quy định không lưu số thẻ —
đây cũng là lý do trong Phần 3 thiết kế sẽ có Adapter thanh toán thay vì lưu thẻ trong CSDL.
Về độ tin cậy, NFR-11 yêu cầu không mất hoặc trùng đơn, dẫn đến thiết kế đặt hàng trong
một giao dịch CSDL ở mục 3.3."
```

---

# PROMPT SLIDE 09 — 6 TÁC NHÂN

```text
Tạo slide "6 TÁC NHÂN CỦA HỆ THỐNG" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC:
- Bên trái (58%): bảng 5 cột (Mã | Tác nhân | Loại | Use Case chính | Mô tả rút gọn),
  7 dòng (header + 6 tác nhân), cỡ chữ 17px, header #0F62FE chữ trắng, xen kẽ #F5F8FC.
  Cột Mã 7%, Tác nhân 22%, Loại 13%, Use Case 22%, Mô tả 36%.
  DÒNG:
  AC01 | Khách vãng lai | Chính | UC01, UC03–UC09, UC19–UC21 | Chưa đăng nhập: xem danh mục, tìm kiếm, tra cứu, xem khuyến mãi
  AC02 | Khách hàng | Chính | UC02, UC10–UC18 | Đã đăng nhập: kế thừa AC01, thêm mua sắm, đơn hàng, đơn thuốc, tư vấn
  AC03 | Dược sĩ | Chính | UC01, UC17, UC18 | Nhân sự chuyên môn: tiếp nhận tư vấn, xem xét đơn thuốc
  AC04 | Quản trị viên | Chính | UC01, UC22–UC27 | Vận hành website: danh mục, sản phẩm, đơn hàng, khuyến mãi, người dùng
  AC05 | Cổng thanh toán | Phụ | UC13 | Hệ thống ngoài xử lý thanh toán trực tuyến: QR, ví điện tử, thẻ
  AC06 | Dịch vụ xác thực bên ngoài | Phụ | UC01 | Hệ thống ngoài xác thực danh tính: OTP, định danh điện tử, Facebook, Google, Apple

- Bên phải (42%): sơ đồ kế thừa tác nhân trên nền #F5F8FC viền #DDE3EA bo góc 12px,
  padding 28px. Vẽ:
    Hộp "AC01 Khách vãng lai" (nền #FFFFFF viền #5A6472 1.5px) ở trên.
    Bên dưới, lệch sang trái một chút: hộp "AC02 Khách hàng" (nền #EAF1FE viền #0F62FE 2px).
    Mũi tên trắng đầu nhọn (kiểu kế thừa) từ AC02 lên AC01.
    Bên phải, hai hộp viền đứt màu #FF8A00: "AC05 Cổng thanh toán" và "AC06 Dịch vụ xác thực".
    Ghi chú 16px #5A6472 dưới: "AC02 kế thừa toàn bộ quyền của AC01; mọi UC của AC02 đều yêu cầu đã đăng nhập (UC01)."

SPEAKER NOTES:
"Hệ thống có sáu tác nhân gồm bốn người và hai hệ thống bên ngoài. Điểm quan trọng là khách
hàng là tác nhân chuyên biệt hóa — kế thừa toàn bộ khả năng của khách vãng lai, và mọi
use case của khách hàng đều yêu cầu đã đăng nhập qua UC01. Đây là lý do trong bảng thiết kế
lớp, lớp NguoiDung có ba lớp con là KhachHang, DuocSi và QuanTriVien. Hai tác nhân bên
ngoài sẽ được cô lập sau Adapter ở Phần 3, để lỗi của dịch vụ bên ngoài không làm ngừng
các chức năng khác."
```

---

# PROMPT SLIDE 10 — 27 USE CASE + HÌNH 1.1

```text
Tạo slide "27 USE CASE — 4 NHÓM CHỨC NĂNG, 3 MỨC" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 1 · Xác định yêu cầu").

BỐ CỤC: hai cột.
CỘT TRÁI (46%): bảng 4 cột (Mức | Màu quy ước | Use Case | Ý nghĩa), 4 dòng, cỡ chữ 18px,
header #0F62FE chữ trắng. Cột "Màu quy ước" chứa một ô màu thật (khung bo góc 4px):
  TRỌNG TÂM | ô xanh #0F62FE | "UC03, UC04, UC05, UC06, UC07, UC11" | "Mô tả Use Case đầy đủ"
  HỖ TRỢ    | ô vàng #FFC94D | "UC01, UC08, UC10, UC13, UC14, UC17" | "Mô tả gọn, có ngoại lệ quan trọng"
  ĐƠN GIẢN  | ô xám #B8C2CC | "UC02, UC09, UC12, UC15, UC16, UC18, UC19, UC20, UC21, UC22, UC23, UC24, UC25, UC26, UC27" | "Mô tả tóm tắt trong bảng tổng hợp"
  NGOÀI PHẠM VI | ô xám trắng viền đứt #5A6472 | "App di động; nhập hàng – kho – chuỗi cung ứng; tiêm chủng chi tiết; tích hợp kỹ thuật cổng thanh toán; chương trình khách hàng thân thiết" | "Chỉ nhắc đến, không phân tích"

  Dưới bảng, khối nhỏ nền #EAF1FE bo gọt 10px padding 16px, chữ 19px #10367A:
  "4 nhóm chức năng: Tài khoản · Mua sắm sản phẩm · Thông tin bổ trợ · Quản trị hệ thống"

CỘT PHẢI (54%): tiêu đề phụ 22px bold #10367A "Hình 1.1 — Biểu đồ Use Case tổng quát",
  bên dưới đặt ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-1.1-use-case.png`,
  khung viền 1px #DDE3EA, canh giữa, cao tối đa 620px, giữ nguyên tỷ lệ gốc.
  Dưới ảnh, chú thích 17px #5A6472:
  "Màu xanh = trọng tâm · màu vàng = hỗ trợ · màu xám = đơn giản. Quan hệ kế thừa AC02 kế thừa AC01."

SPEAKER NOTES:
"Hệ thống có 27 use case chia thành bốn nhóm chức năng và ba mức chi tiết. Sáu use case
trọng tâm là toàn bộ luồng mua sắm: duyệt danh mục, xem danh sách, lọc sắp xếp, xem chi tiết,
tìm kiếm và đặt hàng. Trên biểu đồ, màu xanh là trọng tâm, vàng là hỗ trợ, xám là đơn giản.
Điểm cần chỉ là quan hệ kế thừa giữa khách hàng và khách vãng lai, cùng các quan hệ
include và extend giữa các use case mua sắm. Phần tiếp theo nhóm sẽ đi vào phân tích."
```

---

# PROMPT SLIDE 11 — DIVIDER PHẦN 2

```text
Tạo slide DIVIDER "PHẦN 2 — PHÂN TÍCH HỆ THỐNG".

BỐ CỤC: nền xanh đậm #10367A toàn trang. Một đường kẻ cam #FF8A00 dày 6px rộng 160px
ở phía trên nội dung. Bên dưới:
- Dòng nhỏ 22px trắng 70%, letter-spacing rộng: "PHẦN 2"
- Tiêu đề 58px bold trắng: "PHÂN TÍCH HỆ THỐNG"
- Danh sách 4 mục 22px trắng 85%, giãn dòng 1.7, căn trái trong khung 900px:
  "Kiến trúc mức cao 4 tầng và quyết định kiến trúc"
  "9 phân hệ nghiệp vụ · 33 đối tượng nghiệp vụ trong 7 cụm"
  "Hiện thực hóa Use Case: trình tự, hoạt động, lớp phân tích BCE"
- Logo trường `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png` cao 64px ở góc trên phải.

SPEAKER NOTES:
"Chuyển sang phần hai, phân tích hệ thống. Phần này trả lời bốn câu hỏi: hệ thống được
tổ chức thế nào ở mức cao, hệ thống phải ghi nhớ những đối tượng nghiệp vụ nào, các use
case trọng tâm hoạt động ra sao, và các lớp phân tích trông như thế nào."
```

---

# PROMPT SLIDE 12 — KIẾN TRÚC MỨC CAO

```text
Tạo slide "KIẾN TRÚC MỨC CAO — 4 TẦNG" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 2 · Phân tích hệ thống").

BỐ CỤC:
- Tiêu đề phụ 22px bold #10367A "Hình 2.1 — Kiến trúc mức cao của hệ thống"
- Ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-2.1-kien-truc-muc-cao.png`,
  khung viền 1px #DDE3EA, canh giữa, cao 560px, giữ tỷ lệ gốc.
- Dưới ảnh, 4 ô số liệu nằm ngang (nền #F5F8FC viền #DDE3EA bo góc 10px, số 32px bold
  #0F62FE, nhãn 16px #5A6472):
  - "4 tầng" / "Trình bày – Nghiệp vụ – Truy cập dữ liệu – Dữ liệu"
  - "9" / "Phân hệ nghiệp vụ PH01–PH09 ở tầng Nghiệp vụ"
  - "2" / "Adapter ở biên tầng Nghiệp vụ: thanh toán (AC05), xác thực (AC06)"
  - "1" / "Nhóm thành phần xuyên suốt: bảo mật, nhật ký, xử lý ngoại lệ, cấu hình"

SPEAKER NOTES:
"Nhóm chọn kiến trúc phân lớp theo mô hình client-server nhiều tầng, tầng trình bày dùng mẫu
MVC, và triển khai thành một khối monolith nhưng chia theo phân hệ. Bốn tầng là trình bày,
nghiệp vụ, truy cập dữ liệu và dữ liệu. Chín phân hệ nằm ở tầng nghiệp vụ. Hai adapter
ở cuối tầng này là nơi duy nhất giao tiếp với hệ thống bên ngoài — cổng thanh toán và
dịch vụ xác thực. Các quy tắc phụ thuộc: lời gọi chỉ đi từ tầng trên xuống, tầng trình bày
không truy cập dữ liệu trực tiếp, các phân hệ chỉ trao đổi qua interface công khai."
```

---

# PROMPT SLIDE 13 — SO SÁNH KIẾN TRÚC

```text
Tạo slide "QUYẾT ĐỊNH KIẾN TRÚC — MONOLITH PHÂN LỚP HAY MICROSERVICES" (dải tiêu đề
nền #10367A, bên phải ghi "Phần 2 · Phân tích hệ thống").

BỐ CỤC: bảng 3 cột (Tiêu chí | Monolith phân lớp theo phân hệ — ĐƯỢC CHỌN |
Microservices), 5 dòng (header + 4 tiêu chí), cỡ chữ 19px, chiều cao hàng 108px.
Cột giữa nền #EAF1FE viền #0F62FE 2px, cột phải nền #F5F8FC.

DÒNG 1 — "Độ phức tạp phát triển và vận hành"
  Giữa: "Thấp: một khối triển khai, một nơi cấu hình."
  Phải: "Cao: nhiều dịch vụ, cần hạ tầng điều phối và giám sát riêng."
DÒNG 2 — "Nhất quán đơn hàng – tồn kho (NFR-11)"
  Giữa: "Dễ: dùng chung một cơ sở dữ liệu, giao dịch cục bộ."
  Phải: "Khó: dữ liệu phân tán, cần giao dịch phân tán hoặc cơ chế bù trừ."
DÒNG 3 — "Đáp ứng quy mô yêu cầu (NFR-03, NFR-16)"
  Giữa: "Đáp ứng khi kết hợp bộ nhớ đệm, chỉ mục tìm kiếm và nhiều bản sao ứng dụng."
  Phải: "Đáp ứng tốt hơn khi quy mô rất lớn, nhưng vượt nhu cầu của đề tài."
DÒNG 4 — "Khả năng thay đổi về sau (NFR-15)"
  Giữa: "Được, nếu ranh giới phân hệ rõ; có thể tách một phân hệ thành dịch vụ riêng."
  Phải: "Rất tốt: mỗi dịch vụ độc lập."
DÒNG 5 — "Phù hợp nguồn lực và thời gian của nhóm"
  Giữa: "Phù hợp."
  Phải: "Chưa phù hợp."

Dưới bảng, dải nền #10367A bo góc 10px padding 20px 26px, chữ trắng 20px:
"Quyết định: chọn monolith phân lớp theo phân hệ. Ranh giới giữa 9 phân hệ được giữ rõ
ràng để sau này có thể tách phân hệ Tìm kiếm hoặc Thanh toán thành dịch vụ riêng."

SPEAKER NOTES:
"Đây là bảng so sánh 2.2 và là quyết định kiến trúc quan trọng nhất của Phần 2. Nhóm chọn
monolith phân lớp theo phân hệ vì độ phức tạp vận hành thấp, giao dịch đơn hàng và tồn kho
vẫn nằm trong một cơ sở dữ liệu nên đáp ứng tốt NFR-11 về toàn vẹn dữ liệu, và phù hợp với
nguồn lực nhóm sinh viên. Để không khóa đường mở rộng, ranh giới giữa các phân hệ được
giữ rõ bằng interface công khai, nên về sau có thể tách một phân hệ thành dịch vụ riêng."
```

---

# PROMPT SLIDE 14 — 9 PHÂN HỆ PH01–PH09

```text
Tạo slide "9 PHÂN HỆ NGHIỆP VỤ — PH01 đến PH09" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 2 · Phân tích hệ thống").

BỐ CỤC: lưới 3 cột × 3 hàng = 9 thẻ, mỗi thẻ cao 168px, nền trắng, viền 1px #DDE3EA,
bo góc 10px, padding 16px 18px. Mỗi thẻ có:
  - Dải màu 6px cao ở mép trên: PH01-PH03 màu #0F62FE, PH04-PH06 màu #FF8A00,
    PH07-PH09 màu #10367A (chỉ 3 màu, dùng để phân 3 nhóm chức năng)
  - Mã phân hệ 19px bold #0F62FE
  - Tên phân hệ 21px bold #10367A (2 dòng nếu cần)
  - Dòng "UC: …" 16px #5A6472
  - Dòng "FR: …" 16px #5A6472

NỘI DUNG 9 THẺ:
PH01 | Tài khoản & Xác thực | UC: UC01, UC02, UC26 | FR: FR-01–FR-06, FR-51
PH02 | Danh mục & Sản phẩm | UC: UC03–UC06, UC16, UC22, UC23 | FR: FR-07–FR-16, FR-37, FR-46–FR-48
PH03 | Tìm kiếm & Tra cứu | UC: UC07, UC08 | FR: FR-17–FR-21
PH04 | Giỏ hàng & Đơn hàng | UC: UC10, UC11, UC14, UC15, UC24 | FR: FR-22–FR-27, FR-29, FR-30, FR-32–FR-36, FR-49
PH05 | Thanh toán | UC: UC13 | FR: FR-31
PH06 | Khuyến mãi | UC: UC09, UC12, UC25 | FR: FR-28, FR-41, FR-42, FR-50
PH07 | Đơn thuốc & Tư vấn | UC: UC17, UC18 | FR: FR-38–FR-40
PH08 | Thông tin bổ trợ | UC: UC19, UC20, UC21 | FR: FR-43–FR-45
PH09 | Thống kê báo cáo | UC: UC27 | FR: FR-52

Dưới lưới, khối nền #EAF1FE bo góc 10px padding 16px 22px, chữ 19px #10367A:
"Phân hệ ≠ Module. Module nhóm theo chức năng nhìn từ người dùng; phân hệ nhóm theo dữ liệu
 và quy tắc nghiệp vụ. Vì vậy: UC22, UC23 → PH02 · UC24 → PH04 · UC25 → PH06 · UC26 → PH01 · UC27 → PH09."

SPEAKER NOTES:
"Chín phân hệ nghiệp vụ được xác định bằng cách nhóm các use case có chung dữ liệu và quy tắc
nghiệp vụ. Mỗi use case thuộc đúng một phân hệ chủ trì. Điểm dễ nhầm là phân hệ không trùng
với module ở Phần 1: các chức năng quản trị được đặt vào phân hệ nghiệp vụ tương ứng —
quản trị danh mục và sản phẩm về PH02, quản trị đơn hàng về PH04, quản trị khuyến mãi về
PH06, quản trị người dùng về PH01 và thống kê về PH09. Hai yêu cầu FR-15 và FR-16 bắt đầu
ở PH02 rồi gọi sang PH04 và PH08."
```

---

# PROMPT SLIDE 15 — 33 ĐỐI TƯỢNG NGHIỆP VỤ

```text
Tạo slide "33 ĐỐI TƯỢNG NGHIỆP VỤ — 7 CỤM" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 2 · Phân tích hệ thống").

BỐ CỤC: hai cột.
CỘT TRÁI (56%): bảng 3 cột (Cụm | Mã | Đối tượng), 8 dòng (header + 7 cụm), cỡ chữ 17px,
header #0F62FE chữ trắng, xen kẽ #F5F8FC, cột Cụm 34%, Mã 22%, Đối tượng 44%.
  1 – Người dùng & tài khoản (Hình 2.3) | EN01–EN06 | NguoiDung, KhachHang, DuocSi, QuanTriVien, LienKetDangNhap, DiaChi
  2 – Danh mục & sản phẩm (Hình 2.2) | EN07–EN12 | DanhMuc, SanPham, DonViTinh, ThuongHieu, ThuocTinhSanPham, DanhGia
  3 – Tra cứu thuốc (Hình 2.5) | EN13–EN16 | NhomThuoc, Thuoc, DuocChat, DuocLieu
  4 – Giỏ hàng, đơn hàng, thanh toán (Hình 2.3, 2.4) | EN17–EN23 | GioHang, MucGioHang, DonHang, ChiTietDonHang, YeuCauHuyTra, GiaoDichThanhToan, HoaDonDienTu
  5 – Khuyến mãi (Hình 2.2, 2.4) | EN24–EN27 | Voucher, FlashSale, SanPhamFlashSale, Banner
  6 – Đơn thuốc & tư vấn (Hình 2.5) | EN28–EN30 | DonThuoc, PhienTuVan, TinNhan
  7 – Thông tin bổ trợ (Hình 2.2, 2.4) | EN31–EN33 | NhaThuoc, VacXin, BaiViet

  Dưới bảng, khối nền #EAF1FE bo góc 10px padding 16px 20px, chữ 18px #10367A:
  "Quy tắc nhận diện — ứng viên được giữ khi thỏa đủ 3 điều kiện: (1) có dữ liệu cần lưu lâu
   dài và phân biệt được từng đối tượng; (2) có thuộc tính hoặc quan hệ riêng;
   (3) tham gia ít nhất một Use Case."

CỘT PHẢI (44%): tiêu đề phụ 21px bold #10367A "Hình 2.2 — Mô hình đối tượng cụm Danh mục,
Sản phẩm và Khuyến mãi", bên dưới đặt ảnh
`C:\Users\Think P15\Downloads\SlideAssets\hinh-2.2-danh-muc-san-pham.png`,
khung viền 1px #DDE3EA, canh giữa, cao 500px, giữ tỷ lệ gốc.

SPEAKER NOTES:
"Nhóm duyệt các danh từ trong bảng thuật ngữ, bảng yêu cầu chức năng và mô tả use case để
lập danh sách ứng viên, rồi giữ lại ứng viên thỏa đủ ba điều kiện: có dữ liệu riêng cần lưu,
có thuộc tính hoặc quan hệ riêng, và tham gia ít nhất một use case. Kết quả là 33 đối tượng
trong 7 cụm. Nhóm cũng loại hoặc gộp: ba cấp danh mục được gộp thành một lớp DanhMuc có
thuộc tính cấp; các trạng thái như trạng thái đơn hàng, vai trò chỉ là kiểu liệt kê chứ
không phải đối tượng độc lập; và các giá trị tính toán như phần trăm giảm giá, điểm đánh giá
được tính lúc hiển thị nên không lưu."
```

---

# PROMPT SLIDE 16 — TRÌNH TỰ UC11

```text
Tạo slide "HIỆN THỰC HÓA USE CASE — BIỂU ĐỒ TRÌNH TỰ UC11 ĐẶT HÀNG" (dải tiêu đề nền
#10367A, bên phải ghi "Phần 2 · Phân tích hệ thống").

BỐ CỤC:
- Tiêu đề phụ 21px bold #10367A: "Hình 2.11 — Biểu đồ trình tự UC11 Đặt hàng"
- Ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-2.11-trinh-tu-UC11.png`, khung viền
  1px #DDE3EA, canh giữa, cao 600px, giữ tỷ lệ gốc.
- Dưới ảnh, dải nền #F5F8FC bo góc 10px padding 18px 24px, chữ 19px, 5 mục dạng dòng:
  "Khách hàng → Màn hình đặt hàng → DatHangControl → DonHangRepository → Voucher → Thanh toán"
  "Các bước: mở trang đặt hàng → tính tiền → áp voucher → tạo đơn → trừ tồn kho → tạo giao dịch thanh toán"
  "Chỉ khi thanh toán thành công, DonHang mới được tạo và tồn kho mới được cập nhật"
  "Ngoại lệ 9a: thanh toán thất bại hoặc bị hủy → đơn không xác nhận, khách chọn lại phương thức"
  "Ký hiệu: mũi tên liền = gọi phương thức, mũi tên đứt = trả kết quả"

SPEAKER NOTES:
"Đây là biểu đồ trình tự của use case trọng tâm phức tạp nhất — đặt hàng. Luồng đi từ màn
hình đặt hàng vào DatHangControl, điều khiển này lấy sản phẩm đã chọn từ giỏ hàng và sổ
địa chỉ, tính tiền, áp voucher. Khi khách nhấn Hoàn tất, hệ thống kiểm tra địa chỉ, tồn kho
và giá rồi mới thanh toán. Điểm then chốt là chỉ khi thanh toán thành công thì đơn hàng mới
được tạo và tồn kho mới được trừ — nếu thanh toán thất bại thì đơn không được xác nhận và
khách hàng được chọn lại phương thức. Điều này bảo đảm yêu cầu NFR-11 không mất hoặc trùng đơn."
```

---

# PROMPT SLIDE 17 — HOẠT ĐỘNG UC11

```text
Tạo slide "BIỂU ĐỒ HOẠT ĐỘNG UC11 — ĐẶT HÀNG" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 2 · Phân tích hệ thống").

BỐ CỤC:
- Tiêu đề phụ 21px bold #10367A: "Hình 2.20 — Biểu đồ hoạt động UC11 Đặt hàng"
- Ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-2.20-hoat-dong-UC11.png`, khung viền
  1px #DDE3EA, canh giữa, cao 560px, giữ tỷ lệ gốc.
- Dưới ảnh, 4 ô nhỏ nằm ngang (nền #F5F8FC viền #DDE3EA bo góc 10px, tiêu đề 18px bold
  #10367A, nội dung 16px #5A6472):
  1. "Chọn hình thức nhận" — "Giao tận nơi hoặc nhận tại nhà thuốc; nhập hoặc chọn địa chỉ"
  2. "Chọn thanh toán" — "COD, QR, MoMo, ZaloPay, thẻ quốc tế/Apple Pay, NAPAS"
  3. "Rẽ nhánh ngoại lệ" — "Hết tồn kho → báo lỗi; thanh toán timeout → giữ đơn chờ đối soát"
  4. "Kết quả" — "Thanh toán thành công → tạo đơn, trừ tồn kho, gỡ sản phẩm khỏi giỏ hàng"

SPEAKER NOTES:
"Biểu đồ hoạt động bổ sung góc nhìn về quy trình quyết định. Trên biểu đồ trình tự ta thấy
ai gọi ai, còn trên biểu đồ hoạt động ta thấy các nhánh rẽ quyết định. Cụ thể: nếu hết
tồn kho thì báo lỗi ngay; nếu thanh toán quá thời gian thì giao dịch chuyển sang trạng thái
chờ đối soát chứ không xóa đơn — đây chính là cơ chế bảo vệ NFR-11. Biểu đồ hoạt động
cũng thể hiện rõ hai nhánh lỗi quay lại bước chọn thông tin để khách chỉnh sửa hoặc chọn
lại phương thức thanh toán."
```

---

# PROMPT SLIDE 18 — BCE UC11 + UC13

```text
Tạo slide "BIỂU ĐỒ LỚP PHÂN TÍCH BCE — ĐẶT HÀNG VÀ THANH TOÁN" (dải tiêu đề nền
#10367A, bên phải ghi "Phần 2 · Phân tích hệ thống").

BỐ CỤC:
- Tiêu đề phụ 21px bold #10367A: "Hình 2.27 — Biểu đồ lớp phân tích BCE cho UC11 và UC13"
- Ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-2.27-BCE-dat-hang.png`, khung viền
  1px #DDE3EA, canh giữa, cao 560px, giữ tỷ lệ gốc.
- Dưới ảnh, 3 ô nằm ngang (nền #F5F8FC viền #DDE3EA bo góc 10px, tiêu đề 18px bold #10367A,
  nội dung 16px #5A6472):
  1. "Boundary (2 lớp)" — "Màn hình đặt hàng, Màn hình thanh toán"
  2. "Control (2 lớp)" — "DatHangControl gọi ThanhToanControl bằng mũi tên nét đứt; ThanhToanControl làm việc với AC05"
  3. "Entity (6 lớp)" — "GioHang, DiaChi, DonViTinh, DonHang, ChiTietDonHang, GiaoDichThanhToan"

- Dòng chú thích cuối 17px #5A6472:
  "Mẫu BCE: Boundary = giao diện, Control = điều phối quy tắc nghiệp vụ, Entity = dữ liệu.
   Toàn hệ thống có 17 lớp Boundary và Control, 33 lớp Entity."

SPEAKER NOTES:
"Mô hình BCE tách thành ba nhóm: Boundary là giao diện, Control là điều phối, Entity là dữ liệu.
Điểm cốt lõi cần giảng là điều khiển đặt hàng không gọi trực tiếp cổng thanh toán mà gọi
qua điều khiển thanh toán, và ThanhToanControl được vẽ như một lớp bên ngoài vì nó làm việc
với cổng AC05. Nhờ vậy nếu sau này đổi cổng thanh toán, chỉ cần thay Adapter chứ không phải
sửa nghiệp vụ đặt hàng. Toàn hệ thống có mười bảy lớp Boundary và Control cùng ba mươi
ba lớp Entity, đây chính là đầu vào để thiết kế chi tiết ở Phần 3."
```

---

# PROMPT SLIDE 19 — DIVIDER PHẦN 3

```text
Tạo slide DIVIDER "PHẦN 3 — THIẾT KẾ HỆ THỐNG".

BỐ CỤC: nền xanh đậm #10367A toàn trang. Đường kẻ cam #FF8A00 dày 6px rộng 160px.
Bên dưới:
- Dòng nhỏ 22px trắng 70%: "PHẦN 3"
- Tiêu đề 58px bold trắng: "THIẾT KẾ HỆ THỐNG"
- Danh sách 4 mục 22px trắng 85%, giãn dòng 1.7:
  "3.1 Thiết kế cấu trúc: 21 nhóm lớp và giao diện 9 phân hệ"
  "3.2 Biểu đồ lớp thiết kế chi tiết"
  "3.3 Thiết kế cơ sở dữ liệu: 35 bảng và ERD vật lý"
  "3.4 Thiết kế giao diện"
- Logo trường `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png` cao 64px góc trên phải.

SPEAKER NOTES:
"Chuyển sang phần ba, thiết kế hệ thống. Từ mười bảy lớp phân tích ở Phần 2, nhóm chi tiết
hóa thành hai mươi mốt nhóm lớp thiết kế với đầy đủ thuộc tính và phương thức, vẽ bốn biểu
đồ lớp thiết kế, và thiết kế cơ sở dữ liệu gồm ba mươi lăm bảng cùng ERD vật lý."
```

---

# PROMPT SLIDE 20 — 21 NHÓM LỚP THIẾT KẾ

```text
Tạo slide "THIẾT KẾ CÁC LỚP — 21 NHÓM LỚP THIẾT KẾ" (dải tiêu đề nền #10367A,
bên phải ghi "Phần 3 · Thiết kế hệ thống").

BỐ CỤC: bốn cột theo loại lớp, mỗi cột cao 640px, nền trắng viền 1px #DDE3EA bo góc 12px,
padding 18px. Đầu mỗi cột là dải màu cao 52px bo góc trên, chữ trắng 19px bold, căn giữa.

CỘT 1 — dải #0F62FE — "Entity (10 lớp)"
  DanhMuc · SanPham · DonViTinh · DanhGia · ThuocTinhSanPham · GioHang · DiaChi ·
  DonHang · ChiTietDonHang · GiaoDichThanhToan
  Dưới: ghi chú 15px #5A6472 "Kèm PK, FK, UQ và phương thức: truTonKho(sl), kiemTraKeDon(),
  tinhThanhTien(), xacNhan(), huy(), capNhatKetQua()…"

CỘT 2 — dải #FF8A00 — "Control (11 lớp)"
  DanhMucControl · DanhSachControl · BoLocControl · ChiTietControl · TimKiemControl ·
  DatHangControl · ThanhToanControl · QLDanhMucControl · QLSanPhamControl
  Dưới: ghi chú 15px #5A6472 "Điều phối luồng xử lý từng Use Case: moTrangDatHang(),
  tinhTien(), apDungVoucher(ma), datHang(), taoDon(), thanhToan(), guiYeuCau()…"

CỘT 3 — dải #10367A — "Boundary (9 lớp)"
  ManHinhMenu · ManHinhDanhSach · ManHinhChiTiet · ManHinhTimKiem · ManHinhDatHang ·
  ManHinhThanhToan · ManHinhQLDanhMuc · ManHinhQLSanPham
  Dưới: ghi chú 15px #5A6472 "Hiển thị giao diện, nhận thao tác, gọi tầng nghiệp vụ.
  Không chứa quy tắc nghiệp vụ."

CỘT 4 — dải #5A6472 — "Repository & Interface"
  Repository: DanhMucRepository · SanPhamRepository · DonHangRepository · GiaoDichRepository
  Interface: ICongThanhToan · ITimKiemNangCao
  Dưới: ghi chú 15px #5A6472 "Repository: findCap2(), findByDanhMuc(), searchFullText(),
  save(), softDelete(), capNhatTon()… Interface: taoYeuCau(tt), kiemTraKetQua(maGD),
  nhanDienAnh(anh), speechToText(amThanh)"

Dưới 4 cột, dải nền #EAF1FE bo góc 10px padding 16px 24px, chữ 19px #10367A:
"Nguyên tắc thiết kế: (i) mỗi phân hệ chỉ giao tiếp qua interface công khai, không đọc trực tiếp
 dữ liệu nhau; (ii) mọi truy xuất đi qua Repository, lớp nghiệp vụ không chứa SQL;
 (iii) hệ thống ngoài (AC05, AC06) được cô lập sau Adapter."

SPEAKER NOTES:
"Từ mười bảy lớp phân tích BCE ở Phần 2, nhóm chi tiết hóa thành hai mươi mốt nhóm lớp thiết
kế. Cấu trúc gồm bốn nhóm: mười lớp thực thể mang khóa và quy tắc nghiệp vụ, mười một lớp
điều khiển điều phối luồng của từng use case, chín lớp biên chỉ lo hiển thị và nhận thao tác,
cùng các lớp Repository và Interface. Ba nguyên tắc quan trọng nhất: phân hệ chỉ giao tiếp
qua interface công khai, nghiệp vụ không chứa câu lệnh SQL, và hệ thống ngoài luôn được cô
lập sau Adapter. Đây là nền tảng để vẽ bốn biểu đồ lớp thiết kế ở mục 3.2."
```

---

# PROMPT SLIDE 21 — 9 PHÂN HỆ + INTERFACE + MẪU THIẾT KẾ

```text
Tạo slide "9 PHÂN HỆ VÀ GIAO DIỆN CUNG CẤP — BA MẪU THIẾT KẾ" (dải tiêu đề nền #10367A,
bên phải ghi "Phần 3 · Thiết kế hệ thống").

BỐ CỤC: hai cột.
CỘT TRÁI (58%): bảng 5 cột (Mã | Phân hệ | Use Case | FR | Giao diện / lớp chính),
9 dòng, cỡ chữ 15px, header #0F62FE chữ trắng, xen kẽ #F5F8FC.
Cột Mã 6%, Phân hệ 19%, UC 22%, FR 19%, Giao diện 34%.
  PH01 | Tài khoản và xác thực | UC01, 02, 26 | FR-01–06, 51 | INguoiDung (dangNhap, dangKy, doiMatKhau); Adapter xác thực OTP / định danh / MXH
  PH02 | Danh mục và sản phẩm | UC03–06, 16, 22, 23 | FR-07–16, 37, 46–48 | IDanhMuc (layCayDanhMuc, layDanhMucCap2), ISanPham (xemDanhSach, xemChiTiet, locVaSapXep); DanhMucRepository, SanPhamRepository
  PH03 | Tìm kiếm và tra cứu | UC07, 08 | FR-17–21 | ITimKiem (timKiem, goiY, xepHangKetQua), ITimKiemNangCao (nhanDienAnh, speechToText)
  PH04 | Giỏ hàng và đơn hàng | UC10, 11, 14, 15, 24 | FR-22–27, 29, 30, 32–36 | IDatHang (tinhTien, datHang, taoDon), IGioHang, DonHangRepository; gọi PH02, PH06, PH05
  PH05 | Thanh toán | UC13 | FR-31 | IThanhToan (thanhToan, capNhatGiaoDich), ICongThanhToan + Adapter thanh toán, GiaoDichRepository; không lưu số thẻ
  PH06 | Khuyến mãi | UC09, 12, 25 | FR-28, 41, 42, 50 | IVoucher (kiemTraDieuKien, tinhGiamGia), IFlashSale
  PH07 | Đơn thuốc và tư vấn | UC17, 18 | FR-38–40 | IDonThuoc (taiLen, xacNhan, tuChoi), ITuVan (moPhien, guiTinNhan)
  PH08 | Thông tin bổ trợ | UC19, 20, 21 | FR-43–45 | INhaThuoc, ITiemChung, IBaiViet
  PH09 | Thống kê và báo cáo | UC27 | FR-52 | IThongKe (tongHopDoanhThu, sanPhamBanChay); chỉ đọc dữ liệu nguồn

CỘT PHẢI (42%): tiêu đề phụ 22px bold #10367A "Ba mẫu thiết kế chính", bên dưới ba thẻ
dọc, mỗi thẻ cao 200px, nền #F5F8FC viền 1px #DDE3EA bo góc 10px, padding 18px:
  THẺ 1 — tiêu đề 20px bold #0F62FE "Repository"
    nội dung 17px #5A6472: "Áp dụng cho DanhMucRepository, SanPhamRepository, DonHangRepository,
    GiaoDichRepository. Lợi ích: lớp nghiệp vụ không chứa SQL, dễ thay đổi truy vấn, dễ kiểm thử."
  THẺ 2 — tiêu đề 20px bold #FF8A00 "Adapter"
    nội dung 17px #5A6472: "Áp dụng cho Cổng thanh toán AC05 và Dịch vụ xác thực AC06.
    Lợi ích: che giấu chi tiết giao tiếp; đổi nhà cung cấp không sửa nghiệp vụ; lỗi bên ngoài
    không làm ngừng chức năng khác."
  THẺ 3 — tiêu đề 20px bold #10367A "Factory"
    nội dung 17px #5A6472: "Áp dụng khi tạo giao dịch theo phương thức thanh toán.
    Lợi ích: thêm MoMo, ZaloPay, NAPAS bằng cấu hình, không sửa lõi hệ thống (NFR-15)."

SPEAKER NOTES:
"Bảng 3.2 cho thấy mỗi phân hệ công bố những interface nào để phân hệ khác dùng. Chú ý ba
dòng giao tiếp quan trọng: PH04 gọi PH02 để lấy giá và tồn kho, gọi PH06 để áp voucher,
và gọi PH05 để thanh toán. PH05 tích hợp cổng AC05 qua ICongThanhToan và Adapter thanh
toán; PH01 tích hợp dịch vụ AC06 qua Adapter xác thực. PH09 chỉ đọc để lập báo cáo, không
được cập nhật dữ liệu nguồn. Ba mẫu thiết kế ở bên phải — repository tách truy vấn, adapter
cô lập hệ thống ngoài, factory tạo giao dịch theo phương thức — là câu trả lời trực tiếp
cho yêu cầu NFR-15 về khả năng bảo trì."
```

---

# PROMPT SLIDE 22 — BIỂU ĐỒ LỚP THIẾT KẾ

```text
Tạo slide "BIỂU ĐỒ LỚP THIẾT KẾ — HÌNH 3.1 VÀ 3.2" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 3 · Thiết kế hệ thống").

BỐ CỤC: hai ảnh đặt cạnh nhau, mỗi ảnh chiếm 48% bề ngang.
- ẢNH TRÁI: tiêu đề phụ 19px bold #10367A "Hình 3.1 — Lớp thiết kế: duyệt danh mục và sản phẩm",
  bên dưới `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.1-bieu-do-lop-thiet-ke-1.png`,
  khung viền 1px #DDE3EA, canh giữa, cao 520px, giữ tỷ lệ gốc.
- ẢNH PHẢI: tiêu đề phụ 19px bold #10367A "Hình 3.2 — Lớp thiết kế: tìm kiếm sản phẩm",
  bên dưới `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.2-bieu-do-lop-thiet-ke-2.png`,
  khung viền 1px #DDE3EA, canh giữa, cao 520px, giữ tỷ lệ gốc.
- Dưới cùng, dải nền #EAF1FE bo góc 10px padding 16px 24px, chữ 19px #10367A:
  "Khác biệt so với biểu đồ lớp phân tích (Hình 2.25–2.28): biểu đồ lớp thiết kế thể hiện
   đầy đủ thuộc tính, phương thức, tầm nhìn (+ public, − private, # protected), kiểu tham số,
   kiểu trả về và quan hệ điều hướng giữa các lớp."

SPEAKER NOTES:
"Đây là hai biểu đồ lớp thiết kế chi tiết trong báo cáo. Điểm khác biệt quan trọng so với
biểu đồ lớp phân tích ở Phần 2 là biểu đồ thiết kế thể hiện đầy đủ thuộc tính, phương
thức, tầm nhìn, kiểu tham số và kiểu trả về, cùng quan hệ điều hướng giữa các lớp. Trên
đây là sơ đồ duyệt danh mục và sản phẩm với đầy đủ các lớp Entity, Control, Boundary,
Repository; bên phải là sơ đồ tìm kiếm sản phẩm với TimKiemControl và hai interface
ITimKiem, ITimKiemNangCao. Báo cáo còn hai hình nữa là đặt hàng – thanh toán và quản trị,
nhóm sẽ trình bày nếu thầy yêu cầu."
```

---

# PROMPT SLIDE 23 — ERD KHÁC CLASS DIAGRAM

```text
Tạo slide "ERD KHÁC GÌ CLASS DIAGRAM?" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 3 · Thiết kế hệ thống").

BỐ CỤC:
- Bảng 3 cột (Tiêu chí | ERD — mục 3.3 | Class Diagram — mục 3.2), 6 dòng (header +
5 tiêu chí), cỡ chữ 19px, header #0F62FE chữ trắng, chiều cao hàng 84px.
  Cột giữa nền #EAF1FE viền #0F62FE 2px; cột phải nền #F5F8FC.

  MỤC ĐÍCH | Mô hình dữ liệu vật lý lưu trữ | Cấu trúc hướng đối tượng khi chạy
  THÀNH PHẦN | Bảng, cột, kiểu dữ liệu, PK, FK, UQ, index | Lớp, thuộc tính, phương thức, tầm nhìn (+ − #)
  QUAN HỆ | 1:1, 1:N, N:M — ký hiệu Crow's Foot | Kế thừa, giao diện, đa hình, điều hướng
  HÀNH VI | KHÔNG có phương thức | CÓ phương thức và quy tắc nghiệp vụ
  CHUẨN | Chuẩn hóa 3NF, ràng buộc, index | Mẫu Repository, Adapter, Factory
  ÁNH XẠ | 33 đối tượng (Bảng 2.6) → 35 bảng | 17 lớp BCE (Bảng 2.9) → 21 nhóm lớp thiết kế (Bảng 3.1)

- Dưới bảng, hai khối song song:
  KHỐI TRÁI nền #F5F8FC viền 1px #DDE3EA bo góc 10px padding 16px 20px, chữ 18px #5A6472:
    tiêu đề 19px bold #10367A "Tại sao số bảng nhiều hơn số đối tượng?"
    "Gộp 3 lớp con dùng chung khóa: KhachHang, DuocSi, QuanTriVien → 3 bảng con 1–1
     với PK/FK = nguoi_dung_id. Giữ nguyên 2 bảng nối N–M: thuoc_duoc_chat,
     thuoc_duoc_lieu. 33 − 2 + 4 = 35 bảng."
  KHỐI PHẢI nền #EAF1FE bo góc 10px padding 16px 20px, chữ 18px #5A6472:
    tiêu đề 19px bold #10367A "Hai sơ đồ bổ sung cho nhau"
    "ERD trả lời: dữ liệu lưu ở đâu, khóa chính – khóa ngoại thế nào.
     Class Diagram trả lời: lớp nào chịu trách nhiệm gì, phương thức nào thực hiện quy tắc."

SPEAKER NOTES:
"Đây là câu hỏi thầy hay hỏi nhất, nên nhóm trình bày kỹ. ERD mô hình hóa dữ liệu vật lý:
bảng, cột, kiểu dữ liệu, khóa chính, khóa ngoại, và quan hệ bội số bằng ký hiệu chân quạ.
Nó không có phương thức vì bảng không hành động. Class diagram mô hình hóa cấu trúc hướng đối
tượng khi chạy: có cả dữ liệu và hành vi, có kế thừa, giao diện, đa hình và điều hướng.
Về số lượng: ba mươi ba đối tượng phân tích sinh ra ba mươi lăm bảng, vì ba lớp con dùng
chung khóa với bảng người dùng được tách thành ba bảng con một-một, và hai quan hệ nhiều
nhiều giữa thuốc với dược chất, dược liệu được giữ bằng hai bảng nối. Hai sơ đồ bổ sung
cho nhau chứ không thay thế nhau."
```

---

# PROMPT SLIDE 24 — 35 BẢNG CƠ SỞ DỮ LIỆU

```text
Tạo slide "35 BẢNG CƠ SỞ DỮ LIỆU — 7 CỤM" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 3 · Thiết kế hệ thống").

BỐ CỤC:
- Hàng 1: bốn ô số liệu nằm ngang, nền #F5F8FC viền #DDE3EA bo góc 12px, số 42px bold
  #0F62FE, nhãn 16px #5A6472:
  - "35" / "bảng vật lý"
  - "7" / "cụm nghiệp vụ"
  - "3NF" / "chuẩn hóa"
  - "2" / "bảng nối N–M: thuoc_duoc_chat, thuoc_duoc_lieu"
- Hàng 2: bảng 4 cột (STT | Tên bảng | Khóa chính | Khóa ngoại), 36 dòng (header + 35 bảng),
  cỡ chữ 13px, header #0F62FE chữ trắng, xen kẽ #F5F8FC, chiều cao hàng 25px,
  STT căn phải. Dùng đúng 35 dòng sau:

  1 | nguoi_dung | id | —
  2 | khach_hang | nguoi_dung_id (PK, FK) | → nguoi_dung.id
  3 | duoc_si | nguoi_dung_id (PK, FK) | → nguoi_dung.id
  4 | quan_tri_vien | nguoi_dung_id (PK, FK) | → nguoi_dung.id
  5 | dia_chi | id | khach_hang_id → khach_hang.nguoi_dung_id
  6 | lien_ket_dang_nhap | id | nguoi_dung_id → nguoi_dung.id
  7 | danh_muc | id | danh_muc_cha_id → danh_muc.id (tự tham chiếu)
  8 | san_pham | id | danh_muc_id → danh_muc.id; thuong_hieu_id → thuong_hieu.id
  9 | thuong_hieu | id | —
  10 | don_vi_tinh | id | san_pham_id → san_pham.id
  11 | thuoc_tinh_san_pham | id | san_pham_id → san_pham.id
  12 | danh_gia | id | san_pham_id → san_pham.id; khach_hang_id → khach_hang.nguoi_dung_id
  13 | nhom_thuoc | id | —
  14 | thuoc | id | nhom_thuoc_id → nhom_thuoc.id
  15 | duoc_chat | id | —
  16 | duoc_lieu | id | —
  17 | thuoc_duoc_chat | thuoc_id + duoc_chat_id (PK kép) | → thuoc.id; → duoc_chat.id
  18 | thuoc_duoc_lieu | thuoc_id + duoc_lieu_id (PK kép) | → thuoc.id; → duoc_lieu.id
  19 | gio_hang | id | khach_hang_id → khach_hang.nguoi_dung_id (UQ)
  20 | muc_gio_hang | id | gio_hang_id → gio_hang.id; don_vi_tinh_id → don_vi_tinh.id
  21 | don_hang | id | khach_hang_id; nha_thuoc_id (NULL); voucher_id (NULL); don_thuoc_id (NULL)
  22 | chi_tiet_don_hang | id | don_hang_id → don_hang.id
  23 | giao_dich_thanh_toan | id | don_hang_id → don_hang.id (NULL khi COD)
  24 | hoa_don_dien_tu | id | don_hang_id → don_hang.id
  25 | yeu_cau_huy_tra | id | don_hang_id → don_hang.id
  26 | flash_sale | id | —
  27 | san_pham_flash_sale | id | flash_sale_id → flash_sale.id; don_vi_tinh_id → don_vi_tinh.id
  28 | voucher | id | —
  29 | banner | id | —
  30 | don_thuoc | id | khach_hang_id; duoc_si_id → duoc_si
  31 | phien_tu_van | id | khach_hang_id; duoc_si_id → duoc_si
  32 | tin_nhan | id | phien_tu_van_id → phien_tu_van.id; san_pham_goi_y_id → san_pham.id (NULL)
  33 | nha_thuoc | id | —
  34 | bai_viet | id | —
  35 | vac_xin | id | —

- Dưới bảng, dòng 16px #5A6472:
  "Quy ước: PK id BIGINT tự tăng; FK đặt tên <bang>_id, cho phép NULL khi quan hệ tùy chọn;
   ENUM cho trạng thái; snapshot tên sản phẩm và đơn giá trong chi_tiet_don_hang để giữ lịch sử giá."

SPEAKER NOTES:
"Bảng 3.3 liệt kê ba mươi lăm bảng vật lý cùng khóa chính và khóa ngoại. Bốn quy ước quan
trọng: khóa chính là id kiểu bigint tự tăng; khóa ngoại đặt tên theo bảng cha; các quan hệ
tùy chọn cho phép null, ví dụ voucher và nhà thuốc của đơn hàng, và đơn thuốc; trạng thái
dùng kiểu enum; và bảng chi tiết đơn hàng lưu snapshot tên sản phẩm cùng đơn giá tại thời
điểm đặt, để khi giá sản phẩm thay đổi thì lịch sử đơn hàng vẫn đúng — đây cũng là cách
hiện thực yêu cầu NFR-18 về tính nhất quán."
```

---

# PROMPT SLIDE 25 — ERD VẬT LÝ

```text
Tạo slide "BIỂU ĐỒ ERD VẬT LÝ — 35 BẢNG, KÝ HIỆU CROW'S FOOT" (dải tiêu đề nền #10367A,
bên phải ghi "Phần 3 · Thiết kế hệ thống").

BỐ CỤC:
- Tiêu đề phụ 21px bold #10367A: "Hình 3.3 — Biểu đồ ERD vật lý của hệ thống"
- Ảnh `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.3-ERD-vat-ly.png`, khung viền
  1px #DDE3EA, canh giữa, chiều cao 600px, giữ nguyên tỷ lệ gốc (ảnh rộng nên đặt theo
  chiều ngang, không méo).
- Dưới ảnh, bốn ô nằm ngang (nền #F5F8FC viền #DDE3EA bo góc 10px, tiêu đề 18px bold #10367A,
  nội dung 16px #5A6472):
  1. "Ký hiệu Crow's Foot" — "Chân quạ thể hiện quan hệ một-nhiều; vòng tròn = 0; gạch ngang = bắt buộc"
  2. "Quan hệ 1–1" — "nguoi_dung ↔ khach_hang / duoc_si / quan_tri_vien"
  3. "Quan hệ 1–N" — "danh_muc → san_pham → don_vi_tinh; don_hang → chi_tiet_don_hang"
  4. "Quan hệ N–M" — "thuoc ↔ duoc_chat và thuoc ↔ duoc_lieu qua 2 bảng nối"

SPEAKER NOTES:
"ERD vật lý dùng ký hiệu chân quạ để thể hiện bội số quan hệ. Ba loại quan hệ nổi bật:
quan hệ một-một giữa bảng người dùng và ba bảng hồ sơ con; quan hệ một-nhiều từ danh mục
xuống sản phẩm rồi xuống đơn vị tính, và từ đơn hàng xuống dòng chi tiết đơn hàng; và hai
quan hệ nhiều-nhiều giữa thuốc với dược chất và dược liệu được giải quyết bằng hai bảng
nối có khóa chính kép. Điểm cần chỉ là bảng danh_muc tự tham chiếu — cột
danh_muc_cha_id trỏ về chính bảng đó, để mô hình hóa cây danh mục bốn cấp bằng một bảng duy
nhất thay vì ba bảng."
```

---

# PROMPT SLIDE 26 — THIẾT KẾ GIAO DIỆN

```text
Tạo slide "THIẾT KẾ GIAO DIỆN (MỤC 3.4)" (dải tiêu đề nền #10367A, bên phải ghi
"Phần 3 · Thiết kế hệ thống").

BỐ CỤC:
- Tiêu đề phụ 21px bold #10367A "Nguyên tắc và tiêu chuẩn thiết kế", bên dưới ba ô nằm ngang
  (nền #F5F8FC viền 1px #DDE3EA bo góc 10px, padding 16px 20px, tiêu đề 19px bold #10367A,
  nội dung 17px #5A6472):
  1. "Màu sắc" — "Chủ đạo xanh dương (tạo cảm giác tin cậy, y tế) và nền trắng.
     Nút kêu gọi hành động 'Chọn mua', 'Thanh toán' dùng màu nổi bật cam hoặc xanh dương đậm."
  2. "Typography" — "Font không chân (Sans-serif) như Roboto hoặc Arial; cỡ chữ tối thiểu 14px
     cho nội dung thường để người lớn tuổi dễ đọc."
  3. "Tính đáp ứng" — "Co giãn tự động: Desktop ≥ 1024px, Tablet 768–1023px, Mobile ≤ 767px.
     Header, footer, thanh tìm kiếm và biểu tượng giỏ hàng giữ nguyên vị trí trên mọi trang."

- Giữa slide, tiêu đề phụ 21px bold #10367A "Giao diện chủ yếu", bên dưới ba ảnh đặt cạnh
  nhau, mỗi ảnh 31% bề ngang, khung viền 1px #DDE3EA, giữ tỷ lệ gốc, cao 300px:
  - `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.4-wireframe-giao-dien.png`
    (ghi chú 16px: "Hình 3.4 — Wireframe trang danh sách và bộ lọc")
  - `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.5-giao-dien-dat-hang.png`
    (ghi chú 16px: "Hình 3.5 — Giao diện trang đặt hàng")
  - `C:\Users\Think P15\Downloads\SlideAssets\hinh-3.6-giao-dien-thanh-toan.png`
    (ghi chú 16px: "Hình 3.6 — Giao diện trang thanh toán")

- Dưới cùng, dải cam #FF8A00 4px phía trên, nền #F5F8FC, chữ 17px #5A6472, padding 14px 20px,
  bo gọt 8px:
  "Giao diện phía Khách hàng: trang chủ và Mega menu · trang danh sách kèm bộ lọc · trang chi tiết
   sản phẩm · giỏ hàng và đặt hàng · quản lý đơn thuốc và chat tư vấn dược sĩ.
   Giao diện phía Quản trị: bố cục chung (sidebar + top bar), quản lý sản phẩm, quản lý đơn hàng."

SPEAKER NOTES:
"Mục 3.4 thiết kế giao diện theo ba nhóm tiêu chuẩn: màu sắc chủ đạo xanh dương và trắng với
nút hành động màu nổi bật, font không chân cỡ tối thiểu 14px để người lớn tuổi đọc được,
và giao diện co giãn trên ba kích thước màn hình. Nhóm cũng chốt tính nhất quán: thanh
tìm kiếm, giỏ hàng, header và footer giữ nguyên vị trí trên tất cả trang. Về mặt hình ảnh,
nhóm đã có wireframe trang danh sách với khối bộ lọc bên trái và lưới sản phẩm bên phải, cùng
ảnh giao diện thật của trang đặt hàng và trang thanh toán. Phần giao diện phía quản trị chưa
có trên website thực tế nên là thiết kế đề xuất dựa trên kiến trúc đã phân tích."
```

---

# PROMPT SLIDE 27 — DIVIDER KẾT LUẬN

```text
Tạo slide DIVIDER "KẾT LUẬN".

BỐ CỤC: nền xanh đậm #10367A toàn trang. Đường kẻ cam #FF8A00 dày 6px rộng 160px.
Bên dưới:
- Dòng nhỏ 22px trắng 70%: "PHẦN 4"
- Tiêu đề 58px bold trắng: "KẾT LUẬN"
- Danh sách 4 mục 22px trắng 85%, giãn dòng 1.7:
  "Tổng kết các kết quả đạt được của đồ án"
  "Ưu điểm của hệ thống thiết kế"
  "Hạn chế và hướng phát triển"
  "Tài liệu tham khảo"
- Logo trường `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png` cao 64px góc trên phải.

SPEAKER NOTES:
"Cuối cùng là phần kết luận, tổng kết những gì nhóm đã đạt được, đánh giá ưu điểm và hạn
chế của hệ thống thiết kế, rồi kết thúc bằng tài liệu tham khảo."
```

---

# PROMPT SLIDE 28 — ƯU ĐIỂM VÀ HẠN CHẾ

```text
Tạo slide "ƯU ĐIỂM VÀ HẠN CHẾ CỦA HỆ THỐNG THIẾT KẾ" (dải tiêu đề nền #10367A, bên phải ghi
"Kết luận").

BỐ CỤC: hai cột bằng nhau, cách nhau 32px, cao 560px.
CỘT TRÁI — nền #EAF1FE viền 1px #DDE3EA bo gọt 12px, padding 26px:
  Tiêu đề 26px bold #0F62FE "Ưu điểm"
  3 mục, tiêu đề mục 21px bold #10367A + nội dung 18px #5A6472:
  1. "Tính thực tiễn cao" — "Phản ánh sát thực tế nghiệp vụ của chuỗi nhà thuốc lớn, xử lý
     tốt các bài toán đặc thù: quản lý đa đơn vị tính (Hộp, Vỉ...), phân loại thuốc kê đơn
     (Rx) cần tư vấn dược sĩ, kiểm soát tồn kho và cơ chế đặt hàng linh hoạt."
  2. "Tính mở rộng và bảo trì tốt" — "Kiến trúc phân hệ rõ ràng giúp dễ bổ sung nhóm sản phẩm
     mới, phương thức thanh toán mới, hoặc nâng cấp thành hệ thống vi dịch vụ (microservices)
     trong tương lai mà không ảnh hưởng đến lõi hệ thống."
  3. "Bảo mật và an toàn dữ liệu" — "Đề xuất giải pháp bảo mật toàn diện: HTTPS, phân quyền
     theo vai trò, mã hóa thông tin nhạy cảm, tích hợp cổng thanh toán an toàn không lưu số thẻ."

CỘT PHẢI — nền #F5F8FC viền 1px #DDE3EA bo gọt 12px, padding 26px:
  Tiêu đề 26px bold #5A6472 "Hạn chế"
  2 mục, tiêu đề mục 21px bold #10367A + nội dung 18px #5A6472:
  1. "Giới hạn về dữ liệu và quyền tiếp cận thực tế" — "Nhóm chỉ khảo sát hệ thống qua giao diện
     người dùng công khai, nên nghiệp vụ quản trị chiều sâu, cơ chế bảo mật cấp doanh nghiệp
     và hệ thống kho vận – chuỗi cung ứng chủ yếu dựa trên nghiên cứu tài liệu và suy luận
     logic của nhóm, chưa được kiểm chứng trực tiếp trên hệ thống nội bộ."
  2. "Thời gian và nguồn lực có hạn" — "Các phân hệ phụ trợ hoặc quy mô lớn (tiêm chủng chi tiết,
     tích hợp kỹ thuật cổng thanh toán thực tế với ngân hàng, ứng dụng di động) mới dừng ở
     mức mô hình hóa khái niệm, chưa thể hiện đầy đủ độ phức tạp kỹ thuật khi triển khai thực tế."

Dưới cùng, dòng 18px #10367A đậm căn giữa:
"Hướng phát triển: khảo sát sâu nghiệp vụ nội bộ, xây dựng prototype và kiểm thử theo
 bộ tiêu chí đo lường từ Bảng 1.5."

SPEAKER NOTES:
"Ưu điểm lớn nhất là tính thực tiễn — thiết kế bám sát đặc thù chuối nhà thuốc như đa đơn vị
tính, thuốc kê đơn và kiểm soát tồn kho. Điểm thứ hai là khả năng mở rộng nhờ ranh giới phân
hệ rõ ràng và các mẫu Repository, Adapter, Factory, nên sau này có thể tách dần sang
microservices mà không ảnh hưởng lõi. Điểm thứ ba là bảo mật, đặc biệt là không lưu số thẻ.
Về hạn chế, nhóm thành thật nhận ra chỉ khảo sát được giao diện công khai nên phần quản trị
chiều sâu và nghiệp vụ kho chuỗi cung ứng mang tính đề xuất. Đây cũng chính là hướng phát
triển tiếp theo của đồ án."
```

---

# PROMPT SLIDE 29 — TÀI LIỆU THAM KHẢO

```text
Tạo slide "TÀI LIỆU THAM KHẢO" (dải tiêu đề nền #10367A, bên phải ghi "Kết luận").

BỐ CỤC: bốn thẻ dọc, mỗi thẻ cao 140px, nền #F5F8FC viền 1px #DDE3EA bo góc 10px,
padding 20px 24px, cách nhau 16px. Mỗi thẻ có:
  - Số thứ tự tròn đường viền #0F62FE 1.5px, 34px, chữ 19px bold #0F62FE
  - Nguồn 21px bold #10367A
  - Chi tiết 17px #5A6472

THẺ 1 — số 1
  "Giáo trình môn Phân tích và Thiết kế Phần mềm"
  "TS. Trương Đức Phương, Trường Công nghệ Thông tin Phenikaa, 2026."
THẺ 2 — số 2
  "FPT Long Châu — Website chính thức của hệ thống Nhà thuốc FPT Long Châu"
  "Khảo sát trực tiếp tại nhathuoclongchau.com.vn, tháng 10/2026."
THẺ 3 — số 3
  "OWASP Foundation — OWASP Top 10 Web Application Security Risks"
  "Tài liệu kỹ thuật trực tuyến về bảo mật ứng dụng web, truy cập tại owasp.org/projects/top-ten."
THẺ 4 — số 4
  "Bộ Y tế — Luật Dược số 105/2016/QH13"
  "Quy định về hoạt động kinh doanh dược và thương mại điện tử dược phẩm."

Dưới cùng, dòng 17px #5A6472:
"Các chức năng được đánh dấu (đề xuất) trong báo cáo là do nhóm suy luận từ nghiệp vụ chuỗi
nhà thuốc trực tuyến, không quan sát được trực tiếp trên website."

SPEAKER NOTES:
"Tài liệu tham khảo của đồ án gồm bốn nguồn: bài giảng môn học của thầy năm 2026, website
chính thức của FPT Long Châu — nguồn khảo sát thực tế, tài liệu OWASP Top 10 cho phần bảo
mật, và Luật Dược số 105 năm 2016 cho phần tuân thủ quy định kinh doanh dược và thương mại
điện tử dược phẩm. Nhóm cũng lưu ý trong báo cáo đã đánh dấu rõ các chức năng chỉ là
đề xuất vì không quan sát được từ phía người dùng."
```

---

# PROMPT SLIDE 30 — CẢM ƠN / HỎI ĐÁP

```text
Tạo slide CUỐI "CẢM ƠN THẦY VÀ CÁC BẠN" (nền xanh đậm #10367A toàn trang, KHÔNG dải tiêu đề).

BỐ CỤC: nội dung canh giữa cả theo chiều ngang và chiều dọc.
- Logo trường `C:\Users\Think P15\Downloads\SlideAssets\00-logo-trang-bia.png`, cao 84px,
  đặt trong hộp trắng bo góc 10px, padding 12px, ở trên cùng.
- Tiêu đề 62px bold trắng: "CẢM ƠN THẦY VÀ CÁC BẠN"
- Đường kẻ cam #FF8A00 dày 5px rộng 200px, căn giữa.
- Dòng 26px trắng 90%: "Nhóm sinh viên sẵn sàng trả lời câu hỏi của thầy và các bạn."
- Khối thông tin cuối, 4 dòng 19px trắng 75%, căn giữa:
  "Đồ án: Phân tích và Thiết kế Phần mềm hệ thống Website Nhà thuốc FPT Long Châu"
  "Giảng viên hướng dẫn: TS. Trương Đức Phương"
  "Trường Công nghệ Thông tin Phenikaa — 2026"
  "nhathuoclongchau.com.vn"
- KHÔNG đánh số trang slide này.

SPEAKER NOTES:
"Nhóm em xin cảm ơn thầy và các bạn đã lắng nghe. Đồ án của nhóm là phân tích và thiết kế
lại hệ thống website Nhà thuốc FPT Long Châu với 52 yêu cầu chức năng, 18 yêu cầu phi
chức năng, 27 use case, 9 phân hệ nghiệp vụ, 33 đối tượng nghiệp vụ và 35 bảng cơ sở dữ
liệu. Nhóm sẵn sàng trả lời câu hỏi."
```

---

## PHỤ LỤC — DANH SÁCH 36 ẢNH ĐÃ TRÍCH (đã lưu tại `C:\Users\Think P15\Downloads\SlideAssets\`)

| File | Là gì | Dùng ở slide |
|---|---|---|
| `00-logo-trang-bia.png` | Logo trường | 1, 11, 19, 27, 30 |
| `hinh-1.1-use-case.png` | Hình 1.1 — Biểu đồ Use Case | 10 |
| `hinh-2.1-kien-truc-muc-cao.png` | Hình 2.1 — Kiến trúc mức cao | 12 |
| `hinh-2.2-danh-muc-san-pham.png` | Hình 2.2 — Mô hình đối tượng cụm Danh mục, Sản phẩm, Khuyến mãi | 15 |
| `hinh-2.3-nguoi-dung-gio-hang.png` | Hình 2.3 | (dự phòng) |
| `hinh-2.4-don-hang-thanh-toan.png` | Hình 2.4 | (dự phòng) |
| `hinh-2.5-don-thuoc-tu-van-tra-cuu.png` | Hình 2.5 | (dự phòng) |
| `hinh-2.6…2.10-trinh-tu-*.png` | Hình 2.6–2.10 (UC03, 04, 05, 06, 07) | (dự phòng) |
| `hinh-2.11-trinh-tu-UC11.png` | Hình 2.11 — Trình tự UC11 | 16 |
| `hinh-2.12-trinh-tu-UC13.png` | Hình 2.12 | (dự phòng) |
| `hinh-2.13…2.14-trinh-tu-*.png` | Hình 2.13–2.14 (UC22, UC23) | (dự phòng) |
| `hinh-2.15…2.24-hoat-dong-*.png` | Hình 2.15–2.24 (10 biểu đồ hoạt động) | (dự phòng) |
| `hinh-2.25…2.28-BCE-*.png` | Hình 2.25–2.28 (BCE) | (dự phòng) |
| `hinh-3.1-bieu-do-lop-thiet-ke-1.png` | Hình 3.1 — Lớp thiết kế | 22 |
| `hinh-3.2-bieu-do-lop-thiet-ke-2.png` | Hình 3.2 — Lớp thiết kế | 22 |
| `hinh-3.3-ERD-vat-ly.png` | Hình 3.3 — ERD vật lý | 25 |
| `hinh-3.4-wireframe-giao-dien.png` | Wireframe giao diện | 26 |
| `hinh-3.5-giao-dien-dat-hang.png` | Ảnh giao diện đặt hàng | 26 |
| `hinh-3.6-giao-dien-thanh-toan.png` | Ảnh giao diện thanh toán | 26 |

**Ghi chú về Hình 3.1–3.3 trong file báo cáo hiện tại:** bản `BaoCao_LongChau.docx` chỉ chứa
**2** biểu đồ lớp thiết kế (mục 3.2) và **1** ERD (mục 3.3), chưa có caption đánh số.
Prompt ở slide 22 và 25 đã gán số Hình 3.1 / 3.2 / 3.3 theo thứ tự xuất hiện trong báo cáo.
Nếu bạn bổ sung thêm biểu đồ lớp cho đặt hàng và quản trị vào Word, nhớ chỉnh lại số Hình
và bổ sung dòng vào bảng điều hướng phía trên.


