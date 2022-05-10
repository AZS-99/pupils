package com.company;
/*
Problem Description
A robot has stolen treasure from a factory and needs to escape without getting caught. The factory can be modelled by an
N by M grid, where the robot can move up, down, left, or right.

Each cell of the grid is either empty, a wall, a camera, a conveyor, or the robot’s initial position. The robot can only
walk on empty cells (denoted by .) or conveyors. The first row, last row, first column and last column of the grid
consists of walls (denoted by W), and there may be walls in other cells.

Conveyors cause the robot to move in a specific direction, denoted by L, R, U, D for left, right, up, down respectively.
The robot is unable to move on its own while on a conveyor. It is possible that the robot can become stuck forever on
conveyors.
Cameras (denoted by C) can see in all four directions up, down, left, and right, but cannot see through walls. The robot
will be caught if it is in the same cell as a camera or is seen by a camera while on an empty cell. Conveyors are
slightly elevated, so the robot cannot be caught while on a conveyor, but cameras can see empty cells on the other side
of conveyors.

The robot is initially at the cell denoted by S. The exit could be at any of the empty cells. For each empty cell,
determine the minimum number of steps needed for the robot to move there without being caught, or determine that it is
impossible to move there. A step consists of moving once up, down, left or right. Being moved by a conveyor does not
count as a step.

Input Specification
The first line of input contains two integers N and M (4 ≤ N, M ≤ 100). The next N lines of input will each contain M
characters, each of which is one of the eight characters W, ., C, S, L, R, U, or D.
There will be exactly one S character and at least one . character. The first and last character of every row and column
will be W.

For 5 of the 15 marks available, there are no cameras or conveyors. For an additional 5 of the 15 marks available, there
are no conveyors.

Output Specification
For each empty cell, print one line with one integer, the minimum number of steps for the robot to move to this empty
cell without being caught or −1 if it is impossible to move to this empty cell.
The output should be in row major order; the order of empty cells seen if the input is scanned line by line
top-to-bottom and then left-to-right on each line. See the sample outputs for examples of row major order output.


Sample Input 1
4 5
WWWWW
W.W.W
WWS.W
WWWWW
Output for Sample Input 1
-1
2
1

Explanation of Output for Sample Input 1
The robot cannot move to the top left empty cell because it is blocked by walls.
The top right empty cell can be reached in 2 steps and the bottom right empty cell can be reached
in 1 step.

Sample Input 2
5 7
WWWWWWW
WD.L.RW
W.WCU.W
WWW.S.W
WWWWWWW
Output for Sample Input 2
2
1
3
-1
-1
1

Explanation of Output for Sample Input 2
The empty cell to immediate left of the robot is seen by the camera so the robot cannot move there.
The empty cell right below the R conveyor is also seen by the camera as conveyors do not mark_watched_spots the the
sight of cameras.
Note that the robot can use the U and L conveyors to avoid the getting caught by the camera. If the robot moves to the R conveyor, it will become stuck forever there.
 */




