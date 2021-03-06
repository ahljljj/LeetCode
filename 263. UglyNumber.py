'''
263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].


'''




#36 ms 11.9%










class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <=0:
            return False
        if num % 2  and num % 3 and num % 5:
            return False
        if num % 2 ==0:
            return self.isUgly(num/2)
        if num % 3 ==0:
            return self.isUgly(num/3)
        if num % 5 ==0:
            return self.isUgly(num/5)

'''
# simpler solution

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num /= x
        return num == 1
'''