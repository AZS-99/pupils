class Student:
    count = 1

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_id = Student.count
        self.courses = []
        Student.count += 1

    def __str__(self):
        return "Name:{0}\n Age: {1}\n ID: {2}".format(self.firstname + " " + self.lastname, self.age, self.student_id)

    def __eq__(self, other):
        return other.student_id == self.student_id

    def add_course(self, course):
        self.courses.append(course)