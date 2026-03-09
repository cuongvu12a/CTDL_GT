def main_ai():
    s = input().strip()
    stack = []
    pairs = []  # temp renamed to pairs
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            pairs.append((stack.pop(), i))
    
    results = set()  # Use set for unique strings
    m = len(pairs)
    for mask in range(1, 1 << m):  # From 1 to 2^m - 1, skip empty
        crr = list(s)
        for j in range(m):
            if mask & (1 << j):
                x, y = pairs[j]
                crr[x] = ''
                crr[y] = ''
        results.add(''.join(crr))
    
    # Sort and print
    for expr in sorted(results):
        print(expr)

def sinh_to_hop(pos, k, n, current, result):
    if len(current) == k:
        result.append(current[:])     # copy list
        return
    
    # Từ pos trở đi mới chọn được
    for i in range(pos, n+1):
        current.append(i)
        sinh_to_hop(i+1, k, n, current, result)   # i+1 để không lặp và giữ thứ tự tăng dần
        current.pop()   # backtrack

def main():
    s = input().strip()
    stack = []
    temp = []
    chars = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            temp.append((stack.pop(), i))
        chars.append(c)
    
    res = []
    for i in range(1, len(temp)+1):
        crr_res = []
        sinh_to_hop(1, i, len(temp), [], crr_res)
        res.extend(crr_res)
    
    for i in res:
        crr_chars = chars.copy()
        for j in i:
            x, y = temp[j-1]
            crr_chars[x] = ''
            crr_chars[y] = ''
        print(''.join(crr_chars))
        
    
if __name__ == "__main__":
    # main()
    main_ai()