import re

class Node:
    def __init__(self, coeff, pow):
        self.coeff = coeff
        self.pow = pow
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def add_node(self, coeff, pow):
        """Thêm một hạng tử mới vào cuối danh sách."""
        new_node = Node(coeff, pow)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def parse(self, s):
        """Tách hệ số và số mũ từ chuỗi định dạng '3*x^10 + 2*x^0'."""
        # Sử dụng Regex để tìm tất cả các cặp (hệ số, số mũ)
        terms = re.findall(r'(\d+)\*x\^(\d+)', s)
        for c, p in terms:
            self.add_node(int(c), int(p))

    def display(self):
        """In đa thức ra màn hình đúng định dạng."""
        res = []
        temp = self.head
        while temp:
            res.append(f"{temp.coeff}*x^{temp.pow}")
            temp = temp.next
        print(" + ".join(res))

def add_polynomials(p1, p2):
    """Tính tổng hai danh sách liên kết đa thức."""
    result = Polynomial()
    curr1 = p1.head
    curr2 = p2.head

    while curr1 and curr2:
        if curr1.pow > curr2.pow:
            result.add_node(curr1.coeff, curr1.pow)
            curr1 = curr1.next
        elif curr1.pow < curr2.pow:
            result.add_node(curr2.coeff, curr2.pow)
            curr2 = curr2.next
        else:
            # Hai hạng tử có cùng số mũ
            sum_coeff = curr1.coeff + curr2.coeff
            if sum_coeff != 0:
                result.add_node(sum_coeff, curr1.pow)
            curr1 = curr1.next
            curr2 = curr2.next

    # Thêm các hạng tử còn lại nếu một trong hai danh sách chưa hết
    while curr1:
        result.add_node(curr1.coeff, curr1.pow)
        curr1 = curr1.next
    while curr2:
        result.add_node(curr2.coeff, curr2.pow)
        curr2 = curr2.next

    return result

# --- Xử lý dữ liệu đầu vào ---
def main():
    try:
        t_str = input().strip()
        if not t_str: return
        t = int(t_str)
        
        for _ in range(t):
            line1 = input().strip()
            line2 = input().strip()
            
            p1 = Polynomial()
            p2 = Polynomial()
            
            p1.parse(line1)
            p2.parse(line2)
            
            res = add_polynomials(p1, p2)
            res.display()
    except EOFError:
        pass

if __name__ == "__main__":
    main()