import random
"""
Write a program that lets the user guess whether a flipped coin displays the head or the tail. The program randomly 
generates an integer 0 or 1, which represents head or tail. The program prompts the user to enter a guess and reports 
whether the guess is correct or incorrect.
"""

def coin_flip(guess):
    x = random.randint(0, 1)
    if guess == x:
        print("Correct")
    else:
        print("Incorrect")


"""
Write a program that generates two integers under 100 and prompts the user to enter the sum of these two integers. 
The program then reports true if the answer is correct, false otherwise. 
"""

def sum():
    first_number = random.randint(1, 99)
    second_number = random.randint(1, 99)
    sum2 = first_number + second_number
    guess = int(input("Enter the sum of " + str(first_number) + " and " + str(second_number)))
    if guess == sum2:
        print("nice")
    else:
        print("wrong")


"""
Write a program that displays a random uppercase letter.
"""

def random_uppercase_letter():
    x = random.randint(65, 90)
    print(chr(x))


"""
Pick a random character from a given String
"""

def random_character(string):
    y = len(string)
    index = random.randint(0, y - 1)
    print(string[index])


"""
Generate random String of length 5

Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
"""

def random_string():
    x = random.randint(65, 90)
    y = random.randint(97, 122)
    a = random.randint(65, 90)
    b = random.randint(97, 122)
    c = random.randint(65, 90)
    string = chr(x) + chr(y) + chr(a) + chr(b) + chr(c)
    return string


"""
(Game: pick a card ) Write a program that simulates picking a card from a deck of 52 cards. Your program should display 
the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card. 
Here is a sample run of the program:
The card picked for you is the Jack of Hearts
"""

def random_card():
    rank = random.randint(1, 13)
    suit = random.randint(14, 17)

    dic = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Clubs', 15: "Diamonds", 16: 'Hearts', 17: 'Spades'}
    if 2<= rank <= 10:
        print("The card picked for you is the", rank, "of", dic[suit])
    else:
        print("The card picked for you is the", dic[rank], "of", dic[suit])
