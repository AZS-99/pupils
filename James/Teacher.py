class Teacher:
    tid = 0

    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.ID = Teacher.tid
        self.courses = []
        Teacher.tid += 1

    def __eq__(self, other):
        return other.ID == self.ID and other.ID == self.ID

    def add_teacher(self, course):
        self.courses = course

    def __str__(self):
        return "Name: {0} \nAge: {1} \nID: {2} \n Class Teaching: {3}".format(self.name, self.age, self.ID, self.courses)