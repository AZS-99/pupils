class School:
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.student_list = []
        self.name = name

    def __str__(self):
        return "{0}".format(self.name)



    def enroll(self, student):
        if student not in self.student_list and len(self.student_list) <= self.capacity:
            self.student_list.append(student)
