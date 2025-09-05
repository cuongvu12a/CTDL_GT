"""
BÀI 3. Sorting 3

Đề bài:
Cho mảng A[] gồm n phần tử.  
Hãy tìm số phép đổi chỗ ít nhất giữa các phần tử của mảng để mảng A[] được sắp xếp tăng dần.  

Ví dụ:
A = [4, 3, 2, 1]  
=> Ta cần ít nhất 2 phép đổi chỗ: 
   - Swap(A[0], A[3]) 
   - Swap(A[1], A[2])  

Input:
- Dòng đầu tiên: số lượng bộ test T (1 ≤ T ≤ 100).
- Với mỗi test:
    + Dòng đầu tiên: n (số phần tử của mảng, 1 ≤ n ≤ 10^3).
    + Dòng tiếp: n số nguyên A[i], cách nhau bởi khoảng trắng.

Output:
- Với mỗi test, in ra số phép đổi chỗ ít nhất để sắp xếp mảng.

Ví dụ:
Input:
2
4
4 3 2 1
5
1 5 4 3 2

Output:
2
2
"""

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
