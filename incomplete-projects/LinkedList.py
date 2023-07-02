#how to --
# list of integers in decreasing order
# pick out the query by looking at as little indexes as possible

# state problem clearly
# come up with some  example input/outputs, try to cover all edge cases
# come up with solution. state in plain english
# implement solution, fix any bugs.
# analyze solution/algorithm, overcome inefficiency
# repeat 3-5

class Node():
    value = None
    next_n = None

    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f"Node: {self.value} " #%self.value

class LinkedList():
    pass


n = Node(1)
nn = Node(2)
nnn = Node(3)
nn.next_n = n
nn.next_n.next_n = nnn
print(nn.next_n)
print(nn.next_n.next_n)























