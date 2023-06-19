
while True:
    op = ['+', '-', '*', '/']
    user = input('Input in a Expression:')
    user_input = user.split()
    print(user_input)
#try except
    for item in user_input:
        if item.isdigit():
            item = float(item)
            print(item)
        elif item.isalpha():
            print('Error occurred ')

    print('Calculating...')
    for i in op:
        if i == item
#try except
