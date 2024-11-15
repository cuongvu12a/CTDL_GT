# 5
# 4 1
# 3 2
# 3 1 1
# 2 2 1
# 2 1 1 1
# 1 1 1 1 1

def generateDivision(*, n, maxStart=None):
    if maxStart == None:
        maxStart=n

    if n == 1:
        return [[1]]
    elif n == 0:
        return []
    else:
        result = []
        for i in range(min(n, maxStart), 0, -1):
            sub = generateDivision(n= n-i, maxStart= i)
            if not len(sub):
                result.append([i])
            else: 
                for x in sub:
                    result.append([i] + x)
        else:
            return result
    
def main():
    n = 5
    print(generateDivision(n = n))

main()