def mat_mult(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]
    
def mat_pow(M, power):
    result = [[1, 0], [0, 1]]
    base = M
    
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        power //= 2
    
    return result

def fibonacci(n):
    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    result = mat_pow(F, n - 1)
    return result[0][0]

def main():
    t = int(input()) 
    while t > 0:
        t -= 1
        n = int(input())
        print(fibonacci(n))   

if __name__ == "__main__":
    main()

'''
Input:
---
3
2
6
20

---
Output:
1
8
6765

'''