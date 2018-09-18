"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]


"""

'''
not correct


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(res, [], s, 0)
        return res

    def is_valid(self, s):
        return s == s[::-1]

    def helper(self, res, tmp, s, idx):
        if idx > len(s) - 1: return
        for i in range(idx, len(s)):
            for j in range(len(s) - i):
                if self.is_valid(s[i: i + j + 1]):
                    tmp.append(s[i: i + j + 1])
                    if i + j + 1 == len(s):
                        res.append(tmp[:])
                        return
                    self.helper(res, tmp, s, i + j + 1)
'''