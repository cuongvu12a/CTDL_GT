from math import floor
from math import ceil

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, s, m = map(int, input().split())
        
        if (s >= 7 and n * 6 < m * 7) or (s * m > (s - floor(s / 7)) * n): 
            print(-1)
            
        else:
            print(ceil(s * m / n))
            
main()

'''
Input:
---
3
16 10 2
20 10 30
8 10 7

---
Output:
2
-1
-1
'''