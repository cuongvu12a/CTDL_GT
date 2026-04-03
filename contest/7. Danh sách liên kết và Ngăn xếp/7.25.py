class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def solve():
    try:
        line = input().split()
        if not line: return
        n, m = map(int, line)
    except EOFError:
        return

    if n == 1:
        print(1)
        return

    # Bước 1: Khởi tạo danh sách liên kết vòng
    head = Node(1)
    prev = head
    for i in range(2, n + 1):
        new_node = Node(i)
        prev.next = new_node
        prev = new_node
    prev.next = head  # Nối đuôi về đầu thành vòng tròn

    # Bước 2: Bắt đầu trò chơi
    curr = head
    while curr.next != curr:
        # Đếm M người (di chuyển M-1 bước từ người hiện tại)
        # Hoặc di chuyển M bước để tìm người đứng TRƯỚC người bị loại
        for _ in range(m - 1):
            curr = curr.next
        
        # Người bị loại là curr.next
        # Người đứng trước (curr) sẽ nối thẳng tới người sau người bị loại
        # print(f"Loại người thứ: {curr.next.data}") # Debug nếu cần
        curr.next = curr.next.next
        
        # Người tiếp theo người bị loại bắt đầu đếm từ 1
        curr = curr.next

    print(curr.data)

def main():
    t_str = input().strip()
    if t_str:
        t = int(t_str)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()