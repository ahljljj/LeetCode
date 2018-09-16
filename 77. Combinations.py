"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], n, k, 0)
        return res

    def helper(self, res, tmp, n, k, start):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(start, n):
            tmp.append(i + 1)
            self.helper(res, tmp, n, k - 1, i + 1)
            tmp.pop()