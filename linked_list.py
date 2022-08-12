from node import Node
import copy

class LL_iterator:
    def __init__(self, LL):
        self.list = LL

    def __iter__(self):
        return self

    def __next__(self): # a tu nie mozna iterować bez modyfikacji
        if self.list.head is  None:
            raise StopIteration
        return self.list.pop_front()




class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.rev = False

    # Θ(1)
    def push_front(self, data):
        new_node = Node(data)

        new_node.set_next(self.head, self.rev)
        new_node.set_prev(None, self.rev)
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.set_prev(new_node, self.rev)
        self.head = new_node

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    # Θ(1)
    def push_back(self, data):
        new_node = Node(data)
        new_node.set_prev(self.tail, self.rev)
        new_node.set_next(None, self.rev)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.set_next(new_node, self.rev)
        self.tail = new_node

    # Θ(1)
    def pop_front(self):
        if self.is_empty():
            return
        obj = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next(self.rev)
            self.head.set_prev(None, self.rev)
        return obj

    def pop_back(self):
        if self.is_empty():
            return
        obj = self.tail.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev(self.rev)
            self.tail.set_next(None, self.rev)
        return obj


    # Θ(n)
    def size(self):
        n = 0
        current = self.head
        while current is not None:
            current = current.get_next(self.rev)
            n += 1
        return n

    # Θ(1)
    def is_empty(self):
        return self.head is None

    def reverse(self):
        self.rev = not self.rev
        self.head, self.tail = self.tail, self.head

    def indexOf(self, data):
        current = self.head
        n = 1
        while current is not None:
            if current.get_data() == data: return n
            current = current.get_next(self.rev)
            n += 1
        return

    def __contains__(self, item):
        current = self.head
        while current is not None:
            if current.get_data() == item: return True
            current = current.get_next(self.rev)
        return False
    # O(n)
    def insert_L(self, data, n): # n > 0
        new_node = Node(data)

        if n == 1: return self.push_front(data)
        elif n > 1 and n <= self.size():
            item_R = self.head
            for index in range(n-1):
                item_R = item_R.get_next(self.rev)
            item_L = item_R.get_prev(self.rev)
            new_node.set_next(item_R, self.rev)
            new_node.set_prev(item_L, self.rev)
            item_L.set_next(new_node, self.rev)
            item_R.set_prev(new_node, self.rev)

        else: return self.push_back(data)
    # O(n)
    def insert_R(self, data, n):
        self.reverse()
        self.insert_L(data,n)
        self.reverse()
    # O(n)
    def __add__(self, lst2): # działa na oryginale (tracimy drugi skladnik)
        if lst2.is_empty(): return self
        if self.is_empty(): return lst2

        self.tail.set_next(lst2.head, self.rev)
        lst2.head.set_prev(self.tail, self.rev)
        self.tail = lst2.tail
        return self
    # O(1)


    def __iter__(self):
        return LL_iterator(self)
# Zadanie 5b
""" 
    def __iter__(self): # tu mozna iterowac po liscie bez jej modyfikacji
        item = self.head
        while item is not None:
            yield item.get_data()
            item = item.get_next(self.rev)
"""


if __name__ == "__main__":
    lst = LinkedList()
    tsl = LinkedList()
    for n in range(10):
        lst.push_back(n)  # -> lst: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst.reverse()
    lst.push_back('a')


    print(lst.pop_back())
    print(lst.pop_back())



