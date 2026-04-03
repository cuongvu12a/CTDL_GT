import heapq
from collections import Counter

def min_value_after_k_removals(s: str, k: int) -> int:
    # Trường hợp K lớn hơn hoặc bằng độ dài xâu thì xâu sẽ rỗng
    if k >= len(s):
        return 0

    # Bước 1: Đếm tần suất xuất hiện của mỗi ký tự
    counts = Counter(s)
    
    # Bước 2: Đưa các tần suất vào Max-Heap
    # Python chỉ có Min-Heap nên ta dùng dấu trừ (-) để biến nó thành Max-Heap
    max_heap = [-count for count in counts.values()]
    heapq.heapify(max_heap)
    
    # Bước 3: Thực hiện loại bỏ K ký tự
    for _ in range(k):
        if not max_heap:
            break
            
        # Lấy phần tử lớn nhất (giá trị nhỏ nhất do dùng dấu trừ)
        highest = heapq.heappop(max_heap)
        
        # Giảm số lần xuất hiện đi 1 (tức là cộng thêm 1 vào số âm)
        # Nếu sau khi giảm vẫn > 0 (tức giá trị âm < 0) thì đẩy lại vào heap
        if highest < 0:
            heapq.heappush(max_heap, highest + 1)
            
    # Bước 4: Tính tổng bình phương các giá trị còn lại
    result = sum(count**2 for count in max_heap)
    
    return result

# --- Chạy thử nghiệm ---
s_input = "AAABBCD"
k_input = 2
print(f"Xâu: {s_input}, K = {k_input}")
print(f"Giá trị nhỏ nhất: {min_value_after_k_removals(s_input, k_input)}")

s_input_2 = "ABC"
k_input_2 = 3
print(f"Xâu: {s_input_2}, K = {k_input_2}")
print(f"Giá trị nhỏ nhất: {min_value_after_k_removals(s_input_2, k_input_2)}")