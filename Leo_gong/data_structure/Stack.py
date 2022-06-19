class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, thing):
        self.stack.append(thing)

    def pop(self):
        return self.stack.pop(-1)

    def empty(self):
        return len(self.stack) == 0