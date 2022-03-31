package com.company;
/*
In a primitive video game, a spot bounces around within a rectangular grid. The southwest corner of the grid has
coordinates (0,0) and the northeast corner has coordinates (r,c) where 0 < r <= 10 and 0 < c <= 10. The southeast corner
has coordinates (0,c) and the northwest corner has coordinates (r,0). The spot always travels on the diagonal; that is,
in one of the directions NE, NW, SE, SW. The outer edges of the grid serve as mirrors: after visiting a position on the
edge of the grid the spot "bounces" off according to the normal rules of reflection (Snell's Law). For example, if the
spot were travelling NE and hit the east edge of the grid, it would change direction to NW. If the spot were to hit the
corner of the grid it would change to the opposite direction.

Given a grid size, two points A and B lying on the grid, and an initial direction, you are to determine if the spot
moves from A to B and, if so, how far the spot moves (in terms of number of grid positions) before reaching B the first
time.

Input Specification

The input consists of an integer n, followed by n data sets. Each data set begins with a line containing r and c,
followed by two lines containing the coordinates of points A and B respectively, followed by one line containing NE, NW,
SE, or SW - the initial direction of travel.
Output Specification

For each case, print a sentence as shown below indicating whether B can be reached or not, and, if it can, how far the
spot moves before reaching B.


Sample Input

2
3 4
0 0
0 4
NE
4 2
3 1
3 2
NW
Output for Sample Input

B can be reached from A after 12 move(s).
B cannot be reached from A.


NOTE: (y, x)

 */

import java.io.FileNotFoundException;
import java.util.*;
import java.io.File;


public class BouncingBall  {

    public static int ball(ArrayList<Integer> grid, ArrayList<Integer> A, ArrayList<Integer> B, String d) {
        int r = grid.get(0);
        int c = grid.get(1);
        int x0 = A.get(0);
        int y0 = A.get(1);

        if (d.equals("NE")) {
            for (int n = 0; n < r*r*r*c*c*c; n++) {
                var x = Math.abs(r - Math.abs((n + x0 - r) % (2 * r)));
                var y = Math.abs(c - Math.abs((n + y0 - c) % (2 * c)));
                if (x == B.get(0) && y == B.get(1)) return n;
            }
        }
        if (d.equals("NW")) {
            for (int n = 0; n < r*r*r*c*c*c; n++) {
                var x = Math.abs(r - Math.abs((-n + x0 - r) % (2 * r)));
                var y = Math.abs(c - Math.abs((n + y0 - c) % (2 * c)));
                if (x == B.get(0) && y == B.get(1)) return n;
            }
        }
        if (d.equals("SW")) {
            for (int n = 0; n < r*r*r*c*c*c; n++) {
                var x = Math.abs(r - Math.abs((-n + x0 - r) % (2 * r)));
                var y = Math.abs(c - Math.abs((-n + y0 - c) % (2 * c)));
                if (x == B.get(0) && y == B.get(1)) return n;
            }
        }
        else {
            for (int n = 0; n < r*r*r*c*c*c; n++) {
                var x = Math.abs(r - Math.abs((n + x0 - r) % (2 * r)));
                var y = Math.abs(c - Math.abs((-n + y0 - c) % (2 * c)));
                if (x == B.get(0) && y == B.get(1)) return n;
            }
        }
        return -1;
    }

    public static ArrayList<Integer> bouncingBall() throws FileNotFoundException {
        File file = new File("bouncingball");
        Scanner s = new Scanner(file);
        var grid = new ArrayList<Integer>();
        var A = new ArrayList<Integer>();
        var B = new ArrayList<Integer>();
        var output = new ArrayList<Integer>();
        String d = "";
        int inputCount = s.nextInt();
        s.nextLine();
        for (int c = 0; c < inputCount; c++) {
            grid.add(s.nextInt());
            grid.add(s.nextInt());
            s.nextLine();
            A.add(s.nextInt());
            A.add(s.nextInt());
            s.nextLine();
            B.add(s.nextInt());
            B.add(s.nextInt());
            s.nextLine();
            d = s.nextLine();

            output.add(ball(grid, A, B, d));

            grid.clear();
            A.clear();
            B.clear();
            d = "";
        }
        return output;
    }

}

/*
public static int ball(ArrayList<Integer> grid, ArrayList<Integer> A, ArrayList<Integer> B, String d, int s) {
        if (A == B) return s;
        if (s == grid.get(0)*grid.get(0)*grid.get(0)*grid.get(1)*grid.get(1)*grid.get(1)) return -1;
        if (Objects.equals(d, "NE")) {
            while (!A.get(0).equals(grid.get(0)) && !A.get(1).equals(grid.get(1))) {
                A.set(0, A.get(0)+1);
                A.set(1, A.get(1)+1);
            }
            if (Objects.equals(A.get(0), grid.get(0)) && Objects.equals(A.get(1), grid.get(1))) return ball(grid, A, B, "SW", s+1);
            if (Objects.equals(A.get(0), grid.get(0))) return ball(grid, A, B, "SE", s+1);
            return ball(grid, A, B, "NW", s+1);
        }
        if (Objects.equals(d, "SE")) {
            while (!A.get(0).equals(0) && !A.get(1).equals(grid.get(1))) {
                A.set(0, A.get(0)-1);
                A.set(1, A.get(1)+1);
            }
            if (Objects.equals(A.get(0), 0) && Objects.equals(A.get(1), grid.get(1))) return ball(grid, A, B, "NW", s+1);
            if (Objects.equals(A.get(0), 0)) return ball(grid, A, B, "NE", s+1);
            return ball(grid, A, B, "SW", s+1);
        }
        if (Objects.equals(d, "SW")) {
            while (!A.get(0).equals(0) && !A.get(1).equals(0)) {
                A.set(0, A.get(0)+1);
                A.set(1, A.get(1)+1);
            }
            if (Objects.equals(A.get(0), 0) && Objects.equals(A.get(1), 0)) return ball(grid, A, B, "NE", s+1);
            if (Objects.equals(A.get(0), 0)) return ball(grid, A, B, "NW", s+1);
            return ball(grid, A, B, "SE", s+1);
        }
        else {
            while (!A.get(0).equals(grid.get(0)) && !A.get(1).equals(0)) {
                A.set(0, A.get(0)+1);
                A.set(1, A.get(1)+1);
            }
            if (Objects.equals(A.get(0), grid.get(0)) && Objects.equals(A.get(1), 0)) return ball(grid, A, B, "SE", s+1);
            if (Objects.equals(A.get(0), grid.get(0))) return ball(grid, A, B, "SW", s+1);
            return ball(grid, A, B, "NE", s+1);
        }
    }

    public static ArrayList<Integer> bouncingBall() throws FileNotFoundException {
        File b = new File("bouncingball");
        Scanner s = new Scanner(b);
        var grid = new ArrayList<Integer>();
        var A = new ArrayList<Integer>();
        var B = new ArrayList<Integer>();
        var output = new ArrayList<Integer>();
        String d = "";
        int inputCount = s.nextInt();
        s.nextLine();
        for (int c = 0; c < inputCount; c++) {
            grid.add(s.nextInt());
            grid.add(s.nextInt());
            s.nextLine();
            A.add(s.nextInt());
            A.add(s.nextInt());
            s.nextLine();
            B.add(s.nextInt());
            B.add(s.nextInt());
            s.nextLine();
            d = s.nextLine();

            output.add(ball(grid, A, B, d, 0));

            grid.clear();
            A.clear();
            B.clear();
            d = "";
        }
        return output;
    }
 */