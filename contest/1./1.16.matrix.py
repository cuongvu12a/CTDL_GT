def generatePermutation(*, n):
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

def chooseNumberMatrix(*, c, k):
    length = len(c)
    permutation = generatePermutation(n= length)
    for p in permutation:
        count = 0
        for i in range(length):
            count+= c[i][p[i] -1]
        if count == k:
            yield p


def main():
    for str in chooseNumberMatrix(
        c=[
        [2,4,3],
        [1,3,6],
        [4,2,4]], k=10):
        print(str)

main()
