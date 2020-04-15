'''
329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Accepted
129,963
Submissions
305,696

'''


# 2020/04/15, memoization

'''
Runtime: 512 ms, faster than 60.16% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 15.5 MB, less than 30.77% of Python3 online submissions for Longest Increasing Path in a Matrix.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        res = 0
        memo = {}
        n, m = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                curr = self.dfs(matrix, n, m, dirs, i, j, memo)
                res = max(res, curr)
        return res

    def dfs(self, matrix, n, m, dirs, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        res = 1
        for deltaI, deltaJ in dirs:
            x, y = i + deltaI, j + deltaJ
            if -1 < x < n and -1 < y < m and matrix[x][y] > matrix[i][j]:
                res = max(res, 1 + self.dfs(matrix, n, m, dirs, x, y, memo))
        memo[(i, j)] = res
        return memo[(i, j)]
