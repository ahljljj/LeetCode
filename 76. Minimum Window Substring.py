'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
Accepted
373,854
Submissions
1,098,766

'''


# 2020/05/22, sliding window, too hard

'''
Runtime: 152 ms, faster than 38.52% of Python3 online submissions for Minimum Window Substring.
Memory Usage: 14.3 MB, less than 5.55% of Python3 online submissions for Minimum Window Substring.
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        key_s, key_t = {}, {}
        for ch in t:
            key_t[ch] = key_t.get(ch, 0) + 1
        l, r = 0, 0
        res_l, res_r = -float("inf"), float("inf")
        formed, required = 0, len(key_t)
        for r in range(len(s)):
            key_s[s[r]] = key_s.get(s[r], 0) + 1
            if s[r] in key_t and key_s[s[r]] == key_t[s[r]]:
                formed += 1
            while l <= r and formed == required:
                kick = s[l]
                if r - l < res_r - res_l:
                    res_r, res_l = r, l
                key_s[kick] -= 1
                if kick in key_t and key_s[kick] < key_t[kick]:
                    formed -= 1
                l += 1
        return s[res_l:res_r + 1] if res_r < float("inf") else ""



