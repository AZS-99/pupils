package com.company;

import java.util.ArrayList;
import java.util.Collections;

/*

Write a program that repeatedly reads two numbers n and k and prints all bit patterns of length n with k ones in
descending order (when the bit patterns are considered as binary numbers). You may assume that 30 >= n > 0, 8 > k >= 0,
and n >= k. The first number in the input gives the number of pairs n and k. The numbers n and k are separated by
a single space. Leading zeroes in a bit pattern should be included. See the example below.

Sample input

3
2 1
2 0
4 2

Sample output

The bit patterns are

10
01

The bit patterns are
00

The bit patterns are
1100
1010
1001
0110
0101
0011
 */


public class PatternGenerator {

    public static ArrayList<ArrayList<Integer>> patternGen(int n, int k) {
        var output = new ArrayList<ArrayList<Integer>>();
        if (k == 0) {
            var arr = new ArrayList<>(Collections.nCopies(n, 0));
            output.add(arr);
            return output;
        }
        var less1 = patternGen(n-1, k-1);
        for (var arr: less1) {
            for (int i = 0; i <= arr.size(); i++) {
                var arr1 = new ArrayList<>(arr);
                arr1.add(i, 1);
                if (!output.contains(arr1)) output.add(arr1);
            }
        }
        return output;
    }
    
}

/*

100
010
001

public static ArrayList<ArrayList<ArrayList<Integer>>> patternGenerator(ArrayList<int[]> patterns) {
        var output = new ArrayList<ArrayList<ArrayList<Integer>>>();
        for (int[] array : patterns) {
            output.add(generator(array));
        }
        return output;
    }

    public static ArrayList<ArrayList<Integer>> generator(int[] constraints) {
        var initial = new ArrayList<Integer>();
        var output = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < constraints[1]; i++) initial.add(1);
        for (int i = 0; i < constraints[0] - constraints[1]; i++) initial.add(0);
        output.add(initial);
        var moved = true;
        var digitCount = new HashMap<Integer, Integer>();
        while (moved) {
            digitCount = new HashMap<>();
            digitCount.put(0, 0);
            digitCount.put(1, 0);
            moved = false;
            var recent = output.get(output.size()-1);
            var last1 = recent.lastIndexOf(1);
            while (last1 == recent.size()-1 || recent.get(last1+1) == 1) {
                if (recent.indexOf(1) == last1) return output;
                last1 = recent.subList(0, last1).lastIndexOf(1);
            }
            for (int digit : recent.subList(last1, recent.size()-1)) {
                digitCount.put(digit, digitCount.get(digit)+1);
            }
            recent = (ArrayList<Integer>) recent.subList(0, last1+1);
            for (int i = 0; i<digitCount.get(1); i++) {
                recent.add(1);
            }
            for (int i = 0; i<digitCount.get(0); i++) {
                recent.add(0);
            }
            output.add(recent);
        }
        return output;
    }

 */