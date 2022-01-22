"""
Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the circle centered
at (0, 0) with radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle

Sample Run 1:
Enter a point with two coordinates: 4, 5
Point (4.0, 5.0) is in the circle

Sample Run 2:
Enter a point with two coordinates: 9, 9
Point (9.0, 9.0) is not in the circle
"""
import math


def circle(x, y):
    num = (x ** 2) + (y ** 2)
    if num <= 10 ** 2:
        print("Point (" + str(x) + ", " + str(y) + ") is in the circle")
    else:
        print("Point (" + str(x) + ", " + str(y) + ") is not in the circle")

"""
Write a program that prompts the user to enter a point (x, y) and checks whether the point is within the rectangle 
centered at (0, 0) with width 10 and height 5. For example, (2, 2) is inside the rectangle and (6, 4) is outside the 
rectangle. (Hint: A point is in the rectangle if its horizontal distance to (0, 0) is less than or equal to 10 / 2 and 
its vertical distance to (0, 0) is less than or equal to 5.0 / 2. Test your program to cover all cases.)
Here are two sample runs:

Sample Run 1:
Enter a point with two coordinates: 2, 2
Point (2.0, 2.0) is in the rectangle

Sample Run 2:
Enter a point with two coordinates: 6, 4
Point (6.0, 4.0) is not in the rectangle
"""
def rectangle(x, y):
    if -5 < x < 5 and -2.5 < y < 2.5:
        print("Point (" + str(x) + ", " + str(y) + ") is in the rectangle ")
    else:
        print("Point (" + str(x) + ", " + str(y) + ") is not in the rectangle")



"""
Write a program that prompts the user to enter the center coordinates and radii of two circles and determines whether 
the second circle is inside the first or overlaps with the first.
(Hint: circle2 is inside circle1 if the distance between the two centers <= | r1 - r2| and circle2 overlaps circle1 if 
the distance between the two centers <= r1 + r2. Test your program to cover all cases.)

Sample Run 1:
Enter circle1's center x-, y-coordinates, and radius:
0.5, 5.1, 13
Enter circle2's center x-, y-coordinates, and radius:
1, 1.7, 4.5
circle2 is inside circle1

Sample Run 2: 
Enter circle1's center x-, y-coordinates, and radius:
4.4, 5.7, 5.5
Enter circle2's center x-, y-coordinates, and radius:
6.7, 3.5, 3
circle2 overlaps circle1
"""
def inside_circle(x, y, radius, x2, y2, radius_2):
    distance = math.sqrt((x2 - x) ** 2 + (y2 - y) ** 2)
    difference_radius = abs(radius - radius_2)
    sum_radius = radius + radius_2
    if distance <= difference_radius:
        return True
    elif distance <= sum_radius:
        return False