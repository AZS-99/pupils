from classes import QuadraticEquation




if __name__ == '__main__':

    a, b, c = input("Enter a, b, c:").split(", ")
    a = float(a)
    b = float(b)
    c = float(c)

    q1 = QuadraticEquation(a, b, c)
    discriminant = q1.getDiscriminant()

    if discriminant < 0:
        print("The equation has no roots.")
    elif discriminant > 0:
        r1 = q1.getRoot1()
        r2 = q1.getRoot2()
        print("The roots are", r1, "and", r2)
    else:
        print("The root is", q1.getRoot1())


