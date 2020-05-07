"""
303. Range Sum Query - Immutable


Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

"""


class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if len(nums) > 0:
            self.sum = [0] * len(nums)
            self.sum[0] = nums[0]
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i - 1] + nums[i]
        else:
            self.sum = None

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if self.sum:
            return self.sum[j] - self.sum[i - 1] if i > 0 else self.sum[j]
        else:
            return None

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


# 2020/05/06, dynamic programming

'''
Runtime: 80 ms, faster than 76.93% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.5 MB, less than 10.00% of Python3 online submissions for Range Sum Query - Immutable.
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]