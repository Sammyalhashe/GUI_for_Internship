""" Node is defined as """


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


INT_MAX = 100000
INT_MIN = 0


def checkBST(root):

    return isBST(root, INT_MIN, INT_MAX)


def isBST(node, MIN, MAX):
    if node is None:
        return True
    elif (node.data < MIN or node.data > MAX):
        return False
    else:
        return isBST(node.left, MIN, node.data - 1) and isBST(node.right, node.data + 1, MAX)
