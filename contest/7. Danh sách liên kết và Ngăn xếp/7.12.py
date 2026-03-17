def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        stack = []
        store = []
        curr = []
        for c in s:
            if c in ['+','-','*','/']:
                stack.append(c)
                store.append(curr)
                curr = []
            else:
                curr.append(c)
                while len(curr) == 2:
                    second = curr.pop()
                    first = curr.pop()
                    cal = stack.pop()
                    curr = store.pop()
                    temp = '('+first+cal+second+')'
                    curr.append(temp)
        print(curr)                    
     
if __name__ == '__main__':
    main()
    
import sys

def solve():
    # Đọc tất cả dữ liệu từ đầu vào
    data = sys.stdin.read().split()
    if not data:
        return

    # Phần tử đầu tiên là số lượng bộ test T
    t = int(data[0])
    
    # Các phần tử tiếp theo là các biểu thức tiền tố
    results = []
    for i in range(1, t + 1):
        prefix_exp = data[i]
        stack = []
        
        # Duyệt biểu thức từ phải sang trái
        for char in reversed(prefix_exp):
            if char in "+-*/^%":
                # Lấy 2 phần tử trên cùng của stack
                # Trong tiền tố, khi duyệt ngược: 
                # phần tử lấy ra đầu tiên là toán hạng bên trái (op1)
                # phần tử lấy ra thứ hai là toán hạng bên phải (op2)
                op1 = stack.pop()
                op2 = stack.pop()
                
                # Tạo biểu thức trung tố có dấu ngoặc
                new_item = f"({op1}{char}{op2})"
                stack.append(new_item)
            else:
                # Nếu là toán hạng (A-Z, a-z, 0-9), đẩy vào stack
                stack.append(char)
        
        # Kết quả của mỗi bộ test là phần tử cuối cùng còn lại trong stack
        results.append(stack[0])
    
    # In tất cả kết quả, mỗi kết quả trên một dòng
    print('\n'.join(results))

# if __name__ == '__main__':
#     solve()
