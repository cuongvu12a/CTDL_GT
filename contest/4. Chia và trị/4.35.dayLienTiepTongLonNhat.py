def main():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        max = float('-inf')
        s = 0
        for i in range(n):
            s += a[i]
            if s > max:
                max = s
            if s < 0:
                s = 0
                
        print(max)

if __name__ == "__main__":
    main()
    
'''
Input:
---
1
8
-2 -5 6 -2 -3 1 5 -6

---
Output:
7
'''