def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()
        
def mat_mult(A, B):
    modulo = 10**9 + 7
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def mat_pow(mat, n):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = mat
    while n > 0:
        if n % 2 == 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        n //= 2
    
    return result

def main():
    t = int(input())
    while t > 0:
        t -= 1
        n, k = map(int, input().split())
        mat = []
        while n > 0:
            n -= 1
            mat.append(list(map(int, input().split())))

        print_matrix(mat_pow(mat, k))
        

if __name__ == "__main__":
    main()
    
'''
Input:
---
2
2 5
1 1
1 0
3 1000000000
1 2 3
4 5 6
7 8 9

---
Output:
8 5
5 3
597240088 35500972 473761863
781257150 154135232 527013321
965274212 272769492 580264779

'''