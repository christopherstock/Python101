
# this is the 3td scripts entry point
print('src/3_tuples.py being invoked')

# lists
myList1 = ["a", "b", "c", "d"]
myList2 = list()
myList3 = list(["a", 2, "c", 4])

print('myList1:')
print(myList1)
print(myList2)
print(myList3)

# nested lists
myNestedList1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print('my nested list 1:')
print(myNestedList1)

# combine lists
myList4 = [7, 8, 9]
myList5 = [4, 5, 6]
myList4.extend(myList5)

print('my combined list:')
print(myList4)

# extend list 4
myList4 += myList5

print('my more combined list:')
print(myList4)

myList4.sort()

print('my sorted list:')
print(myList4)

print('my sliced list:')
print(myList4[2:6])

# try tuples
myTuple = (1, 2, 3, 4, 5)

mySlicedTuple = myTuple[0:2]

print('my sliced tuple:')
print(mySlicedTuple)

myNewTuple1 = tuple()
myNewTuple2 = tuple(["a", "b", "c"])

print('my new tuple:')
print(myNewTuple2)

print('my list from tuple:')
myList5 = list(myNewTuple2)
print(myList5)

# try dictionaries
myDictionary1 = {
    "chris": 136,
    "astrid": 76
}
myDictionary2 = dict()

print('my dictionary')
print(myDictionary1)

print('my dictionary - key "chris"')
print(myDictionary1["chris"])

astridInMyDict ="astrid" in myDictionary1
print('Astrid in my dict:')
print(astridInMyDict)

myDictKeys = myDictionary1.keys()
print('My dict keys:')
print(myDictKeys)





