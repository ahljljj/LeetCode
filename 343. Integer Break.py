"""
343. Integer Break


Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.


"""

# a simple way

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] *(n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, n//2 +2):
                tmp = max([dp[j] * dp[i - j], j * (i - j), j * dp[i - j]])
                if tmp > dp[i]:
                    dp[i] = tmp
        return dp[-1]


# simplified one

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] *(n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, n//2 +2):
                # j * (i - j) is used to classify the situation when j = 2 and j - j = 2
                tmp = max(j, dp[j]) * max(i - j, dp[i - j])
                dp[i] = max(tmp, dp[i])
        return dp[-1]