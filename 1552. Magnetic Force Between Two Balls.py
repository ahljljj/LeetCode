# 1552. Magnetic Force Between Two Balls


#2021/01/18, binary search
# Runtime: 1848 ms, faster than 27.37% of Python3 online submissions for Magnetic Force Between Two Balls.
# Memory Usage: 28.3 MB, less than 34.21% of Python3 online submissions for Magnetic Force Between Two Balls.

# 细节很多，题意不好理解。

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)
        l, r = 0, position[-1] - position[0]
        while l + 1 < r:
            mid = (l + r) >> 1
            if self.check_validity(position, m, mid):
                l = mid
            else:
                r = mid
        if self.check_validity(position, m, r):
            return r
        return l

    def check_validity(self, position, m, threshold):
        for i in range(len(position)):
            if i == 0:
                m -= 1
                prev = position[i]
                continue
            if position[i] - prev >= threshold:
                m -= 1
                prev = position[i]
            if m == 0: return True
        return False


