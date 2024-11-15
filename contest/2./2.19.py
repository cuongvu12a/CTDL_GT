
def handle(*, array):
    temp = array
    new = []
    while True:
        yield temp
        if len(temp) == 1:
            break
        for i in range(len(temp) - 1):
            new.append(temp[i] + temp[i + 1])
        else:
            temp = new
            new = []

def main():
    for i in handle(array=[1,2,3,4,5]):
        print(i)

main() 