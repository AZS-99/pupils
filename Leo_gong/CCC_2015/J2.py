"""
Problem Description
We often include emoticons in our text messages to indicate how we are feeling. The three con- secutive characters :-)
indicate a happy face and the three consecutive characters :-( indicate a sad face. Write a program to determine the
overall mood of a message.

Input Specification
There will be one line of input that contains between 1 and 255 characters.

Output Specification
The output is determined by the following rules:
• If the input line does not contain any happy or sad emoticons, output none.
• Otherwise, if the input line contains an equal number of happy and sad emoticons, output unsure.
• Otherwise, if the input line contains more happy than sad emoticons, output happy. • Otherwise, if the input line
  contains more sad than happy emoticons, output sad.

Sample Input 1
How are you :-) doing :-( today :-)?

Output for Sample Input 1
happy

Sample Input 2
:)
Output for Sample Input 2
none

Sample Input 3
This:-(is str:-(:-(ange te:-)xt.
Output for Sample Input 3
sad
"""
def messages():
    file = open("CCC_2015/J2", "r")
    message = file.readline()
    if ":-)" in message and message.count(":-)") == message.count(":-(") and ":-(" in message:
        return "unsure"
    elif ":-)" in message and message.count(":-)") > message.count(":-(") and ":-(" in message:
        return "happy"
    elif ":-)" in message and message.count(":-)") < message.count(":-(") and ":-(" in message:
        return "sad"
    else:
        return "none"