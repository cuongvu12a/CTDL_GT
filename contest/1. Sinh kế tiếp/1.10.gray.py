# Gray -> Binary
# Binary[0] = Gray[0]
# Binary[i] = Gray[i] XOR Binary[i - 1]

# Binary -> Gray
# Gray[0] = Binary[0]
# Gray[i] = Binary[i] XOR Binary[i - 1]

def binaryToGray(*, binary):
    gray = [binary[0]]
    for i in range(1, len(binary)):
        gray.append(binary[i] ^ binary[i - 1])
    return gray

def grayToBinary(*, gray):
    binary = [gray[0]]
    for i in range(1, len(gray)):
        binary.append(gray[i] ^ binary[i - 1])
    return binary

def main():
    print(binaryToGray(binary= [0,1,0,0,1]))
    print(binaryToGray(binary= [0,1,1,0,1]))

main()