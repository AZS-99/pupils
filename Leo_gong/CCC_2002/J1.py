"""
Most digital devices show numbers using a seven segment display. The seven segments are arranged as shown:

  * * *
*       *
*       *
*       *
  * * *
*       *
*       *
*       *
  * * *

For this problem each segment is represented by three asterisks in a line as shown above. Any digit from 0 - 9 can be
shown by illuminating the appropriate segments. For example the digit 1 may be displayed using the two segments on the
right side:

       *
       *
       *

       *
       *
       *


The digit 4 needs four segments to display it properly:


*       *
*       *
*       *
  * * *
        *
        *
        *


Sample Session. User input in italics
Enter a digit between 0 and 9:
9

  * * *
*       *
*       *
*       *
  * * *
        *
        *
        *
  * * *

"""
def nine_numbers():
    num = int(input("Enter a digit between 0 and 9:"))
    if num == 0:
        print("  " + "* " * 3 + " ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print(" ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")

    elif num == 1:
        print(" ")
        print(" " * 6 + "*")
        print(" " * 6 + "*")
        print(" " * 6 + "*")
        print(" ")
        print(" " * 6 + "*")
        print(" " * 6 + "*")
        print(" " * 6 + "*")

    elif num == 2:
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print("  " + "* " * 3 + " ")
        print("*")
        print("*")
        print("*")
        print("  " + "* " * 3 + " ")

    elif num == 3:
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print("  " + "* " * 3 + " ")

    elif num == 4:
        print(" ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
    elif num == 5:
        print("  " + "* " * 3 + " ")
        print("*")
        print("*")
        print("*")
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print("  " + "* " * 3 + " ")

    elif num == 6:
        print("  " + "* " * 3 + " ")
        print("*")
        print("*")
        print("*")
        print("  " + "* " * 3 + " ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")

    elif num == 7:
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")

    elif num == 8:
        print("  " + "* " * 3 + " ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")

    else:
        print("  " + "* " * 3 + " ")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("*", " " * 5, "*")
        print("  " + "* " * 3 + " ")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print(" ", " " * 5, "*")
        print("  " + "* " * 3 + " ")