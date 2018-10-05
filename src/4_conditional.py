
# conditional statements

myConditionTrue = True
myConditionFalse = False

if myConditionFalse:
    print('The condition is true')
else:
    print('The condition is false')

if 1 > 2:
    print('Branch 1')
elif 1 < 2:
    print('Branch 2')
else:
    print('Branch 3')

# try input
# myValue = input('Please enter a number:')
# print('The entered number was [' + myValue + ']')

if 1 < 2 and 2 > 1:
    print('AND condition is true')

if 1 > 2 or 2 > 1:
    print('OR condition is true')

myList = [1, 2, 3]

if 2 in myList:
    print('2 is in my list')

if 4 not in myList:
    print('4 is not in my list')

if 4 != 2:
    print('4 is != 2')

test = None

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list 1")

if not empty_list:
    print("It's an empty list 2")

if not empty_tuple:
    print("It's an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("This is nothing!")

myLineBreakString = 'This is a \n linebreak string'
print(myLineBreakString)

fileName = __name__
print('File Name:')
print(fileName)

if fileName == '__main__':
    print('This script has been started as the main script!')
