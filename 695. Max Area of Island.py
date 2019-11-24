'''
695. Max Area of Island
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

'''


'''
2019/11/18, python dfs

Runtime: 160 ms, faster than 62.19% of Python3 online submissions for Max Area of Island.
Memory Usage: 15.7 MB, less than 54.55% of Python3 online submissions for Max Area of Island.

'''


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        res = 0
        visited = [[False] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == 1:
                    res = max(res, self.dfs(grid, visited, n, m, i, j))
        return res

    def dfs(self, grid, visited, n, m, i, j):
        if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or grid[i][j] != 1:
            return 0
        visited[i][j] = True
        cnt = 1
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for dr in dirs:
            ni, nj = i + dr[0], j + dr[1]
            cnt += self.dfs(grid, visited, n, m, ni, nj)
        return cnt