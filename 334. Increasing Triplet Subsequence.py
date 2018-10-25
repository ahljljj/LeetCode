"""
334. Increasing Triplet Subsequence


Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false



"""


class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        count = 1
        lower = upper = nums[0]
        for num in nums[1:]:
            if num > upper:
                count += 1
                upper = num
            elif lower < num <= upper:
                count = 2
                upper = num
            elif num < lower:
                lower = num
            if count == 3:
                return True
        return False