def pow(x , y):
    if y == 0:
        return 1
    
    temp = pow(x, y//2)
    if y % 2 == 0:
        return temp * temp
    return x * temp * temp

def main():
    t = int(input())
    while t > 0:
        t-=1
        a, b = map(int, input().split())
        print(pow(a, b))

main()

'''
Input:
---
2
2 3
4 2

---
Output:
8
16
'''