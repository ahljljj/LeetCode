"""
435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""


'''
wrong

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        print(len(intervals))
        intervals = sorted(intervals, key=lambda element: (element.start, element.end))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start != intervals[i - 1].start:
                res.append(intervals[i])
#        for itv in res:
#            print(itv.start, itv.end)
        count = len(intervals) - len(res)
#        print(count)
        right = res[0].end
        for i in range(1, len(res)):
            if res[i].start < right:
                count += 1
            else:
                right = res[i].end
        return count
            


            
        


'''

# greedy
# time complexity O(nlgn) for sorting


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        print(len(intervals))
        intervals = sorted(intervals, key=lambda element: (element.start, element.end))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start != intervals[i - 1].start:
                res.append(intervals[i])
        count = len(intervals) - len(res)
        right = res[0].end
        for i in range(1, len(res)):
            if res[i].start >= right:
                right = res[i].end
            else:
                right = min(right, res[i].end)
                count += 1
        return count


# simplified greedy

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda element: (element.start, element.end))
        count = 0
        right = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= right:
                right = intervals[i].end
            else:
                right = min(right, intervals[i].end)
                count += 1
        return count


