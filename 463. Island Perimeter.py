"""
463. Island Perimeter


You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""

'''
wrong

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        self.cell, self.comm = 0, 0
        self.dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.search(grid, n, m, i, j)
                    break
        return self.cell * 4 - self.comm * 2
    
    def search(self, grid, n, m, x, y):
        if grid[x][y] == 0:
            return
        grid[x][y] = 0
        self.cell += 1
        for (i, j) in self.dir:
            nx = x + i
            ny = y + j
            if -1 < nx < n and -1 < ny < m and grid[nx][ny] == 1:
                self.comm += 1
                self.search(grid, n, m, nx, ny)
        
        


'''

# brilliant idea

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        sum = 0
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    sum += 4
                    for (x, y) in dire:
                        ni = x + i
                        nj = y + j
                        if -1 < ni < n and -1 < nj < m and grid[ni][nj] == 1:
                            sum -= 1
        return sum


#
'''
loop over the matrix and count the number of islands;
if the current dot is an island, count if it has any right neighbour or down neighbour;
the result is islands * 4 - neighbours * 2
'''


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        cell, comm = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cell += 1
                    if j + 1 < m and grid[i][j + 1] == 1:
                        comm += 1
                    if i + 1 < n and grid[i + 1][j] == 1:
                        comm += 1
        return cell * 4 - comm * 2


