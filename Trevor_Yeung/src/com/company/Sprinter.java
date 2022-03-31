package com.company;

/*
Problem Description
Trick E. Dingo is trying, as usual, to catch his nemesis the Street Sprinter. His past attempts using magnets, traps and
explosives have failed miserably, so he’s catching his breath to gather observational data and learn more about how fast
Street Sprinter is.
Trick E. Dingo and Street Sprinter both inhabit a single straight west-east road with a particularly famous rock on it
known affectionately as The Origin. Positions on this straight road are measured numerically according to the distance
from The Origin, and using negative numbers for positions west of The Origin and positive numbers for positions east of
The Origin.
The observations by Trick E. Dingo each contain two numbers: a time, and the value of Street Sprinter’s position on the
road at that time. Given this information, what speed must Street Sprinter must be capable of?



Input Specification
The first line contains a number 2 ≤ N ≤ 100 000, the number of observations that follow. The next N lines each contain
an integer 0 ≤ T ≤ 1 000 000 000 indicating the time, in seconds, of when a measurement was made, and an integer
−1 000 000 000 ≤ X ≤ 1 000 000 000 indicating the position, in metres, of the Street Sprinter at that time. No two lines
will have the same value of T.

Output Specification
Output a single number X, such that we can conclude that Street Sprinter’s speed was at least X metres/second at some
point in time, and such that X is as large as possible. If the correct answer is C, the grader will view X as correct
if |X − C|/C < 10^−5.


Sample Input 1
3
0 100
20 50
10 120


Output for Sample Input 1
7.0

Explanation of Output for Sample Input 1
Since the Street Sprinter ran from position 100 to position 120 between time 0 and time 10, we know its speed must have
been at least 2 at some point in time: if it was always less than 2, then the distance of 20 could not be covered in 10
seconds. Likewise, the speed must have been at least 7 in order to travel between position 120 and 50 in 10 seconds.

Sample Input 2
5
20 -5
0 -17
10 31
5 -3
30 11
Output for Sample Input 2
6.8
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.Scanner;
import java.util.HashMap;
import java.util.ArrayList;

public class Sprinter {

    public static double sprinter() throws FileNotFoundException {
        File file = new File("sprinter");
        Scanner s = new Scanner(file);
        var recordings = new HashMap<Double, Double>();

        int rCount = s.nextInt();
        s.nextLine();
        for (int i = 0; i < rCount; i++) {
            recordings.put(s.nextDouble(), s.nextDouble());
            s.nextLine();
        }

        var keys = new ArrayList<>(recordings.keySet());
        Collections.sort(keys);

        double maxSpeed = 0;

        for (int i = 0; i < recordings.size()-1; i++) {
            var speed = Math.abs((recordings.get(keys.get(i+1))-recordings.get(keys.get(i)))/((keys.get(i+1)-keys.get(i))));
            if (speed > maxSpeed) maxSpeed = speed;
        }

        return maxSpeed;

    }

}
