def main():
    t = int(input())
    while t:
        t -= 1
        s = input().strip()

        stack = [False]
        ans = []

        for i, c in enumerate(s):
            if c == '(':
                if i > 0 and s[i - 1] == '-':
                    stack.append(not stack[-1])
                else:
                    stack.append(stack[-1])

            elif c == ')':
                stack.pop()

            elif c == '+':
                ans.append('-' if stack[-1] else '+')

            elif c == '-':
                ans.append('+' if stack[-1] else '-')

            else:
                ans.append(c)

        print(''.join(ans))


if __name__ == "__main__":
    main()
    
    