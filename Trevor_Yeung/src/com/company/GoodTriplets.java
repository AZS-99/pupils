package com.company;

/*
Problem Description
Andrew is a very curious student who drew a circle with the center at (0, 0) and an integer circumference of C ≥ 3. The
location of a point on the circle is the counter-clockwise arc length from the right-most point of the circle.

Andrew drew N ≥ 3 points at integer locations. In particular, the ith point is drawn at location Pi (0 ≤ Pi ≤ C − 1).
It is possible for Andrew to draw multiple points at the same location.

A good triplet is defined as a triplet (a, b, c) that satisfies the following conditions:
• 1 ≤ a < b < c ≤ N.
• The origin (0, 0) lies strictly inside the triangle with vertices at Pa , Pb , and Pc . In particular, the origin is
not on the triangle’s perimeter.

Lastly, two triplets (a, b, c) and (a′, b′, c′) are distinct if a ̸= a′, b ̸= b′, or c ̸= c′.
Andrew, being a curious student, wants to know the number of distinct good triplets. Please
help him determine this number.

Input Specification
The first line contains the integers N and C, separated by one space.
The second line contains N space-separated integers. The ith integer is Pi (0 ≤ Pi ≤ C − 1).

Output Specifications:
Output the number of distinct good triplets.
Sample Input
8 10
0 2 5 5 6 9 0 0

Output for Sample Input
6

Explanation of Output for Sample Input
Andrew drew the following diagram.
The origin lies strictly inside the triangle with vertices P1, P2, and P5, so (1,2,5) is a good triplet. The other five
good triplets are (2, 3, 6), (2, 4, 6), (2, 5, 6), (2, 5, 7), and (2, 5, 8).

 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class GoodTriplets {

    public static long pointsBetween(int p1, int p2, ArrayList<Long> pSumArr) {
        if (p2 > p1) return pSumArr.get(p2)-pSumArr.get(p1);
        return pSumArr.get(pSumArr.size()-1)-pSumArr.get(p1) + pSumArr.get(p2);
    }

    public static long goodTriplets() throws FileNotFoundException {
        Scanner s = new Scanner(new File("goodTriplets"));
        long pCount = s.nextLong();
        int circumference = s.nextInt();
        s.nextLine();

        var circle = new ArrayList<>(Collections.nCopies(circumference, (long)0));
        var prefixSumArray = new ArrayList<Long>();

        for (long i = 0; i < pCount; i++) {
            int n = s.nextInt();
            circle.set(n, circle.get(n)+1);
        }

        prefixSumArray.add(circle.get(0));

        for (int i = 1; i < circumference; i++) {
            prefixSumArray.add(prefixSumArray.get(i-1)+circle.get(i));
        }

        long triangles_count = pCount*(pCount-1)*(pCount-2)/6;

        for (int i = 0; i < circumference; i++) {
            long betweenCount = pointsBetween(i, (circumference/2+i)%circumference, prefixSumArray);
            long pointsAtI = circle.get(i);
            triangles_count -= pointsAtI*(pointsAtI-1)*(pointsAtI-2)/6;
            triangles_count -= pointsAtI*(pointsAtI-1)*betweenCount/2;
            triangles_count -= pointsAtI*betweenCount*(betweenCount-1)/2;
        }

        if (circumference % 2 == 0) {
            for (int i = 0; i < circumference/2; i++) {
                int opposite = (circumference/2+i)%circumference;
                triangles_count += circle.get(i)*(circle.get(i)-1)*circle.get(opposite) / 2;
                triangles_count += circle.get(i)*(circle.get(opposite)-1)*circle.get(opposite) / 2;
            }
        }

        return triangles_count;

    }

}
