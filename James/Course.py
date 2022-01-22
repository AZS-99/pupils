class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def __str__(self):
        return "{0} {1}".format(self.name, self.course_id)

