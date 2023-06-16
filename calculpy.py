import math

print("""
Welcome to our calculator web app. 
Basic uses are -- +, -, *, /, and others. 
To check available commands, type -commands.

First release will be simple, next will take only one input jammed together. 

Enjoy!!
""")

x = float(input('Input number >> '))
op = input('Input operator >> ')
y = float(input('Input number >> '))


def plus():
    result = x + y
    return result


def minus():
    result = x - y
    return result


def times():
    pass


def divide():
    pass


if op == '+' or 'plus':
    plus()
    print(f'Result: {plus()}')
elif op == '-' or 'minus':
    minus()
    print(f'Result: {minus()}')
elif op == '*' or 'times':
    times()
    print(f'Result: {times()}')
elif op == '/' or 'divide':
    divide()
    print(f'Result: {divide()}')


