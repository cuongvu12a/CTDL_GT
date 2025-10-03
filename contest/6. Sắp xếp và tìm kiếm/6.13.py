def first_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            right = mid - 1  # tiếp tục tìm bên trái
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurrence(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1  # tiếp tục tìm bên phải
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    if first == -1:
        return -1
    last = last_occurrence(arr, x)
    return last - first + 1

print(count_occurrences([1,1,2,2,2,2,3], 2))  # 3
print(count_occurrences([1,1,2,2,2,2,3], 6))  # -1
