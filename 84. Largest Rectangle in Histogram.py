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

思路：核心思想是最大矩形的height必然是其中的一个height。所以问题简化为，对其中某个height，它所形成的最大矩形的面积是多大？如果能找到左边第一个小于这个height的端点l 和 右边第一个小于这个height的端点r，那么这个最大矩形的宽度是 r - l - 1。使用单调递增栈，上述的右端点非常好计算，即为当前的index：i。左端点的情况有点复杂。在pop出height后，此时栈顶元素必然是第一个小于height的index：l，因为其后的元素必然都大于l，不可能更小。这题代码写起来很简单，但其实思路很精妙，很难想出来。

时间复杂度：看似嵌套了while循环，但实现上栈中元素最多就是 $n$，while循环也最多只会运行$n$ 次，所以总的时间复杂度是$O(n)$。
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

