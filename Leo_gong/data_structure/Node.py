class Node:
    # n = Node(10)
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.nxt != None:
                current = current.nxt
            current.nxt = Node(data)