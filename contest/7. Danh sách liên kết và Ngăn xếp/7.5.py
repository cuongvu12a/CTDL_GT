def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input().strip()
        stack = []
        last_idx = -1
        curr = 0
        for idx, i in enumerate(s):
            if i == '(':
                stack.append(i)
                continue
            else:
                if len(stack) == 0:
                    last_idx = idx
                    curr = max(curr, idx - last_idx)
                else:
                    stack.pop()
            curr = max(curr, idx - last_idx - len(stack))
        print(curr)

if __name__ == "__main__":
    main()