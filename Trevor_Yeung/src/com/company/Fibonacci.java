package com.company;

/*

The nth Fibonacci number, f(n), is defined thus:

f(1) = 1
f(2) = 1
f(n) = f(n-1) + f(n-2) [for all n > 2]

Write a program that reads several n, one per line, and writes the corresponding f(n), one per line. Each value of n
will be between 1 and 200. The last line of input contains 0.

Sample input

1
2
3
4
5
90
0

Output for sample input

1
1
2
3
5
2880067194370816120
 */


import java.util.HashMap;

public class Fibonacci {

    HashMap<Long, Long> fNums = new HashMap<>();

    public long fibonacci(long n) {
        for (long i = 1; i <= n; i++) {
            if (i <= 2) fNums.put(i-1, (long)1);
            else fNums.put(i-1, fNums.get(i-2) + fNums.get(i-3));
        }
        return fNums.get((long)fNums.size()-1);
    }

}
