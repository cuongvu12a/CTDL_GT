import math

def handle(*, cost, value, curr = None, index = 0):
    if curr is None:
        curr = []
    
    if sum(curr) == value:
        return len(curr)
    
    if index == len(cost):
        return -1
    
    max = math.floor((value - sum(curr)) / cost[index])
    for i in range(max, -1, -1):
        temp = [cost[index] for j in range(i)]
        result= handle(cost=cost, value=value, curr=curr.copy() + temp, index=index+1)
        
        if result != -1:
            return result
    
    return -1

def main():
    cost = list(map(int, '1 2 5 10 20 50 100 200 500 1000'.split()))
    cost.sort(reverse=True)
    
    n = int(input())
    while n > 0:
        n -= 1
        value = int(input())
        print(handle(cost=cost, value=value))
main()

''' 
Input:
---
2
70
121

---
Output:
2
3
'''