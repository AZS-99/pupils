"""
Problem J3: Returning Home
Jane's family has just moved to a new city and today is her first day of school. She has a list of instructions for
walking from her home to the school. Each instruction describes a turn she must make. For example, the list

R
QUEEN
R
FOURTH
R
SCHOOL

means that she must turn right onto Queen Street, then turn right onto Fourth Street, then finally turn right into the
school. Your task is to write a computer program which will create instructions for walking in the opposite direction:
from her school to her home. The input and output for your program will be formatted like the samples below. You may
assume that Jane's list contains at least two but at most five instructions, and you may assume that each line contains
at most 10 characters, all of them capital letters. The last instruction will always be a turn into the "SCHOOL".

Sample Input 1
R
QUEEN
R
FOURTH
R
SCHOOL

Sample Output for Sample Input 1
Turn LEFT onto FOURTH street.
Turn LEFT onto QUEEN street.
Turn LEFT into your HOME.

Sample Input 2
L
MAIN
R
SCHOOL

Sample Output for Sample Input 2
Turn LEFT onto MAIN street.
Turn RIGHT into your HOME.
"""
def returning_home():
    file = open("CCC_2005/J3", "r")
    while file.readline() != 'SCHOOL':

