package games;

public class OthelloNode {

    Boolean state;
    OthelloNode[] neighbours;

    public OthelloNode() {
        state = null;
        neighbours = new OthelloNode[8];
    }

    public OthelloNode(Boolean state) {
        this.state = state;
        neighbours = new OthelloNode[8];
    }

    public String toString() {
        if (state == null) return ".";
        if (state) return "0";
        return "*";
    }

}
