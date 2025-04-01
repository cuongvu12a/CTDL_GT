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
        t -= 1
        n = int(input())
        print(pow(2, n - 1))
        
main()

'''
Input:
---
1
3

---
Output:
4
'''

'''
f(n) = f(1) + f(2) + ... + f(n - 1) + 1
f(n) = 2^(n - 1)
    Lý do:
        f(10) = 10 
            = 1 + f(9)
            = 2 + f(8)
            = 3 + f(7)
            ...
        với f(x) là số cách dãy tổng = x
'''