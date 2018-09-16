'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1


'''

#401 / 401 test cases passed. Runtime: 32 ms
#Your runtime beats 29.85% python3 submissions.


class Solution(object):
    def split(self, n):
        m = 0
        while n:
            m += (n % 10) ** 2
            n = n // 10
        return m

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = self.split(n)
        if n == 1:
            return True
        cycle = []
        while True:
            n = self.split(n)
            if n == 1:
                return True
            elif n in cycle:
                return False
            else:
                cycle.append(n)

