'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 36. Valid Sudoku0
Output: 0
'''

#62 / 62 test cases passed. Runtime: 40 ms
# This running time beats 91.31% of python 3 submissions. May 2018


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        i=0
        num=nums[0]
        while i<n-1 and num<target:
            i+=1
            num=nums[i]
        if i==n-1 and nums[n-1]<target:
            return n
        else:
            return i


''' binary search: haven't verified
 left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left
'''