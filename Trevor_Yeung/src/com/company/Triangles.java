package com.company;

/*
A coloured triangle is created from a row of squares, each of which is red, green or blue. Successive rows, each
 containing one fewer square than the last, are generated by considering the two touching squares in the previous row.
 If these squares are identical, the same colour is used in the new row. If they are different, the missing colour is
 used in the new row. This is continued until the final row, with only a single square, is generated.

In the following three example triangles R, G and B have been used to represent the colours. Note that each row is
generated from the row above.

G G
 G

R B
 G

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G

Write a program which reads in a starting row of between 1 and 10 (inclusive) uppercase letters (each R, G or B).
You should output the colour (R, G or B) of the square in the final row of the triangle


Sample run 1
RG
B

Sample run 2
RBRGBRB
G
 */
public class Triangles {

    public static String getNextLayer(String input) {
        if (input.length() == 2) {
            if (input.charAt(0) == input.charAt(1)) return input.substring(0, 1);
            char a = input.charAt(0);
            char b = input.charAt(1);
            if (a != 'R' && b != 'R') return "R";
            else if (a != 'G' && b != 'G') return "G";
            else return "B";
        }
        return getNextLayer(input.substring(0, input.length()-1)) + getNextLayer((input.substring(input.length()-2)));
    }

    public static String triangle(String input) {
        if (input.length() == 2) return getNextLayer(input);
        return triangle(getNextLayer(input));
    }

}


//if (input.length() == 1) return input;
//        String nextLayer = "";
//        for (int i = 0; i < input.length()-1; i++) {
//            if (input.charAt(i) == input.charAt(i+1)) nextLayer+=input.charAt(i);
//            else {
//                char a = input.charAt(i);
//                char b = input.charAt(i);
//                if (a != 'R' && b != 'R') nextLayer+='R';
//                else if (a != 'G' && b != 'G') nextLayer+='G';
//                else nextLayer+='B';
//            }
//        }
//        return triangle(nextLayer);