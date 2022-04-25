"""
Problem Description
A palindrome is a word which is the same when read forwards as it is when read backwards. For example, mom and anna are
two palindromes.

A word which has just one letter, such as a, is also a palindrome.
Given a word, what is the longest palindrome that is contained in the word? That is, what is the longest palindrome that
we can obtain, if we are allowed to delete characters from the beginning and/or the end of the string?

Input Specification
The input will consist of one line, containing a sequence of at least 1 and at most 40 lowercase letters.
Output Specification
Output the total number of letters of the longest palindrome contained in the input word.

Sample Input 1
banana
Output for Sample Input 1
5

Explanation for Output for Sample Input 1
The palindrome anana has 5 letters.

Sample Input 2
abracadabra
Output for Sample Input 2
3

Explanation for Output for Sample Input 2
The palindromes aca and ada have 3 letters, and there are no other palindromes in the input which are longer.

Sample Input 3
abba
Output for Sample Input 3
4
"""

def isPalindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - (i + 1)]:
            return False
    return True


def palindrome():
    file = open("CCC_2016/J3", "r")
    word = file.readline()
    if isPalindrome(word):
        return len(word)
    longest = str()
    for i in range(len(word)):
        for j in range(i, len(word)):
            if isPalindrome(word[i:j]) and len(word[i:j]) > len(longest):
                longest = word[i:j]
    return len(longest)

