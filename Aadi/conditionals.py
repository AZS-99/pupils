"""
Write a programme that returns the grade of a student based on their marks.
The grade follows the following table:

Mark        Grade
80-100        A
70-79         B
60-69         C
50-59         D
0-49          F
"""
def grade_a(mark):
    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 50:
        grade = "D"
    else: grade = "F"
    return grade


"""
Problem Description
A common problem in mathematics is to determine which quadrant a given point lies in. There are four quadrants, numbered
from 1 to 4
For example, the point A, which is at coordinates (12, 5) lies in quadrant 1 since both its x and y values are positive,
and point B (-12, 5) lies in quadrant 2 since its x value is negative and its y value is positive.
Your job is to take a point and determine the quadrant it is in. You can assume that neither of the two coordinates will
be 0.

Input Specification
The first line of input contains the integer x (−1000 ≤ x ≤ 1000; x ̸= 0). The second line of input contains the integer
y (−1000 ≤ y ≤ 1000; y ̸= 0).

Output Specification
Output the quadrant number (1, 2, 3 or 4) for the point (x, y).

Sample Input 1
12
5
Output for Sample Input 1
1

Sample Input 2
9
-13
Output for Sample Input 2
4
"""
def quadrant_1(x,y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    else:
        return 3


"""
Write a programme that prompts the user to enter a year, then returns true if it is a leap year, false otherwise.
"""
def leap_year():
    year = int(input("Please enter year:"))
    if year % 4 == 0:
        return True
    else:
        return False


"""
Write a programme the prompts the user to enter an integer, then returns true if that integer is even, false otherwise.

Sample Run 1:
Enter an integer: 6

Sample Output 1:
6 is an even number

Sample Run 2:
Enter an integer: 7

Sample Output2:
7 is not an even number
"""
def integers():
    number = int(input("Enter an integer:"))
    if number % 2 == 0:
        return str(number) + " is an even number"
    else:
        return str(number) + " is not an even number"



"""
Write a programme the prompts the user to enter two integers, then returns true if the first is divisible by the second

Sample Run:
Enter an integer: 8
Enter a prime number: 2

Sample output:
2 is a factor of 8


Sample Run:
Enter an integer: 9
Enter a prime number: 5

Sample output
5 is not a factor of 9
"""
def prime_numbers():
    integers = int(input("Enter an integer:"))
    prime_number = int(input("Enter a prime number:"))
    if integers % prime_number == 0:
        return str(prime_number) + " is a factor of " + str(integers)
    else:
        return str(prime_number) + " is not a factor of " + str(integers)
