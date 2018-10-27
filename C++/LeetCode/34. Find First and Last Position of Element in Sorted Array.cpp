/*

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

*/




class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = -1
        left, right = 0, len(nums) - 1
        // first round: search target and return its index, return -1 if not found
        while left <= right:
            mid = (left + right)//2
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
        
        // second round: search the upper index for the target
        while right <= upper:
            mid = (upper + right)//2
            if nums[mid] == target:
                right = mid + 1
            else:
                upper = mid - 1
         
        // third round: search the lower index for the target
        while lower <= left:
            mid = (lower + left)//2
            if nums[mid] == target:
                left = mid - 1
            else:
                lower = mid + 1
                
        return [lower, upper]
        