def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i - j >= 0:
                    dp[i] += dp[i - j]
        
        print(dp[n])
    
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
2 2
4 2

---
Output:
2
5
'''