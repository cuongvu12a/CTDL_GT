def handle(*, arr, target, curr = None, total = None, temp = None):
    if curr is None:
        if sum(arr) % target != 0:
            return False
        
        curr = 0
        total = 0
        temp =  [True for i in range(len(arr))]
    
    if total == target - 1:
        return True
    
    if curr == sum(arr) / target:
        if handle(arr= arr, target= target, curr = 0, total = total + 1, temp = temp):
            return True
        
    if curr > sum(arr) / target:
        return False
        
    for i in range(len(arr)):
        if temp[i]:
            temp[i] = False
            if handle(arr= arr, target= target, curr= curr + arr[i], total= total, temp= temp):
                return True
            temp[i] = True
    else:
        return False
        
        

def main():
    print(handle(arr=[2,1,6,5,4,3,2,1], target=4))
    
main()