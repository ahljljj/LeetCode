"""
209. Minimum Size Subarray Sum


Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


"""
# sliding window approach

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        left = 0
        summation = 0
        for i in range(len(nums)):
            summation += nums[i]
            while summation >= s:
                res = min(res, i + 1 - left)
                summation -= nums[left]
                left += 1
        return res if res != float('inf') else 0

'''
binary search
idea: Since all elements are positive, the cumulative sum must be strictly increasing. Then, a subarray sum can expressed as the difference between two cumulative sum. Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.
'''


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # calculate the cumulative sum
        cum_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cum_sum[i] = nums[i - 1]
            cum_sum[i] += cum_sum[i - 1]
        res = len(cum_sum) + 1
        for l in range(len(cum_sum)):
            r = self.find_right(cum_sum, l, s)
            res = min(res, r - l)
        return res if res <= len(cum_sum) else 0

    def find_right(self, nums, i, target):
        l, r = i, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] - nums[i] >= target:
                r = m
            else:
                l = m
        if nums[r] - nums[i] >= target:
            return r
        elif nums[l] - nums[i] >= target:
            return l
        else:
            return float("inf")

# 2020/05/21, sliding window


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")
        l, r = 0, 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while l <= r and curr_sum >= s:
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        return res if res < float("inf") else 0