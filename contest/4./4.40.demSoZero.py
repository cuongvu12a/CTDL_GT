def handle(a):
    ZERO = 0
    left = 0
    right = len(a) - 1
    last_zero = -1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] == ZERO:
            last_zero = middle
            left = middle + 1
        else:
            right = middle - 1
    
    return last_zero + 1
        

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(handle(a))
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
3
12
0 0 0 0 0 0 0 0 0 1 1 1
5
0 0 0 0 0
6
1 1 1 1 1 1

---
Output:
5
4
'''
