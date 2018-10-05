
# exception handling
print('Exception Handling')

try:
    myTest1 = 1 / 0
except ZeroDivisionError:
    print('Division by zero error caught')
except ArithmeticError:
    print('ArithmeticError error caught')
except Exception:
    print('Exception caught')
finally:
    print('Finally block being invoked')
