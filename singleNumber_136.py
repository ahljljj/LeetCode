'''

136. Single Number
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

#16 / 16 test cases passed. Runtime: 692 ms
#Your runtime beats 7.31% of python 3 submissons.


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nb = len(nums)
        nums2 = nums
        setnums = set(nums2)
        for num in setnums:
            nums.remove(num)
        return list(setnums - set(nums))[0]



