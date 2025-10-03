def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    place_of_value = [0] + count[:-1]
    result = [0] * len(arr)
    for num in arr:
        result[place_of_value[num]] = num
        place_of_value[num] += 1
    
    return result

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = counting_sort(arr)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
