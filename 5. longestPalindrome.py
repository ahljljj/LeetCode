'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

''' running time error: 83 / 94 test cases passed.
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        li=[]
        for i in range(len(s)-1):
            str=s[i]
            for s0 in s[i+1:len(s)]:
                if s0 in str:
                    s0_pos=str.find(s0)
                    str_temp=str[s0_pos:len(str)]+s0
                    if str_temp==str_temp[::-1]:
                        li.append(str_temp)
                str=str+s0
        max_num=1
        max_str=''
        for i in range(len(li)):
            if len(li[i])>max_num:
                max_num=len(li[i])
                max_str=li[i]
        if max_num>1:
            return max_str
        else:
            return s[0]
'''


# passed, not my idea

class Solution:
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res
