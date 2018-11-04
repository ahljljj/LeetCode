"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.


"""

#hashmap


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        for i, ch in enumerate(s):
            if hashmap[ch] == 1:
                return i
        return -1

