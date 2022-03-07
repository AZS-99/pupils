from classes import Circle2D



if __name__ == '__main__':
    [x1, y1, radius1] = [float(num) for num in input("Enter x1, y1, radius1:").split(", ")]
    [x2, y2, radius2] = [float(num2) for num2 in input("Enter x2, y2, radius2:").split(", ")]

    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)

    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1 is", c1.getPerimeter())
    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2 is", c2.getPerimeter())
    print("c1 contains the center of c2?", c1.containsPoint(c2.x, c2.y))
    print("c1 contains c2?", c2 in c1)
    print("c1 overlap c2?", c1.overlaps(c2))
