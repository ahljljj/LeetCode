'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

#59 / 59 test cases passed. Runtime: 36 ms
#This running time beats 96.86& of python 3 submissins. May 2018

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n==0:
            return 0
        idx=n-1
        while idx>=0 and s[idx]==' ':
            idx-=1
        i=0
        j=idx
        while j>=0 and s[j]!=' ':
            i+=1
            j-=1
        return i