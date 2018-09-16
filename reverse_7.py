'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

#1032 / 1032 test cases passed. Runtime: 60 ms

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_r=0
        temp=x
        x=abs(x)
        while x:
            y=x%10
            x=x//10
            x_r=(x_r+y)*10
        x_r=x_r//10
        if x_r> 2**31-1:
            return 0
        if temp<0:
            return -x_r
        else:
            return x_r