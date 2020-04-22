'''
291. Word Pattern II

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.



Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false


Constraints:

You may assume both pattern and str contains only lowercase letters.
Accepted
42,102
Submissions
98,043

'''


'''
2020/04/21, DFS

Runtime: 216 ms, faster than 47.34% of Python3 online submissions for Word Pattern II.
Memory Usage: 13.6 MB, less than 33.33% of Python3 online submissions for Word Pattern II.

'''


class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        m = {}
        res = self.dfs(pattern, 0, str, 0, m, set())
        return res

    def dfs(self, pattern, i, source, j, m, used):
        if i == len(pattern):
            return j == len(source)
        p = pattern[i]
        if p in m:
            prefix = source[j: j + len(m[p])]
            if m[p] != prefix: return False
            return self.dfs(pattern, i + 1, source, j + len(m[p]), m, used)
        for k in range(j, len(source)):
            prefix = source[j: k + 1]
            if prefix in used: continue
            used.add(prefix)
            m[p] = prefix
            if self.dfs(pattern, i + 1, source, k + 1, m, used):
                return True
            del m[p]
            used.remove(prefix)
        return False
