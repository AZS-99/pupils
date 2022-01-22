class Queue:
    def __init__(self):
        self.__q = []

    def __str__(self):
        return str(self.__q)

    def pop(self):
        return self.__q.pop(0)

    def enqueue(self, element):
        self.__q.append(element)

    def empty(self):
        if len(self.__q) == 0:
            return True
        return False

