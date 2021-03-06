"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


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
        start, end = 0, n * m - 1
        while start <= end:
            mid = (start + end) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target: return True
            if target > matrix[row][col]:
                start = mid + 1
            else:
                end = mid - 1
        return False

