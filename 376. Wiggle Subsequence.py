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


# not correct dfs but super fast

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        self.memo = {}
        res = self.helper(nums, None, None)
        return res

    def helper(self, nums, prev, sign):
        if not nums:
            return 0
        key = (nums[0], prev, sign)
        if key in self.memo:
            return self.memo[key]
        incr, decr = 0, 0
        if sign == None:
            incr = 1 + self.helper(nums[1:], nums[0], True)
            decr = 1 + self.helper(nums[1:], nums[0], False)
            #            self.memo[key] = max(incr, decr)
            return max(incr, decr)

        if sign == True:
            tmp = -float("inf")
            for i in range(len(nums)):
                if nums[i] < prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], False))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp
        else:
            tmp = - float("inf")
            for i in range(len(nums)):
                if nums[i] > prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], True))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp


# barely accepted dfs

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        self.memo = {}
        res = self.helper(nums, 0, None, None)
        return res

    # nums: array slice, we pass the unused array to the next state every time
    # prev: previous number, we need this number in order to decide the next number
    # sign: plus if the previous difference is positive, minus otherwise
    # idx: the location of nums[0] in the original array
    # we use (idx, prev, sign) as a key to save the computed result, this will reduce a lot of repeated work
    def helper(self, nums, idx, prev, sign):
        # stopping condition
        if not nums:
            return 0
        # save the previous calculation to the memory
        key = (idx, prev, sign)
        if key in self.memo:
            return self.memo[key]
        incr, decr = 0, 0
        # initial condition, the -1'th element could be infty or -infty, we choose the better of the two
        if sign == None:
            incr = 1 + self.helper(nums[1:], 1, nums[0], True)
            decr = 1 + self.helper(nums[1:], 1, nums[0], False)
            return max(incr, decr)
        # if the previous difference is positive, the next number must less than the previous number
        if sign == True:
            tmp = -float("inf")
            for i in range(len(nums)):
                if nums[i] < prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], idx + i + 1, nums[i], False))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp
        # if the previous difference is negative, the next number must greater than the previous number
        else:
            tmp = - float("inf")
            for i in range(len(nums)):
                if nums[i] > prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], idx + i + 1, nums[i], True))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp


# dynamic programming
# time complexity O(n) space complexity O(n)

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        up, down = [1] * len(nums), [1] * len(nums)
        for i in  range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], 1 + down[i - 1])
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = max(down[i - 1], 1 + up[i - 1])
                up[i] = up[i - 1]
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(up[-1], down[-1])

# dynamic programming
# time complexity O(n^2)

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        up, down = [1] * len(nums), [1] * len(nums)
        for i in  range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], 1 + down[j])
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], 1 + up[j])
 #               else:
 #                   up[i] = up[i - 1]
 #                   down[i] = down[i - 1]
        return max(up[-1], down[-1])