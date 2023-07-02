#how to --
# list of integers in decreasing order
# pick out the query by looking at as little indexes as possible

# state problem clearly
# come up with some  example input/outputs, try to cover all edge cases
# come up with solution. state in plain english
# implement solution, fix any bugs.
# analyze solution/algorithm, overcome inefficiency
# repeat 3-5

#make linked list
class Node():#<-- object
    def __init__(self, d, n=None): #node > data|next
        self.data = d
        self.next = n
    def get_next(self): #returns the next node after current, used for traversing, deleting etc.
        return self.next
    def set_next(self, n): #this makes it easier to see the next data, you make next var (n)
        self.next = n
    def get_data(self):
        return self.data #returns the current data in node
    def set_data(self, d):
        self.data = d #sets data, so you can call Node().data, more readable ig

class Linkedlist(): #<-- object
    def __init__(self, r=None):
        self.root = None
        self.size = 0 #for the size of the LinkedList
    def get_size(self): # will += size when another node gets added
        return self.size

    def add(self, d):
        new_node = Node(d, self.root) #makes a node with data added, and the next data