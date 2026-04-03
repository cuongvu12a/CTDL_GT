### 1. File giống như một "Tờ giấy"
Quyền của file chỉ tác động lên **nội dung trên tờ giấy** đó:
* **`r` (Read):** Bạn được phép đọc chữ trên giấy.
* **`w` (Write):** Bạn được phép cầm bút **tẩy xóa, viết đè** lên nội dung cũ.
* **`x` (Execute):** Nếu tờ giấy là một bản hướng dẫn, bạn được phép làm theo nó.

> **Lưu ý:** Cái tên của tờ giấy không nằm trên tờ giấy đó. Vì vậy, quyền `w` của file **không** cho phép bạn đổi tên hay xé bỏ tờ giấy.

---

### 2. Thư mục giống như một "Cái hộp" (hoặc Ngăn kéo)
Quyền của thư mục tác động lên **những món đồ (files)** nằm trong cái hộp đó:
* **`r` (Read):** Bạn được phép nhìn vào trong hộp để xem có những gì (`ls`).
* **`w` (Write):** Bạn được phép **nhét thêm đồ mới** vào, **nhấc đồ cũ vứt đi** (xoá file), hoặc **dán nhãn lại** (đổi tên file).
* **`x` (Execute):** Bạn được phép thò tay vào trong hộp để chạm vào đồ vật (`cd` hoặc truy cập sâu hơn).



---

### 3. Tại sao "Tên file" lại thuộc về Thư mục?
Trong cấu trúc dữ liệu của Linux, một thư mục thực chất là một danh sách các cặp: 
**`Tên File` <---> `Địa chỉ trên ổ cứng (Inode)`**

Khi bạn đổi tên hoặc xoá file:
1. Bạn đang sửa đổi danh sách này.
2. Vì danh sách này nằm **trong thư mục**, nên bạn cần quyền `w` của thư mục đó.

---

### Tổng kết bằng một bảng "Quyền lực"

| Hành động | Cần quyền trên FILE | Cần quyền trên THƯ MỤC |
| :--- | :---: | :---: |
| Xem nội dung file | `r` | `x` |
| Sửa nội dung file | `w` | `x` |
| **Đổi tên file** | Không cần | **`w`** |
| **Xoá file** | Không cần | **`w`** |
| Chạy file (script) | `x` | `x` |

---

### Ví dụ cực đoan để bạn dễ hình dung:
Nếu mình có một file cực kỳ quan trọng là `luong_thang_nay.txt`:
* File có quyền: `-rwxrwxrwx` (Ai cũng có thể đọc/sửa/chạy).
* Nhưng thư mục chứa nó có quyền: `dr-x------` (Bạn chỉ có thể đọc và vào xem, không được ghi).

**Kết quả:** Kẻ xấu có thể vào sửa số tiền lương của bạn (vì file có `w`), nhưng chúng **không thể xoá** hay **đổi tên** file đó để làm nó biến mất (vì thư mục không có `w`).

Bạn có muốn mình chỉ cho cách kiểm tra xem một thư mục có đang bật **Sticky Bit** (quyền bảo vệ file khỏi bị xoá nhầm) như mình đã nhắc tới ở trên không? Nó sẽ hiển thị là chữ `t` ở cuối chuỗi quyền đấy!