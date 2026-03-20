import re

def priority(op):
    if op == '^': return 3
    if op == '*' or op == '/': return 2
    if op == '+' or op == '-': return 1
    return 0

def process_top(values, ops):
    op = ops.pop()
    right = values.pop()
    left = values.pop()
    if op == '+': values.append(left + right)
    elif op == '-': values.append(left - right)
    elif op == '*': values.append(left * right)
    elif op == '/': values.append(int(left / right)) # Chia nguyên theo đề bài
    elif op == '^': values.append(left ** right)

def tokenize(exp):
    exp = exp.replace(" ", "")
    tokens = []
    i = 0
    while i < len(exp):
        # Trường hợp là số
        if exp[i].isdigit():
            num = ""
            while i < len(exp) and exp[i].isdigit():
                num += exp[i]
                i += 1
            tokens.append(int(num))
            continue
        
        # Trường hợp xử lý số âm (Unary Minus)
        elif exp[i] == '-':
            # Điều kiện: '-' ở đầu HOẶC sau dấu '('
            if i == 0 or exp[i-1] == '(':
                i += 1
                num = ""
                while i < len(exp) and exp[i].isdigit():
                    num += exp[i]
                    i += 1
                tokens.append(-int(num)) # Lưu luôn thành số âm
                continue
            else:
                tokens.append('-') # Đây là phép trừ (Binary)
        
        else:
            tokens.append(exp[i]) # (, ), +, *, /
        i += 1
    return tokens

def cal_infix(exp):
    # Tách số và toán tử bằng Regex để tránh lỗi gộp số thủ công
    tokens = tokenize(exp)
    
    stack_ops = []     # Chứa toán tử
    stack_values = []  # Chứa giá trị số

    for token in tokens:
        if str(token).isdigit():
            stack_values.append(int(token))
        elif token == '(':
            stack_ops.append(token)
        elif token == ')':
            while stack_ops and stack_ops[-1] != '(':
                process_top(stack_values, stack_ops)
            stack_ops.pop() # Bỏ dấu '('
        else:
            # Xử lý độ ưu tiên
            while stack_ops and priority(stack_ops[-1]) >= priority(token):
                process_top(stack_values, stack_ops)
            stack_ops.append(token)
            
    while stack_ops:
        process_top(stack_values, stack_ops)
        
    return stack_values[0]

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(str(cal_infix(exp)))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()