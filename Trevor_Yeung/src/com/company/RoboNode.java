package com.company;

public class RoboNode {

    char type;
    Double val;
    RoboNode up, down, left, right;
    boolean visited;

    public RoboNode(char type) {
        this.type = type;
        visited = false;

        if (type == 'S') val = 0.0;
        else val = Double.POSITIVE_INFINITY;

        up = down = left = right = null;
    }

    public String toString() {
        var str = "";
        if (left != null)
            str += "←";
        if (down != null)
            str += "↓";
        if (up != null)
            str += "⬆";
        if (right != null)
            str += "→";
        return str;
    }

}
