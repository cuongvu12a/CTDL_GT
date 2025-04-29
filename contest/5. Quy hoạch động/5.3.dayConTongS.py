def handle(n , s):
    dp = [False] * (s + 1)
    dp[s] = True
    for i in n:
        if dp[i] == True:
            return 'YES'
        for s in range(s, i - 1, -1):
            if dp[s]:
                dp[s - i] = True            
            
    return 'NO'

def has_subset_sum(A, S):
    dp = [False] * (S + 1)
    dp[0] = True
    for a in A:
        for s in range(S, a - 1, -1):
            if dp[s - a]:
                dp[s] = True
    if dp[S]: 
        return 'YES'
    return 'NO'


def main():
    t = int(input())
    for _ in range(t):
        a, s = map(int, input().split())
        n = list(map(int, input().split()))
        print(handle(n, s))
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
5 6
1 2 4 3 5
10 15
2 2 2 2 2 2 2 2 2 2

---
Output:
YES
NO
'''