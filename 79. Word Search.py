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

# cpp, rewrite, matrix search with dfs

'''
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int n = board.size(), m = board[0].size();
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                if (dfs(board, word, 0, i, j)) return true;
        return false;   
    }
    
    bool dfs(vector<vector<char>> & board, string word, int idx, int i, int j){
        if (idx == word.length()) return true;
        if (i < 0 || i > board.size() - 1 || j < 0 || j > board[0].size() - 1) return false;
        if (word[idx] != board[i][j]) return false;
        vector<vector<int>> dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        char tmp = board[i][j];
        board[i][j] = '#';
        for (vector<int> dir: dirs){
            int ni = i + dir[0], nj = j + dir[1];
            if (dfs(board, word, idx + 1, ni, nj)) return true;
        }
        board[i][j] = tmp;
        return false;
    }
};
'''


