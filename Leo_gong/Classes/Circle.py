import math


class Circle:
    # Constructor
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius * self.radius * math.pi

    def circumference(self):
        return self.radius * 2 * math.pi



def circumference():
    radius = float(input("Please enter the radius:"))
    return radius * 2 * math.pi

def area():
    radius = float(input("Please enter the radius:"))
    return radius * radius * math.pi


