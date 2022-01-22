"""
Table:
80-100: A
70-80:  B
60-70:  C
50-60: D


F

"""


def print_hi():
    print("hi")


def get_grade(mark):
    if 80 <= mark <= 100:
        return "A"
    elif 70 <= mark < 80:
        return "B"
    elif 60 <= mark < 70:
        return "C"
    elif 50 <= mark < 60:
        return "D"
    else:
        return "F"


