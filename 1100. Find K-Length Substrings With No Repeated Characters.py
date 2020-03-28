'''
1100. Find K-Length Substrings With No Repeated Characters

Given a string S, return the number of substrings of length K with no repeated characters.



Example 1:

Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation:
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: S = "home", K = 5
Output: 0
Explanation:
Notice K can be larger than the length of S. In this case is not possible to find any substring.


Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4
Accepted
7,919
Submissions
11,088


2020/03/28, sliding window

Runtime: 52 ms, faster than 51.60% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.
Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Find K-Length Substrings With No Repeated Characters.


'''


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        l, r = 0, 0
        res = 0
        m = {}
        for r in range(len(S)):
            if S[r] not in m:
                m[S[r]] = 1
            else:
                m[S[r]] += 1
            while l <= r and (len(m) > K or m[S[r]] > 1):
                m[S[l]] -= 1
                if m[S[l]] == 0: del m[S[l]]
                l += 1
            if len(m) == K: res += 1
        return res
