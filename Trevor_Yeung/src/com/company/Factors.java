package com.company;



/*
A prime number is a whole number, greater than 1, that can only be divided by itself and the number 1. Every integer
greater than 1 can be uniquely expressed as the product of prime numbers (ignoring reordering those numbers).
This is called the prime factorisation of the number.
For example:
• 100 = 2 x 2 x 5 x 5
• 101 = 101 (since 101 is a prime number)

In this question we are interested in the product of the distinct prime factors of a given number; in other words each
number in the prime factorisation is to be used only once.
 For example:
• Since 100 = 2 x 2 x 5 x 5 the product we require is 10 (i.e. 2 * 5)

Write a program which reads in a single integer n (1 < n < 1,000,000) and outputs a single integer, the product of the
distinct prime factors of n. Your program can have a complexity of at most O(n * log(n))

Sample run 1
100
10

Sample run 2
101
101
 */


import java.util.ArrayList;
import java.util.Arrays;

public class Factors {

    public static ArrayList<Integer> prime(int value) {
        boolean[] primes = new boolean[value+1];
        ArrayList<Integer> primesList = new ArrayList<>();
        Arrays.fill(primes, true);
        primes[0] = primes[1] = false;
        for (int i = 2; i < value+1; i++) {
            if (primes[i]) {
                for (int j = i*i; j < value+1; j+=i) {
                    primes[j] = false;
                }
                primesList.add(i);
            }
        }
        return primesList;
    }

    public static ArrayList<Integer> findFactors(int value) {
        var primes = prime(value);
        var factors = new ArrayList<Integer>();
        for (var prime: primes) {
            if (value%prime == 0) {
                factors.add(prime);
            }
        }
        return factors;
    }

    public static Integer factors(int number) {
        var factors = findFactors(number);
        Integer output = 1;
        for (var factor: factors) {
            output *= factor;
        }
        return output;
    }

}
