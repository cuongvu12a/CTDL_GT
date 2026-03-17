def prefix_2_postfix(exp):
    stack = []
    exp_rev = reversed(exp)
    for c in exp_rev:
        if c in "+-*/^%":
            first = stack.pop()
            second = stack.pop()
            new_item = f"{first}{second}{c}"
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
        result.append(prefix_2_postfix(exp))
    print('\n'.join(result))
        

if __name__ == '__main__':
    solve()