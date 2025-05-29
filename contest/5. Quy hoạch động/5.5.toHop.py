MOD = 10**9 + 7

def comb_dp(n, k):
    C = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        C[i][0] = 1  # C(i, 0) = 1
        for j in range(1, min(i, k) + 1):
            C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

    return C[n][k]

def comb_dp_1d(n, k):
    C = [0] * (k + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            C[j] = (C[j] + C[j - 1]) % MOD
    return C[k]

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(f"{comb_dp(n, k)}||{comb_dp_1d(n, k)}")
        
if __name__ == "__main__":
    main()
    
    
'''
Input:
---
2
5 2
10 3

---
Output:
10
120
'''