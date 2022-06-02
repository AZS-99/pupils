package com.company;

import java.util.ArrayList;

public class LifeNode {

    boolean isAlive;
    ArrayList<LifeNode> neighbours;

    public LifeNode() {
        isAlive = false;
        neighbours = new ArrayList<>();
    }

    public LifeNode(boolean isAlive) {
        this.isAlive = isAlive;
        neighbours = new ArrayList<>();
    }

    public LifeNode copy() {
        var node = new LifeNode();
        node.isAlive = this.isAlive;
        neighbours = new ArrayList<>();
        return node;
    }

    public String toString() {
        return isAlive? "0" : ".";
    }

}
