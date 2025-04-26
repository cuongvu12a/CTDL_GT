def main():
    t = int(input())
    while t > 0:
        t-=1
        s = input()
        result = 0
        xoa = 0
        stack = []
        for c in s:
            # print(''.join(stack), result ,c, xoa)
            
            if len(stack) == 0:
                stack.append(c)
                continue
            elif stack[-1] == '[' and c == ']':
                xoa += 2
                stack.pop()
            elif  stack[-1] == ']' and c == '[':
                result += xoa + len(stack)
                stack.pop()
            else:
                stack.append(c)
                
            if len(stack) == 0:
                xoa = 0
                
        print(''.join(stack), result)

main()

'''
Input:
---
3
]][[][
[]][][
[][][]

---
Output:
4
2
0

'''