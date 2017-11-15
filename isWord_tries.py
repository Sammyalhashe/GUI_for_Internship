"""import Statements

Importing Everything I need

Use the struct module to store characters in a trie like this:

node = struct.pack('c',"char")

import struct
"""

class Node:

    def __init__(self,character,word_complete):
        self.storedChar = character
        self.pointed_nodes = {}
        self.complete_word = word_complete

    def add_child(self,node):
        #self.pointed_nodes.append(node.storedChar)
        self.pointed_nodes[node.storedChar] = node

    def isRoot(self):
        return self.storedChar == "*"

    def isWordComplete(self):
        return self.complete_word

    def pointsToChar(self,char):
        return char in self.pointed_nodes

    def isLastNode(self):
        return self.pointed_nodes == {}

    def getNextNode(self,char):
        return self.pointed_nodes[char]


class word_trie:
    """Trie containing words with characters at each node

    1) root is *
    2) each node points to nodes with different characters
    3) when adding a word, you see if the node already exists before you add anything else
    4) The beginning of each word is right after the root. ie) no words start on the 2nd level onwards
    """

    def __init__(self):
        """Initialize the trie with root node "*"

        [description]
        """
        self.root = Node("*")

    def add_word(self,word):
        """Add a word to the try

        1) Goes through each character in the word
        2) Initially sets the current node to be the root
        3) If the current node does not point to a node with the next character in question, add the node and point to it
        4) If the character is the last character in the word, but the current node doesn't hold that character, add the character
        to the current node and set isWordComplete to True. Also point to the new node added and give it a child with char **; signifying the
        end of a word
        5) If the character is the last character in the word, and the current node does connect to a node with that character, go to that node and then
        set its isWordComplete attribute to True and add  the node with the ** char if not already there
        6) In all other conditions (character is not the last character and the character is already pointed to), move to the next node

        Arguments:
            word {[type]} -- [description]
        """
        curr_node = self.root
        for char in word:
            if(not curr_node.pointsToChar(char)):
                curr_node.add_child(Node(char,False))
                curr_node = curr_node.getNextNode(char)
            elif(char==word[-1] and not curr_node.pointsToChar(char)):
                curr_node.add_child(Node(char,True))
                curr_node = curr_node.getNextNode(char)
                curr_node.add_child(Node("**",False))
                break
            elif(char==word[-1] and curr_node.pointsToChar(char)):
                curr_node = curr_node.getNextNode(char)
                curr_node.isWordComplete = True
                if(not curr_node.pointsToChar("**")):
                    curr_node.add_child(Node("**",False))
                break
            else:
                curr_node = curr_node.getNextNode(char)