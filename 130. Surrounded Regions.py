"""
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""

'''

# DFS

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board:
            return 
        row, column,res = len(board), len(board[0]), []
        for j in range(column):
            self.find(board, 0, j, res, row, column)
            self.find(board, row-1, j, res, row, column)
        for i in range(row):
            self.find(board, i, 0, res, row, column)
            self.find(board, i, column-1, res, row, column)
        for i in range(row):
            for j in range(column):
                if [i, j] not in res:
                    board[i][j] = "X"
                
    def find(self, board, i, j, res, row, column):
        if i < 0 or j < 0 or i >= row or j >= column or [i,j] in res:
            return 
        if board[i][j] == "O":
            res.append([i,j])
            self.find(board, i+1, j, res, row, column)
            self.find(board, i-1, j, res, row, column)
            self.find(board, i, j+1, res, row, column)
            self.find(board, i, j-1, res, row, column)
        else:
            return 

'''

# BFS

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        visited = set()
        valid_nums = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    current = (i, j)
                    numbers = self.bfs(current, board, len(board) - 1, len(board[0]) - 1)
                    visited = visited.union(numbers)
                    if self.is_valid(list(numbers), len(board) - 1, len(board[0]) - 1):
                        valid_nums.extend(list(numbers))

        for (i, j) in valid_nums:
            board[i][j] = 'X'

    def bfs(self, root, board, x_length, y_length):
        next_visit = [root]
        visited = set()
        while len(next_visit) > 0:
            current = next_visit.pop(0)
            i = current[0]
            j = current[1]
            if i >= 0 and i <= x_length and j >= 0 and j <= y_length:
                if board[i][j] == 'O' and (i, j) not in visited:
                    visited.add((i, j))
                    next_visit.append((i - 1, j))
                    next_visit.append((i, j - 1))
                    next_visit.append((i + 1, j))
                    next_visit.append((i, j + 1))
        return visited

    def is_valid(self, nums, x_max, y_max):
        for i in range(len(nums)):
            if nums[i][0] == 0 or nums[i][0] == x_max:
                return False
            if nums[i][1] == 0 or nums[i][1] == y_max:
                return False
        return True