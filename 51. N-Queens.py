'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
Accepted
187,348
Submissions
420,224

'''


'''
2020/04/20, permutations

Runtime: 160 ms, faster than 23.02% of Python3 online submissions for N-Queens.
Memory Usage: 14.3 MB, less than 5.00% of Python3 online submissions for N-Queens.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, [], res)
        return res

    def dfs(self, n, cols, res):
        if len(cols) == n:
            board = self.draw_board(cols)
            res.append(board)
        # the row of next potential queens
        row = len(cols)
        for col in range(n):
            if not self.is_valid(cols, row, col):
                continue
            cols.append(col)
            self.dfs(n, cols, res)
            cols.pop()

    def is_valid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True

    def draw_board(self, cols):
        board = []
        n = len(cols)
        for col in cols:
            row = ['Q' if i == col else '.' for i in range(n)]
            board.append(''.join(row))
        return board

