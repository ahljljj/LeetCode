'''
159. Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

2020/03/27, sliding window

Runtime: 60 ms, faster than 44.82% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
Memory Usage: 14.1 MB, less than 50.00% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.

'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        m = {}
        for r in range(len(s)):
            if s[r] not in m:
                m[s[r]] = 1
            else:
                m[s[r]] += 1
            while l < r and len(m) > 2:
                m[s[l]] -= 1
                if m[s[l]] == 0: del m[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res