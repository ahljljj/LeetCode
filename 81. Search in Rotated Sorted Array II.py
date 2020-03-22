"""

81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why



"""

'''

wrong

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            if target > nums[mid]:
                if target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            if target < nums[mid]:
                if target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False
        

'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True

            if nums[high] == nums[mid] and nums[mid] == nums[low]:
                low += 1
                high -= 1
                continue
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


# brute force, 2020/03/22
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False

# binary search, 2020/03/22
#Runtime: 56 ms, faster than 40.15% of Python3 online submissions for Search in Rotated Sorted Array II.
#Memory Usage: 13.3 MB, less than 82.86% of Python3 online submissions for Search in Rotated Sorted Array II.

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
                continue
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m
            else:
                if nums[m] < target <= nums[r]:
                    l = m
                else:
                    r = m
        if nums[l] == target: return True
        if nums[r] == target: return True
        return False