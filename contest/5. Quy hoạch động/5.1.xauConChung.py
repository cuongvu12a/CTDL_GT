def main():
    t = int(input())
    for _ in range(t):
        a = input()
        b = input()
        res = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        for i, ai in enumerate(a, 1):
            for j, bj in enumerate(b, 1):
                if ai == bj:
                    res[i][j] = res[i - 1][j - 1] + 1
                else:
                    res[i][j] = max(res[i - 1][j], res[i][j - 1])
        print(res[-1][-1])
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
AGGTAB
GXTXAYB
AA
BB

---
Output:
'''
