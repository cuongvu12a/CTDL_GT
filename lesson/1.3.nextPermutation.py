# 1 2 3 
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
#...

def generatePermutation(*, n):
    '''
    Generate all possible permutations of n
    * Mathematically, there are n! possible permutations of n
    1. Start with the first permutation 1 2 3 ... n
    2. Find the rightmost element that is less than the element to its right
    3. Find the smallest element to the right of the element found in step 2 that is greater than the element found in step 2
    4. Swap the elements found in step 2 and step 3
    5. Reverse the elements to the right of the element found in step 2
    6. Repeat step 2 until you reach the first element
    7. If you can't find an element in step 2, then you are done
    '''
    permutation = [i for i in range(1, n + 1)]
    while True:
        yield permutation
        for i in range(n - 1, 0, -1):
            if permutation[i - 1] < permutation[i]:
                minValue = permutation[i]
                index = i
                for j in range(i, n, 1):
                    if permutation[j] < minValue and permutation[j] > permutation[i - 1]:
                        minValue = permutation[j]
                        index = j
                
                permutation[index] = permutation[i - 1]
                permutation[i - 1] = minValue

                permutation = permutation[:i] + permutation[i:][::-1]
                break
        else:
            break


def main():
    for str in generatePermutation(n= 4):
        print(str)

main()
