def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        print(left + 1)

if __name__ == "__main__":
    main()
