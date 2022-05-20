"""
Problem J4: Cyclic Shifts
Problem Description
Thuc likes finding cyclic shifts of strings. A cyclic shift of a string is obtained by moving characters from the
beginning of the string to the end of the string. We also consider a string to be a cyclic shift of itself. For example,
the cyclic shifts of ABCDE are:
ABCDE, BCDEA, CDEAB, DEABC, and EABCD. Given some text, T, and a string, S, determine if T contains a cyclic shift of S.

Input Specification
The input will consist of exactly two lines containing only uppercase letters. The first line will be the text T , and
the second line will be the string S . Each line will contain at most 1000 characters.
For 6 of the 15 available marks, S will be exactly 3 characters in length.

Output Specification
Output yes if the text, T, contains a cyclic shift of the string, S. Otherwise, output no.

Sample Input 1
ABCCDEABAA
ABCDE
Output for Sample Input 1
yes

Explanation of Output for Sample Input 1
CDEAB is a cyclic shift of ABCDE and it is contained in the text ABCCDEABAA.

Sample Input 2
ABCDDEBCAB
ABA
Output for Sample Input 2
no

Explanation of Output for Sample Input 2
The cyclic shifts of ABA are ABA, BAA, and AAB. None of these shifts are contained in the text ABCDDEBCAB.
"""

def generate_cyclic_strings(string: str) -> list:
    lst = [string]
    for i in range((len(string)) - 1):
        string = string[1:] + string[0]
        lst.append(string)
    return lst

def cyclic_shifts():
    file = open("CCC_2020/J4", "r")
    text = file.readline()
    string = file.readline()
    lst = generate_cyclic_strings(string)
    for substring in lst:
        if substring in text:
            print(substring, string)
            return "yes"
    return "no"