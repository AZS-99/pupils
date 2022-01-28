import math
import grades
import grades_Br

"""
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. Write a program that displays the average speed in 
miles per hour. (Note that 1 mile is 1.6 kilometers.)
"""
def average_speed(distance, time):
    return (distance / 1.6) / (time / 60)




def get_min(num1, num2):
    if num1 < num2:
        return num1
    elif num1 > num2:
        return num2
    else:
        raise Exception("Both numbers are equal!")

def is_even(num):
    return num % 2 == 0

def is_leap_year(year):
    return year % 4 == 0


def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


def get_triangle_type(angle1, angle2, angle3):
    if angle1 == angle2 == angle3:
        return "equilateral"
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        return "isosceles"
    else:
        return "Scalene"

def area(radius):
    return radius ** 2 * math.pi

def volume(radius, height):
    return radius ** 2 * math.pi * height

"""
Write a program that reads a number in feet, converts it to meters, and displays the result. One foot is 0.305 meters. 

Here is a sample run:
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters
"""
def converts_to_meters(feet):
    return feet * 0.305

if __name__ == '__main__':
    feet = float(input("Enter a value for feet:"))
    print(converts_to_meters(feet))


























