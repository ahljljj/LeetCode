'''
1254. Number of Closed Islands

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
Accepted
12,388
Submissions
20,911

'''

'''
2020/04/18, DFS, only record the nodes at the first time be visited

Runtime: 152 ms, faster than 38.03% of Python3 online submissions for Number of Closed Islands.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Number of Closed Islands.

'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        visited = [[False] * m for _ in range(n)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and not visited[i][j] and self.dfs(grid, n, m, dirs, i, j, visited):
                    res += 1
        return res

    def dfs(self, matrix, n, m, dirs, i, j, visited):
        if i < 0 or i >= n or j < 0 or j >= m:
            return False
        if visited[i][j] or matrix[i][j] == 1:
            return True
        visited[i][j] = True
        flag = True
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            flag &= self.dfs(matrix, n, m, dirs, x, y, visited)
        return flag