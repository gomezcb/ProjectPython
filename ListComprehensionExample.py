# implement both IF and LIST COMPREHENSION to append information to a list

myList = []
myString = 'Willzyx'

for _ in myString:
    myList.append(_)

## List comprehension list
myList = [ x for x in myString if x == 'W'] ## inserts data if condition is met
myList = [ x for x in myString]             ## inserts data

print(f'List Comprehesion: \n{myList}')