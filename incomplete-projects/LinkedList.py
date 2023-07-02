#how to --
# list of integers in decreasing order
# pick out the query by looking at as little indexes as possible

# state problem clearly
# come up with some  example input/outputs, try to cover all edge cases
# come up with solution. state in plain english
# implement solution, fix any bugs.
# analyze solution/algorithm, overcome inefficiency
# repeat 3-5


def binary_search(list, query):
    low, high = 0, len(list) - 1

    while low <= high: # we will change low and high values to narrow down query
        middle = (low + high) // 2
        middle_number = list[middle]
        #print(middle)
        #print(middle_number)
        if middle_number == query: #it returns the index, but if multiple, it returns the one it sees first, not the first index of query
            return middle
        elif query < middle_number:
            low = middle + 1
        else:
            high = middle - 1
    return -1


class Nod(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, d):
        self.data = d

class Linked(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Nod(d, self.root)
        self.root = new_node
        self.size += 1
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_data())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

mylist = Linked()

mylist.add(3)
mylist.add(9)
mylist.add(10)
print(mylist.find(1))
























