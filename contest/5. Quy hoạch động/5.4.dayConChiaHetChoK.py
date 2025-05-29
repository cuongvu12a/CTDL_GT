def main():
    t = int(input())
    for _ in range(t):
        n, a = map(int, input().split())
        arr = list(map(int, input().split()))
        dp = [-float('inf')] * n
        dp[0] = 0
        for i in arr:
            next_dp = dp[:]
            for r in range(n):
                if dp[r] >= 0:
                    next_r = (i + r) % n
                    next_dp[next_r] = max(next_dp[next_r], dp[r] + 1)
            dp = next_dp
        print(dp[0])

if __name__ == "__main__":
    main()
    
    
'''
Input:
---
1
10 3
2 3 5 7 9 6 12 7 11 15

---
Output:
9
'''