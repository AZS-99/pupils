class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def enqueue(self, name):
        self.queue.append(name)

    def pop(self):
        return self.queue.pop(0)



# self.queue = ["Leo", "Adam"]
# q = Queue()
# q.pop()
# print(q) ["Adam"]