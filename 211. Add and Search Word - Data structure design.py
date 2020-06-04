
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

# 2020/06/04, trie, hashtable


'''

Runtime: 336 ms, faster than 70.68% of Python3 online submissions for Add and Search Word - Data structure design.
Memory Usage: 28.3 MB, less than 8.70% of Python3 online submissions for Add and Search Word - Data structure design.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(word, self.root, 0)

    def dfs(self, word, node, pos):
        if pos == len(word):
            return node.is_word
        if word[pos] != '.':
            node = node.children.get(word[pos], None)
            if not node: return False
            return self.dfs(word, node, pos + 1)
        else:
            for son in node.children:
                if self.dfs(word, node.children[son], pos + 1):
                    return True
        return False