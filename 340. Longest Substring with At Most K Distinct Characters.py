'''
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
Accepted
125,130
Submissions
288,079

'''

# 2020/05/22, sliding window

'''
Runtime: 104 ms, faster than 31.06% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Longest Substring with At Most K Distinct Characters.
'''


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        cnt = {}
        l, r = 0, 0
        ans = 0
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            while l <= r and len(cnt) > k:
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0: del cnt[s[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans
