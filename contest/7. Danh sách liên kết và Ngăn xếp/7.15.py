def postfix_2_infix(exp):
    stack = []
    for c in exp:
        if c in '+-*/':
            op2 = stack.pop()
            op1 = stack.pop()
            new_cal = f'({op1}{c}{op2})'
            stack.append(new_cal)
        else:
            stack.append(c)
    return stack.pop()

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(postfix_2_infix(exp))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()