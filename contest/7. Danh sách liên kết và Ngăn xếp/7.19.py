def detect_inc_dec(exp):
    available = [i for i in range(1, 10)]
    stack = []
    result = ''
    for c in exp:
        if c == 'I':
            min_s = min(x for x in available if x is not None)
            if len(stack):
                last_val = stack[-1]
                for i, value in enumerate(available):
                    if value != None and value + last_val >= min_s:
                        result += str(value)
                        available[i] = None
                        length = len(stack) + 1
                        for j in range(length):
                            for idx in range(i-1 , -1, -1):
                                if available[idx] is not None:
                                    result += str(available[idx])
                                    available[idx] = None
                                    break
                        stack = []
                        break
            else:
                result += str(min_s)
                available[min_s - 1] = None
        else:
            last_val = stack[-1] if len(stack) else 0
            new_val = last_val - 1
            stack.append(new_val)
    min_s = min(x for x in available if x is not None)
    if len(stack):
        last_val = stack[-1]
        for i, value in enumerate(available):
            if value != None and value + last_val >= min_s:
                result += str(value)
                available[i] = None
                length = len(stack) + 1
                for j in range(length):
                    for idx in range(i-1 , -1, -1):
                        if available[idx] is not None:
                            result += str(available[idx])
                            available[idx] = None
                            break
                stack = []
                break
    else:
        result += str(min_s)
        available[min_s - 1] = None
    return result

def solve():
    t = int(input())
    result = []
    while t:
        t -= 1
        exp = input().strip()
        result.append(str(detect_inc_dec(exp)))
    print('\n'.join(result))

if __name__ == '__main__':
    solve()
    