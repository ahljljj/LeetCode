"""
357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99


"""

# math + dp
'''
intuition

This is a digit combination problem. Can be solved in at most 10 loops.

When n == 0, return 1. I got this answer from the test case.

When n == 1, _ can put 10 digit in the only position. [0, ... , 9]. Answer is 10.

When n == 2, _ _ leading digit has 9 choices [1, ..., 9], second one has 9 choices excluding the already chosen one. So totally 9 * 9 = 81. answer should be 10 + 81 = 91

When n == 3, _ _ _ total choice is 9 * 9 * 8 = 684. answer is 10 + 81 + 648 = 739

When n == 4, _ _ _ _ total choice is 9 * 9 * 8 * 7.

...

When n == 10, _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1

When n == 11, _ _ _ _ _ _ _ _ _ _ _ total choice is 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 * 0 = 0



'''



class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * 11
        dp[0] = 1
        extra = 1
        for i in range(1, 11):
            if i == 1:
                extra *= 9
            else:
                extra *= 10 - (i - 1)
            dp[i] = extra + dp[i - 1]
        return dp[n] if n < 11 else dp[10]


'''
# backtracking TLE


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        self.upper = min(10**n, 10**10)
        used = [False] * 10 # record the digits have been used
        count = 1
        for i in range(1, 10): # the leading digit cann't be zero
            used[i] = True
            count += self.helper(i, used)
            used[i] = False # back to the upper layer and release the digit i
        return count
    
    def helper(self, prev, used):
        # prev: use previous value to compute the current value
        # used: use the length-10 array to lock and release the digits
        count = 0
        if prev < self.upper: # stopping criterion
            count += 1
        else:
            return count
        for i in range(10):
            if not used[i]: # if digit i havn't been used
                used[i] = True
                curr = 10 * prev + i
                count += self.helper(curr, used)
                used[i] = False
        return count
                
        
'''