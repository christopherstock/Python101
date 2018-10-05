
# exception handling
print('Exception Handling')

try:
    myTest1 = 1 / 0
except ZeroDivisionError:
    print('Division by zero error caught')
except ArithmeticError:
    print('ArithmeticError error caught')
except (Exception):
    print('Exception caught')
except (IndexError, ArithmeticError):
    print('One of the specified exceptions occurred')
except:
    print('This is a "bare except"')
finally:
    print('Finally block being invoked')

# my list
my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("The index '6' is not in the list")

# no exception
print("Trying no exception:")
try:
    myTest2 = 0 / 1
except ZeroDivisionError:
    print('Division by zero error caught')
else:
    print('Else branch being passed!')
finally:
    print('Finally branch being passed!')
