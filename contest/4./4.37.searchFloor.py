def _search_floor_recursion(a, left, right, x):
    middle = (left + right) // 2
    if left > right:
        return -1
    
    if a[middle] == x:
        return middle
    if a[middle] < x:
        if middle + 1 > right or a[middle + 1] > x:
            return middle
        else:
            return _search_floor_recursion(a, middle + 1, right, x)
    
    if a[middle] > x:
        return _search_floor_recursion(a, left, middle - 1, x)
    
def search_floor(a, left, right, x):
    res = -1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] == x:
            return middle
        if a[middle] < x:
            res = middle
            left = middle + 1
        else:
            right = middle -1
    return res
        
    
def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        result = search_floor(a, 0, n - 1, x)
        if result == -1:
            print(-1)
        else:
            print(result + 1)
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

---
Output:
-1
2
4
'''
            
        
        