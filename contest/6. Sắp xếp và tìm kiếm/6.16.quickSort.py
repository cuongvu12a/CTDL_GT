def partition(arr, low, high):
    pivot = arr[high]  # chọn phần tử cuối làm pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)   # sắp xếp bên trái pivot
        quick_sort_in_place(arr, pi + 1, high) # sắp xếp bên phải pivot

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = quick_sort(arr)
        results.append(' '.join(map(str, sorted_arr)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()