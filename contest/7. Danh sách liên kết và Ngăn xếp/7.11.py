def priority(op):
    if op == '^': return 3
    if op == '*' or op == '/': return 2
    if op == '+' or op == '-': return 1
    return 0

def infix_to_postfix(exp):
    stack = []
    result = ""
    
    for char in exp:
        # Nếu là toán hạng, thêm vào kết quả
        if char.isalnum():
            result += char
        # Nếu là dấu mở ngoặc, đẩy vào stack
        elif char == '(':
            stack.append(char)
        # Nếu là dấu đóng ngoặc
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop() # Xóa dấu '('
        # Nếu là toán tử
        else:
            while stack and priority(stack[-1]) >= priority(char):
                result += stack.pop()
            stack.append(char)
            
    # Lấy nốt các toán tử còn lại trong stack
    while stack:
        result += stack.pop()
    return result

# Xử lý Input
import sys

def solve():
    try:
        line = sys.stdin.readline()
        if not line: return
        t = int(line.strip())
        for _ in range(t):
            exp = sys.stdin.readline().strip()
            if exp:
                print(infix_to_postfix(exp))
    except EOFError:
        pass


if __name__ == "__main__":
    solve()