'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


'''

# not my idea

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        nb = len(nums)
        low, high = 0, nb-1
        while low <= high:
            mid = (low + high)//2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# 2020/03/22

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > nums[r]:
                if nums[l] <= target and target < nums[m]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m
                else:
                    r = m
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1
    '''Runtime: 36 ms, faster than 88.12% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.2 MB, less than 84.62% of Python3 online submissions for Search in Rotated Sorted Array.'''