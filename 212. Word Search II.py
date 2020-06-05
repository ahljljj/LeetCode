'''
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
Accepted
176,516
Submissions
540,529

'''


'''

2020/04/22, wrong, time limit exceeded, 34 / 36 test cases passed.
# starting from dictionary is not correct...

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = set(words)
        res = []
        for word in words:
            if self.search(board,   word):
                res.append(word)
        return res
    
    def dfs(self, board, n, m, dirs, i, j,  pos, word, visited):
        if pos == len(word) - 1 and word[pos] == board[i][j]:
            return True
        if word[pos] != board[i][j]:
            return False
        visited[i][j] = True
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            if x < 0 or x >= n or y < 0 or y >= m \
            or visited[x][y]:
                continue
            visited[x][y] = True
            if self.dfs(board, n, m, dirs, x, y,   pos + 1, word, visited):
                return True
            visited[x][y] = False
        visited[i][j] = False
        return False
    
    def search(self, board, word):
        n, m = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if self.dfs(board, n, m, dirs, i, j,  0, word, visited):
                    return True
        return False
        
        
'''

# 2020/04/22, starting from matrix since dict could be very big in general

'''
Runtime: 332 ms, faster than 71.22% of Python3 online submissions for Word Search II.
Memory Usage: 22.2 MB, less than 100.00% of Python3 online submissions for Word Search II.
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefix_words = set()
        for word in words:
            for i in range(len(word)):
                prefix_words.add(word[:i + 1])
        words = set(words)
        n, m = len(board), len(board[0])
        res = []
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        res = set()
        for i in range(n):
            for j in range(m):
                self.dfs(board, n, m, dirs, i, j, prefix_words, words, board[i][j], res, set([(i, j)]))
        return list(res)

    def dfs(self, matrix, n, m, dirs, i, j, prefix_words, words, word, res, visited):
        if word not in prefix_words: return
        if word in words:
            res.add(word)
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited:
                continue
            visited.add((x, y))
            self.dfs(matrix, n, m, dirs, x, y, prefix_words, words, word + matrix[x][y], res, visited)
            visited.remove((x, y))

# 2020/06/05, trie


'''
Runtime: 956 ms, faster than 6.55% of Python3 online submissions for Word Search II.
Memory Usage: 32.1 MB, less than 45.24% of Python3 online submissions for Word Search II.
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        words_trie = Trie()
        for word in words:
            words_trie.insert(word)
        ans = set()
        for i in range(n):
            for j in range(m):
                self.dfs(board, n, m, dirs, words_trie, ans, i, j, board[i][j], set([(i, j)]))
        return list(ans)

    def dfs(self, board, n, m, dirs, trie, ans, i, j, word, visited):
        if not trie.startsWith(word): return
        if trie.search(word):
            ans.add(word)
        for delta_i, delta_j in dirs:
            n_i = i + delta_i
            n_j = j + delta_j
            if n_i < 0 or n_i >= n or n_j < 0 or n_j >= m or (n_i, n_j) in visited:
                continue
            visited.add((n_i, n_j))
            self.dfs(board, n, m, dirs, trie, ans, n_i, n_j, word + board[n_i][n_j], visited)
            visited.remove((n_i, n_j))


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c, None)
            if not node: return None
        return node

    def search(self, word):
        node = self.find(word)
        return node and node.is_word

    def startsWith(self, prefix):
        return self.find(prefix)

