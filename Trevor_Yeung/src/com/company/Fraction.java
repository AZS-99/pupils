package com.company;

import java.util.ArrayList;

/*
When ancient Egyptians wrote fractions they were only able to use ones of the form 1/a, called unit fractions. An
Egyptian wanting to write the fraction b/c, where b was not 1, had to write it as the sum of (different) unit fractions.
 All fractions b/c (b < c) can be written as an Egyptian fraction. For example, the fraction 5/6 was written as
 1/2 + 1/3, and 6/7 was written as 1/2 + 1/3 + 1/42.
 2/3 can be written as 1/2 + 1/6, but not 1/3 + 1/3, since each term of the Egyptian Fraction has to be 'maximal'.
 Another example is 19/45 which cannot be represented as the sum of two unit fractions, but there are 5 ways of
 representing it as the sum of 3 unit fractions: 1/3 + 1/12 + 1/180, 1/3 + 1/15 + 1/45, 1/3 + 1/18 + 1/30,
 1/4 + 1/6 + 1/180 and 1/5 + 1/6 + 1/18. Only the first combination is correct.

 Write a program that inputs two numbers a and b, and calculates an Egyptian fraction representing a/b with no more
 than a unit fractions. You will only be given fractions with 0 < a < b < 1000. Your program should then output the
 denominators (bottom parts) of the unit fractions.

Sample run
Numerator: 19
Denominator: 45
3 12 180
 */

public class Fraction {

    public int num;
    public int den;

    public Fraction(int num, int den) {
        int gcd = GCD(num, den);
        this.num = num/gcd;
        this.den = den/gcd;

    }

    public String toString(){
        return num + "/" + den;
    }
    public int GCD(int n1, int n2) {
        int result = 1;
        for (int i = 1; i <= n1; i++) {
            if (n1%i == 0 && n2%i == 0) {
                result = i;
            }
        }
        return result;
    }

    public int LCM(int n1, int n2) {
        return (n1*n2)/GCD(n1, n2);
    }

    public Fraction add(Fraction f) {
        int lcm = LCM(den, f.den);
        int num1 = (lcm / den) * num;
        int num2 = (lcm / f.den) * f.num;
        return new Fraction((num1 + num2), lcm);
    }

    public Fraction subtract(Fraction f) {
        int lcm = LCM(den, f.den);
        int num1 = (lcm / den) * num;
        int num2 = (lcm / f.den) * f.num;
        return new Fraction((num1 - num2), lcm);
    }

    public static ArrayList<Integer> EgyptianFraction(Fraction f) {
        ArrayList<Integer> subfractions = new ArrayList<>();
        for (int i = 2; i <= 999; i++) {
            if ((new Fraction(1, i).subtract(f)).num <= 0) {
                f = f.subtract((new Fraction(1, i)));
                subfractions.add(i);
            }
        }
        return subfractions;
    }

}
