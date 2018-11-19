"""
424. Longest Repeating Character Replacement


Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.



"""

# sliding window

'''
The problem says that we can make at most k changes to the string (any character can be replaced with any other character). So, let's say there were no constraints like the k. Given a string convert it to a string with all same characters with minimal changes. The answer to this is

length of the entire string - number of times of the maximum occurring character in the string

Given this, we can apply the at most k changes constraint and maintain a sliding window such that

(length of substring - number of times of the maximum occurring character in the substring) <= k

'''

class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = end = 0
        currmax = 0
        res = 0
        count = {}
        for end in range(len(s)):
            # update the occurance of the curent letter in this window
            count[s[end]] = count.get(s[end], 0) + 1
            # update the maximal occurance of some letter in this window, similar to dynamic grogramming
            currmax = max(currmax, count[s[end]])
            if end - start + 1 - currmax > k:
                # shift right if without enough replacement
                # then update the occurance of the beginning letter
                count[s[start]] -= 1
                # new window
                start += 1
            res = max(res, end - start + 1)
        return res

