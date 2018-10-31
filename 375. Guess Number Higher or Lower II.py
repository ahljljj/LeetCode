"""
375. Guess Number Higher or Lower II


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.


"""

# dynamic programming
# time complexity O(n^3) space complexity O(n^2)
# you are on the right strategy but your luck is really bad. You always goes the wrong choice. You can only win when
# there are no other possibilities.



class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[i][j]: the minimum cost by guessing the correct number from the interval [i, j]
        # in particular if j = i + 1, it equlas i, if j = i + 2, it return i + 1
        # since the minimum cost for a guess from i , i + 1, and i + 2 is i + 1
        dp = [[0] * (1 + n) for i in range(n + 1)]
        # iterate over the length of the interval
        # start from the length 1 interval and use the idea of dynamic progragmming to dervie the value of the next state
        for length in range(1, n):
            # i: left bound of the interval
            for i in range(1, n - length + 1):
                j = i + length # right bound of the interval
                # return the smallest number in the set if there are only two elements, all intervals are inclusive here
                dp[i][j] = float("inf")
                if length == 1:
                    dp[i][j] = i
                else:# use dynamic programming to derive the value of next state if the length > 1
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][j], max(dp[i][k - 1], dp[k + 1][j]) + k)
        return dp[1][n]