## programmerL Carlos

def getValuesFromUser():
    calulatorOn = True
    
    # check if value are valid
    while(calulatorOn):
        valueA = input('Enter a number: ')
        try:
            number = float(valueA)
            calulatorOn = False
        except:
            print("number entered was not a number, try again\n\n")
    return number

def caluculateValues(x, y):
    
    print("'*' Multiply\n '/' Divide \n'-' Subtract\n'-' Add\n")
    operator = input("Enter choice: ")
    
    calculateBattery = True
    
    while(calculateBattery):
        if(operator == '+'):
            return x+y
        elif(operator == '-'):
            return x-y
        elif(operator == '/'):
            return x/y
        elif(operator == '*'):
            return x*y
        else:
            print("not a valid operator")    
    pass
            
def main():
    print('Calculator Booting up! ~~~~~\n')
    
    # get values from user
    print('Enter 1st value')
    valueA = getValuesFromUser()
    print('Enter 2nd value')
    valueB = getValuesFromUser()
    
    print(f'\nNumber A: {valueA}\nNumber B: {valueB}')
    
    # calculate values
    print("Answer", caluculateValues(valueA, valueB))

    print("---- END PROGRAM ----")

main()