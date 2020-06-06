'''
677. Map Sum Pairs

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
Accepted
38,576
Submissions
72,592

'''

# 2020/06/05, trie

'''
Runtime: 24 ms, faster than 97.07% of Python3 online submissions for Map Sum Pairs.
Memory Usage: 14 MB, less than 23.10% of Python3 online submissions for Map Sum Pairs.
'''


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.m = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.m:
            self.trie.insert(key)
        self.m[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for word in self.trie.find(prefix):
            ans += self.m[word]
        return ans


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.words_list = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.words_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node: return []
        return node.words_list

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)