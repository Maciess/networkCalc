class Stack:
    def __init__(self):
        self.items = []

    # Θ(1)
    def is_empty(self):
        return self.items == []

    # Θ(1)
    def push(self, item):
        self.items.append(item)

    # Θ(1)
    def pop(self):
        return self.items.pop()

    # Θ(1)
    def peek(self):
        return self.items[-1]

    # Θ(1)
    def size(self):
        return len(self.items)


# alternatywna implementacja stosu
class Stack1:
    def __init__(self):
        self.items = []

    # Θ(1)
    def is_empty(self):
        return self.items == []

    # Θ(n)
    def push(self, item):
        self.items.insert(0, item)

    # Θ(n)
    def pop(self):
        return self.items.pop(0)

    # Θ(1)
    def peek(self):
        return self.items[0]

    # Θ(1)
    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack() # s -> []
    print(s.is_empty())
    s.push(4) # s -> [4]
    s.push("pies") # s -> [4, 'pies']
    print(s.peek())
    s.push(True) # s -> [4, 'pies', True]
    print(s.size())
    print(s.is_empty())
    s.push(8.4) # s -> [4, 'pies', True, 8.4]
    print(s.pop()) # s -> [4, 'pies', True]
    print(s.pop()) # s -> [4, 'pies']
    print(s.size())
