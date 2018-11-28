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
