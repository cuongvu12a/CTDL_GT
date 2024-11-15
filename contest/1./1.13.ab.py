# n= 5, k= 3 => len() = 5, AAA => 3
# AAABA
# AAABB
# ABAAA
# BAAAB
# BBAAA

def generateBinary(*, length):
    n = length - 1
    bitString = ['B'] * length
    while True:
        yield bitString
        for i in range(n, -1, -1):
            if bitString[i] == 'B':
                bitString[i] = 'A'
                break
            else:
                bitString[i] = 'B'
        else:
            break

def generateAB(*, n, k):
    result = []
    for binary in generateBinary(length= n):
        maxLen= 0
        count= 0
        for i in binary:
            if i == 'A':
                maxLen+= 1
                if(maxLen == k):
                    count+= 1
                elif maxLen > k:
                    break
            else:
                maxLen= 0
        else:
            if count == 1:
                result.append(binary)
            print(result)
    return result

def main():
    n = 5
    k = 3
    print(generateAB(n= n, k= k))

main()