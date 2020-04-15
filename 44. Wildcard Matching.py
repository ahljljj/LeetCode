'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
Accepted
228,395
Submissions
943,459

'''

# 2020/04/15, memoization, too hard

'''
Runtime: 832 ms, faster than 51.16% of Python3 online submissions for Wildcard Matching.
Memory Usage: 93.4 MB, less than 41.67% of Python3 online submissions for Wildcard Matching.
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        self.dfs(s, 0, p, 0, memo)
        return memo[(0, 0)]

    def dfs(self, string, i, pattern, j, memo):
        if (i, j) in memo: return memo[(i, j)]
        if i >= len(string):
            for k in range(j, len(pattern)):
                if pattern[k] != '*':
                    memo[(i, j)] = False
                    return False
            memo[(i, j)] = True
            return memo[(i, j)]
        if j >= len(pattern):
            memo[(i, j)] = False
            return memo[(i, j)]
        if pattern[j] != '*':
            memo[(i, j)] = self.is_valid(string[i], pattern[j]) \
                           and self.dfs(string, i + 1, pattern, j + 1, memo)
        else:
            memo[(i, j)] = self.dfs(string, i + 1, pattern, j, memo) \
                           or self.dfs(string, i, pattern, j + 1, memo)
        return memo[(i, j)]

    def is_valid(self, s, p):
        return s == p or p == '?'
