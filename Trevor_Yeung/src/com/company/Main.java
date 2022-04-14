package com.company;

import java.util.Arrays;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) throws Exception {

        var arr = new ArrayList<>(Arrays.asList(4, 6, 12));
        for (int i : arr) {
            System.out.println(Abundancy.abundancy(i));
        }

    }
}
