class TreeNode(object):
    """docstring for TreeNode"""

    def __init__(self, parent, val, left=None, right=None, ht=0):
        super().__init__()
        self.val = val
        self.right = right
        self.left = left
        self.ht = ht
        self.parent = parent

    def NumberChildren(self):
        if self.left is None and self.right is None:
            return 0
        elif (self.left is None and self.right is not None) or (self.left is not None and self.right is None):
            return 1
        return 2

    def smallestChild(self):
        return self.left if self.left.val < self.right.val else self.right


class BST(object):
    """docstring for BST"""

    def __init__(self, root):
        super().__init__()
        self.root = root

    def getMinimumNode(self, root):
        if root.left is None and root.right is None:
            return root.val
        return self.getMinimumNode(root.left)

    def insertion(self, node, val, ht=0, parent=None):
        if node is None:
            return TreeNode(parent, val)
        ht += 1
        if val < node.val:
            node.left = self.insertion(node.left, val, ht=ht, parent=node)
        elif val > node.val:
            node.right = self.insertion(node.right, val, ht=ht, parent=node)
        # Don't want duplicates
        else:
            return

    def deletion(self, root, val):
        while root is not None:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                if root.NumberChildren() == 0:
                    root.parent = None
                elif(root.NumberChildren() == 1):
                    if root is root.parent.right:
                        if root.left is None:
                            root.parent.right = root.right
                            root.right.parent = root.parent
                        else:
                            root.parent.right = root.left
                            root.left.parent = root.parent
                    else:
                        if root.left is None:
                            root.parent.left = root.right
                            root.right.parent = root.parent
                        else:
                            root.parent.left = root.left
                            root.left.parent = root.parent
                elif(root.NumberChildren() == 2):
                    # choose minimum element in right subtree
                    min_node = self.getMinimumNode(root.right)

                    # replace the node being removed with the min node just found
                    root.val = min_node.val

                    # remove the now-duplicate node (previously the min of the right subtree)
                    self.deletion(root.right, min_node.val)
