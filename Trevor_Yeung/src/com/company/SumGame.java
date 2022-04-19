package com.company;

import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.util.ArrayList;

public class SumGame {

    public static int sumGame() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("SumGame"));

        int N = scanner.nextInt();

        var team1 = new ArrayList<Integer>();
        var team2 = new ArrayList<Integer>();

        for (int i = 0; i < N; i++) {
            team1.add(scanner.nextInt());
        }
        for (int i = 0; i < N; i++) {
            team2.add(scanner.nextInt());
        }

        int scoreDiff = 0;
        int sameScoreDay = 0;

        for (int i = 1; i <= N; i++) {
            scoreDiff += team1.get(i-1);
            scoreDiff -= team2.get(i-1);
            if (scoreDiff == 0) sameScoreDay = i;
        }

        return sameScoreDay;
    }

}
