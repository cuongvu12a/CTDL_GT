def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input().strip()
        stack = []
        result = False
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                has_operator = False
                while True:
                    last = stack.pop()
                    if last == '(':
                        break
                    elif last in '+-*/':
                        has_operator = True
                if not has_operator:
                    result = True
                    break
        print('YES' if result else 'NO')

if __name__ == "__main__":
    main()