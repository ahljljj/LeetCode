'''
1020. Number of Enclaves

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.
Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation:
All 1s are either on the boundary or can reach the boundary.


Note:

1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
Accepted
14,011
Submissions
25,019

'''

'''
2020/04/18, DFS from the edge of matrix

Runtime: 628 ms, faster than 32.17% of Python3 online submissions for Number of Enclaves.
Memory Usage: 15 MB, less than 50.00% of Python3 online submissions for Number of Enclaves.

'''


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        visited = [[False] * m for _ in range(n)]
        self.can, total = 0, 0
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    total += 1
                    if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                        self.dfs(A, n, m, dirs, i, j, visited)
        return total - self.can

    def dfs(self, matrix, n, m, dirs, i, j, visited):
        if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or matrix[i][j] == 0:
            return
        visited[i][j] = True
        self.can += 1
        for deltaI, deltaJ in dirs:
            self.dfs(matrix, n, m, dirs, i + deltaI, j + deltaJ, visited)
