def decode_string(s):
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            # Xử lý số có nhiều chữ số
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Lưu lại xâu hiện tại và số lần lặp vào stack
            stack.append((current_str, current_num))
            # Reset để xử lý nội dung bên trong ngoặc
            current_str = ""
            current_num = 0
        elif char == ']':
            # Lấy dữ liệu từ stack khi kết thúc một cụm
            last_str, num = stack.pop()
            # Nhân bản xâu hiện tại và nối với xâu phía trước
            current_str = last_str + (num * current_str)
        else:
            # Nếu là ký tự chữ, cộng vào xâu hiện tại
            current_str += char
            
    return current_str

def solve(chars):
    stack = []
    i = len(chars) - 1
    while i >= 0:
        curr = chars[i]
        if curr == ']':
            stack.append(curr)
        elif curr == '[':
            temp = ''
            while stack and stack[-1] != ']':
                temp += stack.pop()
            if stack: stack.pop()
            stack.append(temp)
        elif curr.isdigit():
            # Gom toàn bộ số
            num_str = ''
            while i >= 0 and chars[i].isdigit():
                num_str = chars[i] + num_str # Cộng vào bên trái vì đang duyệt ngược
                i -= 1
            i += 1 # Bù lại chỉ số i vì vòng while bên ngoài cũng giảm i
            
            last_str = stack.pop()
            stack.append(last_str * int(num_str))
        else:
            stack.append(curr)
        i -= 1
    return "".join(stack[::-1]) # Đảo ngược stack lần cuối nếu cần

def main():
    t = int(input())
    result = []
    while t:
        t -= 1
        chars = input().strip()
        result.append(solve(chars))
    print('\n'.join(result))

if __name__ == '__main__':
    main()