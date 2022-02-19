"""
Write a program that displays the area and perimeter of a circle that has a radius of 5.5 using the following formulas:
                            area = radius * radius * pi
                            perimeter = 2 * radius * pi
Find the answer to the nearest 2 decimal places.
"""
import math


def area(r):
    area = r ** 2 * math.pi
    return round(area, 2)

def perimeter(r):
    perimeter = 2 * r * math.pi
    return round(perimeter,2)




