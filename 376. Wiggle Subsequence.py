"""
376. Wiggle Subsequence


A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?

"""

# dfs time limit exceeded


class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        res = self.helper(nums, None, None)
        return res

    def helper(self, nums, prev, sign):
        if not nums:
            return 0
        incr, decr = 0, 0
        if prev == None:
            incr = 1 + self.helper(nums[1:], nums[0], True)
            decr = 1 + self.helper(nums[1:], nums[0], False)
            return max(incr, decr)

        if sign == True:
            tmp = -float("inf")
            for i in range(len(nums)):
                if nums[i] < prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], False))
            return tmp if tmp != -float("inf") else 0
        else:
            tmp = - float("inf")
            for i in range(len(nums)):
                if nums[i] > prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], True))
            return tmp if tmp != -float("inf") else 0