"""
(Check substrings) You can check whether a string is a substring of another string by using the find method in the str
class. Write your own function to implement find. Write a program that prompts the user to enter two strings and then
checks whether the first string is a substring of the second string.
"""

def find(string, substring):
    return substring in string


"""
(Check password) Some Web sites impose certain rules for passwords. Write a function that checks whether a string is a 
valid password. Suppose the password rules are as follows:
■ A password must have at least eight characters.
■ A password must consist of only letters and digits.
■ A password must contain at least two digits.
Write a program that prompts the user to enter a password and displays valid password if the rules are followed or 
invalid password otherwise.
"""
def check_password(password):
    count = 0
    for x in password:
        if x.isdigit():
            count += 1
    return len(password) >= 8 and password.isalnum() and count >= 2


"""
(Occurrences of a specified character) Write a function that finds the number of occurrences of a specified character in 
a string using the following header:
def count(s, ch):
The str class has the count method. Implement your method without using the count method. For example, 
count("Welcome", 'e') returns 2. Write a test program that prompts the user to enter a string followed by a character 
and displays the number of occurrences of the character in the string.
"""
# def count(s, ch):
#     y = 0
#     for x in s:
#         if ch == x:
#             y += 1
#     return y


"""
(Occurrences of a specified string) Write a function that counts the occurrences of a specified non-overlapping string 
s2 in another string s1 using the following header:
def count(s1, s2):
For example, count("system error, syntax error", "error") returns 2. Write a test program that prompts the user to enter 
two strings and displays the number of occurrences of the second string in the first string.
"""
def count(s1, s2):
    if s2 not in s1:
        return 0
    else:
        return s1.count(s2)


"""
(Count the letters in a string) Write a function that counts the number of letters in a string using the following 
header:
def countLetters(s):
Write a test program that prompts the user to enter a string and displays the number of letters in the string.
"""
def countLetters(s):
    y = 0
    for l in s:
        if l.isalpha():
            y += 1
    return y


"""
(Phone keypads) The international standard letter/number mapping for telephones is:
1           2           3
-          abc         def

 4          5           6
ghi        jkl         mno

 7          8           9
pqrs       tuv         wxyz

Write a function that returns a number, given an uppercase letter, as follows:
def getNumber(uppercaseLetter):
Write a test program that prompts the user to enter a phone number as a string. The input number may contain letters. 
The program translates a letter (uppercase or lowercase) to a digit and leaves all other characters intact. Here is a 
sample run of the program:    
 
Enter a string: 1-800-flowers
1-800-3569377

Enter a string: 1800flowers
18003569377
"""
def getNumber(uppercaseLetter):
    y = ""
    for x in uppercaseLetter:
        if x.isalpha():
            if x == "a" or x == "b" or x == "c":
                y += "2"
            elif x == "d" or x == "e" or x == "f":
                y += "3"
            elif x == "g" or x == "h" or x == "i":
                y += "4"
            elif x == "j" or x == "k" or x == "l":
                y += "5"
            elif x == "m" or x == "n" or x == "o":
                y += "6"
            elif x == "p" or x == "q" or x == "r" or x == "s":
                y += "7"
            elif x == "w" or x == "x" or x == "y" or x == "z":
                y += "9"
            else:
                y += "8"
        else:
            y += x
    return y


"""
(Binary to decimal) Write a function that parses a binary number as a string into a decimal integer. Use the function 
header:
def binaryToDecimal(binaryString):
For example,binary string 10001 is 17 (1*24 +0*23 +0*22 +0*2 + 1 = 17). So, binaryToDecimal("10001") returns 17. Write a 
test program that prompts the user to enter a binary string and displays the corresponding decimal integer value.
"""
def binaryToDecimal(binaryString):
    binaryString = binaryString[::-1]
    count = -1
    answer = 0
    for x in binaryString:
        count += 1
        if x == str(1):
            answer += 2 ** count
    return answer


"""
(Reverse a string) Write a function that reverses a string. The header of the function is:
def reverse(s):
Write a test program that prompts the user to enter a string, invokes the reverse
function, and displays the reversed string.
"""
def reverse(s):
    string = ''
    for i in range(len(s)-1, -1, -1):
        string += s[i]
    return string


"""
(Bioinformatics: find genes) Biologists use a sequence of letters A, C, T, and G to model a genome. A gene is a 
substring of a genome that starts after a triplet ATG and ends before a triplet TAG, TAA, or TGA. Furthermore, the 
length of a gene string is a multiple of 3 and the gene does not contain any of the triplets ATG, TAG, TAA, and TGA. 
Write a program that prompts the user to enter a genome and displays all genes in the genome. If no gene is found in 
the input sequence, the program displays no gene is found. Here are the sample runs:

Enter a genome string: TTATGTTTTAAGGATGGGGCGTTAGTT
TTT
GGGCGT

Enter a genome string: TGTGTGTATAT
no gene is found
"""

def find_genes(s):
    first = s.find('ATG')
    tag_index = s.find('TAG')
    taa_index = s.find('TAA')
    tga_index = s.find('TGA')
    if tag_index != -1:
        print(s[first + 3: tag_index])
    elif taa_index != -1:
        print(s[first + 3:taa_index])
    elif tga_index != -1:
        print(s[first + 3:tga_index])
    else:
        print("no gene is found")
