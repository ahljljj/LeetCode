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

# 2020/04/16, subsets

'''
Runtime: 100 ms, faster than 37.42% of Python3 online submissions for Combination Sum II.
Memory Usage: 13.6 MB, less than 6.52% of Python3 online submissions for Combination Sum II.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, [], 0)
        return res

    def dfs(self, candidates, target, subsets, subset, pos):
        if target == 0:
            subsets.append(subset[:])
            return
        if pos == len(candidates) or target < 0: return
        for i in range(pos, len(candidates)):
            if i > pos and candidates[i] == candidates[i - 1]: continue
            subset.append(candidates[i])
            self.dfs(candidates, target - candidates[i], subsets, subset, i + 1)
            subset.pop()