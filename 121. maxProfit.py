'''

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

'''

'''
solution 1, 2 time limit exceed

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nb = len(prices)
        maxprice = 0
        for i in range(nb - 1):
            temp = max(prices[i + 1:nb]) - prices[i]
            if temp > maxprice:
                maxprice = temp
        return maxprice


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nb = len(prices)
        maxprice = 0
        for i in range(nb):
            for j in range(i+1,nb):
                temp=prices[j]-prices[i]
                if temp>maxprice:
                    maxprice=temp
        return maxprice
'''

#200 / 200 test cases passed. Runtime: 40 ms
# your runtime beats 100% of python 3 submissions.

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nb = len(prices)
        maxprofit = 0
        minprice=float('Inf')
        for i in range(nb):
            if prices[i]<minprice:
                minprice=prices[i]
            elif prices[i]-minprice>maxprofit:
                maxprofit=prices[i]-minprice
        return maxprofit


# cpp, dp
'''
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) return 0;
        int res = 0, prevMin = prices[0];
        for (int i = 1; i < prices.size(); ++i) {
            res = max(res, prices[i] - prevMin);
            prevMin = min(prices[i], prevMin);
        }
        return res;
        
    }
};

'''

# 2020/05/05, dp

'''
Runtime: 72 ms, faster than 26.78% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 15.1 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_min = float("inf")
        for i in range(1, len(prices)):
            curr_min = min(curr_min, prices[i - 1])
            res = max(res, prices[i] - curr_min)
        return res