//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Scanner;
//import java.util.HashSet;
//import java.io.FileNotFoundException;
//import java.io.File;
//
//public class RoboGrid {
//
//    int height;
//    int width;
//
//    ArrayList<ArrayList<String>> array_2d;
//    ArrayList<ArrayList<Boolean>> traveled;
//    ArrayList<ArrayList<Integer>> cameras;
//    ArrayList<ArrayList<Integer>> camVision;
//    ArrayList<ArrayList<Integer>> paths;
//    Scanner s;
//    int [] start;
//
//    public RoboGrid() throws FileNotFoundException {
//        s = new Scanner(new File("RoboGrid"));
//        this.height = s.nextInt();
//        this.width = s.nextInt();
//        array_2d = new ArrayList<>();
//        traveled = new ArrayList<>();
//        cameras = new ArrayList<>();
//        camVision = new ArrayList<>();
//        paths = new ArrayList<>();
//        start = new int[2];
//    }
//
//    public String toString() {
//        StringBuilder str = new StringBuilder();
//        for (ArrayList<String> arr : array_2d) {
//            for (String s : arr) {
//                str.append(s);
//            }
//            str.append("\n");
//        }
//        return str.toString();
//    }
//
//    public ArrayList<ArrayList<Integer>> getNeighbours(int x, int y) {
//        if (array_2d.get(x).get(y).equals("W")) return new ArrayList<>();
//        var neighbours = new ArrayList<ArrayList<Integer>>();
//        if (x > 0 && (array_2d.get(x - 1).get(y).equals(".") || array_2d.get(x - 1).get(y).equals("D") || array_2d.get(x - 1).get(y).equals("S")))
//            neighbours.add(new ArrayList<>(Arrays.asList(x-1, y)));
//        if (x < array_2d.size()-1 && (array_2d.get(x + 1).get(y).equals(".") || array_2d.get(x + 1).get(y).equals("U") || array_2d.get(x + 1).get(y).equals("S")))
//            neighbours.add(new ArrayList<>(Arrays.asList(x+1, y)));
//        if (y > 0 && (array_2d.get(x).get(y-1).equals(".") || array_2d.get(x).get(y-1).equals("R") || array_2d.get(x).get(y-1).equals("S")))
//            neighbours.add(new ArrayList<>(Arrays.asList(x, y-1)));
//        if (y < width-1 && (array_2d.get(x).get(y+1).equals(".") || array_2d.get(x).get(y+1).equals("L") || array_2d.get(x).get(y+1).equals("S")))
//            neighbours.add(new ArrayList<>(Arrays.asList(x, y+1)));
//        return neighbours;
//    }
//
//    public Double count(int x, int y) {
//        if (start[0] == x && start[1] == y) return 0.0;
//        if (array_2d.get(x).get(y).equals("W")) return Double.POSITIVE_INFINITY;
//        var neighbours = getNeighbours(x, y);
//        var is_dot = array_2d.get(x).get(y).equals(".");
//        if (is_dot) array_2d.get(x).set(y, "M");
//        var min_count = Double.POSITIVE_INFINITY;
//        for (ArrayList<Integer> n : neighbours) {
//            if (array_2d.get(x).get(y).equals("M")) min_count += 1;
//            double c = count(n.get(0), n.get(1));
//            if (is_dot) c++;
//            if (c < min_count) min_count = c;
//        }
//        if (is_dot) array_2d.get(x).set(y, ".");
//        return min_count;
//    }
//
//    public ArrayList<ArrayList<Integer>> getCamVision(ArrayList<ArrayList<Integer>> cameras, ArrayList<ArrayList<String>> map) {
//        var camVision = new ArrayList<ArrayList<Integer>>();
//        for (ArrayList<Integer> cam : cameras) {
//            camVision.add(cam);
//            int i = cam.get(0)+1;
//            int j = cam.get(1);
//            while (!map.get(i).get(j).equals("W")) {
//                if (map.get(i).get(j).equals(".")) {
//                    camVision.add(new ArrayList<>(Arrays.asList(i, j)));
//                }
//                i++;
//            }
//            i = cam.get(0)-1;
//            while (!map.get(i).get(j).equals("W")) {
//                if (map.get(i).get(j).equals(".")) {
//                    camVision.add(new ArrayList<>(Arrays.asList(i, j)));
//                }
//                i--;
//            }
//            i = cam.get(0);
//            j = cam.get(1)+1;
//            while (!map.get(i).get(j).equals("W")) {
//                if (map.get(i).get(j).equals(".")) {
//                    camVision.add(new ArrayList<>(Arrays.asList(i, j)));
//                }
//                j++;
//            }
//            j = cam.get(1)-1;
//            while (!map.get(i).get(j).equals("W")) {
//                if (map.get(i).get(j).equals(".")) {
//                    camVision.add(new ArrayList<>(Arrays.asList(i, j)));
//                }
//                j--;
//            }
//        }
//
//        var set = new HashSet<>(camVision);
//        camVision.clear();
//        camVision.addAll(set);
//
//        return camVision;
//    }
//
//    public ArrayList<Integer> robogrid() {
//        s.nextLine();
//        for (int i = 0; i < height; i++) {
//            var str = s.nextLine();
//
//            ArrayList<String> myList = new ArrayList<>(Arrays.asList(str.split("")));
//            for (int j = 0; j < myList.size(); j++) {
//                switch (myList.get(j)) {
//                    case "." -> paths.add(new ArrayList<>(Arrays.asList(i, j)));
//                    case "C" -> cameras.add(new ArrayList<>(Arrays.asList(i, j)));
//                    case "S" -> {
//                        start[0] = i;
//                        start[1] = j;
//                    }
//                }
//            }
//            array_2d.add(myList);
//        }
//
//        camVision = getCamVision(cameras, array_2d);
//
//        for (ArrayList<Integer> point : camVision) {
//            var arr = array_2d.get(point.get(0));
//            arr.set(point.get(1), "W");
//            array_2d.set(point.get(0), arr);
//        }
//
//        var output = new ArrayList<Integer>();
//
//        for (ArrayList<Integer> arr : paths) {
//            double d = count(arr.get(0), arr.get(1));
//            if (d == Double.POSITIVE_INFINITY) d = -1;
//            output.add((int) d);
//        }
//
//        return output;
//    }
//
//}
