"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]


"""

'''
time limit exceeded

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def pow(x,n):
            tmp = x
            for i in range(n-1):
                tmp *= x
            return tmp
        if n > 0:
            return min(pow(x,n), 2**31-1)
        elif n < 0:
            return 1/pow(x,-n)
        else:
            return 1

'''

#recursive

class Solution:
        def myPow(self, x, n):
                """
                :type x: float
                :type n: int
                :rtype: float
                """
                sign = 1
                if n < 0:
                        n = - n
                        sign = 0
                return self.power(x, n) if sign == 1 else 1. / self.power(x, n)

        def power(self, x, n):
                if n == 0:
                        return 1
                if n == 1:
                        return x
                if n % 2 == 1:
                        return x * self.power(x * x, n // 2)
                else:
                        return self.power(x * x, n // 2)

#iteration

class Solution:
        def myPow(self, x, n):
                """
                :type x: float
                :type n: int
                :rtype: float
                """
                sign = 1
                if n < 0:
                        n = -n
                        sign = -1
                return self.power(x, n) if sign == 1 else 1.0 / self.power(x, n)

        def power(self, x, n):
                if n == 0:
                        return 1
                if n == 1:
                        return x
                res = 1
                num = x
                while n > 1:
                        if n % 2 == 1:
                                res *= num
                        num *= num
                        n //= 2
                return res * num


# python, rewrite

class Solution:
        def myPow(self, x, n):
                """
                :type x: float
                :type n: int
                :rtype: float
                """
                if n == 0: return 1
                if n > 0:
                        return self.pow(x, n)
                else:
                        return self.npow(x, n)

        def pow(self, x, n):
                if n == 1:
                        return x
                if n % 2 == 0:
                        return self.pow(x, n // 2) ** 2
                else:
                        return x * self.pow(x, n // 2) ** 2

        def npow(self, x, n):
                if n == -1:
                        return 1.0 / x
                if n % 2 == 0:
                        return self.npow(x, n // 2) ** 2
                else:
                        return 1 / x * self.npow(x, n // 2 + 1) ** 2