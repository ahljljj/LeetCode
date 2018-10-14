"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

'''
# wrong solution

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.helper(n)
        return self.res
    
    def helper(self, n):
        if n == (int(math.sqrt(n)))**2:
            self.res += 1
            return
        self.res += 1
        self.helper(n -  (int(math.sqrt(n)))**2)



'''

'''
# dfs: time limit exceeded

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = float("inf")
        self.helper(n, 0)
        return self.res
    
    def helper(self, n, idx):
        if n == 0:
            if idx < self.res:
                self.res = idx
            return
        for i in range(1, 1 + int(math.sqrt(n))):
            self.helper(n - i**2, idx + 1)
'''