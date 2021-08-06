# coding=utf-8

# this is the application's entry point
print('src/2_strings.py being invoked')

# print a second line
print('second line ..')

# print third line
print('third line ..')

# try strings in variables
myString1 = 'Christopher'
myString2 = 'Stock'
myString3 = '''    Test1
    Test2
    Test3
'''
myString4 = """Test 4"""

print(myString1)
print(myString2)
print(myString3)
print(myString4)

myNumber = 123
myString5 = str(myNumber)
myInteger1 = int(myString5)

# will launch an exception
# myTest5 = int('test')

print(myString5)
print(myInteger1)

# change string assignment for variable 'myString4'
myString4 = "Hallo"
print(myString4)

# show object ids
print('')
print('IDs:')
print(id(myString1))
print(id(myString2))
print(id(myString3))
print(id(myString4))
myString4 = 'MyNewString'
print(id(myString4))

# try unicode strings - obsolete in python 3.x -- all strings are unicode here!
myString5 = u'MyUnicodeString äöüßÄÖÜ`!"§$%&/()=?'
print(myString5)

# string concatenation
myString6 = 'My concatenated ' + 'String'
print(myString6)
print(myString6.upper())
print(myString6.lower())

print('   My String with leading and trailing whitespaces     '.strip())

print('=====')
print('Possible String methods:')
print(dir(myString6))

# help for a function
# help(myString6.capitalize)

# introspect an object
# print('Type of myString6:')
# print(type(myString6))

# second character of test string 6
# print('Fourth character of myString6:')
# print(myString6[3])
