def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        
        print(dp)
        print(dp[n])
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
3
5
4
10
---
Output:
42
14
16796
'''