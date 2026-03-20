def cal_postfix(exp):
    stack = []
    for c in exp:
        if c in '+–-*/':
            op2 = int(stack.pop())
            op1 = int(stack.pop())
            if c == '+':
                stack.append(op1+op2)
            elif c in '–-':
                stack.append(op1-op2)
            elif c == '*':
                stack.append(op1*op2)
            else:
                stack.append(op1/op2)
        else:
            stack.append(c)
    return stack.pop()

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(str(cal_postfix(exp)))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()