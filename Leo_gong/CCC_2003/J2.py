"""
Roy has a stack of student yearbook photos. He wants to lay the pictures on a flat surface edge- to-edge to form a
filled rectangle with minimum perimeter. All photos must be fully visible. Each picture is a square with dimensions 1
unit by 1 unit.
For example, he would place 12 photos in the following configuration, where each photo is indicated with an X
XXXX
XXXX
XXXX
Of course, he could orient them in the other direction, such as
XXX
XXX
XXX
XXX


which would have the same perimeter, 14 units.
Your problem should be interactive. It should repeatedly read a positive integer C, the number of pictures to be laid
out. For each input, it should print the smallest possible perimeter for a filled rectangle that is formed by laying all
the pictures edge-to-edge. Also print the dimensions of this rectangle.
You may assume that there are less than 65,000 photos. An input value of C = 0 indicates that the program should
terminate.

Sample Session User input in italics
Enter number of pictures:
100
Minimum perimeter is 40 with dimensions 10 x 10

Enter number of pictures:
15
Minimum perimeter is 16 with dimensions 3 x 5

Enter number of pictures:
195
Minimum perimeter is 56 with dimensions 13 x 15

Enter number of pictures:
0
"""
import math

def photos():
    num_pictures = int(input("Enter number of pictures:"))
    sqrt_num = math.sqrt(num_pictures)
    num = num_pictures // sqrt_num
    while num_pictures % num != 0:
        num = num - 1
    print("Minimum perimeter is", int((num * 2 + (num_pictures / num) * 2)), "with dimensions", int(num), "x", int(num_pictures / num))