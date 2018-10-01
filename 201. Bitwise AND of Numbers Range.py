"""
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0


"""

'''
#bruteforce

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = m
        for j in xrange(m+1, n+1):
            if res == 0:
                return res
            res = res & j
        return res
        

'''


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0: return 0

        if 2 * m > n:
            res = m
            for i in xrange(m + 1, n + 1):
                if res == 0: return 0
                res = res & i
            return res
        else:
            return 0

