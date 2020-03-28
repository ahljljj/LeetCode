"""
240. Search a 2D Matrix II



Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        r, c = 0, m - 1
        while r < n and  c >= 0:
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False


# 2020/03/28, divide and conquer


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        # index of first and last row
        l, r = 0, len(matrix[0]) - 1
        # index of first and last column
        u, d = 0, len(matrix) - 1
        return self.search(matrix, l, r, u, d, target)

    def search(self, matrix, l, r, u, d, target):
        if l > r or u > d:
            return False
        if target < matrix[u][l] or target > matrix[d][r]:
            return False
        i = u
        m = (l + r) // 2
        while i <= d and matrix[i][m] <= target:
            if matrix[i][m] == target:
                return True
            i += 1
        return self.search(matrix, l, m - 1, i, d, target) or self.search(matrix, m + 1, r, u, i - 1, target)