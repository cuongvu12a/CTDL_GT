def handle(a, b):
    left = 0
    right = len(b) - 1
    last_idx_equal = 0
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b[mid]:
            last_idx_equal = mid
            left = mid + 1
        if a[mid] < b[mid]:
            right = mid - 1
        
    real_idx = last_idx_equal + 1
    return real_idx + 1 # first item not equal
            

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(handle(a, b))
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
7
2 4 6 8 9 10 12
2 4 6 8 10 12
6
3 5 7 9 11 13
3 5 7 11 13

---
Output:
5
4
'''
