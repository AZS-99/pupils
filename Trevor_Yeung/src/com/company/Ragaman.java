package com.company;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.HashMap;

public class Ragaman {

    public static boolean ragaman() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Ragaman"));

        String input = scanner.nextLine();
        String anagram = scanner.nextLine();

        if (input.length() != anagram.length()) return false;

        var inMap = new HashMap<Character, Integer>();
        var anaMap = new HashMap<Character, Integer>();

        for (char c : input.toCharArray()) {
            if (inMap.containsKey(c)) inMap.put(c, inMap.get(c)+1);
            else inMap.put(c, 1);
        }
        for (char c : anagram.toCharArray()) {
            if (anaMap.containsKey(c)) anaMap.put(c, anaMap.get(c)+1);
            else anaMap.put(c, 1);
        }

        for (char c : inMap.keySet()) {
            if (inMap.get(c) < anaMap.get(c)) return false;
        }
        return true;
    }

}
