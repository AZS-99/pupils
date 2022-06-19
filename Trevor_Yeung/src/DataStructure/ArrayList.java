package DataStructure;

import java.util.Arrays;

public class ArrayList <T> {

    private Object[] array;
    private int capacity, length;

    public ArrayList() {
        this.length = 0;
        capacity = 5;
        array = new Object[capacity];
    }

    public String toString() {
        StringBuilder output = new StringBuilder();
        output.append('[');
        for (int i = 0; i < length; i++) {
            output.append(array[i].toString());
            if (i < length - 1) output.append(", ");
        }
        output.append(']');
        return output.toString();
    }

    public void add(T value) {
        if (length == capacity) enlarge();
        array[length] = value;
        length++;
    }

    public void addAll(ArrayList<T> arraylist2) {
        var temp = new ArrayList<T>();
        for (int i = 0; i < arraylist2.length; i++) {
            temp.add((T) arraylist2.array[i]);
        }
        for (int i = 0; i < temp.length; i++) {
            this.add((T) temp.array[i]);
        }
    }

    public void addAll(ArrayList<T> arraylist2, int index) {
        var temp = new ArrayList<T>();
        if (index < 0 || index > arraylist2.length-1) return;
        for (int i = index; i < arraylist2.length; i++) {
            temp.add((T) arraylist2.array[i]);
        }
        for (int i = 0; i < temp.length; i++) {
            this.add((T) temp.array[i]);
        }
    }

    public void clear() {
        length = 0;
        capacity = 5;
        array = new Object[capacity];
    }

    public ArrayList<T> clone() {
        var arr = new ArrayList<T>();
        arr.array = new Object[capacity];
        arr.capacity = capacity;
        arr.length = length;
        if (length >= 0) System.arraycopy(array, 0, arr.array, 0, length);
        return arr;
    }

    public boolean contains(T value) {
        for (int i = 0; i < length; i++) {
            if (array[i] == value) return true;
        }
        return false;
    }

    private void enlarge() {
        array = Arrays.copyOf(array, capacity * 2);
        capacity *= 2;
    }

    public T get(int index) {
        if (index > length-1 || index < 0) return null;
        return (T) array[index];
    }

    public int indexOf(T value) {
        for (int i = 0; i < length; i++) {
            if (array[i] == value) return i;
        }
        return -1;
    }

    public boolean isEmpty() {
        return length == 0;
    }

    public int lastIndexOf(T value) {
        for (int i = length-1; i > -1; i--) {
            if (array[i] == value) return i;
        }
        return -1;
    }

    public void remove() {
        length--;
        if (length == capacity/2 && capacity > 10) array = Arrays.copyOf(Arrays.copyOfRange(array, 0, length), capacity/2);
    }

    public void remove(int index) {
        if (index < 0 || index > length-1) return;
        for (int i = index; i < length-1; i++) {
            array[i] = array[i+1];
        }
        remove();
    }

    public void removeAll() {
        length = 0;
    }

    public void retainAll(ArrayList<T> array1) {
        var arr = array1.clone();
        arr.sort();
        for (int i = 0; i < length; i++) {

        }
    }

    public int size() {
        return length;
    }

    public void sort() {
        Arrays.sort(array);
    }

    public static void main(String[] args) {
        var array = new ArrayList<Integer>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.add(4);
        array.add(5);
        array.remove(4132);
        System.out.println(array);

    }

}
