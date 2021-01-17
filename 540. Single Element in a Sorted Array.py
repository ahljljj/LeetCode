# 540. Single Element in a Sorted Array





# 2021/01/07, binary search
# 每次将数组分成两半，唯一数肯定在长度为奇数的那一半。

# Runtime: 96 ms, faster than 8.11% of Python3 online submissions for Single Element in a Sorted Array.
# Memory Usage: 16.5 MB, less than 38.10% of Python3 online submissions for Single Element in a Sorted Array.

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1
        while l + 2 < r:
            m = (l + r) >> 1
            if nums[m] != nums[m - 1]:
                m -= 1
            if (m - l) % 2 == 0:
                r = m
            else:
                l = m + 1
        if nums[l] != nums[l + 1]: return nums[l]
        return nums[r]


