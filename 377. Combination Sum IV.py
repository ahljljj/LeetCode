"""
377. Combination Sum IV


Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?


In order to allow negative numbers, the size of the sequence must have a upperbound. Otherwise the result will INF.


"""
# the Memoization is always worse than DP in performance but better in readability.





# dfs tle
# global count

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = set(nums)
        self.count = 0
        self.helper(target)
        return self.count

    def helper(self, target):
        # edge case
        if target == 0:
            self.count += 1
            return
        for i in self.nums:
            if i <= target:
                self.helper(target - i)

# dfs tle local count

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = set(nums)
        return self.helper(target)

    def helper(self, target):
        # edge case
        if target == 0:
            return 1
        if target < 0:
            return -1
        count = 0
        for i in self.nums:
            tmp = self.helper(target - i)
            if tmp >= 0:
                count += tmp
        return count


# fast recursive: memory trick
# extra space


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = set(nums)
        self.memo = {}
        return self.helper(target)

    def helper(self, target):
        if target in self.memo:
            return self.memo[target]
        # edge case
        if target == 0:
            return 1
        count = 0
        for i in self.nums:
            if target >= i:
                count += self.helper(target - i)
        self.memo[target] = count
        return count


# dp time complextiy O(n^2)


'''
intuition

Think about the recurrence relation first. How does the # of combinations of the target related to the # of combinations of numbers that are smaller than the target?

So we know that target is the sum of numbers in the array. Imagine we only need one more number to reach target, this number can be any one in the array, right? So the # of combinations of target, comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].

In the example given, we can actually find the # of combinations of 4 with the # of combinations of 3(4 - 1), 2(4- 2) and 1(4 - 3). As a result, comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].

Then think about the base case. Since if the target is 0, there is only one way to get zero, which is using 0, we can set comb[0] = 1.

EDIT: The problem says that target is a positive integer that makes me feel it's unclear to put it in the above way. Since target == 0 only happens when in the previous call, target = nums[i], we know that this is the only combination in this case, so we return 1.
'''

class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[target]




