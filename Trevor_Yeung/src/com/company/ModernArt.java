package com.company;
/*
Problem Description
A new and upcoming artist has a unique way to create checkered patterns. The idea is to use an M-by-N canvas which is
initially entirely black. Then the artist repeatedly chooses a row or column and runs their magic brush along the row or
column. The brush changes the colour of each cell in the row or column from black to gold or gold to black.
Given the artist’s choices, your job is to determine how much gold appears in the pattern determined by these choices.

Input Specification
The first line of input will be a positive integer M. The second line of input will be a positive integer N. The third
line of input will be a positive integer K. The remaining input will be K lines giving the choices made by the artist.
Each of these lines will either be R followed by a single space and then an integer which is a row number, or C followed
by a single space and then an integer which is a column number. Rows are numbered top down from 1 to M. Columns are
numbered left to right from 1 to N.

Output Specification
Output one non-negative integer which is equal to the number of cells that are gold in the pattern determined by the artist’s choices.
Sample Input 1
3
3
2
R1
C1
Output for Sample Input 1
4

Explanation of Output for Sample Input 1
After running the brush along the first row, the canvas looks like this:
GGG
BBB
BBB
Then after running the brush along the first column, four cells are gold in the final pattern determined by the artist’s
choices:
BGG
GBB
GBB

Sample Input 2
4
5
7
R3
C1
C2
R2
R2
C1
R4
Output for Sample Input 2
10

Explanation of Output for Sample Input 2
Ten cells are gold in the final pattern determined by the artist’s choices:
BGBBB
BGBBB
GBGGG
GBGGG
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class ModernArt {

    public static int modernArt() throws FileNotFoundException {
        var rows = new HashMap<Integer, Boolean>();
        var columns = new HashMap<Integer, Boolean>();

        // find number of tiles with only one instruction applied

        Scanner s = new Scanner(new File("ModernArt"));

        var r = s.nextInt();
        s.nextLine();
        var c = s.nextInt();
        s.nextLine();
        int instructionCount = s.nextInt();
        s.nextLine();
        for (int i = 0; i < instructionCount; i++) {
            String instruction = s.nextLine();
            var num = Integer.parseInt(instruction.substring(1));
            if (instruction.charAt(0) == 'R') {
                if (rows.containsKey(num)) rows.put(num, !rows.get(num));
                else rows.put(num, true);
            } else {
                if (columns.containsKey(num)) columns.put(num, !columns.get(num));
                else columns.put(num, true);
            }
        }

        int changedRows = 0;
        int changedColumns = 0;
        for (int i : rows.keySet()) {
            if (rows.get(i)) changedRows += 1;
        }
        for (int i : columns.keySet()) {
            if (columns.get(i)) changedColumns += 1;
        }

        return c*changedRows + r*changedColumns - 2*changedColumns*changedRows;

    }

}
