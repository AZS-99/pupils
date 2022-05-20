"""
Keeping Score
In a card game, each player's hand is made up of 13 cards. Each hand has a total point value determined by the number of
cards that have a point value. The cards which are worth points are the Ace (4 points), King (3 points), Queen
(2 points) and Jack (1 point). The other cards (2, 3, 4, 5, 6, 7, 8, 9, 10) have no point value. There are four of each
type of card, one in each of the four suits. The suits are called clubs (C), diamonds (D), hearts (H), and spades (S).
As well, points are assigned for each suit which has a void (3 points), a singleton (2 points), or a doubleton
(1 point). A void in a suit means that there are no cards of that suit (e.g. a hand with no spades). A singleton in a
suit means that there is only one card in that suit (e.g. a hand with only one diamond). A doubleton in a suit means
that there are only two cards in that suit.

Write a program to read a set of thirteen cards in the form of a string, then evaluate the number of points in the hand.
The suits will appear in increasing alphabetical order. Within each suit there will be no duplicate cards.
The output is to be the hand and the point value shown in a table form as below. Your output should list the cards in
the same order as the input. Note that 10 is represented by the character T in both the input and the output. Input is
from the keyboard, output to the screen.

Sample session (user input in italics)
Enter cards:
C258TJKD69QAHSTJA

Cards Dealt                 points
Clubs 2 5 8 T J K             4
Diamonds 6 9 Q A              6
Hearts                        3
Spades T J A                  5
                            Total 18

Enter cards:
CAD578KAHAS47TQKA

Cards Dealt                 points
Clubs A                       6
Diamonds 5 7 8 K A            7
Hearts A                      6
Spades 4 7 T Q K A            9
                            Total 28
"""
def card_game():
    cards = input("Enter cards:")
    cards_lst = [x for x in cards]
    c = d = h = s = 0
    dic = {"A": 4, "K": 3, "Q":2, "J": 1}
    num_dic = {0: 3, 1: 2, 2: 1}
    index_c = cards.find("C")
    index_d = cards.find("D")
    index_h = cards.find("H")
    index_s = cards.find("S")

    clubs = cards[1:index_d]
    diamonds = cards[index_d+1:index_h]
    hearts = cards[index_h+1:index_s]
    spades = cards[index_s+1:]

    for ch in clubs:
        if ch in dic.keys():
            c += dic[ch]

    c_count = len(clubs)
    if c_count in num_dic.keys():
        c += num_dic[c_count]

    for i in range(len(diamonds)):
        ch = clubs[i]
        if ch in dic.keys():
            d += dic[ch]

    d_count = len(hearts)
    if d_count - 1 in num_dic.keys():
        d += num_dic[d_count]

    for i in range(len(clubs)):
        ch = clubs[i]
        if ch in dic.keys():
            h += dic[ch]

    h_count = len(clubs)
    if h_count - 1 in num_dic.keys():
        h += num_dic[h_count]

    for i in range(len(clubs)):
        ch = clubs[i]
        if ch in dic.keys():
            s += dic[ch]

    s_count = len(clubs)
    if s_count - 1 in num_dic.keys():
        s += num_dic[s_count]




    print(clubs, c)
    print()






