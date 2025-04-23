def main():
    t = int(input())
    while t > 0:
        t -= 1
        s1, s2 = input().split()
        num1 = int(s1, 2)
        num2 = int(s2, 2)
        product = num1 * num2
        
        print(product)
        
if __name__ == "__main__":
    main()
    
'''
Input:
---
2
1100 01
01 01

---
Output:
12
1
'''