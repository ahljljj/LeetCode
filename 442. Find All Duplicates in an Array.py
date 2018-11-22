"""
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# swap / change the original array
# maintain the visited nodes


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        res = []
        while i < len(nums):
            idx = nums[i] - 1
            if idx == -2 or idx == i:
                i += 1
                continue
            if idx != i:
                if nums[idx] != nums[i]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    res.append(nums[i])
                    nums[i] = -1
        return res

#

'''
when find a number i, flip the number at position i-1 to negative. 
if the number at position i-1 is already negative, i is the number that occurs twice.

'''

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return res


