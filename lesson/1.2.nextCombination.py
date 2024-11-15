# 123
# 124
# 125
# 134
# 135
# 145
# 234
# 235
# 245
# 345

def generateCombination(*, n, k):
    '''
    Generate all possible combinations of n choose k
    * Mathematically, there are C(n, k) possible combinations of n choose k
    1. Start with the first combination 1 2 3 ... k
    2. Increment the last element by 1
    3. If the last element meets the maximum value (n - k + index), then increment the previous element by 1
    4. Repeat step 3 until you reach the first element
    5. If the first element meets the maximum value (n - k + 1), then you are done
    '''
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

def main():
    for str in generateCombination(n = 5, k = 3):
        print(str)

main()
  


