"""
345. Reverse Vowels of a String


Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".


"""

#two pointers

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start = 0
        end = len(s) - 1
        vowels = set("aeiouAEIOU")
        while start < end:
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)

