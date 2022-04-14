"""
A trident is a fork with three tines (prongs). A simple picture of a trident can be made from asterisks and spaces:
*  *  *
*  *  *
*  *  *
*******
   *
   *
   *
   *

In this example, each tine is a vertical column of 3 asterisks. Each tine is separated by 2 spaces. The handle is a
vertical column of 4 asterisks below the middle tine.

Tridents of various shapes can be drawn by varying three parameters: t, the height of the tines, s, the spacing between
tines, and h, the length of the handle. For the example above we have
t = 3, s = 2, and h = 4.

You are to write an interactive program to print a trident. Your program should accept as input the parameters t, s, and
h, and print the appropriate trident. You can assume that t, s, h are each at least 0 and not larger than 10.

Sample Session User input in italics
Enter tine length:
4
Enter tine spacing:
3
Enter handle length:
2
*   *   *
*   *   *
*   *   *
*   *   *
*********
    *
    *
"""
def trident():
    tine_length = int(input("Enter tine length: "))
    tine_space = int(input("Enter tine spacing: "))
    handle = int(input("Enter handle length: "))
    for j in range(tine_length):
        for i in range(3):
            print("*" + " " * tine_space, end="")
        print()
    asterisk_count = 3 + tine_space * 2
    print("*" * asterisk_count)
    for _ in range(handle):
        print(" " * tine_space, "*")
