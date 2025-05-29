def main():
    c, n = map(int, input().split())
    a = []
    for i in range(n):
        temp = int(input())
        a.append(temp)
        
    dp = [0] * (c + 1)
    for i in range(n):
        print(f"Processing movie {i + 1} with duration {a[i]}")
        for j in range(c, a[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - a[i]] + a[i])
            print(f"Updated dp[{j}] to {dp[j]} after considering movie {i + 1}, {j - a[i]}")
    print("Final DP array:", dp)
    print(dp[c])
    
if __name__ == "__main__":
    main()
    
'''
Input:
259 5
81
58
42
33
61

---
Output:
242
'''