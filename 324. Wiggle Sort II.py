'''
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?


'''

'''
2020/03/30, sort, extra space 

Runtime: 176 ms, faster than 72.20% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 16.7 MB, less than 11.11% of Python3 online submissions for Wiggle Sort II.

'''


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums) // 2
        if len(nums) % 2 == 0:
            i, j = m - 1, len(nums) - 1
            l, r = 0, m
        else:
            i, j = m, len(nums) - 1
            l, r = 1, m + 1
        if i == j: return
        dummy = sorted(nums)
        k = 0
        while i >= l and j >= r:
            nums[k] = dummy[i]
            i -= 1; k += 1
            nums[k] = dummy[j]
            j -= 1; k += 1
        if len(nums) % 2: nums[-1] = dummy[0]