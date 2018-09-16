'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''


#476 / 476 test cases passed. Runtime: 92 ms
# Your runtime beats 14.91% of py3 submissions.

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news = ''
        for s1 in s:
            if s1 >= 'a' and s1 <= 'z':
                news += s1
            elif s1 >= 'A' and s1 <= 'Z':
                news += s1.lower()
            elif s1 >= '0' and s1 <= '9':
                news += s1
        if news == news[::-1]:
            return True
        else:
            return False
