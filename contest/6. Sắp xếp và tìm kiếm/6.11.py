def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        left = 0
        right = n - 1
        min_sum = float('inf')
        while left < right:
            diff = arr[right] + arr[left]
            if abs(diff) < abs(min_sum):
                min_sum = diff

            if diff == 0:
                break
            elif diff > 0:
                right -= 1
            else:
                left += 1
        results.append(min_sum)

    print('\n'.join(map(str, results)))
    
if __name__ == "__main__":
    main()
    