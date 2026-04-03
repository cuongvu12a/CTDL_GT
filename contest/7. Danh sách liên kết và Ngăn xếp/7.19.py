def find_smallest_number(s):
    result = []
    stack = []
    
    # Duyệt qua n + 1 số (vì chuỗi độ dài n tạo ra số có n + 1 chữ số)
    for i in range(len(s) + 1):
        # Đẩy số (i + 1) vào stack
        stack.append(i + 1)
        
        # Nếu gặp 'I' hoặc là ký tự cuối cùng
        if i == len(s) or s[i] == 'I':
            while stack:
                result.append(str(stack.pop()))
                
    return "".join(result)

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(str(find_smallest_number(exp)))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()
    