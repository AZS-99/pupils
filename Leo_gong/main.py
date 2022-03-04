from classes import Point



if __name__ == '__main__':

    x, y, x2, y2 = input("Enter two points: ").split(", ")
    x = float(x)
    y = float(y)
    x2 = float(x2)
    y2 = float(y2)
    s1 = Point(x, y)
    s2 = Point(x2, y2)

    print(s1.distance(s2))
