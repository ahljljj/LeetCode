"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        idx_row = False
        idx_col = False

        for j in range(m):
            if matrix[0][j] == 0:
                idx_row = True
                break
        for i in range(n):
            if matrix[i][0] == 0:
                idx_col = True
                break

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(n):
            if i == 0: continue
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        for j in range(m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        if idx_row:
            for j in range(m):
                matrix[0][j] = 0
        if idx_col:
            for i in range(n):
                matrix[i][0] = 0