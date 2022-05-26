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


import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class RoboGraph {

    ArrayList<ArrayList<RoboNode>> graph;
    ArrayList<RoboNode> queue;
    ArrayList<RoboNode> dots;


    public RoboGraph() throws FileNotFoundException {
        Scanner sc = new Scanner(new File("RoboGrid"));
        graph = new ArrayList<>();
        queue = new ArrayList<>();
        dots = new ArrayList<>();
        var cameras = new ArrayList<ArrayList<Integer>>();
        var cameraHasVision = new ArrayList<ArrayList<Integer>>();
        int rows = sc.nextInt();
        int columns = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < rows; i++) {
            var arr = new ArrayList<RoboNode>();
            var cr = sc.nextLine().toCharArray();
            for (int j = 0; j < columns; j++) {
                if (cr[j] == 'C') cameras.add(new ArrayList<>(Arrays.asList(i, j)));
                arr.add(new RoboNode(cr[j]));
                if (cr[j] == 'S') queue.add(arr.get(j));
                if (cr[j] == '.') dots.add(arr.get(j));
            }
            graph.add(arr);
        }

        for (ArrayList<Integer> cam : cameras) {
            cameraHasVision.add(cam);
            int r = cam.get(0);
            int c = cam.get(1);
            for (var row = r + 1; graph.get(row).get(c).type != 'W'; ++row) {
                char ch = graph.get(row).get(c).type;
                if (ch == '.' || ch == 'S') cameraHasVision.add(new ArrayList<>(Arrays.asList(row, c)));
            }
            for (var row = r - 1; graph.get(row).get(c).type != 'W'; --row) {
                char ch = graph.get(row).get(c).type;
                if (ch == '.' || ch == 'S') cameraHasVision.add(new ArrayList<>(Arrays.asList(row, c)));
            }
            for (var column = c + 1; graph.get(r).get(column).type != 'W'; ++column) {
                char ch = graph.get(r).get(column).type;
                if (ch == '.' || ch == 'S') cameraHasVision.add(new ArrayList<>(Arrays.asList(r, column)));
            }
            for (var column = c - 1; graph.get(r).get(column).type != 'W'; --column) {
                char ch = graph.get(r).get(column).type;
                if (ch == '.' || ch == 'S') cameraHasVision.add(new ArrayList<>(Arrays.asList(r, column)));
            }
        }
        for (ArrayList<Integer> v : cameraHasVision) {
            graph.get(v.get(0)).set(v.get(1), new RoboNode('W'));
        }

        for (int i = 1; i < rows-1; i++) {
            for (int j = 1; j < columns-1; j++) {
                RoboNode node = graph.get(i).get(j);
                char type = node.type;
                if (type != 'W') {
                    if ((type == '.' || type == 'S' || type == 'U') && !(graph.get(i-1).get(j).type == 'W' || graph.get(i-1).get(j).type == 'D' || graph.get(i-1).get(j).type == 'S')) {
                        node.up = graph.get(i-1).get(j);
                    }
                    if ((type == '.' || type == 'S' || type == 'D') && !(graph.get(i+1).get(j).type == 'W' || graph.get(i+1).get(j).type == 'U' || graph.get(i+1).get(j).type == 'S')) {
                        node.down = graph.get(i+1).get(j);
                    }
                    if ((type == '.' || type == 'S' || type == 'L') && !(graph.get(i).get(j-1).type == 'W' || graph.get(i).get(j-1).type == 'R' || graph.get(i).get(j-1).type == 'S')) {
                        node.left = graph.get(i).get(j-1);
                    }
                    if ((type == '.' || type == 'S' || type == 'R') && !(graph.get(i).get(j+1).type == 'W' || graph.get(i).get(j+1).type == 'L' || graph.get(i).get(j+1).type == 'S')) {
                        node.right = graph.get(i).get(j+1);
                    }
                }
            }
        }
        dijkstra();
    }

    public String toString() {
        StringBuilder output = new StringBuilder();
        for (var arr : graph) {
            for (var node : arr) {
                if (node.val.isInfinite()){
                    output.append("X ");
                } else {
                    output.append(node.val.intValue()).append(" ");
                }
            }
            output.append("\n");
        }
        return output.toString();
    }


    private boolean allVisited() {
        for (var node : queue) {
            if (!node.visited) return false;
        }
        return true;
    }

    private void dijkstra() {
        if (queue.size() < 1 || allVisited()) return;
        RoboNode minValNode = new RoboNode('W');
        int index = 0;
        for (var i = 0; i < queue.size(); i++) {
            var node = queue.get(i);
            if (!node.visited && node.val < minValNode.val) {
                minValNode = node;
                index = i;
            }
        }

//        System.out.println(this);
//        System.out.println();

        queue.get(index).visited = true;

        if (minValNode.up != null && !minValNode.up.visited) {
            if (minValNode.up.type == '.') {
                if (minValNode.up.val > minValNode.val) minValNode.up.val = minValNode.val + 1;
            } else {
                if (minValNode.up.val > minValNode.val) minValNode.up.val = minValNode.val;
            }
            queue.add(minValNode.up);
        }
        if (minValNode.right != null && !minValNode.right.visited) {
            if (minValNode.right.type == '.') {
                if (minValNode.right.val > minValNode.val) minValNode.right.val = minValNode.val + 1;
            } else {
                if (minValNode.right.val > minValNode.val) minValNode.right.val = minValNode.val;
            }
            queue.add(minValNode.right);
        }
        if (minValNode.down != null && !minValNode.down.visited) {
            if (minValNode.down.type == '.') {
                if (minValNode.down.val > minValNode.val) minValNode.down.val = minValNode.val + 1;
            } else {
                if (minValNode.down.val > minValNode.val) minValNode.down.val = minValNode.val;
            }
            queue.add(minValNode.down);
        }
        if (minValNode.left != null && !minValNode.left.visited) {

            if (minValNode.left.type == '.') {
                if (minValNode.left.val > minValNode.val) minValNode.left.val = minValNode.val + 1;
            } else {
                if (minValNode.left.val > minValNode.val) minValNode.left.val = minValNode.val;
            }
            queue.add(minValNode.left);
        }
        queue.remove(index);


        dijkstra();
    }

    private ArrayList<Integer> output() {
        var out = new ArrayList<Integer>();
        for (var node: dots) {
            if (node.type == '.') {
                if (node.val < 1000) {
                    out.add(node.val.intValue());
                } else {
                    out.add(-1);
                }
            }
        }
        return out;
    }

    public static void main(String[] args) throws FileNotFoundException {
        var r = new RoboGraph();
        for (int i : r.output()) {
            System.out.println(i);
        }
    }

}