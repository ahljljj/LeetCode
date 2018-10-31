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


# recursive solution TLE

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        nums = [i for i in range(1, n + 1)]
        res = self.helper(nums)
        return res

    def helper(self, nums):
        if len(nums) < 2:
            return 0
        elif len(nums) <= 3:
            return nums[-2]
        cost = float("inf")
        for i in range(1, len(nums)):
            cost = min(cost, nums[i] + max(self.helper(nums[:i]), self.helper(nums[i + 1:])))
        return cost


# recursive
# use memeory to save the itermedia result
# break when the left > right, it looks like a parabola, the peaks at the turning point
# time complexity O(n!)


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        self.memo = {} # use dictionary to save the used result, you can also use a n X n matrix for this one
        res = self.helper(1, n)
        return res

    def helper(self, lower, upper):
        key = (lower, upper)
        if key in self.memo:
            return self.memo[key]
        if upper == lower: # stopping condition 1: [i, i]: return 0 when the length is 1
            return 0
        elif upper - lower <= 2: # stopping condition 2: [i, i + 1] or [i, i + 1, i + 2]: return second last element when the length is 2 or 3
            return upper - 1
        cost = float("inf")
        left, right = None, None
        for i in range(lower + 1, upper):
            left = self.helper(lower, i - 1)
            right = self.helper(i + 1, upper)
            cost = min(cost, i + max(left, right))
            if left > right:
                break
        self.memo[key] = cost
        return cost

# not correct dfs but super fast

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        self.memo = {}
        res = self.helper(nums, None, None)
        return res

    def helper(self, nums, prev, sign):
        if not nums:
            return 0
        key = (nums[0], prev, sign)
        if key in self.memo:
            return self.memo[key]
        incr, decr = 0, 0
        if sign == None:
            incr = 1 + self.helper(nums[1:], nums[0], True)
            decr = 1 + self.helper(nums[1:], nums[0], False)
            #            self.memo[key] = max(incr, decr)
            return max(incr, decr)

        if sign == True:
            tmp = -float("inf")
            for i in range(len(nums)):
                if nums[i] < prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], False))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp
        else:
            tmp = - float("inf")
            for i in range(len(nums)):
                if nums[i] > prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], nums[i], True))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp

# barely accepted dfs

class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        self.memo = {}
        res = self.helper(nums, 0, None, None)
        return res

    def helper(self, nums, idx, prev, sign):
        if not nums:
            return 0
        key = (idx, prev, sign)
        if key in self.memo:
            return self.memo[key]
        incr, decr = 0, 0
        if sign == None:
            incr = 1 + self.helper(nums[1:], 1, nums[0], True)
            decr = 1 + self.helper(nums[1:], 1, nums[0], False)
            return max(incr, decr)

        if sign == True:
            tmp = -float("inf")
            for i in range(len(nums)):
                if nums[i] < prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], idx + i + 1, nums[i], False))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp
        else:
            tmp = - float("inf")
            for i in range(len(nums)):
                if nums[i] > prev:
                    tmp = max(tmp, 1 + self.helper(nums[i + 1:], idx + i + 1, nums[i], True))
            tmp = tmp if tmp != -float("inf") else 0
            self.memo[key] = tmp
            return tmp