# Function: Create Guido's Gorgeous Lasagna
# Programmer: Carlos Gomez

bakeTime = 40

def ExpectedBakeTime():
    print(f"Estimated baketime: {bakeTime} minutes\n")

def RemainingBakeTime(timeInOven):        
    timeRemaining = bakeTime - timeInOven
    print(f"The lasagna has been in the oven for {timeInOven} minutes\n")
    print(f"Time remaining: {timeRemaining} minutes")
    return timeRemaining
    
def main():
    ExpectedBakeTime()
    RemainingBakeTime(23)

main()