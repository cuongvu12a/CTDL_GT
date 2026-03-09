def min_flips(s):
    balance = 0
    ans = 0
    
    for c in s:
        if c == '(':
            balance += 1
        else:  # ')'
            balance -= 1
        
        if balance < 0:
            ans += 1
            balance += 2   # đổi ) thành ( → +2 thay vì -1
    
    # Phần dư thừa '(' ở cuối
    ans += balance // 2
    
    return ans


T = int(input())
for _ in range(T):
    s = input().strip()
    print(min_flips(s))

def main():
    t = int(input())
    while t > 0:
        t -= 1
        s = input().strip()
        ans = min_flips(s)
        print(ans)

if __name__ == "__main__":
    main()