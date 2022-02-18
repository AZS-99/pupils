package com.company;

/*
A palindrome is a sequence of characters that reads the same forwards and backwards. e.g. RADAR, MADAMIMADAM
You are to write a program which finds the longest palindrome in a given string of characters.

Input:
The input file will begin with a line containing one positive integer n, the number of strings to be tested, followed by
n lines each containing one string of characters of up to 25,000 characters in length and terminated with a blank. The
input strings will contain upper case letters only.

Output:
Your program should output a pair of lines for each test case with the palindrome on the first line and the length of
the palindrome on the second. In the event of a tie for longest, any of the palindromes in the tie may be reported.
Sample Input

1
AHAHJHFYUBNMLOIUYTRERTYUIOLMNBAGWOIS
Output for sample input

BNMLOIUYTRERTYUIOLMNB
21
 */

public class Palindrome {

    public static boolean isPalindrome(String s) {
        if (s.length() < 2) return true;
        return (s.charAt(0) == s.charAt(s.length()-1) && isPalindrome(s.substring(1, s.length()-1)));
    }

    public static String longestPalindrome(String s) {
        if (isPalindrome(s)) return s;
        String p1 = longestPalindrome(s.substring(1));
        String p2 = longestPalindrome(s.substring(0, s.length()-2));
        System.out.println(p1);
        System.out.println(p2);
        return p1.length() > p2.length()?  p1 : p2;
    }

}
