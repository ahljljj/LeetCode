"""
300. Longest Increasing Subsequence


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


"""

# dynamic programming: time complexity: O(n^2), space complexity: O(n)

'''
intuition

This method relies on the fact that the longest increasing subsequence possible upto the i 
th index in a given array is independent of the elements coming later on in the array. Thus, if we know the length of the LIS upto i 
th index, we can figure out the length of the LIS possible by including the (i+1) th
  element based on the elements with indices j such that 0 \leq j \leq (i + 1).

We make use of a dp array to store the required data. dp[i] represents the length of the longest increasing subsequence possible considering the array elements upto the ith index only ,by necessarily including the ith
 element. In order to find out dp[i], we need to try to append the current element(nums[i]) in every possible increasing subsequences upto the (i−1)th index(including the (i−1)th index), such that the new sequence formed by adding the current element is also an increasing subsequence. Thus, we can easily determine dp[i]dp[i] using:

dp[i] = max(dp[j]) + 1, forall 0\leq j 

At the end, the maximum out of all the dp[i]'s to determine the final result.

LIS_{length}= text{max}(dp[i]), forall 0\leq i 	
'''


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res