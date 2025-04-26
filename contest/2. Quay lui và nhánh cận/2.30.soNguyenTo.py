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
         
def generateCombination(*, n, k):
    combination = [i for i in range(1, k+ 1)]
    while True:
        yield combination
        for i in range(k - 1, -1, -1):
            maxValue = n - k + i + 1
            if combination[i] != maxValue: # != or <, both are correct
                combination[i]+=1
                for j in range(i+1, k, 1):
                    combination[j] = combination[j - 1] + 1
                break
        else:
            break
 
def handle(*, count, start, target):
    prime = list(sang(start= start, end= target - 2)) # end = target - 2: prime.first = 2 -> number <= target - 2
    for combination in generateCombination(n = len(prime), k = count):
        if sum([prime[index - 1] for index in combination]) == target:
            print([prime[index -1] for index in combination])
            # yield [prime[index] for index in combination]
            
def main():
    handle(count= 2, start= 7, target= 28)            
    handle(count= 3, start= 2, target= 23)            
    
main()