package testing;

import java.util.ArrayList;

public class test {

    public static void main(String[] args) {
        var arr = new ArrayList<Integer>();
        arr.add(1);
        arr.addAll(arr);
        System.out.println(arr);
        arr.addAll(arr);
        System.out.println(arr);
        arr.addAll(arr);
        System.out.println(arr);
    }

}
