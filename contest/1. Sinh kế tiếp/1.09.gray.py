#  0
#  1

# 00
# 01
# 11
# 10

# 000
# 001
# 011
# 010
# 110
# 111
# 101
# 100

# 0000
# 0001
# 0011
# 0010
# 0110
# 0111
# 0101
# 0100
# 1100
# 1101
# 1111
# 1110
# 1010
# 1011
# 1001
# 1000

def generateGray(*, n):
    '''
    Generate all possible Gray codes of length n
    * Mathematically, there are 2^n possible Gray codes of length n
        Mã nhị phân phản xạ Gray là một chuỗi nhị phân mà hai số liên tiếp trong chuỗi chỉ khác nhau một bit.
        Các giá trị ở nửa sau của chuỗi Gray là phản xạ (đối xứng) của các giá trị ở nửa đầu của chuỗi.
            Ngoại trừ bit cao nhất bị đảo giá trị, nửa đầu là 0, nửa sau là 1.
    * Algorithm:
        1. Start with the first Gray code n = 1: 0, 1
        2. Generate the Gray code of length n - 1
        3. Append 0 to the left of the Gray code of length n - 1
        4. Append 1 to the left of the reverse of the Gray code of length n - 1
        5. Concatenate the results of step 3 and step 4
        6. Repeat step 2 until you reach the first Gray code
    '''
    if n == 1:
        return ['0', '1']
    
    result = []
    resultLeft = generateGray(n= n - 1)
    for x in resultLeft:
        result.append('0' + x)
    for x in resultLeft[::-1]:
        result.append('1' + x)

    return result

def main():
    print(generateGray(n= 4))

main()