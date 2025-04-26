
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

def atm(*, target, money):
    length = len(money)
    for i in range(1, length +1):
        for combination in generateCombination(n= length, k= i):
            sum = 0
            for j in combination:
                sum+= money[j -1]
            if sum == target:
                return i
    return -1

def main():
    print(atm(target= 5, money= [1,2, 3,4]))
    print(atm(target= 5, money= [1, 4, 5]))
    print(atm(target= 100, money= [10, 20, 30, 40, 50]))

main()