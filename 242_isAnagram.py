'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


#52md 57.98%


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) - len(t):
            return False

        ds = {}
        dt = {}
        for (ss, tt) in zip(s, t):
            if ss not in ds:
                ds[ss] = 1
            else:
                ds[ss] += 1
            if tt not in dt:
                dt[tt] = 1
            else:
                dt[tt] += 1
        return ds == dt
