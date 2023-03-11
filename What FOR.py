from random import randint
myList = []
for x in range(9):
    a = randint (1,10)
    myList.append(a)


print(myList)

searchForNumber = 2
elm_count = myList.count(searchForNumber)
print(elm_count)

if elm_count > 0:
    print("Element " + str(searchForNumber) + " is found " + str(elm_count) + " times ")
else:
    print( "Element " + str (searchForNumber) + " is not found")


