import math

print("""
Welcome to our calculator web app. 
Basic uses are -- +, -, *, /, and others. 
To check available commands, type -commands.

First release will be simple, next will take only one input jammed together. 

Enjoy!!
""")

x = 7  #float(input('Input number >> '))
op = input('Input operator >> ')
y = 10.8  #  float(input('Input number >> '))


def plus():
    result = x + y
    return result


def minus():
    pass


def times():
    pass


def divide():
    pass


if op == '+' or 'plus':
    plus()
    print(f' Result: {plus()}')

