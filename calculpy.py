import math

print("""
Welcome to our calculator web app. 
Basic uses are -- +, -, *, /, and others. 
To check available commands, type -commands.

First release will be simple, next will take only one input jammed together. 

Enjoy!!
""")

try:
    x = float(input('Input number >> '))
    op = str(input('Input operator >> '))
    y = float(input('Input number >> '))


    def plus():
        result = x + y
        return result


    def minus():
        result = x - y
        return result


    def times():
        result = x * y
        return result


    def divide():
        result = x / y
        return result


    if op == '+':
        plus()
        print(f'Result: {plus()}')
    elif op == '-':
        minus()
        print(f'Result: {minus()}')
    elif op == '*':
        times()
        print(f'Result: {times()}')
    elif op == '/':
        divide()
        print(f'Result: {divide()}')

except ValueError:
    print('ValueError.')
except NameError:
    print('NameError.')
except ZeroDivisionError:
    print('ZeroDivisionError')



