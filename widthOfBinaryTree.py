def widthOfBinaryTree(self, root):
    # Stores Nodes
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        # This condition makes sure it never does the width calculation when at
        # a null (None) node
        if node:
            # If the node exists, add its left and right children.
            # By assigning position values:
            # left child = 2*pos; right child = 2*pos + 1,
            # it makes it such that the width between two nodes is
            # (Right-Left+1)
            queue.append((node.left, depth + 1, pos * 2))
            queue.append((node.right, depth + 1, pos * 2 + 1))
            # Update the level if its not already updated. This snippet will
            # only be called when we first reach the next level
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans
