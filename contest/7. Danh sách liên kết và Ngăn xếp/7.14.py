def postfix_2_prefix(exp):
    stack = []
    for c in exp:
        if c in '+-*/^%':
            second = stack.pop()
            first = stack.pop()
            new_item = f"{c}{first}{second}"
            stack.append(new_item)
        else:
            stack.append(c)
    return stack[0]

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(postfix_2_prefix(exp))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()