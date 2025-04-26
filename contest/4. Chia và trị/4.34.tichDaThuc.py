def main():
    t = int(input())
    while t > 0:
        t -= 1
        m, n = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = [0] * (m + n - 1)
        for i in range(m):
            for j in range(n):
                c[i + j] += a[i] * b[j]
        
        print(" ".join(map(str, c)))
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
4 3
1 0 3 2
2 0 4
5 4
1 9 3 4 7
4 0 2 5

---
Output:
2 0 10 4 12 8
4 36 14 39 79 23 34 35
'''