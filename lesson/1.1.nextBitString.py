# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111



def generateBitString(*, length):
    '''
    Generate all possible bit strings of length n
    * Mathematically, there are 2^n possible bit strings of length n
        1. Start with the first bit string 000...0
        2. Increment the last bit by 1
        3. If the last bit is 1, then increment the previous bit by 1
        4. Repeat step 3 until you reach the first bit
        5. If the first bit is 1, then you are done
    * Algorithm:
        1. Start with the first bit string 000...0
        2. Find the rightmost 0 and change it to 1, then change all the bits to the right of it to 0
        3. If you can't find a 0, then you are done
    '''
    n = length - 1
    bitString = [0] * length
    while True:
        yield bitString
        for i in range(n, -1, -1):
            if bitString[i] == 0:
                bitString[i] = 1
                break
            else:
                bitString[i] = 0
        else:
            break


def main():
    for str in generateBitString(length= 3):
        print(str)

main()
