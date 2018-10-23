"""
322. Coin Change


You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


"""


'''
# dynamic programming: TLE
# use too much step to get the final answer


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        for i in range(1, amount + 1):
            tmp = float("inf")
            if i in coins:
                dp[i] = 1
                continue
            for coin in coins:
                if i - coin >= 1:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[-1] if dp[-1] != float("inf") else -1
        
        
# bfs: another TLE

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        queue = set([amount])
        step = 0
        while queue:
            tmp = set()
            step += 1
            for i in queue:
                for coin in coins:
                    if i == coin:
                        return step
                    elif i > coin:
                        tmp.add(i - coin)
            queue = tmp
        return -1
                        
        
'''