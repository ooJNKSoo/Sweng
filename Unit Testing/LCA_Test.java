import static org.junit.Assert.assertEquals;

import jdk.nashorn.internal.objects.Global;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

@RunWith(JUnit4.class)
class Node {
    int data;
    Node left, right;

    Node(int item){
        data = item;
        left = right = null;
    }

}

@RunWith(JUnit4.class)
public class LCA_Test {

    Node root;
    void initNodes() {
        root = new Node(20);
        root.left = new Node(8);
        root.right = new Node(22);
        root.left.left = new Node(4);
        root.left.right = new Node(12);
        root.left.right.left = new Node(10);
        root.left.right.right = new Node(14);
    }

    LCA tree = new LCA();

    @Test
    public void lca_test() {
        initNodes();
        assertEquals(tree.lca(root, 10, 14).data, 12);
        assertEquals(tree.lca(root, 14, 8).data, 8);
        assertEquals(tree.lca(root, 10, 22).data, 20);
    }
}