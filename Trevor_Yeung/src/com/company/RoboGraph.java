package com.company;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class RoboGraph {

    ArrayList<ArrayList<RoboNode>> graph;
    ArrayList<RoboNode> queue;

    public RoboGraph() throws FileNotFoundException {
        Scanner sc = new Scanner(new File("RoboGrid"));
        graph = new ArrayList<>();
        queue = new ArrayList<>();
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

    }

    public void dijkstra() {

    }

    public ArrayList<ArrayList<RoboNode>> getDistances() {
        queue = new ArrayList<>();
        dijkstra();
        return graph;
    }

}
