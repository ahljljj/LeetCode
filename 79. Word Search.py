"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


"""


"""
Wrong 

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        res = ''
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if self.helper(board, word, 0, i, j): return True
        return False

    def helper(self, board, word, idx, row, col):
        if idx == len(word): return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): return False
        if board[row][col] != word[idx]: return False

        exist = self.helper(board, word, idx + 1, row + 1, col)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row - 1, col)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row, col + 1)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row, col - 1)
        if exist: return True

"""


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        res = ''
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if self.helper(board, word, 0, i, j): return True
        return False

    def helper(self, board, word, idx, row, col):
        if idx == len(word): return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]): return False
        if board[row][col] != word[idx]: return False

        tmp = board[row][col]
        board[row][col] = '#'

        exist = self.helper(board, word, idx + 1, row + 1, col)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row - 1, col)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row, col + 1)
        if exist: return True
        exist = self.helper(board, word, idx + 1, row, col - 1)
        if exist: return True

        board[row][col] = tmp


