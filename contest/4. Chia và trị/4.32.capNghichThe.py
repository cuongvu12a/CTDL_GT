def merge_arr(arr_left, arr_right, count):
    arr = []
    i = 0
    j = 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr.append(arr_left[i])
            i += 1
        else:
            count += len(arr_left) - i
            arr.append(arr_right[j])
            j += 1    
    
    while i < len(arr_left):
        arr.append(arr_left[i])
        i += 1
    while j < len(arr_right):
        arr.append(arr_right[j])
        j += 1
    
    return arr, count

def merge_sort_count(arr, count=0):
    if len(arr) <= 1:
        return arr, count
    middle = len(arr) // 2
    merge_left, count_left = merge_sort_count(arr[:middle], count)
    merge_right, count_right = merge_sort_count(arr[middle:], count)
    count += count_left + count_right
    return merge_arr(merge_left, merge_right, count)
    

def main():
    t = int(input())
    while t > 0:
        t -= 1 
        n = int(input())
        a = list(map(int, input().split()))
        arr, count = merge_sort_count(a)
        print(count)
        
if __name__ == "__main__":
    main()
        
'''
Input:
---
2
5
2 4 1 3 5
5
5 4 3 2 1

---
Output:
3
10

'''