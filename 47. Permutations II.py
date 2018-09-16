"""
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]



"""


#not my idea

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False] * len(nums)
        nums.sort()

        def dfs(nums, tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]: continue
                used[i] = True
                tmp.append(nums[i])
                dfs(nums, tmp)
                used[i] = False
                tmp.pop()

        dfs(nums, [])
        return res
