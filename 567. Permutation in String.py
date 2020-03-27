'''
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].


2020/03/27, sliding window

Runtime: 76 ms, faster than 54.67% of Python3 online submissions for Permutation in String.
Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Permutation in String.


'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        l, r = 0, 0
        m1 = {}
        for s in s1:
            if s not in m1:
                m1[s] = 1
            else:
                m1[s] += 1
        m2 = {}
        for r in range(len(s2)):
            if s2[r] not in m2:
                m2[s2[r]] = 1
            else:
                m2[s2[r]] += 1
            while l <= r and (s2[r] not in m1 or m1[s2[r]] < m2[s2[r]]):
                m2[s2[l]] -= 1
                if m2[s2[l]] == 0: del m2[s2[l]]
                l += 1
            if m1 == m2: return True
        return False