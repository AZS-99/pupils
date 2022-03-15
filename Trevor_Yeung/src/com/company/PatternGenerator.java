package com.company;

import java.lang.reflect.Array;
import java.util.ArrayList;

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
    
    public static ArrayList<ArrayList<ArrayList<Integer>>> patternGenerator(ArrayList<int[]> patterns) {
        var output = new ArrayList<ArrayList<ArrayList<Integer>>>();
        for (int[] array : patterns) {
            output.add(generator(array));
        }
        return output;
    }

    public static ArrayList<ArrayList<Integer>> generator(int[] constraints) {
        var initial = new ArrayList<Integer>();
        for (int i = 0; i < constraints[1]; i++) initial.add(1);
        for (int i = 0; i < constraints[0] - constraints[1]; i++) initial.add(0);
        return new ArrayList<>() {{add(initial);}};
    }
    
}


/*

11100
11010
11001
10110
10101
10011


 */