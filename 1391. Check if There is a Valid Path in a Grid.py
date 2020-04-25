'''
1391. Check if There is a Valid Path in a Grid

Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


You will initially start at the street of the upper-left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.



Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
Accepted
7,447
Submissions
16,798

'''

'''
2020/04/25, matrix based dfs, not hard, but tedious

Runtime: 1776 ms, faster than 54.85% of Python3 online submissions for Check if There is a Valid Path in a Grid.
Memory Usage: 112.1 MB, less than 100.00% of Python3 online submissions for Check if There is a Valid Path in a Grid.

'''


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        graph = {(1, 0, 1): [1, 3, 5], (1, 0, -1): [1, 4, 6],
                 (2, 1, 0): [2, 5, 6], (2, -1, 0): [2, 3, 4],
                 (3, 1, 0): [5, 6, 2], (3, 0, -1): [1, 4, 6],
                 (4, 0, 1): [1, 3, 5], (4, 1, 0): [2, 5, 6],
                 (5, -1, 0): [2, 3, 4], (5, 0, -1): [1, 4, 6],
                 (6, 0, 1): [3, 5, 1], (6, -1, 0): [2, 3, 4]}
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n, m = len(grid), len(grid[0])
        return self.dfs(grid, graph, n, m, dirs, 0, 0, set())

    def dfs(self, matrix, graph, n, m, dirs, i, j, visited):
        if (i, j) == (n - 1, m - 1):
            return True
        for delta_i, delta_j in dirs:
            x, y = i + delta_i, j + delta_j
            if x < 0 or x >= n or y < 0 or y >= m \
                    or (x, y) in visited \
                    or (matrix[i][j], delta_i, delta_j) not in graph \
                    or matrix[x][y] not in graph[(matrix[i][j], delta_i, delta_j)]:
                continue
            visited.add((x, y))
            if self.dfs(matrix, graph, n, m, dirs, x, y, visited):
                return True
        return False


