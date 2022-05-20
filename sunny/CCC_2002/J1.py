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


  * * *
 *
 *
 *
   * * *
         *
         *
         *
   * * *


   * * *
 *
 *
 *
   * * *
 *       *
 *       *
 *       *
   * * *

`
"""
def sample_input():
    enter = int(input("Enter a digit between 0 and 9: "))

    if enter == 1:
        for i in range(0, 3):
            print(" " * 7 + "*")
        print(" ")
        for i in range(0, 3):
            print(" " * 7 + "*")

    elif enter == 2:
        print("  " + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 8 + "*")
        print("  " + "* * *" + " ")
        for i in range(0, 3):
            print("*")
        print("  " + "* * *" + " ")

    elif enter == 3:
        print("  " + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 8 + "*")
        print("  " + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 8 + "*")
        print("  " + "* * *" + " ")

    elif enter == 4:
        for i in range(0, 3):
            print(" " + "*" + " " * 7 + "*")
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 9 + "*")

    elif enter == 5:
        print(" " * 3 + "* * *" + "  ")
        for i in range(0, 3):
            print(" " + "*")
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 9 + "*")
        print(" " * 3 + "* * *" + " ")

    elif enter == 6:
        print(" " * 3 + "* * *" + "  ")
        for i in range(0, 3):
            print(" " + "*")
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " + "*" + " " * 7 + "*")
        print(" " * 3 + "* * *" + "  ")

    elif enter == 7:
        print(" " + "* * *" + " ")
        print(" " * 7 + "*")
        for i in range(0, 2):
            print(" " * 7 + "*")
        print(" ")
        for i in range(0, 3):
            print(" " * 7 + "*")

    elif enter == 8:
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " + "*" + " " * 7 + "*")
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " + "*" + " " * 7 + "*")
        print(" " * 3 + "* * *" + " ")

    else:
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " + "*" + " " * 7 + "*")
        print(" " * 3 + "* * *" + " ")
        for i in range(0, 3):
            print(" " * 9 + "*")
        print(" " * 3 + "* * *" + " ")







