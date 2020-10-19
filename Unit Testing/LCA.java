public class LCA {

    static Node lca(Node root, int num0, int num1) {
        while (root != null) {

            if (root.data > num0 && root.data > num1)
                root = root.left;

            else if (root.data < num0 && root.data < num1)
                root = root.right;

            else break;
        }
        return root;
    }
}

