"""
221. Maximal Square


Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""



class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dynamic programming
        # time complicity O(mn), space complicity O(mn)

        # return 0 for null matrix
        if not matrix: return 0
        # the largest size we have find
        maxlen = 0
        n = len(matrix)  # number of rows
        m = len(matrix[0])  # number of cols
        # edge case: rows = 1
        if n == 1:
            return max([int(c) for c in matrix[0]])
        # initialize the first col/row
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = int(matrix[0][j])
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
        # update max size after initialize the 1st row/col
        maxlen = max(max(dp))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '1':
                    dp[i][j] = min(min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i][j - 1]) + 1
                    maxlen = max(dp[i][j], maxlen)
        return maxlen ** 2

