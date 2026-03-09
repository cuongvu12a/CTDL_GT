def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input()
        stack = []
        is_valid = True
        for i in s:
            if i == ' ':
                continue
            elif i in '([{':
                stack.append(i)
                continue
            else:
                if len(stack) == 0:
                    is_valid = False
                    break
                last = stack.pop()
                if (i == ')' and last != '(') or \
                   (i == ']' and last != '[') or \
                   (i == '}' and last != '{'):
                    is_valid = False
        
        if not is_valid or len(stack) != 0:
            print('NO')
        else: 
            print('YES')

if __name__ == "__main__":
    main()