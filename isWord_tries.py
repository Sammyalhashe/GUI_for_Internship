
class Node:
    """Node to store characters in trie

    1) Initialized with a character to store, a dictionary of nodes that it points to, and a boolean value signifying if word is complete (default False)
    2) has methods (explained below) that do most things the trie needs

    Variables:
         storedChar {[char]} -- [character the node holds in the trie]
         pointed_nodes {[dict]} -- [a dictionary holding the child nodes that the current node has connected. The
         key is the character and the value is the Node obect]
         complete_word {[BOOL]} -- True if this character is the end of some word
    """

    def __init__(self, character, word_complete=False):
        self.storedChar = character
        self.pointed_nodes = {}
        self.complete_word = word_complete

    def add_child(self, node):
        """adds a child

        adds a child to the dictionary of stored nodes this node points to

        Arguments:
            node {[Node]} -- [New Node object to add to pointed_nodes dictionary]
        """
        self.pointed_nodes[node.storedChar] = node

    def isRoot(self):
        """Tells us if this node is a root of a trie

        returns a bool if so

        Returns:
            [BOOL] -- [True if a root of a trie]
        """
        return self.storedChar == "*"

    def isWordComplete(self):
        """easy way to see if the character we have gotten to so far is the end

        returns True if so

        Returns:
            [BOOL] -- [True if the char stored is the last char of a word]
        """
        return self.complete_word

    def pointsToChar(self, char):
        """Tells us if the current node points to another node that stores character char

        returns True if so

        Arguments:
            char {[str]} -- [checking if char is pointed to]

        Returns:
            [BOOL] -- [True if so]
        """
        return char in self.pointed_nodes

    def isLastNode(self):
        # Checks if the current node doesn't point to anything else
        return self.pointed_nodes == {}

    def getNextNode(self, char):
        """Returns the next node that the current node points to storing char

        [returns the next node that the current node points to storing char]

        Arguments:
            char {[str]} -- [char that the next node stores]

        Returns:
            [Node] -- [Next node]
        """
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

        [Trie stores characters at each node. Aka; each letter of a word. The root is specified by a '*'
        while an end of a word is specified by a '**']
        """
        self.root = Node("*")

    def add_word(self, word):
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
            word {[String]} -- [Word to be added to the trie]
        """
        curr_node = self.root
        for char in word:
            if(not curr_node.pointsToChar(char) and char != word[-1]):
                curr_node.add_child(Node(char, False))
                curr_node = curr_node.getNextNode(char)
                print("added char %s" % (char))
            elif(char == word[-1] and not curr_node.pointsToChar(char)):
                curr_node.add_child(Node(char, True))
                curr_node = curr_node.getNextNode(char)
                curr_node.add_child(Node("**", False))
                print("added char, end of word %s" % (char))
                break
            elif(char == word[-1] and curr_node.pointsToChar(char)):
                curr_node = curr_node.getNextNode(char)
                curr_node.isWordComplete = True
                if(not curr_node.pointsToChar("**")):
                    curr_node.add_child(Node("**", False))
                break
            else:
                curr_node = curr_node.getNextNode(char)

    def add_word_rec(self, word):
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
            word {[String]} -- [Word to be added to the trie]
        """
        self.traverse_trie_down(self.root,)

    def traverse_trie_down(self, start_node, word):
        """Used by the add_word_rec function to recursively traverse down and place characters

        1) Start at start node, if start node does not contain char you want to insert, create a new one that has it
        and add the standard '**' node if the word has ended. Then move onto the next letter by popping from word. (recursive call)
        2) If it points to a node that contains the char, recursively call this function with the new start node of that ndoe with the char and move to next letter (by popping word).
        Arguments:
            start_node {[Node]} -- [Start node for traversing the trie]
            word {[String]} -- [Word to recursively insert]

        """

        if(len(word) == 1):
            if(not start_node.pointsToChar(word[0])):
                start_node.add_child(Node(word[0], True if word[0] in ('a', 'i') else False))
                start_node = start_node.getNextNode(word.pop(0))
                start_node.add_child(Node("**"))
                return
            else:
                start_node = start_node.getNextNode(word.pop())
                start_node.add_child(Node("**"))
                return

        else:
            if(not start_node.pointsToChar(word[0])):
                start_node.add_child(Node(word[0], True))
                character = word.pop(0)
                self.traverse_trie_down(start_node.getNextNode(character), word)
            else:
                character = word.pop(0)
                self.traverse_trie_down(start_node.getNextNode(character), word)
                return


if __name__ == '__main__':
    trie = word_trie()
    trie.add_word("sammy")
    trie.add_word("alhashemi")
