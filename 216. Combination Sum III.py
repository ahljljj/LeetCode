"""
216. Combination Sum III


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]


"""


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        self.helper(res, [], n, k, 1)
        return res

    def helper(self, res, tmp, target, k, idx):
        # edge condition
        if k == 0:
            if target == 0:
                res.append(tmp[:])
            return
        if target == 0:
            return
        for i in range(idx, min(9, target) + 1):
            tmp.append(i)
            self.helper(res, tmp, target - i, k - 1, i + 1)
            tmp.pop()


# 2021/01/31
# untime: 52 ms, faster than 8.12% of Python3 online submissions for Combination Sum III.
# Memory Usage: 14.2 MB, less than 61.29% of Python3 online submissions for Combination Sum III.

# 全子集标准模板，剪枝后得到最终子集

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(k, n, 1, ans, [])
        return ans

    def dfs(self, k, n, start, ans, subset):
        if len(subset) > k or sum(subset) > n: return
        if len(subset) == k and sum(subset) == n:
            ans.append(subset[:])
            return
        for i in range(start, 10):
            subset.append(i)
            self.dfs(k, n, i + 1, ans, subset)
            subset.pop()
