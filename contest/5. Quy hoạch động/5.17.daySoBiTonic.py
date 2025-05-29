def main_2():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        inc = a.copy()
        dec = a.copy()

        # Tổng dãy tăng kết thúc tại i
        for i in range(n):
            for j in range(i):
                if a[i] > a[j] and inc[i] < inc[j] + a[i]:
                    inc[i] = inc[j] + a[i]

        # Tổng dãy giảm bắt đầu tại i
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if a[i] > a[j] and dec[i] < dec[j] + a[i]:
                    dec[i] = dec[j] + a[i]

        max_sum = 0
        for i in range(n):
            max_sum = max(max_sum, inc[i] + dec[i] - a[i])  # Trừ a[i] vì bị tính 2 lần

        result.append(max_sum)

    print('---')
    print("\n".join(result))


def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        dp_inc = a.copy()
        dp_dec = a.copy()
        
        for i in range(1, n):
            for j in range(i):
                if a[i] > a[j]:
                    dp_inc[i] = max(dp_inc[i], dp_inc[j] + a[i])
                elif a[i] < a[j]:
                    dp_dec[i] = max(dp_dec[i], dp_inc[j] + a[i], dp_dec[j] + a[i])
        
        result.append(max(max(dp_inc + dp_dec), 0))
    
    print('---')
    print("\n".join(result))

        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
6
80 60 30 40 20 10
9
1 15 51 45 33 100 12 18 9

---
Output:
210
194
'''