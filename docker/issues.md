Lỗi này trong Docker được gọi là:

**"Docker NAT Bridge IP leakage"** hoặc phổ biến hơn là **"Docker bridge network trust issue"**

Cụ thể hơn, khi tìm kiếm bạn có thể dùng các từ khóa:

- **`Docker bridge NAT localhost bypass`** — mô tả đúng nhất vấn đề
- **`Docker container sees 172.x.x.x instead of localhost`** — mô tả triệu chứng
- **`Docker host networking vs bridge networking`** — để hiểu giải pháp `network_mode: host`

---

**Bản chất ngắn gọn:** Khi app trong container kết nối ra ngoài (hoặc ngược lại), Docker dịch IP qua NAT bridge (`172.17.0.x`, `172.18.0.x`...) thay vì giữ nguyên `127.0.0.1`. Các app có logic "chỉ trust localhost" sẽ từ chối kết nối vì thấy IP lạ — đó là lý do OpenClaw bắt pairing dù token đúng.