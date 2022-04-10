"""
Problem Description
In Sweden, there is a simple child’s game similar to Pig Latin called Ro ̈varspra ̊ket (Robbers Lan- guage).
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
def Ro_varspra_ket():
    file = open("CCC_2015/J3", "r")
    string = str()
    word = file.readline()
    vowels_lst = [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]
    for i in range(len(word)):
        letter = word[i]
        consonant_ascii = ord(letter)
        if letter in ['a', 'e', 'i', 'o', 'u']:
            string += str(letter)
        else:
            string += letter
            min_difference = float('inf')
            chosen_vowel = str()
            for j in range(5):
                # a
                vowel_ascii = vowels_lst[j]
                difference = abs(consonant_ascii - vowel_ascii)
                if difference < min_difference:
                    min_difference = difference
                    chosen_vowel = chr(vowel_ascii)
            string += chosen_vowel
            string += chr(consonant_ascii + 1) if chr(consonant_ascii + 1) not in ['a', 'e', 'i', 'o', 'u'] \
                else chr(consonant_ascii + 2)
    return string
