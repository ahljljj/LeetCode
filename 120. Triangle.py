"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        n = len(triangle)
        layer = [float('inf')] * n
        for row in range(n):
            tmp = layer[:]
            for col in range(len(triangle[row])):
                if tmp[0] == float('inf'):
                    layer[0] = triangle[row][col]
                else:
                    layer[col] = triangle[row][col] + min(tmp[col - 1], tmp[col])
        return min(layer)

# 2020/05/12, dp, space O(n^2)
'''
Runtime: 56 ms, faster than 87.60% of Python3 online submissions for Triangle.
Memory Usage: 14.9 MB, less than 6.67% of Python3 online submissions for Triangle.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        return min(dp[n-1])

