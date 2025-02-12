def main():
    t = int(input())
    while t > 0:
        t -= 1
        s, d = map(int, input().split())
        if s < 1 or s > d * 9:
            print(-1)
            continue
        
        nums = [1] + [0] * (d - 1)
        s -= 1
        
        for i in range(d, -1, -1):
            if s >= 9:
                nums[i - 1] += 9
                s -= 9
            else:
                nums[i - 1] += s
                break
        
        print(''.join(map(str, nums)))
        

main()

'''
Input:
---
4
9 2
20 3
20 2
0 1

---
Output:
18
299
-1
-1
'''