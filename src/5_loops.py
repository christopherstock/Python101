
# loops
print('All about Loops')

myRange = range(0, 7)
print(myRange)

myList = list(myRange)
print(myList)

# for loop
for myNumber in myRange:
    print('my range number [' + str(myNumber) + ']')

for myNumber in myList:
    print('my list number [' + str(myNumber) + ']')

myDictionary = {
    "myTest1": 1,
    "myTest2": 4,
    "myTest3": 9,
}

for myKey in myDictionary:
    print('My key in my dict: [' + myKey + ']')

# while loop
myIndex = 0
print('While loop with myIndex [' + str(myIndex) + ']')
while myIndex < 10:
    myIndex += 1
    print('myIndex: [' + str(myIndex) + ']')

    if (myIndex == 4):
        print('Continue on index four!')
        continue

    if (myIndex == 7):
        print('Break on seven!')
        break

# else in loops
myList = [1, 2, 3, 4, 5]
print('Iterating over myList')
print(myList)
for i in myList:

#    if i == 3:
#        print("Index 3 found - breaking")
#        break
    print('index: ' + str(i))
else:
    print("Item not found - loop was not breaked!")
