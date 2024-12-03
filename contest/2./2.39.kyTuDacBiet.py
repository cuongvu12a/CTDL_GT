def handle(*, str, index, lenStr = None):
    if index <= len(str):
        return str[int(index) - 1]
        
    if lenStr is None:
        lenStr = len(str)
    
    while lenStr < index:
        lenStr *= 2
    
    if index <= lenStr / 2:
        return handle(str= str, index= index, lenStr= lenStr / 2)
    
    index = index - lenStr / 2
    
    if index == 1:
        index = lenStr / 2
    else:
        index = index - 1
        
    return handle(str= str, index= index, lenStr= lenStr / 2)
    

def main():
    print(handle(str= 'COW', index= 6))
    print(handle(str= 'COW', index= 8))
    print(handle(str= 'COW', index= 9))
    print(handle(str= 'COW', index= 10))
    print(handle(str= 'COW', index= 11))
    print(handle(str= 'COW', index= 13))
    
main()