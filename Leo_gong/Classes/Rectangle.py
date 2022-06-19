class Rectangle:

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.width + self.length) * 2