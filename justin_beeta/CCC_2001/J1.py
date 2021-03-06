"""
Dressing Up
It is important to keep our computers safe and clean. Some people feel that computers should be well-dressed, also. For
this question, you will write a program to print out a bow tie on the computer screen.
Your program should take as input the height H of the bow tie, where H is an odd positive integer greater than or equal
to 5. A bow tie with H rows (and 2H columns) should then be printed using the pattern shown below. You may assume that
all input data will be valid.

For this question you should read the input from the keyboard and print the output to the screen.
Sample Session: (User input is in italics.)
Enter height:
5

*        *
***    ***
**********
***    ***
*        *

Enter height:
7
*            *
***        ***
*****    *****
**************



*
***
*****
*******
*****
***
*

"""
def bow_tie_on_computer():
    num = int(input("Enter height:"))
    for i in range(1, num + 1, 2):
        num_of_asterisks = i * 2
        num_space = num * 2 - num_of_asterisks
        print("*" * i + " " * num_space + "*" * i)

    for j in range(num - 2, 0, -2):
        num_of_asterisks = j * 2
        num_space = num * 2 - num_of_asterisks
        print("*" * j + " " * num_space + "*" * j)

