package com.company;

/*
Problem Description
For various given positive integers N > 3, find two primes, A and B such that N is the average (mean) of A and B. That
 is, N should be equal to (A + B)/2.
Recall that a prime number is an integer P > 1 which is only divisible by 1 and P . For example, 2, 3, 5, 7, 11 are the
first few primes, and 4, 6, 8, 9 are not prime numbers.

Input Specification
The first line of input is the number T (1 ≤ T ≤ 1000), which is the number of test cases. Each of the next T lines
contain one integer Ni (4 ≤ Ni ≤1000000,1 ≤i ≤T).

Output Specification
The output will consist of T lines. The ith line of output will contain two integers, Ai and Bi, separated by one space.
It should be the case that Ni = (Ai + Bi)/2 and that Ai and Bi are prime numbers.
If there are more than one possible Ai and Bi for a particular Ni, output any such pair. The order of the pair Ai and Bi
does not matter.
It will be the case that there will always be at least one set of values Ai and Bi for any given Ni.

Sample Input
4
8
4
7
21

Possible Output for Sample Input
3 13
5 3
7 7
13 29

Footnote
You may have heard about Goldbach’s conjecture, which states that every even integer greater than 2 can be expressed as
the sum of two prime numbers. There is no known proof, yet, so if you want to be famous, prove that conjecture
(after you finish the CCC).
This problem can be used to help verify that conjecture, since every even integer can be written as 2N,
and your task is to find two primes A and B such that 2N = A+B.
 */

import java.util.ArrayList;
import java.util.Scanner;
import java.util.Collections;
import java.io.File;
import java.io.FileNotFoundException;

public class Goldbachs {

    public static ArrayList<Boolean> primesToN(int n) {
        var primes = new ArrayList<>(Collections.nCopies(n, true));
        primes.set(0, false);
        primes.set(1, false);
        for (int i = 2; i < n; i++) {
            if (primes.get(i)) {
                for (int j = i*i; j < n; j+=i) {
                    primes.set(j, false);
                }
            }
        }
        return primes;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new File("Goldbachs"));

        var numArr = new ArrayList<Integer>();
        int count = sc.nextInt();
        for (int i = 0; i < count; i++) {
            numArr.add(sc.nextInt());
        }
        System.out.println(Collections.max(numArr));
        var primes = primesToN(2*Collections.max(numArr) + 1);

        for (int n : numArr) {
            for (int i = 0; i < n; i++) {
                if (primes.get(i) && primes.get(2*n-i)) {
                    System.out.println(i + " " + (2*n-i));
                    break;
                }
            }
        }

    }

}
