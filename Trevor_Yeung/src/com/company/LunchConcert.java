package com.company;

/*
Problem Description
It’s lunchtime at your school! Your N friends are all standing on a long field, as they usually do. The field can be
represented as a number line, with the ith friend initially at position Pi metres along it. The ith friend is able to
walk in either direction along the field at a rate of one metre per Wi seconds, and their hearing is good enough to be
able to hear music up to and including Di metres away from their position. Multiple students may occupy the same
positions on the field, both initially and after walking.

You’re going to hold a little concert at some position c metres along the field (where c is any integer of your choice),
and text all of your friends about it. Once you do, each of them will walk along the field for the minimum amount of
time such that they end up being able to hear your concert (in other words, such that each friend i ends up within Di
units of c).

You’d like to choose c such that you minimize the sum of all N of your friends’ walking times. What is this minimum sum
(in seconds)? Please note that the result might not fit within a 32-bit integer.

Input Specification
The first line of input contains N.
The next N lines contain three space-separated integers, Pi, Wi, and Di (1 ≤ i ≤ N).

Output Specification
Output one integer which is the minimum possible sum of walking times (in seconds) for all N of your friends to be able
to hear your concert.

Sample Input 1
1
0 1000 0
Output for Sample Input 1
0

Explanation of Output for Sample Input 1
If you choose c = 0, your single friend won’t need to walk at all to hear it.

Sample Input 2
2
10 4 3
20 4 2
Output for Sample Input 2
20

Explanation of Output for Sample Input 2
One possible optimal choice of c is 14, which would require your first friend to walk to position 11
(taking 4 × 1 = 4 seconds) and your second friend to walk to position 16 (taking 4 × 4 = 16 seconds), for a total of 20
seconds.

Sample Input 3
3
6 8 3
1 4 1
14 5 2
Output for Sample Input 3
43
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class LunchConcert {

    public static int sumOfDistances(ArrayList<ArrayList<Integer>> friends, int c) {
        int sum = 0;
        for (ArrayList<Integer> arr : friends) {
            int i = arr.get(1)*(Math.abs(c-arr.get(0))-arr.get(2));
            if (i > 0) sum += i;
        }
        return sum;
    }

    public static int findOptimalPosition(ArrayList<ArrayList<Integer>> friends, int min, int max) {
        int median = (min+max)/2;
        int med1below = sumOfDistances(friends, median-1);
        int atMedian = sumOfDistances(friends, median);
        int med1above = sumOfDistances(friends, median+1);
        if (atMedian < med1above && atMedian > med1below) return findOptimalPosition(friends, min, median);
        if (atMedian > med1above && atMedian < med1below) return findOptimalPosition(friends, median, max);
        return atMedian;
    }

    public static int lunchConcert() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("LunchConcert"));

        int friendCount = scanner.nextInt();
        scanner.nextLine();

        var friends = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i < friendCount; i++) {
            var arr = new ArrayList<Integer>();
            arr.add(scanner.nextInt());
            arr.add(scanner.nextInt());
            arr.add(scanner.nextInt());
            friends.add(arr);
        }

        var positionArr = new ArrayList<Integer>();

        for (ArrayList<Integer> arr : friends) {
            positionArr.add(arr.get(0));
        }

        Collections.sort(positionArr);

        return findOptimalPosition(friends, positionArr.get(0), positionArr.get(positionArr.size()-1)+1);
    }

}
