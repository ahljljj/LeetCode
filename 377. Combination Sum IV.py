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

"""

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


