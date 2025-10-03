def merge_sort_in_place(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def merge(first, second):
    merged = []
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    while i < len(first):
        merged.append(first[i])
        i += 1
    while j < len(second):
        merged.append(second[j])
        j += 1
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        sorted_arr = merge_sort(arr)
        results.append(' '.join(map(str, sorted_arr)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()
