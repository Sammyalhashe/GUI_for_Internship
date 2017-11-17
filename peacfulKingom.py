class Tree(object):
    """docstring for Tree"""
    def __init__(self, root): #root is a Node() object
        super().__init__()
        """Initialize the tree
        [
        root is a Node() object and it is set to be the root of the tree
        nodeList is a dict that maintaines what Nodes have been added with key of the city number and value of the Node() object
        ]
        """
        self.root = root
        self.nodeList = {}
        self.nodeList[root.city] = root
        self.totalLevels = 1

    def addEdge(self, city1, city2):
        """add and Edge to the tree

        [
        access the Node() object corresponding to city1 in the tree, create a new Node() object for city 2 and add it as a child (by adding to the Nodes
        children dict (keyed by city number as well) for city1. Then add to the nodeList dict the city2 key with value of its Node() object just created
        -> accessed by going into the nodeList, getting the Node() object corresponding to city1, and then accessing the children dict in that node (works similarily)
        for the Node() object just added as child. Then make the parent of city2 be city1
        ]

        Arguments:
            city1 {[int]} -- [city number of a city that's already in the tree]
            city2 {[int]} -- [city number of a city that is not in the tree (property of trees)]
        """
        if (city1 in self.nodeList and city2 not in self.nodeList):
            self.nodeList[city1].addChild(Node(city2, self.nodeList[city1].level + 1, parent = self.nodeList[city1]))
            self.nodeList[city2] = self.nodeList[city1].children[city2]
            self.totalLevels = max(self.totalLevels, self.nodeList[city2].level)
        elif (city2 in self.nodeList and city1 not in self.nodeList):
            self.nodeList[city2].addChild(Node(city1, self.nodeList[city2].level + 1, parent = self.nodeList[city2]))
            self.nodeList[city1] = self.nodeList[city2].children[city1]
            self.totalLevels = max(self.totalLevels, self.nodeList[city1].level)



    def findParent(self,city):
        """ return the parent of Node() in question (indexed by city number) """
        return self.nodeList[city].parent



class Node(object):
    """Node object for the Tree

    [
    Node() object contain:
        1) Their city number
        2) A children dictionary keyed by the city number and has value of children Node() objects
        3) A parent Node() object
    ]

    """
    def __init__(self, city, level, parent = None):
        """initialize the Node() object

        Arguments:
            city {[int]} -- [city number the Node() object is intialized to hold]

        Keyword Arguments:
            parent {[Node]} -- [Node() object who is the parent of the Node() being made currently] (default: {None})
        """
        super().__init__()
        self.city = city
        self.children = {}
        self.parent = parent
        self.level = level

    def addChild(self, cityNode):
        """Add a child to the Node() object

        [
        Accesses the children dictionary by the new Node() object's city value and adds the Node() as the dictionaries keyed value
        ]

        Arguments:
            cityNode {[Node]} -- [Node() object to be added as a child to the current Node()]
        """
        self.children[cityNode.city] = cityNode #key is city number; val is Node() object

    def getLevel(self):
        return self.level

# SOLUTION:
def peacefulKingdom(kingdomTree):
    # Cycle through levels from second-last to first
    levels = kingdomTree.totalLevels


if __name__ == '__main__':
    n = int(input().strip())

    edge1 = tuple(map(lambda x:int(x), input().strip().split()))
    root = Node(edge1[0], True, 1) #level = 1 for root
    kingdom = Tree(root)
    kingdom.addEdge(edge1[0], edge1[1])
    for i in range(n-1):
        edge = tuple(map(lambda x:int(x), input().strip().split()))
        kingdom.addEdge(edge[0], edge[1])


    number = peacefulKingdom(kingdom)


"""
You may try the following approach if you didn't get the editorial. Observe that if you know that answers (valid combinations) for the children of a node, you can calculate the answer for that node from the answers of it's children. - This can be done as following: Suppose a node has N children. If the child C1 is given color red (0), suppose number of valid combinations for that configuration (with child C1 as red) are C1r. If the child C1 is given color black (1), suppose number of valid combinations for that configuration (with child C1 as black) are C1b. Similarly the answer for ith child with color as red is Cir and with color as black is Cib. Then the answer for that parent node should be (C1r+C1b)(C2r+C2b).........(CNr+CNb). This may seem right at the first glance but it's not always true, as we MAY have also added some invalid combinations while we calculated our answer for the parent node. What are these invalid combinations? Suppose the parent has color black, then we've also added the combinations in our answer for the parent node where C1 is red, C2 is red,.... CN is red, which are (C1r*C2r*C3r....CNr). BUT POINT 1 - These combinations are only invalid, if the parent's color is black and the color of parent's parent is red (as these combinations clearly leaves the parent(black) with no other black nodes directly connected to it, which are indeed invalid as the children with red color can then attack it's parent with black color) POINT 2 - Same combinations are valid, if the parent's color is black and the color of parent's parent is also black. So we have to maintain two things. What's the color of current node? Is the color of current node's parent same as the color of current node (which I've done as 2, if true, and 1 if false in my code)? So, if the color of node and node's parent are same, then don't subtract the 'potential' invalid combinations, else subtract them. Recursively calculate answer for each node using DFS.
"""