package com.company;
/*
A digital river is a sequence of numbers where the number following n is n plus the sum of its digits. For example,
12345 is followed by 12360, since 1+2+3+4+5 = 15. If the first number of a digital river is k we will call it river k.
For example, river 480 is the sequence beginning {480, 492, 507, 519, ...} and river 483 is the sequence beginning
{483, 498, 519, ...}.

Normal streams and rivers can meet, and the same is true for digital rivers. This happens when two digital rivers share
some of the same values. For example: river 480 meets river 483 at 519, meets river 507 at 507, and never meets river
481

Every digital river will eventually meet river 1, river 3 or river 9. Write a program which inputs a single
integer n (1<=n<=16384), and outputs the value where river n first meets one of these three rivers. You can assume this
will always happen within the first 1000 terms of the sequence.

Sample run
River: 86
First meets river 1 at 101
 */

import java.util.ArrayList;

public class River {

    ArrayList<Integer> r = new ArrayList<>();

    public River(int k) {
        r.add(k);
        stretch();
    }

    public int digitSum(int n) {
        if (n < 10) return n;
        return n%10 + digitSum((n-n%10)/10);
    }

    public void stretch() {
        while (r.size() <= 1000) {
            r.add(r.get(r.size()-1)+digitSum(r.get(r.size()-1)));
        }
    }

    public int findIntersection(River river2) {
        for (int element:r) {
            if (river2.r.contains(element)) return element;
        }
        return 0;
    }

    public String chooseRiver() {
        int river1 = findIntersection(new River(1));
        int river3 = findIntersection(new River(3));
        int river9 = findIntersection(new River(9));
        if (river1 != 0) return "First meets river 1 at " + river1;
        else if (river3 != 0) return "First meets river 3 at " + river3;
        else return "First meets river 9 at " + river9;
    }

}
