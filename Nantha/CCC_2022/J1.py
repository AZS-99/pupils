"""
Problem Description
A regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes. There are 28 students in a class and a
total of at least 28 cupcakes. Your job is to determine how many cupcakes will be left over if each student gets one
cupcake.

Input Specification
The input consists of two lines
• The first line contains an integer R ≥ 0, representing the number of regular boxes.
• The second line contains an integer S ≥ 0, representing the number of small boxes.

Output Specification
Output the number of cupcakes that are left over.

Sample Input 1
2
5
Output for Sample Input 1
3

Explanation of Output for Sample Input 1
The total number of cupcakes is 2 × 8 + 5 × 3 which equals 31. Since there are 28 students, there are 3 cupcakes left
over.

Sample Input 2
2
4
Output for Sample Input 2
0

Explanation of Output for Sample Input 2
The total number of cupcakes is 2 × 8 + 4 × 3 which equals 28. Since there are 28 students, there are no cupcakes left
over.
"""

def cupcakes_fn():
    file = open("CCC_2022/J1")
    regular_boxes = int(file.readline())
    small_boxes = int(file.readline())
    cupcakes = regular_boxes * 8 + small_boxes * 3
    leftover = cupcakes - 28
    print(leftover)