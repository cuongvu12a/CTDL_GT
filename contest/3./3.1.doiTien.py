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
    # cost = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    cost = [65, 25, 10]
    print(handle(cost=cost, value=70)) # 1
    # print(handle(cost=cost, value=121)) # 2
    
main()

''' 
    3.6 ...
'''