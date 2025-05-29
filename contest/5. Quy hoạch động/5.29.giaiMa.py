def decode_ways(s):
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 

    for i in range(2, n + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        two_digits = int(s[i - 2:i])
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

t = int(input())
for _ in range(t):
    s = input().strip()
    print(decode_ways(s))


def main():
    t = int(input())
    for _ in range(t):
        a = input()
        print(decode_ways(a))

if __name__ == "__main__":
    main()

'''
Input:
2
123
2563

---
Output:
3
2
'''
            