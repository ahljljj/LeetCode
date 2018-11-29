"""
459. Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.



Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


"""

# brute force
# time complexity O(nlgn)

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        find = True
        for i in range(1, len(s) // 2 + 1):
            tmp = s[:i]
            j = i
            while j + len(tmp) < len(s) + 1:
                if s[j: j + len(tmp)] != tmp:
                    find = False
                    break
                j += len(tmp)
            if j == len(s) and find:
                return True
            find = True
        return False


# kmp algorithm
'''
First, we build the KMP table.

Roughly speaking, dp[i+1] stores the maximum number of characters that the string is repeating itself up to position i.
Therefore, if a string repeats a length 5 substring 4 times, then the last entry would be of value 15.
To check if the string is repeating itself, we just need the last entry to be non-zero and str.size() to divide (str.size()-last entry).

'''


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        kmp = [0] * (n + 1)
        i, j = 1, 0
        while i < n:
            if s[i] == s[j]:
                j += 1
                i += 1
                kmp[i] = j
            elif j == 0:
                i += 1
            else:
                j = kmp[j]
        res = kmp[n] and kmp[n] % (len(s) - kmp[n]) == 0
        return res == 1
