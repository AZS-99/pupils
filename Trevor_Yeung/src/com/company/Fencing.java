package com.company;

/*
Problem Description
You need to paint a wooden fence between your house and your neighbour’s house. You want to determine the area of the
fence, in order to determine how much paint you will use.
However, the fence is made out of N non-uniform pieces of wood, and your neighbour believes that they have an artistic
flair. In particular, the pieces of wood may be of various widths. The bottom of each piece of wood will be horizontal,
both sides will be vertical, but its top may be cut on an angle.

Thankfully, the fence has been constructed so that adjacent pieces of wood have the same height on the sides where they
touch, which makes the fence more visually appealing.


Input Specification
The first line of the input will be a positive integer N, where N ≤ 10000.
The second line of input will contain N +1 space-separated integers h1,...,hN+1 (1 ≤ hi ≤ 100, 1 ≤ i ≤ N + 1) describing
the left and right heights of each piece of wood. Specifically, the left height of the ith piece of wood is hi and the
right height of the ith piece of wood is hi+1 .
The third line of input will contain N space-separated integers wi (1 ≤ wi ≤ 100, 1 ≤ i ≤ N) describing the width of the
ith piece of wood.

Output Specification
Output the total area of the fence.

Sample Input 1
3
2 3 6 2
4 1 1


Output for Sample Input 1
18.5


Sample Input 2
4
6 4 9 7 3
5 2 4 1
Output for Sample Input 2
75

 */

import java.util.ArrayList;

public class Fencing {

    public static double getArea(ArrayList<Integer> heights, ArrayList<Integer> widths) {
        int count = widths.size();
        double area = 0;
        for (int i = 0; i < count; i++) {
            area += (((double)(heights.get(i)+heights.get(i+1))/2)*widths.get(i));
        }
        return area;
    }

}
