import math

def sang(*, start = 0, end):
    prime = [1 for i in range(end + 1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(2, math.floor(math.sqrt(end) + 1)):
        if prime[i]:
            for j in range(i*i, end + 1, i):
                prime[j] = 0
                
    for i in range(start, end + 1):
        if prime[i]:
            yield i
 
def handle(*, prime, n):
    uoc = []
    temp = n
    while temp != 1:
        for i in prime:
            if temp % i == 0:
                uoc.append(i)
                temp = temp // i
                break

    min = float('inf')
    stack = [uoc]
    visited = {}
    while stack:
        curr = stack.pop()
        if len(curr) == 0:
            continue
        
        sorted_numbers = sorted(curr, reverse= True)
        
        if tuple(sorted_numbers) in visited:
            continue
        visited[tuple(sorted_numbers)] = True
        
        check = 1
        for base , exponent in zip(prime, sorted_numbers):
            check *= base ** (exponent - 1)
        
        if check < min:
            min = check
            
        for i in range(len(curr)):
            for j in range(i + 1, len(curr)):
                new_combo = curr[:i] + curr[i+1:j] + curr[j+1:] + [curr[i] * curr[j]]
                stack.append(new_combo)

    print(visited)

    return min

def main():
    prime = list(sang(start= 0, end= 100))
    print(handle(prime= prime, n= 6))
    
main()

'''
    Nếu một số N có thể được phân tích thành 2 ^ a * 3 ^ b * 5 ^ c * ... với (2,3,5, ... là các số nguyên tố)
    thì số ước của N là (a + 1) * (b + 1) * (c + 1) * ...
'''