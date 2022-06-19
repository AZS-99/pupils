"""
Problem J1: Which Alien?
Problem Description
Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our
space. A person who witnessed the appearance of the alien has come forward to describe the alien’s appearance. It is
your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of,
described below:

• TroyMartian, who has at least 3 antenna and at most 4 eyes;
• VladSaturnian, who has at most 6 antenna and at least 2 eyes;
• GraemeMercurian, who has at most 2 antenna and at most 3 eyes.

Input Specification
The user will be prompted to enter two numbers. First, the user will be prompted to enter the number of antenna that
the witness claimed to have seen on the alien. Second, the user will be prompted to enter the number of eyes seen on the
alien.

Output Specification
The output will be the list of aliens who match the possible description given by the witness. If no aliens match the
description, there is no output.

Sample Session 1 (with output shown in text, user input in italics)
How many antennas?
4
How many eyes?
5
VladSaturnian

Sample Session 2
How many antennas?
2
How many eyes?
3
VladSaturnian
GraemeMercurian

Sample Session 3
How many antennas?
8
How many eyes?
6
"""


def alien_test():
    antenna = int(input("How many antennas?\n"))
    eye = int(input("How many eyes?\n"))
    if antenna > 2 and eye < 5:
        print("TroyMartian")
    if antenna < 7 and eye > 1:
        print("VladSaturnian")
    if antenna < 3 and eye < 4:
        print("GraemeMercurian")

