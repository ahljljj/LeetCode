# 1283. Find the Smallest Divisor Given a Threshold

#2021/01/17, binary search over solution space

# Runtime: 892 ms, faster than 5.03% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
# Memory Usage: 19.8 MB, less than 89.39% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l + 1 < r:
            m = (l + r) >> 1
            if self.check_validity(nums, m, threshold):
                r = m
            else:
                l = m
        if self.check_validity(nums, l, threshold):
            return l
        return r

    def check_validity(self, nums, d, threshold):
        ans = 0
        for num in nums:
            ans += num // d
            if num % d: ans += 1
        if ans <= threshold:
            return True
        return False

