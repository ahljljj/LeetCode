'''
698. Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.


Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
Accepted
77,884
Submissions
174,085

'''


# 2020/05/16, dp, similar to permutations, too hard


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k: return False
        side = total_sum // k
        nums.sort(reverse=True)
        visited = [False] * len(nums)

        return self.dfs(nums, 0, k, side, 0, visited)

    def dfs(self, nums, pos, k, side, path_sum, visited):
        if k == 1:
            return True
        if side == path_sum:
            return self.dfs(nums, 0, k - 1, side, 0, visited)
        for i in range(pos, len(nums)):
            if visited[i]: continue
            visited[i] = True
            if self.dfs(nums, i + 1, k, side, path_sum + nums[i], visited):
                return True
            visited[i] = False
        return False




