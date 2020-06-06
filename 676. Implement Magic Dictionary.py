'''

676. Implement Magic Dictionary

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
Accepted
37,738
Submissions
70,034

'''

# 2020/06/06, trie


'''
Runtime: 52 ms, faster than 10.77% of Python3 online submissions for Implement Magic Dictionary.
Memory Usage: 13.8 MB, less than 66.09% of Python3 online submissions for Implement Magic Dictionary.
'''


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.dfs(self.root, word, 0, 0)

    def dfs(self, root, word, count, pos):
        if count > 1: return False
        if pos == len(word):
            if count == 0:
                return False
            return root.is_word
        for son in root.children:
            if son == word[pos]:
                if self.dfs(root.children[word[pos]], word, count, pos + 1):
                    return True
            elif self.dfs(root.children[son], word, count + 1, pos + 1):
                return True
        return False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)