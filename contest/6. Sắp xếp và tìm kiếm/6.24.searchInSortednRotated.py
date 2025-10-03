def latestRotatedIndex(arr, n):
    left, right = 0, n - 1
    key = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            key = mid
            break
        elif arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid - 1
    return key

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

def search_rotated(arr, n, x):
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid  # trả về index

        # Nếu đoạn trái tăng dần
        if arr[l] <= arr[mid]:
            if arr[l] <= x < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            # Đoạn phải tăng dần
            if arr[mid] < x <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1  # không tìm thấy

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        key = latestRotatedIndex(arr, n)
        left, right = 0, n - 1
        if key == -1:
            left, right = 0, n - 1
        elif k >= arr[0] and k <= arr[key]:
            left, right = 0, key
        else:
            left, right = key + 1, n - 1
            
        found = binary_search(arr, k, left, right)
        found2 = search_rotated(arr, n, k)
        assert found == found2
        print(found)
        
if __name__ == "__main__":
    main()
