# 1229. Meeting Scheduler

# Runtime: 568 ms, faster than 44.24% of Python3 online submissions for Meeting Scheduler.
# Memory Usage: 21.6 MB, less than 72.81% of Python3 online submissions for Meeting Scheduler.


# 2021/01/24, two pointer
# 和 LeetCode 986 几乎一样
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(); slots2.sort()
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            left = max(slots1[i][0], slots2[j][0])
            right = min(slots1[i][1], slots2[j][1])
            if right >= left + duration:
                return [left, left + duration]
            if slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1
        return []