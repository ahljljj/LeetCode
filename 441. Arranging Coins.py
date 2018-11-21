"""
441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.


"""

# binary search

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.bisearch(n)

    def bisearch(self, n):
        left, right = 1, n + 1 # the right has to be one in order to pass the n = 1 case
        while left < right:
            mid = (left + right) >> 1
            if mid * (mid + 1) >> 1 > n:
                right = mid
            else:
                left = mid + 1
        return left - 1

# newton method
# f(x) = x(x + 1)/2 -n and f'(x) = x + 1/2
# iteration formula: x_n+1 = x_n - (x_n^2 + x^n - 2*n)/(2*x + 1)

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.newton(n)

    def newton(self, n):
        curr = n + 1
        while n < curr * (curr + 1) >> 1:
            update = (curr ** 2 + curr - 2 * n) // (2 * curr + 1)
            if update > 0:
                curr = curr - update
            else:
                return curr - 1
    # modified newton method

    class Solution:
        def arrangeCoins(self, n):
            """
            :type n: int
            :rtype: int
            """
            return self.newton(n)

        def newton(self, n):
            curr = n + 1
            update = (curr ** 2 + curr - 2 * n) // (2 * curr + 1)
            while update:
                curr = curr - update
                update = (curr ** 2 + curr - 2 * n) // (2 * curr + 1)
            return curr - 1



