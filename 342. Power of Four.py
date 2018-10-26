"""
342. Power of Four


Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?



"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        return num > 3 and math.log(num, 4) % 1 == 0

#another one

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        while num > 1:
            count += 1
            if num & 1:
                return False
            num >>= 1
        return num > 0 and count % 2 == 0

# clever one
# the (num - 1) % 3 == 0 is used to distinguish the 4^n from 2^n.


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0