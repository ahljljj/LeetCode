"""
416. Partition Equal Subset Sum


Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.


"""

# brute force (tle): try all possible situations


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        mean = total / 2

        return self.helper(nums, mean, 0)

    def helper(self, nums, target, idx):
        if target == 0:
            return True
        for i in range(idx, len(nums)):
            if target >= nums[i] and self.helper(nums, target - nums[i], i + 1):
                return True
        return False


# dfs + memorization (AC)
# a little bit tricky here

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 == 1:
            return False
        mean = total / 2
        nums.sort()
        if nums[-1] > mean:
            return False
        self.memo = {}
        return self.helper(nums, mean, 0)

    def helper(self, nums, target, idx):
        if (target, idx) in self.memo:
            return self.memo[(target, idx)]
        if target == 0:
            return True
        for i in range(idx, len(nums)):
            if target >= nums[i] and self.helper(nums, target - nums[i], i + 1):
                self.memo[(target, idx)] = True
                return True
            elif target < nums[i]:
                self.memo[(target, idx)] = False
                return False
        self.memo[(target, idx)] = False
        return False

# dynamic programming: tle on python 3 AC on python 2 but ridiculous slow

'''
intuition

This problem is essentially let us to find whether there are several numbers in a set which are able to sum to a specific value (in this problem, the value is sum/2).

Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not. Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers. If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.

Base case: dp[0][0] is true; (zero number consists of sum 0 is true)

Transition function: For each number, if we don't pick it, dp[i][j] = dp[i-1][j], which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j (we can just ignore nums[i]). If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]], which represents that j is composed of the current value nums[i] and the remaining composed of other previous numbers. Thus, the transition function is dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

'''

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total & 1:
            return False
        mean = total // 2
        dp = [[False] * (1 + mean) for i in range(1 + len(nums))]

        for i in range(1, 1 + len(nums)):
            if nums[i - 1] > mean:
                return False
            dp[i][nums[i - 1]] = True
            for j in reversed(range(1, mean + 1)): # donot need reverse
                if dp[i][j]:
                    continue
                dp[i][j] |= dp[i - 1][j]
                if j > nums[i - 1]:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]
        return dp[-1][mean]



