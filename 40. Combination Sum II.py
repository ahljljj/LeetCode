"""
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]


"""

# not my idea

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def helper(nums, tmp, target, idx):
            if target < 0:
                return
            if target == 0:
                res.append(tmp[:])
                return
            i = idx
            while i >= idx and i < len(nums):
                tmp.append(nums[i])
                helper(nums, tmp, target - nums[i], i+1)
                tmp.pop()
                while i < len(nums) - 1 and nums[i] == nums[i+1]:
                    i += 1
                i += 1
        helper(candidates, [], target, 0)
        return res