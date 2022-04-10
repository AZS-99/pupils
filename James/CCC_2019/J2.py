"""
Problem Description
You and your friend have come up with a way to send messages back and forth.
Your friend can encode a message to you by writing down a positive integer N and a symbol. You
can decode that message by writing out that symbol N times in a row on one line. Given a message that your friend has
encoded, decode it.

Input Specification
The first line of input contains L, the number of lines in the message.
The next L lines each contain one positive integer less than 80, followed by one space, followed
by a (non-space) character.

Output Specification
The output should be L lines long. Each line should contain the decoding of the corresponding line of the input.
Specifically, if line i + 1 of the input contained N x, then line i of the output should contain just the character x
printed N times.

Sample Input
4
9 +
3 -
12 A
2 X

Output for Sample Input
+++++++++
---
AAAAAAAAAAAA
XX
"""
def decode():
    file = open("CCC_2019/J2")
    lines = int(file.readline())
    for i in range(lines):
        [charnum, character] = [x for x in file.readline().split(" ")]

        charnum = int(charnum)
        if i < lines - 1:
            character = character[:-1]

        print(character * charnum, end="")
        print()


