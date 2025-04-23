def pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    
    half_part = pow(a, n // 2) % (10**9 + 7)
    if n % 2 == 0:
        return (half_part * half_part) % (10**9 + 7)
    else:
        return (a * half_part * half_part) % (10**9 + 7)
    
def main():
    t = int(input())
    while t > 0 :
        t -= 1
        a = int(input())
        reversed_a = int(str(a)[::-1])
        print(pow(a, reversed_a))
        
if __name__ == "__main__":
    main()
        
'''
Input:
---
2
2
12

---
Output:


'''