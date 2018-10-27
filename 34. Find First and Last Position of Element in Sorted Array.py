'''

34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

'''

# not correct

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nb = len(nums)
        if nb == 1 and target == nums[0]:
            return [0, 0]
        low, high = 0, nb - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and mid == 0:
                idx = mid
                break
            if nums[mid] == target and nums[mid - 1] < target:
                idx = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid - 2
        left = idx

        low, high = 0, nb - 1
        idx = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target and mid == nb - 1:
                idx = mid
                break
            if nums[mid] == target and nums[mid + 1] > target:
                idx = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                high = mid + 2
        right = idx
        return [left, right]



# binary search correct

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if idx == -1:
            return [-1, -1]

        right = idx
        left = idx
        upper = len(nums) - 1
        lower = 0

        while right <= upper:
            mid = (upper + right) // 2
            if nums[mid] == target:
                right = mid + 1
            else:
                upper = mid - 1

        while lower <= left:
            mid = (lower + left) // 2
            if nums[mid] == target:
                left = mid - 1
            else:
                lower = mid + 1

        return [lower, upper]





