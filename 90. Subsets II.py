"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]


"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        self.helper(res, [], nums, 0)
        res.append([])
        return res

    def helper(self, res, tmp, nums, idx):
        for i in range(idx, len(nums)):
            tmp.append(nums[i])
            if tmp not in res: res.append(tmp[:])
            self.helper(res, tmp, nums, i + 1)
            tmp.pop()
