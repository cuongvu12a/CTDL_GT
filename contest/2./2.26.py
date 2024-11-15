
def handle(*, input, count):
    if count == 0:
        return input
    
    input_list = list(input)
    sort = sorted([num for num in input_list], reverse=True)
    for index, num in enumerate(input_list):
        if num != sort[index]:
            temp = input_list[index:index+1]
            input_list[index:index+1] = sort[index]
            lastIdxSwap=  next((i for i in range(len(input_list) - 1, -1, -1) if input_list[i] == sort[index]), None)
            input_list[lastIdxSwap:lastIdxSwap+1] = temp

            count-=1
            if count == 0:
                break
    
    return ''.join(input_list)
            
    
def main():
    print(handle(input='1234567', count=2))
    
main()