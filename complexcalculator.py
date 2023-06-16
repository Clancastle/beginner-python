import math

#z = input('Write an equation. ').lower() #
operators = ['!', "@", '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', ':', '/','[', ']', '{', '}', '=']

z = "50 + 50"
#z = "I love thinking"

# def transform(): #can split into len(z), and go like, for a loop, if putting str on it
# not work, then put float
# -> could work this -> dont let the input be more than 3 (0, 1, 2), and split, or partition
# then # idk prolly not
#could use index(). -> ex, like look for operators, and if not operator, convert to float.
# nope does not work.
#idea 2, make a for loop. so evry time it runs, it splits z, and the split parts
# are then assigned a variable, like x1, x2, x3. but ive yet to learn
#nope, i just put isdigit() and it is fixed. 

input_split = z.split(' ')
print(input_split)
#def is_number(): find out how to return values before
for i in input_split:
    if i.isdigit():
        print(i)
# print(z.rindex(operators))
# print(input_split.isdigit())




