package com.company;


/*
A planet has n moons revolving about it in constant clockwise coplanar circular orbits. How often do all the moons
appear directly overhead as viewed from some point on the planet? We will call such a situation a 'vertical alignment'.

Your input consists of a number of sets of lines; each set consists of an integer n, indicating the number of moons,
followed by n distinct positive integers, one per line, indicating the exact period of revolution for each moon, in
days. (Thus there are n+1 lines of data for each set with the first line containing n.) The last line contains only a
zero.

For each input set, except the last, generate a line of output indicating the interval in days, to two decimal places,
between consecutive vertical alignments.

Sample Input

2
20
30

3
20
30
40

2
10
3

0


Sample Output

60.00
120.00
4.29
 */


import java.util.ArrayList;

public class Planets {

    public static double alignmentPeriod2(double m1, double m2) {
        double angularV1 = (Math.PI*2)/m1;
        double angularV2 = (Math.PI*2)/m2;
        double relativeAngularVelocity = Math.abs(angularV1-angularV2);
        return (double)Math.round(((200*Math.PI)/relativeAngularVelocity))/100;
    }

    public static double GCD(double n1, double n2) {
        if (n2 == 0) return n1;
        return GCD(n2, n1 % n2);
    }

    public static double LCM2(double n1, double n2) {
        return n1*n2/GCD(n1, n2);
    }

    public static double LCM(ArrayList<Double> l) {
        var nextLayer = new ArrayList<Double>();
        if (l.size() == 1) return l.get(0);
        for (int i = 0; i < l.size()-1; i++) {
            nextLayer.add(LCM2(l.get(i), l.get(i+1)));
        }
        return LCM(nextLayer);
    }

    public static double alignmentPeriod(ArrayList<Double> l) {
        var l2 = new ArrayList<Double>();
        for (int i = 0; i < l.size()-1; i++) {
            l2.add(alignmentPeriod2(l.get(i), l.get(i+1)));
        }
        return LCM(l2);
    }

}
