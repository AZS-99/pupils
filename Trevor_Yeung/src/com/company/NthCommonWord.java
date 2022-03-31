package com.company;

/*
Given a sequence of m words from a newspaper article and an integer k, find the kth most common word.

Input Specification

Input will consist of an integer n followed by n data sets. Each data set begins with a line containing m and k,
followed by m lines, each containing a word of up to 20 lower case letters. There will be no more than 1000 words per
data set.

Output Specification

For each input data set, determine the kth most common word(s). To be precise, a word w is the kth most common if
exactly k-1 distinct words occur more frequently than w in the data set. Note that w might be multiply defined (i.e.
there is a tie for the kth most common word) or w might not exist (i.e. there is no kth most common word). For each data
set, print a title line indicating k using normal ordinal notation (1st, 2nd, 3rd, 4th, 5th, ...) followed by a number
of lines giving all the possible values for the kth most common word. A blank line should follow the last word for each
data set.


Sample Input

3
8 2
the
brown
the
fox
red
blue
the
red
1 3
the
2 1
the
wash


Output for Sample Input

2nd most common word(s):
red

3rd most common word(s):

1st most common word(s):
the
wash
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class NthCommonWord {

    public static ArrayList<String> nthCommon(int m, int k, Scanner s) {
        var words = new HashMap<String, Integer>();
        var output = new ArrayList<String>();
        for (int i = 0; i < m; i++) {
            String word = s.nextLine();
            if (!words.containsKey(word)) words.put(word, 1);
            else words.put(word, words.get(word)+1);
        }
        var arr = new ArrayList<>(words.values());
        arr.sort(Collections.reverseOrder());
        var val = 0;
        if (k < m) val = arr.get(k-1);
        else return output;
        for (String key : words.keySet()) {
            if (words.get(key).equals(val)) output.add(key);
        }
        return output;
    }

    public static void nthCommonWord() throws FileNotFoundException {
        var file = new File("nthCommon");
        Scanner s = new Scanner(file);
        int inputs = s.nextInt();
        s.nextLine();
        for (int i = 0; i < inputs; i++) {
            int m = s.nextInt();
            int k = s.nextInt();
            s.nextLine();
            System.out.println(nthCommon(m, k, s));
        }
    }

}
