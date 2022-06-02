"""
Problem Description
You have been asked to take a small icon that appears on the screen of a smart telephone and scale it up so it looks
bigger on a regular computer screen.
The icon will be encoded as characters (x and *) in a 3 × 3 grid as follows:
*x*
 xx
* *

Write a program that accepts a positive integer scaling factor and outputs the scaled icon. A scaling factor of k means
that each character is replaced by a k × k grid consisting only of that character.

Input Specification
The input will be a positive integer k such that k < 25.

Output Specification
The output will be 3k lines, which represent each individual line scaled by a factor of k and repeated k times. A line
is scaled by a factor of k by replacing each character in the line with k copies of the character.

Sample Input
3
Output for Sample Input
***xxx***
***xxx***
***xxx***
   xxxxxx
   xxxxxx
   xxxxxx
***   ***
***   ***
***   ***
"""
def scale_it_up():
    file = open("CCC_2012/J3", 'r')
    times = int(file.readline())
    for i in range(times):
        print("*" * times + "x" * times + "*" * times)
    for i in range(times):
        print(" " * times + "x" * times + "*" * times)
    for i in range(times):
        print("*" * times + " " * times + "*" * times)

