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
            
# OR

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
        if idx >= self.res:
            return
        if n == (int(math.sqrt(n)))**2:
            if idx + 1 < self.res:
                self.res = idx + 1
            return
        for i in range((int(math.sqrt(n))), 0, -1):
            self.helper(n -  i**2, idx + 1)
'''


#BFS
#time/space complicity: O(log(n)) similar to binary tree???

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # current level
        queue = [n]
        squares = []
        i = 1
        while i**2 <= n:
            squares.append(i ** 2)
            i += 1
        level = 0
        while queue:
            level += 1
            tmp = set()
            # split the current level to get the next level
            for x in queue:
                for y in squares:
                    if x == y:
                        return level
                    if x < y:
                        break
                    tmp.add(x - y)
            queue = tmp


'''

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = []
        dp = [float("inf")] *(n + 1)
        i = 1
        while i**2 <= n:
            squares.append(i ** 2)
            dp[i**2] = 1
            i += 1
        for i in range(2, n + 1):
            if dp[i] < float("inf"): continue
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], 1 + dp[i - square])
        return dp[-1]


'''