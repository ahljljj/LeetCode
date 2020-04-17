'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Accepted
123,869
Submissions
419,012

'''


# 2020/04/17, memoization

'''
Runtime: 992 ms, faster than 9.85% of Python3 online submissions for Palindrome Partitioning II.
Memory Usage: 15.2 MB, less than 90.00% of Python3 online submissions for Palindrome Partitioning II.
'''


class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        self.dfs(s, 0, memo)
        return memo[0]

    def dfs(self, source, pos, memo):
        if pos in memo: return memo[pos]
        if pos == len(source):
            memo[pos] = -1
            return memo[pos]
        res = float("inf")
        for i in range(pos, len(source)):
            prefix = source[pos: i + 1]
            if not self.is_valid(prefix): continue
            res = min(res, 1 + self.dfs(source, i + 1, memo))
        memo[pos] = res
        return memo[pos]

    def is_valid(self, s):
        return s == s[::-1]
