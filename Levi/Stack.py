class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return str(self.__stack)

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        return self.__stack.pop(-1)