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


# 2020/04/11， wrong

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.res = False
        for i in range(n):
            for j in range(m):
                visited = [[False] * m for _ in range(n)]
                self.backtracking(board, visited, n, m, i, j, dirs, 0, word)
                if self.res: return True
        return False

    def backtracking(self, board, visited, n, m, x, y, dirs, i, word):
        if i == len(word) or board[x][y] == word:
            self.res = True
            return
        for deltaX, deltaY in dirs:
            nx, ny = x + deltaX, y + deltaY
            if -1 < nx < n and -1 < ny < m and board[nx][ny] == word[i] \
                    and not visited[nx][ny]:
                visited[nx][ny] = True
                self.backtracking(board, visited, n, m, nx, ny, dirs, i + 1, word)
                visited[nx][ny] = False

# 2020/04/22, permutation, pass with slight modification


'''
Runtime: 308 ms, faster than 88.09% of Python3 online submissions for Word Search.
Memory Usage: 14.8 MB, less than 27.66% of Python3 online submissions for Word Search.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.res = False
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                if self.backtracking(board, set([(i, j)]), n, m, i, j, dirs, 1, word):
                    return True
        return False

    def backtracking(self, board, visited, n, m, x, y, dirs, pos, word):
        if pos == len(word):
            return True
        for deltaX, deltaY in dirs:
            nx, ny = x + deltaX, y + deltaY
            if -1 < nx < n and -1 < ny < m and (nx, ny) not in visited and board[nx][ny] == word[pos]:
                visited.add((nx, ny))
                if self.backtracking(board, visited, n, m, nx, ny, dirs, pos + 1, word):
                    return True
                visited.remove((nx, ny))
        return False
