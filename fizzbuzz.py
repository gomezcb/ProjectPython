
# fizz buzz file

def FizzBuzz():
    x = range(1, 101)
    for _ in x:
        if _ % 3 == 0 and _ % 5 == 0:
            print('fizzbuzz')
        elif _ % 3 == 0:
            print('fizz')
        elif _ % 5 == 0:
            print('buzz')
        else:
            print(_)
def main():
    FizzBuzz()

main()