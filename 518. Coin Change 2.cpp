/*
518. Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.



Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer

*/

// cpp, dynamic programming

/*
This is a classic knapsack problem. Honestly, I'm not good at knapsack problem, it's really tough for me.

dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
State transition:

not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
Initialization: dp[i][0] = 1
*/

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<vector<int>> dp(coins.size() + 1, vector<int>(amount + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= coins.size(); ++i){
            dp[i][0] = 1;
            for (int j = 1; j <= amount; ++j){
                dp[i][j] = dp[i - 1][j] + (j >= coins[i - 1] ? dp[i][j - coins[i - 1]]: 0);
            }
        }
        return dp[coins.size()][amount];

    }
};


/*
# 2020/04/16， DFS + memo, barely AC

Runtime: 1988 ms, faster than 7.36% of Python3 online submissions for Coin Change 2.
Memory Usage: 37.3 MB, less than 16.67% of Python3 online submissions for Coin Change 2.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        coins.sort()
        self.dfs(coins, amount, 0, 0, memo)
        return memo[(0,0)]

    def dfs(self, coins, target, current, pos, memo):
        if (current, pos) in memo: return memo[(current, pos)]
        if current > target:
            memo[(current, pos)] = 0
            return memo[(current, pos)]
        if current == target:
            memo[(current, pos)] = 1
            return memo[(current, pos)]
        calculation = 0
        for i in range(pos, len(coins)):
            if current + coins[i] > target: break
            calculation += self.dfs(coins, target, current + coins[i], i, memo)
        memo[(current, pos)] = calculation
        return memo[(current, pos)]


*/