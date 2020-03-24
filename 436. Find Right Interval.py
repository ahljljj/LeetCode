"""
436. Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.


"""

# stardard binary search to find the least upper bound


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        itvs = []
        for i, itv in enumerate(intervals):
            itvs.append((itv, i))  # ivts: (interval, index)
        itvs = sorted(itvs, key=lambda elem: elem[0].start)
        res = [-1] * len(itvs)
        for (itv, i) in itvs:
            idx = self.bisearch(itvs, itv)
            res[i] = idx
        return res

    def bisearch(self, itvs, node):
        left, right = 0, len(itvs)
        target = node.end
        while left < right:
            mid = (left + right) >> 1
            if itvs[mid][0].start >= target:
                right = mid
            else:
                left = mid + 1
        return itvs[left][1] if left < len(itvs) else -1


'''
2020/03/24, rewrite using binary search

Runtime: 452 ms, faster than 20.65% of Python3 online submissions for Find Right Interval.
Memory Usage: 18.3 MB, less than 33.33% of Python3 online submissions for Find Right Interval.
'''


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        itvs = []
        # reorganize intervals so that the first position denote the position of the interval
        # by doing this, it will remeber the position of each interveral in the origial list
        for i, itv in enumerate(intervals):
            itvs.append((i, itv))
        # sort the intervals according to the starting point in order to apply binary search
        itvs = sorted(itvs, key=lambda elem: elem[1][0])
        res = [-1] * len(itvs)
        for (i, itv) in itvs:
            # find the right interval with smallest starting point >= ending point of the given interval
            idx = self.find_right(itvs, itv[1])
            res[i] = idx
        return res

    def find_right(self, itvs, target):
        # search the right interval with smallest starting point >= target within itvs
        l, r = 0, len(itvs) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if itvs[m][1][0] == target:
                return itvs[m][0]
            elif itvs[m][1][0] > target:
                r = m
            else:
                l = m
        if itvs[l][1][0] >= target:
            return itvs[l][0]
        if itvs[r][1][0] >= target:
            return itvs[r][0]
        return -1