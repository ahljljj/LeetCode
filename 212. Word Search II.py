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