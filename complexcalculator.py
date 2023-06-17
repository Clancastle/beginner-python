
#####THOUGHTS ___ HOW I GOT TO MAKE IT -------- #####
# def transform(): #can split into len(z), and go like, for a loop, if putting str on it
# not work, then put float
# -> could work this -> dont let the input be more than 3 (0, 1, 2), and split, or partition
# then # idk prolly not
#could use index(). -> ex, like look for operators, and if not operator, convert to float.
# nope does not work.
#idea 2, make a for loop. so evry time it runs, it splits z, and the split parts
# are then assigned a variable, like x1, x2, x3. but ive yet to learn
#nope, i just put isdigit() and it is fixed.
# if while loop is only under the for loop, it doesnt stop, ever.
#more efficient to use one for loop, and have several for nests, inside that one

#also an idea to split string if operater is touching a number
import math

 # class or one big function with lots of ifs?

class Solve(): #operators is used...
    pass


while True:

    numbers_list_in_order = []
    operator_list_in_order = []
    z = input('Write an equation. ')

    operators = ['+', '-', '*', '/', '^', '(', ')', '%', '=', '!', "@", '#', '$','&', ':', '[', ']', '{', '}']

    input_split = z.split() # split to identify each unit. #next is probably ('87+87')
#to identify and separate by operator, or space #after 90+90 triggers error, run modified
    #code down. like z.split(operators). <-- make that work
# print(input_split)

    for i in input_split: #

        if i.isdigit():
            i = float(i)
            numbers_list_in_order.append(i)
            print(numbers_list_in_order)
            # Solve(operator_list_in_order, numbers_list_in_order)

        for operator in operators: #
            if i == operator:
                operator_list_in_order.append(operator)
                print(operator_list_in_order)

            if operator == operators[0]: #add
                print(True)
            elif operator == operators[1]: #minus
                print(True)
            elif operator == operators[2]: #times
                print(True)
            elif operator == operators[3]: #division
                print(True)
            elif operator == operators[4]: #exponent **
                print(True)
            elif operator == operators[5]: #paranthasis '('
                print(operators[5])

                # Solve.add(self)
                #i can put the solving here, but functions are more challenging to me and
                # i want to try and see what i can do. plus It's more neat
