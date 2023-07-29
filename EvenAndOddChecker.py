

def myFunction():
    print('\nHello World!\nNow checking for EVEN and ODD numbers\n')
    
    myList = [1,2,3,4,5,6,7,8,9,0]

    for _ in myList:
        # print only evens
    
        if(myList[_] % 2 == 0):
            print(f'{myList[_]} is an EVEN number')
        else:
            print(f'{myList[_]} is an ODD number')

def main():
    myFunction()

main()