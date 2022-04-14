package com.company;

/*
Mathematicians, as opposed to computer scientists, write expressions using single lower case letters as variables.
Addition is represented by a plus sign and multiplication is represented by placing the variables or expressions
adjacent with no symbol in between. Multiplication is done before addition unless the addition is parenthesized.

For this problem, we consider mathematical expressions consisting of only variables, addition, multiplication, and
parentheses. (There are no other symbols, like spaces, division, subtraction, or numerals in the input or output.) For
example,

a+b+c
xyz
xyz+ab+cd
(a+b)(c+d)e

Your task is to read in a number of expressions in this notation and to rearrange each, using the laws of algebra, to
equivalent expressions with no parentheses. For example,
                                                    (a+b)(c+d)e
Can be re-expressed as
                                                  ace+ade+bce+bde
If there are several solutions, any one will do. The order of variables within terms does not matter, nor does the order
of terms within the expression. You do not need to collect like terms; indeed, this is impossible as there are to be no
numerals in the output.

Libraries specifications:
Only formatting and regex

Input and Output Specification

The first line of input contains an integer n. n lines of input follow, each containing a valid expression as described
above. No input line exceeds 100 characters. Your output should consist of n lines, each giving a parenthesis-free
expression equivalent to the corresponding line of input.

Sample Input
5
a+b+c
(a+b)(c+d)e
(c+cb+a+c)
(a+a)(a+a)
((a+b)+(f+g)(c+d))e


Output for Sample Input (order is irrelevant)
a+b+c
ace+ade+bce+bde
c+cb+a+c
aa+aa+aa+aa
ae+be+fce+fde+gce+gde
 */

import com.sun.source.tree.ArrayAccessTree;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SumOfProducts {

    public static String multiply(String string1, String string2) {
        // should be guaranteed to be simplified already
        var S1 = string1.split("[+]");
        var S2 = string2.split("[+]");
        String output = "";
        for (String s1 : S1) {
            for (String s2 : S2) {
                output = output + s1 + s2 + "+";
            }
        }
        output = output.substring(0, output.length()-1);
        return output;
    }

    public static String removeExcessParentheses(String s) {
        int paren = 0;
        if (!(s.charAt(0) == '(') && s.charAt(s.length()-1) == ')' || !s.contains("(")) return s;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') paren++;
            else if (s.charAt(i) == ')') paren--;
            if (paren == 0) {
                if (i == s.length()-1) return s.substring(1, s.length()-1);
                else return s;
            }
        }
        return s;
    }

    public static String getSumOfProducts(String expression) {
        expression = removeExcessParentheses(expression);
        if (!expression.contains("(")) return expression;
        if (expression.charAt(0) != '(') {
            char firstNonLetter = '\0';
            int nonLetterIndex = 0;
            char[] expArray = expression.toCharArray();
            char c;
            for (int i = 0; i < expArray.length; i++) {
                c = expArray[i];
                if (c == '(') {
                    firstNonLetter = '(';
                    nonLetterIndex = i;
                    break;
                }
                else if (c == '+') {
                    firstNonLetter = '+';
                    nonLetterIndex = i;
                    break;
                }
            }
            if (firstNonLetter == '+') return expression.substring(0, nonLetterIndex+1) + getSumOfProducts(expression.substring(nonLetterIndex+1));
            return multiply(expression.substring(0, nonLetterIndex), getSumOfProducts(expression.substring(nonLetterIndex)));
        } else {
            int paren = 0;
            // splitIndex is on the beginning of second segment
            int splitIndex = 0;
            for (int i = 0; i < expression.length(); i++) {
                if (expression.charAt(i) == '(') paren++;
                else if (expression.charAt(i) == ')') paren--;
                if (paren == 0) {
                    splitIndex = i+1;
                    break;
                }
            }

            if (expression.charAt(splitIndex) == '+') return getSumOfProducts(expression.substring(0, splitIndex)) + "+" + getSumOfProducts(expression.substring(splitIndex+1));
            return multiply(getSumOfProducts(expression.substring(0, splitIndex)), getSumOfProducts(expression.substring(splitIndex)));

        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        var s = new Scanner(new File("sumOfProducts"));
        int expressionCount = s.nextInt();
        s.nextLine();
        for (int i = 0; i < expressionCount; i++) {
            System.out.println(getSumOfProducts(s.nextLine()));
        }
    }

}
