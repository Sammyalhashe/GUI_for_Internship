import System;
class Node {
    int val;
    int ht;
    Node left;
    Node right;

    Node (int d) {
        //Constructor
        val = d;
        ht = 0; // height of leaf node is 0
        left = null;
        right = null;
    }
}

public class AVLtree {

    Node root;

    public AVLtree (Node root) {
        // Constructor
        root = root;
    }

    static int height (Node N) {
        if(N == null) {
            return -1;
        } else {
            return N.ht;
        }
    }

    static int max(int a, int b) {
        return (a>b)?a:b;
    }

    static int BalanceFactor(Node node) {
        if(node == null) {
            return 0;
        } else {
            return (height(node.left) - height(node.right));
        }

    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.ht = max(height(y.left), height(y.right)) + 1;
        x.ht = max(height(x.left), height(x.right)) + 1;

        // Return new root
        return x;
    }

    Node leftRotate(Node y) {
        Node x = y.right;
        Node T2 = x.left;

        // perform rotation
        x.left = y;
        y.right =  T2;

        // Update heights
        y.ht = max(height(y.left),height(y.right)) + 1;
        x.ht = max(height(x.left),height(x.right)) + 1;

        return x; // new root
    }

    Node insert(Node node, int key) {

        /* 1.  Perform the normal BST insertion */
        if (node == null)
            return (new Node(key));

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else // Duplicate keys not allowed
            return node;

        /* 2. Update height of this ancestor node */
        node.ht = 1 + max(height(node.left),
                              height(node.right));

        /* 3. Get the balance factor of this ancestor
              node to check whether this node became
              unbalanced */
        int balance = BalanceFactor(node);

        // If this node becomes unbalanced, then there
        // are 4 cases Left Left Case
        if (balance > 1 && key < node.left.key) {
            return this.rightRotate(node);
        }

        // Right Right Case
        if (balance < -1 && key > node.right.key) {
            return this.leftRotate(node);
        }

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return this.rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return this.leftRotate(node);
        }

        /* return the (unchanged) node pointer */
        return node;
    }

    void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }
}