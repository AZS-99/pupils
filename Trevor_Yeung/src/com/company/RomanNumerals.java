package com.company;
/*
In Roman times, numbers were represented using letters. The way of doing this, known as Roman Numerals, is often seen
depicting the copyright date on films and television.
Roman numerals are conventionally defined to represent numbers using seven letters: I=1, V=5, X=10, L=50, C=100, D=500
and M=1000. Numbers other than these are formed by placing letters together from left to right, in descending order of
size, and adding their values. The basic rule is to always use the biggest numeral possible (e.g. 15 is represented
as XV, but never as VVV, VX or XIIIII).

Letters may not appear more than three times in a row, so there are six exceptions to these rules -
the combinations IV, IX, XL, XC, CD and CM. In these cases a letter is placed before one of greater value,
and the smaller value is subtracted from the larger, e.g. CD = 400.

Examples:
26    XXVI
94    XCIV
555   DLV
1998  MCMXCVIII


Write a program which accepts a numeral, between 1 and 10000 inclusive, and outputs the same numeral in Roman numerals [20 Marks]

Sample run
1999
MCMXCIX

888
DCCCLXXXVIII

444
CDXLIV

Write a program which accepts two numbers in Roman Numerals, between I and CM, and returns the summation of the
two numbers [10 Marks]

Sample run
VII+II
IX
 */

import java.util.*;

public class RomanNumerals {

    ArrayList<Integer> denominations = new ArrayList<>() {{
        add(1000);
        add(900);
        add(500);
        add(400);
        add(100);
        add(90);
        add(50);
        add(40);
        add(10);
        add(9);
        add(5);
        add(4);
        add(1);
    }};


    public String intToRomanNumeral(int num) {
        if (num == 1) return "I";
        if (num == 4) return "IV";
        if (num == 5) return "V";
        if (num == 9) return "IX";
        if (num == 10) return "X";
        if (num == 40) return "XL";
        if (num == 50) return "L";
        if (num == 90) return "XC";
        if (num == 100) return "C";
        if (num == 400) return "CD";
        if (num == 500) return "D";
        if (num == 900) return "CM";
        if (num == 1000) return "M";
        int largestDenomination = findLargestDenomination(num);
        return intToRomanNumeral(largestDenomination) + intToRomanNumeral(num-largestDenomination);
    }

    public int findLargestDenomination(int num) {
        for (int i : denominations)
            if (i < num) return i;
        return 0;
    }

    public int romanNumeralToInt(String rom) {
        if (rom.equals("I")) return 1;
        if (rom.equals("V")) return 5;
        if (rom.equals("X")) return 10;
        if (rom.equals("L")) return 50;
        if (rom.equals("C")) return 100;
        if (rom.equals("D")) return 500;
        if (rom.equals("M")) return 1000;
        var last_char_value = romanNumeralToInt(rom.substring(rom.length()-1));
        var penultimate_char_value = romanNumeralToInt(rom.substring(rom.length()-2, rom.length()-1));
        if (last_char_value <= penultimate_char_value)
            return romanNumeralToInt(rom.substring(0, rom.length()-1)) + last_char_value;
        return (rom.length() > 2? romanNumeralToInt(rom.substring(0, rom.length() - 2)) : 0) + last_char_value - penultimate_char_value;
    }

    public String addRomanNumerals(String r1, String r2) {
        return intToRomanNumeral(romanNumeralToInt(r1) + romanNumeralToInt(r2));
    }

}
