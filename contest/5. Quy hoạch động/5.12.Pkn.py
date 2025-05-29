MOD = 10**9 + 7

def permutations(n, k):
    dp = [0] * (k + 1)
    dp[0] = 1  # P(n, 0) = 1

    for i in range(1, k + 1):
        dp[i] = dp[i - 1] * (n - i + 1) % MOD

    return dp[k]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        result = permutations(n, k)
        print(result)
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
5 2
4 2

---
Output:
20
12
'''