package com.company;

public class BST<T extends Comparable<T>>{

    BST<T> left;
    BST<T> right;
    T value;

    public BST (T value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public String toString() {
        return getLayers(this.depth());
    }

    public String getLayers(int depth) {
        if (depth == 0) return getLayer(0);
        return getLayers(depth - 1) + "\n" + getLayer(depth);
    }

    public String getLayer(int layer) {
        String thisLeft = " ";
        String thisRight = " ";
        if (layer == 0) return this.value.toString();
        if (this.left != null) thisLeft = this.left.getLayer(layer-1);
        if (this.right != null) thisRight = this.right.getLayer(layer-1);
        return thisLeft + " " + thisRight;
    }

    public int size() {
        int l = 0;
        int r = 0;
        if (this.left != null) l = this.left.size();
        if (this.right != null) r = this.right.size();
        return l+r+1;
    }

    public void insert(T value) {
        if (value.compareTo(this.value) < 0) {
            if (this.left == null) this.left = new BST<T>(value);
            else this.left.insert(value);
        } else if (value.compareTo(this.value) > 0) {
            if (this.right == null) this.right = new BST<T>(value);
            else this.right.insert(value);
        }
    }

    public int height_fn() {
        int l = 0;
        int r = 0;
        if (this.left != null) l = this.left.height_fn();
        if (this.right != null) r = this.right.height_fn();
        return Math.max(l, r)+1;
    }

    public int depth() {
        return this.height_fn()-1;
    }

    public BST<T> search(T value) {
        if (value.compareTo(this.value) == 0) return this;
        if (value.compareTo(this.value) < 0 && this.left != null) return this.left.search(value);
        if (value.compareTo(this.value) > 0 && this.right != null) return this.right.search(value);
        return null;
    }

    public BST<T> getSecondLeftmostLeaf() {
        if (this.left == null) return null;
        if (this.left.left == null) return this;
        return this.left.getSecondLeftmostLeaf();
    }

    public void remove(T value) {
        remove_root(this.search(value));
    }

    public static<T extends Comparable<T>> void remove_root(BST<T> root) {
        if (root == null) return;
        if (root.right == null && root.left == null) {
            root.value = null;
        } else if (root.right == null) {
            var thisLeft = root.left;
            root.left = thisLeft.left;
            root.right = thisLeft.right;
            root.value = thisLeft.value;
        } else if (root.right.left == null) {
            var thisRight = root.right;
            root.right = thisRight.right;
            root.value = thisRight.value;
        } else {
            var secondLeftmostLeaf = root.right.getSecondLeftmostLeaf();
            root.value = secondLeftmostLeaf.left.value;
            if (secondLeftmostLeaf.left.right != null) {
                secondLeftmostLeaf.left = secondLeftmostLeaf.left.right;
            } else {
                secondLeftmostLeaf.left = null;
            }
        }
    }

}
