"""
464. Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.


"""

# dfs with memorization

'''
Top Down DFS with Memoization: Time: O(N * 2^N). Space: O(2^N)

We create an array allowed which has all the integers from 1 to maxChoosableInteger.
We test if the input is valid or not i.e. sum(allowed) >= desiredTotal.
How do we define the state of the game? This answer determines how we will do memoization as well. Clearly list of current allowed numbers are needed to define the state. It might also look that so_far is also required to define the state. However, given all allowed values and the current set of allowed values, so_far is really the difference of the sum of the two. Therefore only allowed values uniquely determine the state.
How many allowed values sets are possible? The length of the allowed value set can range 1 to maxChoosableInteger(N). So the answer is (N,1) + (N,2) + ..(N,N) where (N,K) means choose K from N. This is equal to 2^N.
Now at my turn, if the max(allowed) + so_far >= target, then I will win. Otherwise, I choose from the allowed values one by one and recursively call for the other player. If with any choice the opponent fails for sure, then also I can win for sure from this state.
What is the time complexity? For a brute force solution, the game tree has 10 choices at first level, each of these choices has 9 choices at second level, and so on. So the complexity is N!. But with memoization, we only compute 2^N sub-problems, and in each problem we do O(N) work. So total time complexity is O(N2^N).

'''

class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        self.memo = {}
        allowed = list(range(1, maxChoosableInteger + 1))
        return self.dfs(allowed, desiredTotal)

    def dfs(self, allowed, remaining):
        state = tuple(allowed)
        if state in self.memo:
            return self.memo[state]
        if not allowed or sum(allowed) < remaining:
            return False
        if max(allowed) >= remaining:
            return True
        self.memo[state] = False
        for x in allowed:
            tmp = [_ for _ in allowed if _ != x]
            if self.dfs(tmp, remaining - x) == False:
                self.memo[state] = True
                return True
        return False


