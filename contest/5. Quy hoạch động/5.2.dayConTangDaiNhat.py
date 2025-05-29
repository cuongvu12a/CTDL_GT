import bisect

def longest_increasing_subsequence(arr):
    tail = []
    for num in arr:
        # Tìm vị trí cần chèn num vào để giữ tail tăng
        idx = bisect.bisect_left(tail, num)
        if idx == len(tail):
            tail.append(num)
        else:
            tail[idx] = num
    return len(tail)

def length_of_lis(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def main():
    int(input())
    n = list(map(int, input().split()))
                
    print(length_of_lis(n))
    print(longest_increasing_subsequence(n))
    

if __name__ == "__main__":
    main()
    
'''
Input:
---
6
1 2 5 4 6 2

---
Output:
4
'''
