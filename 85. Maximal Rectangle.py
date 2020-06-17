'''
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
Accepted
171,969
Submissions
463,883

'''

# 2020/06/17, mono stack

'''
Runtime: 200 ms, faster than 91.08% of Python3 online submissions for Maximal Rectangle.
Memory Usage: 14.6 MB, less than 29.82% of Python3 online submissions for Maximal Rectangle.

思路:计算以每层为底的柱状图的高度,从而转化为上题目.非常精妙.
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        heights.append(-1)
        area = 0
        for i in range(n):
            self.update_heights(matrix, i, heights)
            area = max(area, self.find_area(heights))
        return area

    def update_heights(self, matrix, r, heights):
        n, m = len(matrix), len(matrix[0])
        row = matrix[r]
        for c in range(m):
            if row[c] == '1':
                heights[c] += 1
            else:
                heights[c] = 0
        return

    def find_area(self, heights):
        area = 0
        stack = []
        for r in range(len(heights)):
            while stack and heights[stack[-1]] > heights[r]:
                h = heights[stack.pop()]
                w = r - stack[-1] - 1 if stack else r
                area = max(area, h * w)
            stack.append(r)
        # heights.pop()
        return area



