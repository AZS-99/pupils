package com.company;
/*
Counting in Lojban, an artificial language developed over the last forty years, is easier than in most languages.
The numbers from zero to nine are:


1 pa    4 vo    7 ze
2 re    5 mu    8 bi    0 no
3 ci    6 xa    9 so

Write a program that reads in a Lojban string (representing a number less than or equal to 1,000,000) and outputs
it in numbers.

Sample run
Lojban: renonore
Number: 2002
 */

import java.util.HashMap;

public class Lojban {
    
    public static Integer lojban(String input) {
        String num = "";
        String temp = "";
        var map = new HashMap<String, String>() {{
            put("pa", "1");
            put("re", "2");
            put("ci", "3");
            put("vo", "4");
            put("mu", "5");
            put("xa", "6");
            put("ze", "7");
            put("bi", "8");
            put("so", "9");
            put("no", "0");
        }};
        for (int i = 0; i<input.length(); i+=2) {
            temp = "";
            temp += input.charAt(i);
            temp += input.charAt(i+1);
            num += map.get(temp);
        }
        return Integer.parseInt(num);

    }
    
}
