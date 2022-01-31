package com.company;

public class Node<T extends Comparable<T>> {
    T value;
    Node<T> nxt;

    public Node(T value) {
        this.value = value;
        nxt = null;
    }

    public String toString() {
        if (nxt == null) return value.toString() + " --> |";
        else return String.format("%s --> %s", value.toString(), nxt);
    }

    public void append(T value) {
        if (nxt == null) nxt = new Node<T>(value);
        else nxt.append(value);
    }

    public int length() {
        if (nxt == null) return 1;
        else return nxt.length()+1;
    }

    public boolean contains(T value) {
        if (this.value == value) return true;
        if (nxt == null) return false;
        return nxt.contains(value);
    }

    public Node<T> copy() {
        if (nxt == null) return new Node<T>(value);
        var a = new Node<T>(value);
        a.nxt = nxt.copy();
        return a;
    }

    public Node<T> getLastNode() {
        if (nxt == null) return this;
        return nxt.getLastNode();
    }

    public Node<T> add(Node<T> n) {
        var c = this.copy();
        c.getLastNode().nxt = n.copy();
        return c;
    }

    public Node<T> getPenultimateNode() {
        if (nxt == null) return null;
        if (nxt.nxt == null) return this;
        return nxt.getPenultimateNode();
    }

    public void reverse() {
        if (nxt == null) return;
        var last = this.getLastNode();
        var penultimate = this.getPenultimateNode();
        penultimate.nxt = null;
        this.reverse();
        last.nxt = this.nxt;
        this.nxt = last;
        var temp = last.value;
        last.value = this.value;
        this.value = temp;
    }

    public int count(T value) {
        if (nxt == null) return this.value == value? 1 : 0;
        return nxt.count(value) + (this.value == value? 1 : 0);
    }

    public void insertLast(Node<T> lastNode, Node<T> node) {
        if (node == null) return;
        if (node.nxt != null) {
            if (lastNode.value.compareTo(node.nxt.value) < 0) {
                lastNode.nxt = node.nxt;
                node.nxt = lastNode;
                return;
            }
            this.insertLast(lastNode, node.nxt);
        } else {
            node.nxt = lastNode;
        }
    }

    public void sort() {
        if (nxt == null) return;
        var penultimateNode = this.getPenultimateNode();
        var lastNode = penultimateNode.nxt;
        penultimateNode.nxt = null;
        this.sort();
        if (lastNode.value.compareTo(this.value) < 0) {
            lastNode.nxt = this.nxt;
            this.nxt = lastNode;
            var temp = lastNode.value;
            lastNode.value = this.value;
            this.value = temp;
        } else {
            this.insertLast(lastNode, this);
           var current = this;
//            while (current.nxt != null) {
//                if (lastNode.value.compareTo(current.nxt.value) < 0) {
//                    lastNode.nxt = current.nxt;
//                    current.nxt = lastNode;
//                    return;
//                }
//                current = current.nxt;
//            }
            //current.nxt = lastNode;
        }
    }

    public T pop(int index) throws Exception {
        if (index < this.length()) {
            T pop_value;
            if (index == 0) {
                if (this.nxt == null) {
                    pop_value = this.value;
                    this.value = null;
                }
                else {
                    pop_value = this.value;
                    var temp = this.nxt.value;
                    this.nxt.value = this.value;
                    this.value = temp;
                    this.nxt = this.nxt.nxt;
                }
                return pop_value;
            }
            return this.nxt.pop(index-1);
        }
        else {
            throw new Exception("Index out of range");
        }
    }

    public void skipValue(Node<T> node) {
        if (node == null) return;
        if (node.nxt != null) {
            if (node.nxt.value == this.value) {
                node.nxt = node.nxt.nxt;
                this.skipValue(node);
            } else {
                this.skipValue(node.nxt);
            }
        }
    }

    public void removeDuplicates() {
        if (this.nxt == null) return;
        this.nxt.removeDuplicates();
        skipValue(this);
//        var current = this;
//        while (current.nxt != null) {
//            if (current.nxt.value == this.value) {
//                current.nxt = current.nxt.nxt;
//            } else {
//                current = current.nxt;
//            }
//        }
    }

    public void prepend(T value) {
        var newNode = new Node<T>(value);
        newNode.nxt = this.nxt;
        this.nxt = newNode;
        var temp = this.value;
        this.value = value;
        newNode.value = temp;
    }

    /*
    Swap the two nodes which come right after the first occurrence of the passed value
     */

    public void swapAfter(T value) {
        if (this.nxt == null || this.nxt.nxt == null) return;
        if (this.value == value) {
            var temp = this.nxt.value;
            this.nxt.value = this.nxt.nxt.value;
            this.nxt.nxt.value = temp;
            return;
        }
        this.nxt.swapAfter(value);
    }

}
