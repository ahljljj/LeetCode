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
time limit exceeded


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
        if idx == len(s)  and ''.join(tmp) == s:
            res.append(tmp[:])
            return
        for i in range(idx, len(s)):
            for j in range(len(s) - i):
                if self.is_valid(s[i: i + j + 1]):
                    tmp.append(s[i: i + j + 1])
                    self.helper(res, tmp, s, i + j + 1)
                    tmp.pop()
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(res, [], s)
        return res

    def is_valid(self, s):
        return s == s[::-1]

    def helper(self, res, tmp, s):
        if not s:
            res.append(tmp[:])
            return
        for i in range(1, len(s) + 1):
            if self.is_valid(s[:i]):
                tmp.append(s[:i])
                self.helper(res, tmp, s[i:])
                tmp.pop()
