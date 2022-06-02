package CCC_2004;
/*

A collection of words is prefix-free if no word is a prefix of any other word. A collection of words is suffix-free if
no word is a suffix of any other word. A collection of words is fix-free if it is both prefix-free and suffix-free.

For this problem, a word is a sequence of lower-case letters of length between 1 and 25. A word X is a prefix of word Y
if X consists of the first n characters of Y, in order, for some n. That is, the word “cat” has prefixes “c”, “ca”, and
“cat”. Similarly, a word X is a suffix of Y if X consists of the last n characters of Y, in order, for some n.
Your input will be 3N+1 lines: the first line will be the number N, and the remaining 3N lines will be the N collections
of 3 words each. (That is, lines 2, 3, and 4 compose the
first collection, lines 5, 6, and 7 compose the second collection, and so on). Your output will be N lines, each line
containing either Yes (if that collection of words is fix-free) or No (if that collection is not fix-free).

Sample Input
2
abba
aab
bab
a
ab
aa
Sample Output
Yes
No
 */

import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class S1 {

    public static boolean fix_free(ArrayList<String> words) {
        int l1;
        int l2;
        for (int i = 0; i < 2; i++) {
            for (int j = i+1; j < 3; j++) {
                l1 = words.get(i).length();
                l2 = words.get(j).length();
                if (l1 < l2) {
                    if (words.get(j).substring(0, l1).equals(words.get(i)) || words.get(j).substring(l2-l1).equals(words.get(i))) return false;
                }
                // copy above
            }
        }
        return true;
    }

    public static void main(String[] args) throws FileNotFoundException {
        var sc = new Scanner(new File("CCC_2004"));
        int count = sc.nextInt();
        ArrayList<String> words;
        boolean fix_free;
        for (int i = 0; i < count; i++) {
            words = new ArrayList<>();
            words.add(sc.nextLine());
            words.add(sc.nextLine());
            words.add(sc.nextLine());
            fix_free = fix_free(words);
            if (fix_free) System.out.println("Yes");
            else System.out.println("No");
        }
    }

}
