'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ''' wrong ans
        for num in nums:
            if (num==target/2):
                nums_ori=nums
                nums_reverse=nums.reverse()
                if nums_ori.index(num)!= len(nums)-1-nums_reverse.index(target - num):
                    return list([nums.index(num), len(nums)-1-nums_reverse.index(target - num)])
            elif (target-num in nums):
                return list([nums.index(num), nums.index(target-num)])
        '''

        class Solution:
            def twoSum(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
                for i in range(len(nums)):
                    if nums[i] == target / 2:
                        if nums[i] in nums[i + 1:len(nums)]:
                            return list([i, i + 1 + nums[i + 1:len(nums)].index(nums[i])])
                    elif (target - nums[i] in nums):
                        return list([i, nums.index(target - nums[i])])
