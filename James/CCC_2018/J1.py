"""
Problem Description
Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers
where the last four digits have three properties. Looking just at the last four digits, these properties are:

• the first of these four digits is an 8 or 9;
• the last digit is an 8 or 9;
• the second and third digits are the same.

For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.
Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. If the
number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore it.

Input Specification
The input will be 4 lines where each line contains exactly one digit in the range from 0 to 9.

Output Specification
Output either ignore if the number matches the pattern for a telemarketer number; otherwise, output answer.

Sample Input 1
9
6
6
8
Output for Sample Input 1
ignore

Explanation of Output for Sample Input 1
The first digit is 9, the last digit is 8, and the second and third digit are both 6, so this is a telemarketer number.

Sample Input 2
5
6
6
8
Output for Sample Input 2
answer

Explanation of Output for Sample Input 2
The first digit is 5, and so this is not a telemarketer number.
"""
def telephone():
    file = open("CCC_2018/J1")
    numbers = []
    for i in range(4):
        numbers.append(int(file.readline()))
    if (numbers[0] == 8 or numbers[0] == 9) and numbers[1] == numbers[2] and (numbers[3] == 8 or numbers[3] == 9):
        print("ignore")
    else:
        print("answer")

