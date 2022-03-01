package com.company;

/*
A palindrome is a word that shows the same sequence of letters when reversed. If a word can have its letters grouped
together in two or more blocks (each containing one or more adjacent letters) then it is a block palindrome if reversing
the order of those blocks results in the same sequence of blocks.

For example, using brackets to indicate blocks, the following are block palindromes:
• BONBON can be grouped together as (BON)(BON);
• ONIION can be grouped together as (ON)(I)(ON);
• BBACBB can be grouped together as (B)(BACB)(B) or (BB)(AC)(BB) or (B)(B)(AC)(B)(B)
Note that (BB)(AC)(B)(B) is not valid as the reverse (B)(B)(AC)(BB) shows the blocks in a different order.

Sample Run:
BBACBB
3

ONION
1
 */



public class BlockPalindrome {

    public int blockpalindrome(String word) {
        if (word.length() < 2) return 1;

        System.out.println(word.substring(1, word.length() - 1));
        var count = (word.charAt(0) != word.charAt(word.length()-1))? 1 : blockpalindrome(word.substring(1, word.length() - 1));
        for (int i = 0; i < word.length()/2; i++) {
            if (word.substring(0, i+1).equals(word.substring(word.length()-i-1)))
                count += 1;
        }
        return count;

    }

}
