def min_swaps_to_sort(arr):
    n = len(arr)
    # Tạo danh sách (giá trị, chỉ số gốc)
    arr_pos = list(enumerate(arr))
    print(arr_pos)
    # Sắp xếp theo giá trị
    arr_pos.sort(key=lambda x: x[1])
    print(arr_pos)

    visited = [False] * n
    swaps = 0

    for i in range(n):
        # Bỏ qua nếu đã đúng vị trí hoặc đã thăm
        if visited[i] or arr_pos[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = arr_pos[j][0]  # nhảy đến vị trí tiếp theo trong cycle
            cycle_size += 1

        if cycle_size > 0:
            swaps += (cycle_size - 1)

    return swaps

def handleWhenNotDuplicateValue(arr):
    index = {}
    for i in range(len(arr)):
        if arr[i] not in index:
            index[arr[i]] = i
    arr_sort = arr.copy()
    arr_sort.sort()
    count_swap = 0
    for i in range(len(arr)):
        if arr[i] == arr_sort[i]:
            continue
        else:
            count_swap += 1
            swap_index = index[arr_sort[i]]
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            index[arr[i]] = i
            index[arr[swap_index]] = swap_index
            
    return count_swap

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # results.append(handleWhenNotDuplicateValue(arr))
        results.append(min_swaps_to_sort(arr))
        
    print("\n".join(map(str, results)))
        
        
if __name__ == "__main__":
    main()
