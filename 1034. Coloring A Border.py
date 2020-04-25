'''
1034. Coloring A Border

Given a 2-dimensional grid of integers, each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component that are either 4-directionally adjacent to a square not in the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border of the connected component of that square with the given color, and return the final grid.



Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]


Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000
Accepted
8,701
Submissions
19,604

'''


'''
2020/04/25, matrix based dfs, not easy

Runtime: 136 ms, faster than 69.90% of Python3 online submissions for Coloring A Border.
Memory Usage: 14.1 MB, less than 6.06% of Python3 online submissions for Coloring A Border.

'''


class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        visited, border = set([(r0, c0)]), set()
        n, m = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.dfs(grid, n, m, dirs, r0, c0, visited, border)
        for i in range(n):
            for j in range(m):
                if (i, j) in border:
                    grid[i][j] = color
        return grid

    def dfs(self, matrix, n, m, dirs, i, j, visited, border):
        if self.is_border(matrix, n, m, dirs, i, j): border.add((i, j))
        for delta_i, delta_j in dirs:
            x, y = i + delta_i, j + delta_j
            if x < 0 or x >= n or y < 0 or y >= m or (x, y) in visited \
                    or matrix[x][y] != matrix[i][j]:
                continue
            visited.add((x, y))
            self.dfs(matrix, n, m, dirs, x, y, visited, border)

    def is_border(self, matrix, n, m, dirs, i, j):
        if i in (0, n - 1) or j in (0, m - 1):
            return True
        target = matrix[i][j]
        for delta_i, delta_j in dirs:
            if matrix[i + delta_i][j + delta_j] != target:
                return True
        return False




