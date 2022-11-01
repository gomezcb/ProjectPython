
def getValuesFromUser():
    gameOn = True
    
    # check if value are valid
    while(gameOn):
        valueA = input('Enter a number: ')
        try:
            number = float(valueA)
            gameOn = False
        except:
            print("number entered was not a number, try again\n\n")
    return number
            
def main():
    print('Calculator Booting up! ~~~~~\n\n')
    
    # get values from user
    valueA = getValuesFromUser()
    valueB = getValuesFromUser()
    
    print(f'Number A: {valueA}\nNumber B: {valueB}')
    
    # calculate values
    
    pass

main()