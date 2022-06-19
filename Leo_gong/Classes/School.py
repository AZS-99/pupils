class Student:
    count = 0
    def __init__(self, fn, ln, a, grade):
        self.first_name = fn
        self.last_name = ln
        self.age = a
        Student.count += 1
        self.id = Student.count + 100000
        self.gr = grade

    def __repr__(self):
        return "Name: {} {}\nGr: {}   STU # id:{}".format(self.first_name, self.last_name, self.gr, self.id)


class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, first_name, last_name, grade, age ):
        s = Student(first_name, last_name, grade, age)
        self.students.append(s)

    def __repr__(self):
        return str(self.students)