'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


'''
We divided the search into two steps:
1. search for substrings without any repeated characters, and store the results into a list
2. search over the list to find the longest substring

983 / 983 test cases passed.
Status: Accepted
Runtime: 84 ms

The running time beats 91.58% of python 3 submissions
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = ''
        li = []
        for str1 in s:
            if str1 in str:
                li.append(str)
                str1_idx = str.find(str1)
                str = str[str1_idx + 1:len(str)] + str1
            else:
                str = str + str1
        li.append(str) # this is not a good way, but it satisfy what we need here
        max_str_num = 0
        for str2 in li:
            if len(str2) > max_str_num:
                max_str_num = len(str2)
                max_str = str2
        return max_str_num

'''
2020/03/27, sliding window

Runtime: 72 ms, faster than 44.97% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13 MB, less than 98.98% of Python3 online submissions for Longest Substring Without Repeating Characters.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l, r = 0, 0
        res = 0
        m = {}
        for r in range(len(s)):
            if s[r] not in m:
                m[s[r]] = 1
            else:
                m[s[r]] += 1
            while l <= r and m[s[r]] > 1:
                m[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res