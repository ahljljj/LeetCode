"""
200. Number of Islands


Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3


"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        # number of islands
        count = 0
        self.dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.rows = len(grid)
        self.cols = len(grid[0])
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '1':
                    count += 1
                    self.helper(grid, i, j)
        return count

    def helper(self, grid, row, col):
        # edge/condition
        if row < 0 or row > self.rows - 1 or col < 0 or col > self.cols - 1 or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        for (i, j) in self.dirs:
            neiX = row + i
            neiY = col + j
            self.helper(grid, neiX, neiY)
