def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [1]
        idx2 = idx3 = idx5 = 0
        while len(dp) < n:
            next_ugly = min(dp[idx2] * 2, dp[idx3] * 3, dp[idx5] * 5)
            dp.append(next_ugly)
            if next_ugly == dp[idx2] * 2:
                idx2 += 1
            if next_ugly == dp[idx3] * 3:
                idx3 += 1
            if next_ugly == dp[idx5] * 5:
                idx5 += 1
            
        print(dp[n - 1])
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
10
4

---
Output:
12
4
'''