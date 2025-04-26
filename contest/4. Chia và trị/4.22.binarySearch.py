def binarySearch(arr, left, right, k):
    middle = left + ((right - left) // 2)

    if left > right:
        return -1
    if arr[middle] == k:
        return middle
    if arr[middle] > k:
        return binarySearch(arr, left, middle - 1, k)
    return binarySearch(arr, middle + 1, right, k)

def main():
    t = int(input())
    while t > 0:
        t-=1
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        
        print(binarySearch(arr, 0, n - 1, k))

main()
        
'''
Input:
---
2
5 3
1 2 3 4 5
6 5
0 1 2 3 9 10

---
Output:
3
NO
'''