package com.company;

/*
'Life' is a computer simulation played out on a rectangular board of squares. Each square has two possible states,
on ('0' - zero) or off ('.'), and the state of the squares at the next generation is fully determined by the current
state and some simple rules. The configuration at generation 0 is selected by the user.
Each square on the board has eight neighbours, those touching it directly (including diagonally), except border squares
which have some of these pieces missing.

The rules for generating the next generation are:

Survival: Any 'on' square with two or three neighbouring 'on' squares stays 'on' next generation.
Death:	  Any 'on' square with less than two or more than three neighbouring 'on' squares goes 'off' next generation.
Birth:	  Any 'off' square with exactly three neighbouring 'on' squares goes 'on' next generation; otherwise, stays 'off'

The rules stay the same for border squares, though they have fewer neighbours - in other words squares outside the
11x11 board are to be treated as permanently off. You should also remember that all births, deaths and survivals
between generations occur simultaneously. For example:

Generation 0:
..0..
...0.
.000.
.....
.....

Generation 1:
.....
.0.0.
..00.
..0..
.....

Generation 2:
.....
...0.
.0.0.
..00.
.....


You are to write a program to play Life on an 11x11 board. Your program should first read in a 5x5 board, which will be
in the form of five lines of five characters (either '0' or '.'). This 5x5 board should be used as the centre section
of the 11x11 board for generation 0, the rest of which is to be treated as off. This will be generation 0 for the entire
run of your program. Once this is done you should display generation 0.


Until your program terminates you should repeatedly wait for input, and then:
1- If you receive an integer 'n' with a hash before it (such as #5), you should calculate generation 'n' and display it on
the screen.
2- If you receive an integer 'n' with a plus before it (such as +5), you should calculate 'n' generations on from the last
generation shown, and then display the new one on the screen.
3- If you receive the number -1 you should terminate.
4- Ignore any other input.

Sample run
.....
.....
...0.
....0
..000


...........
...........
...........
...........
...........
......0....
.......0...
.....000...
...........
...........
...........


#5
...........
...........
...........
...........
...........
...........
...........
......0.0..
.......00..
.......0...
...........

+1
...........
...........
...........
...........
...........
...........
...........
........0..
......0.0..
.......00..
...........

-1
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Life {

    LifeNode[][] graph;

    public Life() throws FileNotFoundException {
        graph = new LifeNode[11][11];
        var sc = new Scanner(new File("Life"));
        sc.useDelimiter("");
        String ch;
        for (int i = 0; i < 11; i++) {
            for (int j = 0; j < 11; j++) {
                graph[i][j] = new LifeNode();
                if (i > 2 && i < 8 && j > 2 && j < 8){
                    ch = sc.next();
                    if (ch.equals("0")) graph[i][j].isAlive = true;
                }
            }
            if (i < 7 && i > 2) sc.next();
        }
        link();
    }

    public void link() {
        LifeNode node;
        for (int i = 0; i < 11; i++) {
            for (int j = 0; j < 11; j++) {
                node = graph[i][j];
                if (i > 0) {
                    node.neighbours.add(graph[i-1][j]);
                    if (j > 0) node.neighbours.add(graph[i-1][j-1]);
                    if (j < 10) node.neighbours.add(graph[i-1][j+1]);
                }
                if (i < 10) {
                    node.neighbours.add(graph[i+1][j]);
                    if (j > 0) node.neighbours.add(graph[i+1][j-1]);
                    if (j < 10) node.neighbours.add(graph[i+1][j+1]);
                }
                if (j > 0) node.neighbours.add(graph[i][j-1]);
                if (j < 10) node.neighbours.add(graph[i][j+1]);
            }
        }
    }

    public String toString() {
        StringBuilder output = new StringBuilder();
        for (var row : graph) {
            for (var node : row) {
                output.append(node);
            }
            output.append("\n");
        }
        return output.toString();
    }

    public void nextGeneration() {
        var change = new ArrayList<LifeNode>();
        int aliveNeighbours;
        for (var row : graph) {
            for (var node : row) {
                aliveNeighbours = 0;
                for (var neighbour : node.neighbours) {
                    if (neighbour.isAlive) aliveNeighbours++;
                }
                if (node.isAlive && !(aliveNeighbours == 2 || aliveNeighbours == 3)) change.add(node);
                else if (!node.isAlive && aliveNeighbours == 3) change.add(node);
            }
        }
        for (var node : change) node.isAlive = !node.isAlive;
    }

    public Life copy() throws FileNotFoundException {
        var copy = new Life();
        for (int i = 0; i < 11; i++) {
            for (int j = 0; j < 11; j++) {
                copy.graph[i][j] = graph[i][j].copy();
            }
        }
        link();
        copy.link();
        return copy;
    }

    public void run() throws FileNotFoundException {
        var original = copy();
        var runCopy = copy();
        var sc = new Scanner(System.in);
        int val;
        while (true) {
            String cmd = sc.nextLine();
            if (cmd.equals("-1")) return;
            val = Integer.parseInt(cmd.substring(1));
            if (cmd.charAt(0) == '#') runCopy = original.copy();
            for (int i = 0; i < val; i++) {
                runCopy.nextGeneration();
            }
            System.out.println(runCopy);
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        var life = new Life();
        life.run();
    }

}
