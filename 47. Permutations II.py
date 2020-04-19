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

# 2020/04/19, permutations + reduce duplicates

'''
Runtime: 60 ms, faster than 50.82% of Python3 online submissions for Permutations II.
Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Permutations II.
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = [False] * len(nums)
        nums.sort()
        self.dfs(nums, res, [], visited)
        return res

    def dfs(self, nums, result, permutation, visited):
        if len(permutation) == len(nums):
            result.append(permutation[:])
        for i in range(len(nums)):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            permutation.append(nums[i])
            self.dfs(nums, result, permutation, visited)
            permutation.pop()
            visited[i] = False