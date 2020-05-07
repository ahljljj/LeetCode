'''
308. Range Sum Query 2D - Mutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
Accepted
44,564
Submissions
128,149

'''



# 2020/05/07, binary indexed tree, too hard

'''
Runtime: 404 ms, faster than 46.56% of Python3 online submissions for Range Sum Query 2D - Mutable.
Memory Usage: 15.5 MB, less than 20.00% of Python3 online submissions for Range Sum Query 2D - Mutable.
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.matrix = [[]]
            self.bit = [[0]]
            return
        n, m = len(matrix), len(matrix[0])
        self.matrix = [[0] * m for _ in range(n)]
        self.bit = [[0] * (1 + m) for _ in range(1 + n)]
        for i in range(n):
            for j in range(m):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        n, m = len(self.matrix), len(self.matrix[0])
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= n:
            j = col + 1
            while j <= m:
                self.bit[i][j] += delta
                j += self.lowbit(j)
            i += self.lowbit(i)

    def prefix_sum(self, row, col):
        i = row
        res = 0
        while i > 0:
            j = col
            while j > 0:
                res += self.bit[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum(row2 + 1, col2 + 1) \
               - self.prefix_sum(row2 + 1, col1) - self.prefix_sum(row1, col2 + 1) \
               + self.prefix_sum(row1, col1)

    def lowbit(self, x):
        return x & (-x)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)