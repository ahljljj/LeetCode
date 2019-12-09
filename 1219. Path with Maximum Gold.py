'''
1219. Path with Maximum Gold

In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Accepted
10,170
Submissions
16,479


'''

'''
2019/11/28, python,  wrong and time limit exceeded
'''

class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for i in range(n)]
        self.res = 0
        self.backtracking(grid, visited, n, m, 0, 0, 0)
        return self.res

    def backtracking(self, grid, visited, n, m, i, j, curr):
        if grid[i][j] == 0:
            curr = 0
        else:
            curr += grid[i][j]
        self.res = max(self.res, curr)
        visited[i][j] = True
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for x, y in dirs:
            ni, nj = i + x, j + y
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]:
                continue
            self.backtracking(grid, visited, n, m, ni, nj, curr)
        visited[i][j] = False

'''
2019/11/28, python, backtracking

Runtime: 1548 ms, faster than 46.99% of Python3 online submissions for Path with Maximum Gold.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Path with Maximum Gold.

'''


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for i in range(n)]
        res = 0
        # self.backtracking(grid, visited, n, m, 0, 0, 0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    res = max(res, self.backtracking(grid, visited, n, m, i, j))
        return res

    def backtracking(self, grid, visited, n, m, i, j):
        curr = 0
        visited[i][j] = True
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for x, y in dirs:
            ni, nj = i + x, j + y
            if ni >= 0 and ni < n and nj >= 0 and nj < m and not visited[ni][nj] and grid[i][j] > 0:
                curr = max(curr, grid[i][j] + self.backtracking(grid, visited, n, m, ni, nj))
        visited[i][j] = False
        return curr

