
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

#also an idea to split string if operater is touching a number
# import math
#
#
z = input('Write an equation. ')
operators = ['!', "@", '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', ':', '/','[', ']', '{', '}', '=']

input_split = z.split()

print(input_split)
for i in input_split:
    if i.isdigit():
        i = float(i)
        print(i)
        #if a digit, turn it into a float. then call math function

for i in input_split:
    for operator in operators:
        if i == operator:

            print(operator)
            print(True)
def solve():
    pass
