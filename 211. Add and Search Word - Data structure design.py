
"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


"""


class trienode(object):

    def __init__(self):
        self.children = {}
        self.endofword = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = trienode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for character in word:
            if character not in curr.children:
                curr.children[character] = trienode()
            curr = curr.children[character]
        curr.endofword = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        self.res = False
        self.helper(word, self.root)
        return self.res

    def helper(self, word, node):
        if not word:
            if node.endofword == True:
                self.res = True
            return
        if word[0] == '.':
            for character in node.children:
                self.helper(word[1:], node.children[character])
        else:
            if word[0] not in node.children:
                return
            else:
                self.helper(word[1:], node.children[word[0]])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)