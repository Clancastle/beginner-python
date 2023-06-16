import math

print("""
Welcome to our calculator web app. 
Basic uses are -- +, -, *, /, and others. 

Update upcoming!! 

Enjoy!!
""")

# since it is really annoying when errors pop up, i put the whole code in the try, except thing.
# it is very readable, if anyone has problems, it is because they dont know python.

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



