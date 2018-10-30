"""
367. Valid Perfect Square


Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

# binary search O(lgn)

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        left, right = 2, num
        while left <= right:
            mid = (left + right)//2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

# math: time complexity O(root(n))
# idea: 1 + 3 + ... + (2k - 1) = k^2
# every perfect square can be written in the above form

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        res = i
        while i:
            if res == num:
                return True
            elif res > num:
                return False
            i += 2


            res += i


# newton's method time complexity: O(0.5ln(n)) faster than binary search
# f(x) = f'(xn)(x - xn) + f(xn)  ----> = 0
# x(n+1) = x(n) - f(xn)/f'(xn) = 0.5(x + n/x)
# n/2^k > n^0.5 ---> 2^k < n^0.5---> k < 0.5lg(n)


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while (x **2 > num):
            x = (x + num // x)>>1
        return num == x**2