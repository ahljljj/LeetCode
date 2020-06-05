'''

425. Word Squares

Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Accepted
34,891
Submissions
73,779

'''

'''
brute force: tle 13/16, 2020/06/24


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        self.dfs(words, ans, [])
        return ans
        
    def dfs(self, words, ans, square):
        if len(square) == len(words[0]):
            ans.append(square[:])
            return
        for i in range(len(words)):
            if not self.is_valid(square, words[i]):
                continue
            square.append(words[i])
            self.dfs(words, ans, square)
            square.pop()
        
    def is_valid(self, square, word):
        n = len(square)
        if n == 0 or n == len(word): return True
        candidate = ""
        for i in range(n):
            candidate += square[i][n]
        return word[:n] == candidate
            
'''


# 2020/06/05, trie+backtracking


'''
Runtime: 520 ms, faster than 41.68% of Python3 online submissions for Word Squares.
Memory Usage: 15.8 MB, less than 61.52% of Python3 online submissions for Word Squares.
'''


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        ans = []
        words_trie = Trie()
        for word in words:
            words_trie.insert(word)
        self.dfs(words_trie, ans, [], len(words[0]))
        return ans

    def dfs(self, words_trie, ans, square, n):
        if len(square) == n:
            ans.append(square[:])
            return
        prefix = self.get_prefix(square)
        for word in words_trie.find(prefix):
            square.append(word)
            self.dfs(words_trie, ans, square, n)
            square.pop()

    def get_prefix(self, square):
        if not square: return ""
        prefix = ""
        n = len(square)
        for i in range(n):
            prefix += square[i][n]
        return prefix


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
            node.words_list.append(word)
            node = node.children[c]
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c, None)
            if not node: return []
        return node.words_list



