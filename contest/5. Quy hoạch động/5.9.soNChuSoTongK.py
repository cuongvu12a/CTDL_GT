def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, 10):
            if i <= k:
                dp[1][i] = 1
                
        for i in range(2, n + 1):
            for j in range(k + 1):
                for l in range(10):
                    if l <= j:
                        dp[i][j] += dp[i - 1][j - l]
        
        print(dp[n][k])

if __name__ == "__main__":
    main()
    
'''
Input:
---
3
2 2
2 5
3 6

---
Output:
2
5
21
'''