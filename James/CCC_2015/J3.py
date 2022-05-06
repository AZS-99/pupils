"""
Problem Description
In Sweden, there is a simple child’s game similar to Pig Latin called Ro ̈varspra ̊ket (Robbers Language).
In the CCC version of Ro ̈varspra ̊ket, every consonant is replaced by three letters, in the following order:
• the consonant itself;
• the vowel closest to the consonant in the alphabet (e.g., if the consonant is d, then the closest vowel is e), with
the rule that if the consonant falls exactly between two vowels, then the vowel closer to the start of the alphabet will
be chosen (e.g., if the consonant is c, then the closest vowel is a);
• the next consonant in the alphabet following the original consonant (e.g., if the consonant is d, then the next
 consonant is f) except if the original consonant is z, in which case the next consonant is z as well.

Vowels in the word remain the same. (Vowels are a, e, i, o, u and all other letters are consonants.) Write a program
that translates a word from English into Ro ̈varspra ̊ket.

Input Specification
The input consists of one word entirely composed of lower-case letters. There will be at least one letter and no more
than 30 letters in this word.

Output Specification
Output the word as it would be translated into Ro ̈varspra ̊ket on one line.

Sample Input 1
joy
Output for Sample Input 1
jikoyuz

Sample Input 2
ham
Output for Sample Input 2
hijamon
"""
def choose_vowel(letter, v1, v2):
    if ord(letter) <= (ord(v1) + ord(v2)) / 2:
        return v1
    return v2



def robberslang():
    file = open("CCC_2015/J3", "r")
    letters = [x for x in file.readline()]
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = str()
    for letter in letters:
        if letter not in vowels:
            if ord('a') < ord(letter) < ord('e'):
                string += letter + choose_vowel(letter, 'a', 'e') + (chr(ord(letter) + 1) if chr(ord(letter) + 1) not in vowels else chr(ord(letter) + 2))
            elif ord('e') < ord(letter) < ord('i'):
                string += letter + choose_vowel(letter, 'e', 'i') + (
                    (ord(letter) + 1) if chr(ord(letter) + 1) not in vowels else chr(ord(letter) + 2))
            elif ord('i') < ord(letter) < ord('o'):
                string += letter + choose_vowel(letter, 'i', 'o') + (chr(ord(letter) + 1) if chr(ord(letter) + 1) not in vowels else chr(ord(letter) + 2))
            elif ord('o') < ord(letter) < ord('u'):
                string += letter + choose_vowel(letter, 'o', 'u') + (chr(ord(letter) + 1) if chr(ord(letter) + 1) not in vowels else chr(ord(letter) + 2))
            elif letter == 'z':
                string += letter + 'u' + 'z'
            else:
                string += letter + 'u' + chr(ord(letter) + 1)
        else:
            string += letter
    print(string)