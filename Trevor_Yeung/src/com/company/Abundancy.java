package com.company;

/*
Write a program that repeatedly reads a positive integer, determines if the integer is deficient, perfect, or abundant,
and outputs the number along with its classification.

A positive integer, n, is said to be perfect if the sum of its proper divisors equals the number itself.
(Proper divisors include 1 but not the number itself.) If this sum is less that n, the number is deficient, and if the
sum is greater than n, the number is abundant.

The input starts with the number of integers that follow. For each of the following integers, your program should output
the classification, as given below. You may assume that the input integers are greater than 1 and less than 32500.

Sample input
3
4
6
12

Sample output
4 is a deficient number.
6 is a perfect number.
12 is an abundant number
 */

public class Abundancy {

    public static String abundancy(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) {
            if (n%i == 0) sum += i;
        }
        if (sum == n) return n + " is a perfect number";
        if (sum < n) return n + " is a deficient number";
        return n + " is an abundant number";
    }

}
