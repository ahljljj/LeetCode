"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos , neg = nums[0], nums[0]
        maxprod = max(pos, neg)
        for num in nums[1:]:
            tmp1 , tmp2 = pos, neg
            pos = max(num, max(num * tmp1, num * tmp2))
            neg = min(num, min(num * tmp1, num * tmp2))
            maxprod = max(maxprod, max(pos, neg))
        return maxprod