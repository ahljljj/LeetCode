
"""

397. Integer Replacement


Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1



"""


# math

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            count += 1
            if n % 2 == 0:
                n //= 2
            else:
                if (n + 1) % 4 == 0 and n > 3:
                    n += 1
                else:
                    n -= 1
        return count


# recursive solution

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))


# fast recursion: memorization

class Solution:
    def __init__(self):
        self.memo = {}

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return 0
        if n % 2 == 0:
            tmp = self.integerReplacement(n // 2) + 1
        else:
            tmp = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        self.memo[n] = tmp
        return tmp

