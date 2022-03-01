package com.company;
/*
The lucky numbers are produced by taking a list of all the odd numbers and systematically removing some of the numbers.
Our first lucky number is 1. We now repeatedly take the next highest number n that is still in the list, mark it as a
lucky number and then remove every nth number from the list.
For example, with lucky numbers underlined as we progress:
• Initially we have:                        1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, ...
• The next lucky number is 3, giving us:    1, 3,    7, 9,     13, 15,     19, 21 ,    25, 27,     31, ...
• Next is 7:                                1, 3,    7, 9,     13, 15,         21 ,    25, 27,     31, ...
• Next is 9:                                1, 3,    7, 9,     13, 15,         21 ,    25,         31, ...

Write a program which reads in a single integer between 2 and 10,000 inclusive.
You should output two numbers. Firstly the closest lucky number that is less than the input, followed by the closest
lucky number that is greater than the input.


Sample run:
5
3 7
 */

import java.util.ArrayList;

public class LuckyNumbers {

    public static ArrayList<Integer> luckyNumbers(int num) {
        ArrayList<Integer> nums = new ArrayList<>();
        ArrayList<Integer> nums2 = new ArrayList<>();
        for (int i = 1; i < 10000; i+=2) {
            nums.add(i);
        }
        int i = 1;
        while (i < nums.size()) {

            for (int j = 0; j < nums.size(); j++) {
                if ((j + 1) % nums.get(i) != 0) nums2.add(nums.get(j));
            }

            nums.clear();
            nums.addAll(nums2);
            nums2.clear();
            i++;
        }
        nums2.clear();
        for (int j = nums.size()-1; j > 0; j--) {
            if (nums.get(j) < num) {
                nums2.add(nums.get(j));
                break;
            }

        }
        for (int j = 0; j < nums.size(); j++) {
            if (nums.get(j) > num){
                nums2.add(nums.get(j));
                break;
            }

        }
        return nums2;
    }

}

/*
find way to skip deleted values that doesnt eviscerate runtime
linked list?
while loop?
 */