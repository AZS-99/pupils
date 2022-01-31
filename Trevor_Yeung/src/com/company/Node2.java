package com.company;

public class Node2<T> {
    T value;
    Node2<T> nxt;
    Node2<T> prev;

    public Node2(T value) {
        this.value = value;
        this.nxt = null;
        this.prev = null;
    }

    public String toString() {
        if (this.nxt == null) return value + " --> |";
        return this.value + " --> " + this.nxt.toString();
    }

    public void append(T value) {
        if (this.nxt == null) {
            this.nxt = new Node2<T>(value);
            this.nxt.prev = this;
        } else {
            this.nxt.append(value);
        }
    }

    public T getItem(int index) {
        if (index == 0) return this.value;
        return this.nxt.getItem(index-1);
    }

    public void insert(T value, int index) {
        if (index == 0) {
            var node = new Node2<T>(value);
            node.nxt = this.nxt;
            node.prev = this;
            this.nxt = node;
            if (node.nxt != null) node.nxt.prev = node;
            T temp = this.value;
            this.value = this.nxt.value;
            this.nxt.value = temp;
        } else {
            this.nxt.insert(value, index-1);
        }
    }

    public T getPenultimateValue() {
        if (this.nxt == null) return null;
        if (this.nxt.nxt == null) return this.value;
        return this.nxt.getPenultimateValue();
    }

    public String printReverse() {
        if (this.nxt == null) return this.value.toString();
        return this.nxt.printReverse() + " --> " + this.value;
    }

    public Node2<T> getPenultimateNode() {
        if (this.nxt == null) return null;
        if (this.nxt.nxt == null) return this;
        return this.nxt.getPenultimateNode();
    }

    public Node2<T> getLastNode() {
        if (this.nxt == null) return this;
        return this.nxt.getLastNode();
    }

    public void reverse() {
        if (this.nxt == null) return;
        var penultimate = this.getPenultimateNode();
        var lastNode = penultimate.nxt;
        penultimate.nxt = null;
        this.reverse();
        lastNode.nxt = this.nxt;
        lastNode.prev = this;
        this.nxt = lastNode;
        if (lastNode.nxt != null) lastNode.nxt.prev = lastNode;
        T temp = this.value;
        this.value = this.nxt.value;
        this.nxt.value = temp;
    }

    public void add(Node2<T> node) {
        var lastNode = this.getLastNode();
        lastNode.nxt = node;
        node.prev = lastNode;
    }

    /*
        cut_point is a node somewhere in the list. Move all the Nodes
        before cut_point to the end of the list (keeping their order the same),
        making cut_point the new front. Precondition: the list
        is not empty. Example: if the list contains the data 1, 2, 3, 4 and
        cut_point points to the node containing 3, then the resulting list
        should contain the data 3, 4, 1, 2.
     */

    public Node2<T> getCutPoint(T value) {
        if (this.value == value) return this;
        return this.nxt.getCutPoint(value);
    }

    public void cutPoint(T value) {
//        var c = this.getCutPoint(value);
//        var afterCutPoint = c.nxt;
//        c.nxt = null;
//        afterCutPoint.prev = null;
//        this.reverse();
//        var beginning = this.nxt;
//        beginning.reverse();
//        this.nxt = afterCutPoint;
//        afterCutPoint.prev = this;
//        var lastNode = c.getLastNode();
//        lastNode.nxt = beginning;
//        beginning.prev = lastNode;

        var c = this.getCutPoint(value);
        var last = this.getLastNode();
        last.nxt = this;
        this.prev = last;
        c.prev.nxt = null;
        c.prev = null;
        this.swap(this, c);

    }

    public void swap(Node2<T> node1, Node2<T> node2) {
        var node1prev = node1.prev;
        var node1nxt = node1.nxt;
        var node2prev = node2.prev;
        var node2nxt = node2.nxt;
        if (node1prev != null) node1prev.nxt = node2;
        if (node1nxt != null) node1nxt.prev = node2;
        if (node2prev != null) node2prev.nxt = node1;
        if (node2nxt != null) node2nxt.prev = node1;
        node1.prev = node2prev;
        node1.nxt = node2nxt;
        node2.prev = node1prev;
        node2.nxt = node1nxt;
        T temp = node1.value;
        node1.value = node2.value;
        node2.value = temp;
    }

}
