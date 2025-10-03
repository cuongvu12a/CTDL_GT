def binary_search(arr, k, left, right):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        left, right = 0, n - 1
        ans = binary_search(arr, k, left, right)
        print(ans)

if __name__ == "__main__":
    main()
