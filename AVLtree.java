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

class AVLtree {

    Node root;

    AVLtree (Node root) {
        // Constructor
        root = root;
    }

    int height (Node N) {
        if(N == null) {
            return -1;
        } else {
            return N.ht;
        }
    }

    int max(int a, int b) {
        return (a>b)?a:b;
    }

    int BalanceFactor(Node node) {
        if(node == null) {
            return -1;
        }
        return (node.left.ht - node.right.ht);
    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;

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
        y.height = max(height(y.left),height(y.right)) + 1;
        x.height = max(height(x.left),height(x.right)) + 1;

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
        node.height = 1 + max(height(node.left),
                              height(node.right));

        /* 3. Get the balance factor of this ancestor
              node to check whether this node became
              unbalanced */
        int balance = getBalance(node);

        // If this node becomes unbalanced, then there
        // are 4 cases Left Left Case
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
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