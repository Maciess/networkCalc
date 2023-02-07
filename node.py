class Node:
    def __init__(self, data):
        self.data = data #kfdskf;skdf
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self, rev):
        if rev:
            return self.prev
        return self.next

    def get_prev(self, rev):
        if rev:
            return self.next
        return self.prev

    def set_data(self, new_data):

        self.data = new_data

    def set_next(self, new_next, rev):
        if rev:
            self.prev  = new_next
        else:
            self.next = new_next

    def set_prev(self, new_prev, rev):
        if rev:
            self.next  = new_prev
        else:
            self.prev = new_prev
