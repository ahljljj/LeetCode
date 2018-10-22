"""
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]


"""

'''
intuition

Sharing my thought. We have three status, which are sell, buy, and cooldown. For this series of stock problem, key point is to figure out status transition function.
In this case, we have to buy before selling, the previous status of buy operation should be cooldown. Based on this, the code is self explaining. (buy[i] is the maximum benefit we can get at position i if the last operation is buying)

'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # three states: buy, cool, and sell
        # buy -> hold/cool -> ... -> hold/cool -> sell -> cool -> .... -> cool -> buy
        # suppose we have infinite amount of money, we can buy anything, we are interested in the maximal profit

        if not prices:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        cool = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            cool[i] = max(cool[i - 1], sell[i - 1])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], cool[i - 1] - prices[i])
        return sell[-1]

