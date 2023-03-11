from random import randint
myList = []
for x in range(9):
    a = randint (1,10)
    myList.append(a)


print(myList)

searchForNumber = 2

numberCounter = 0
for number in myList:
    if number == searchForNumber:
        numberCounter +=1

if numberCounter > 0:
    print("Element " + str(searchForNumber) + " is found " + str(numberCounter) + " times ")
else:
    print("Element " + str(searchForNumber) + " is not found")

