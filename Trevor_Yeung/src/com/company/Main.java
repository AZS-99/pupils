package com.company;

import java.util.Arrays;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws Exception {

        int[] a = new int[] {5, 3};
        System.out.println(PatternGenerator.patternGenerator(new ArrayList<>() {{add(a);}}));

    }
}
