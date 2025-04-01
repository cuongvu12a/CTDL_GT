def main():
    t = int(input())
    while t > 0:
        t -= 1
        a, b = map(int, input().split())
        temp = [1, 1]
        for i in range(2, a + 1):
            temp.append(temp[i - 2] + temp[i - 1])
            
        while b > 2:
            if b > temp[a - 2]:
                b -= temp[a - 2]
                a -= 1
            else:
                a -= 2
        
        if a == 1:
            print('A')
        else:
            print('B')
        
main()

'''
Input:
---
2
6 4
8 19

---
Output:
A
B
'''