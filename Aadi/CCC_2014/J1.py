"""
Problem Description
You have trouble remembering which type of triangle is which. You write a program to help. Your program reads in three
angles (in degrees).

• If all three angles are 60, output Equilateral.
• If the three angles add up to 180 and exactly two of the angles are the same, output Isosceles.
• If the three angles add up to 180 and no two angles are the same, output Scalene.
• If the three angles do not add up to 180, output Error.

Input Specification
The input consists of three integers, each on a separate line. Each integer will be greater than 0 and less than 180.
Output Specification
Exactly one of Equilateral, Isosceles, Scalene or Error will be printed on one line.

Sample Input 1
60
70
50
Output for Sample Input 1
Scalene

Sample Input 2
60
75
55
Output for Sample Input 2
Error
"""
def angles():
    file = open("CCC_2014/J1", "r")
    angle_one = int(file.readline())
    angle_two = int(file.readline())
    angle_three = int(file.readline())
    if angle_one + angle_two + angle_three == 180:
        if angle_one == angle_two == angle_three:
            print ("Equilateral")
        elif angle_one == angle_two or angle_two == angle_three or angle_one == angle_three:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")
