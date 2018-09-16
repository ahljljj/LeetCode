'''
16. 3Sum Closest


Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


'''


#88ms 38.60%

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = float('inf')
        nums.sort()
        nb = len(nums)
        for i in range(nb):
            l, r = i + 1, nb - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp < target:
                    if abs(tmp - target) < abs(result - target):
                        result = tmp
                    l += 1
                elif tmp > target:
                    if abs(tmp - target) < abs(result - target):
                        result = tmp
                    r -= 1
                else:
                    return tmp
        return result
