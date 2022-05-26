package com.company;

public class LifeNode {

    boolean isAlive;
    LifeNode N, NE, E, SE, S, SW, W, NW;

    public LifeNode(boolean isAlive) {
        this.isAlive = isAlive;
        N = NE = E = SE = S = SW = W = NW = null;
    }

    public String toString() {
        return isAlive? "0" : ".";
    }

}
