'''
713. Subarray Product Less Than K

Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.


2020/03/27 sliding window


Runtime: 1268 ms, faster than 26.60% of Python3 online submissions for Subarray Product Less Than K.
Memory Usage: 18 MB, less than 11.11% of Python3 online submissions for Subarray Product Less Than K.

idea: The number of sub intervals of [left, right] with subarray product less than k and with right-most coordinate right, is right - left + 1.
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        res = 0
        p = 1
        while r < len(nums):
            p *= nums[r]
            while l <= r and p >= k:
                p /= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res