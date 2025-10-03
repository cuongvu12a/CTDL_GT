def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        left, right = 0, n - 1
        for i in range(n - 2):
            if arr[i] > arr[i + 1]:
                left = i
                break
            
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                right = i
                break
        
        min, max = arr[left], arr[left]
        for i in range(left, right + 1):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
        
        for i in range(left):
            if arr[i] > min:
                left = i
                break
        
        for i in range(n - 1, right, -1):
            if arr[i] < max:
                right = i
                break
        
        print(left + 1, right + 1)

if __name__ == "__main__":
    main()
