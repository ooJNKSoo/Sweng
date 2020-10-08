class Node {
    int data;
    Node left, right;

    Node(int item){
        data = item;
        left = right = null;
    }
}

class BinaryTree {
    Node root;
    
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
    
    public static void main(String args[]) {
        
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(20);
        tree.root.left = new Node(8);
        tree.root.right = new Node(22);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(12);
        tree.root.left.right.left = new Node(10);
        tree.root.left.right.right = new Node(14);

        int num0 = 10, num1 = 14;
        Node t = tree.lca(tree.root, num0, num1);
        System.out.println("LCA of " + num0 + " and " + num1 + " is " + t.data);

        num0 = 14;
        num1 = 8;
        t = tree.lca(tree.root, num0, num1);
        System.out.println("LCA of " + num0 + " and " + num1 + " is " + t.data);

        num0 = 10;
        num1 = 22;
        t = tree.lca(tree.root, num0, num1);
        System.out.println("LCA of " + num0 + " and " + num1 + " is " + t.data);
    }
}