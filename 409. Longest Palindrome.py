"""
409. Longest Palindrome


Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""

# hashmap


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        odd = False
        res = 0
        for key in dic:
            if dic[key] % 2 == 1:
                if odd:
                    res += dic[key] - 1
                else:
                    res += dic[key]
                    odd = True
            else:
                res += dic[key]
        return res

# brief modify

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        odd = False
        res = 0
        for key in dic:
            if dic[key] % 2 == 1:
                if odd:
                    res -= 1
                else:
                    odd = True
            res += dic[key]
        return res