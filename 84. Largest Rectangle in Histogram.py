'''
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:

Input: [2,1,5,6,2,3]
Output: 10
Accepted
253,850
Submissions
735,795


'''


# 2020/06/17, monotonous stack

'''
Runtime: 108 ms, faster than 79.60% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 15.7 MB, less than 48.76% of Python3 online submissions for Largest Rectangle in Histogram.
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                area = max(area, h * w)
            stack.append(i)
        return area

