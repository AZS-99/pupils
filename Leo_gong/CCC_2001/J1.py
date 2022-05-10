"""
Dressing Up
It is important to keep our computers safe and clean. Some people feel that computers should be well-dressed, also. For
this question, you will write a program to print out a bow tie on the computer screen.
Your program should take as input the height H of the bow tie, where H is an odd positive integer greater than or equal
to 5. A bow tie with H rows (and 2H columns) should then be printed using the pattern shown below. You may assume that
all input data will be valid.
For this question you should read the input from the keyboard and print the output to the screen.

Sample Session 1: (User input is in italics.)
Enter height:
5
*        *
***    ***
**********
***    ***
*        *

Sample Session 2:
Enter height:
7
*            *
***        ***
*****    *****
**************
*****    *****
***        ***
*            *
"""
def computer_safety():
    height = int(input("Enter height:"))
    for i in range(1, height + 1, 2):
        print("*" * i + " " * (height * 2 - i * 2) + "*" * i)

    for i in range(height - 2, -1, -2):
        print("*" * i + " " * (height * 2 - i * 2) + "*" * i)


    # letter = "*"
    # middle = ""
    # for i in range(1, height, 2):
    #     print(("*" * i) + " " * (height * 2 - i) + ("*" * i))
    #
    # for i in range(height // 2):
    #     middle +=letter
    #     letter += "**"
    # middle = (middle + "**") * 2
    #
    # space = " " * (len(middle) - 2)
    # print(letter)
    # for i in range(height, 2):
    #     print(letter + space + letter)
    #     letter += "**"
    #     space -= "    "


    #for i in range(height // 2):
