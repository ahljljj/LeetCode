'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
Accepted
402,714
Submissions
1,527,990

'''

# 2020/04/15, memoization, too hard

'''
Runtime: 40 ms, faster than 86.27% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 13.7 MB, less than 5.55% of Python3 online submissions for Regular Expression Matching.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        self.dfs(s, 0, p, 0, memo)
        return memo[(0, 0)]

    def dfs(self, source, i, pattern, j, memo):
        if (i, j) in memo: return memo[(i, j)]
        if i >= len(source):
            memo[(i, j)] = self.is_empty(pattern[j:])
            return memo[(i, j)]
        if j >= len(pattern):
            memo[(i, j)] = False
            return False
        if j + 1 < len(pattern) and pattern[j + 1] == '*':
            memo[(i, j)] = self.dfs(source, i, pattern, j + 2, memo) \
                           or (self.is_valid(source[i], pattern[j]) and self.dfs(source, i + 1, pattern, j, memo))
        else:
            memo[(i, j)] = self.is_valid(source[i], pattern[j]) and \
                           self.dfs(source, i + 1, pattern, j + 1, memo)
        return memo[(i, j)]

    def is_valid(self, s, p):
        return s == p or p == '.'

    def is_empty(self, p):
        if len(p) % 2 == 1: return False
        for i in range(len(p) // 2):
            if p[2 * i + 1] != '*':
                return False
        return True
