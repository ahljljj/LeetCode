"""
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right


"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res = obstacleGrid

        n = len(res)
        m = len(res[0])

        if m == 1 and n == 1:
            if res[0][0] == 1:
                return 0
            else:
                return 1
        if res[0][0] == 1:
            res[0][0] = None
        else:
            res[0][0] = 1

        for i in range(1, n):
            if res[i - 1][0] == None:
                res[i][0] = None
                continue
            if res[i][0] != 1:
                res[i][0] = 1
            else:
                res[i][0] = None
        for i in range(1, m):
            if res[0][i - 1] == None:
                res[0][i] = None
                continue
            if res[0][i] != 1:
                res[0][i] = 1
            else:
                res[0][i] = None
        for i in range(1, n):
            for j in range(1, m):
                if res[i][j] == 1:
                    res[i][j] = None
                    continue
                if res[i - 1][j] != None and res[i][j - 1] != None:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
                elif res[i - 1][j] != None:
                    res[i][j] = res[i - 1][j]
                elif res[i][j - 1] != None:
                    res[i][j] = res[i][j - 1]
                else:
                    res[i][j] = None
        return res[n - 1][m - 1] if res[n - 1][m - 1] != None else 0


# 2020/05/12, dp

'''
Runtime: 36 ms, faster than 98.07% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.8 MB, less than 8.89% of Python3 online submissions for Unique Paths II.
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]