"""
56. Merge Intervals


Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        res = []
        for itv in intervals:
            if not res:
                res.append(itv)
                tmp = itv
                continue
            if itv.start <= tmp.end:
                if itv.end > tmp.end:
                    res.pop()
                    tmp = Interval(tmp.start, itv.end)
                    res.append(tmp)
            else:
                res.append(itv)
                tmp = itv
        return res






