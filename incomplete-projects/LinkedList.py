#creating a linked list class and creating needed functions
#also creating a binary search

list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1]

# print(Node()) this results in it printing a address where on the ram this is stored.

class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self, head):
        self.head = head

    def append(self):
        pass
    def traverse(self):
        pass
    def delete(self):
        pass
    def reverse(self):
        pass

order = [30, 25, 20, 15, 10, 5, 3, 0]
#Binary Search
dict = {
    "list": [],
    'query': None,
    "output": None
}

#find a number in a decreasing sorted list


#search for all edge cases and remove

def BinarySearch(list, query):
    lo, hi = 0, len(list) - 1  # since counting starts at 0


    while lo <= hi:
        med = (hi + lo) // 2  # lo is 0, but this is if it gets reassigned later during running the program
        midnum = list[med]
        print(midnum)
        if query == midnum:
            return midnum
        elif query < midnum:
            lo = med + 1
            return lo
        else: # if not equal or less, it is more than
            hi = med - 1
            return hi



print(BinarySearch(order, 30))