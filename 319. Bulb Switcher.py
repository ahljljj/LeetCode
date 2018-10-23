"""
319. Bulb Switcher


There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.



"""

'''
#TLE

class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [1] * n
        for i in range(2, n + 1):
            for j in range(n):
                if (j + 1) % i == 0:
                    bulbs[j] = 1 - bulbs[j]
        return sum(bulbs)
        
        
        
# slight better but still TLE

class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        bulbs = [1] * n
        for i in range(2, n + 1):
            j = i - 1
            while j < n:
                bulbs[j] = 1- bulbs[j]
                j += i
        return sum(bulbs)
'''

'''
explanation

For prime numbers, they must be off because we can reach them only twice (The first round and their own round).

For other numbers, if we can reach them odd times, then they are on; otherwise, they are off. So only 
 those numbers who have square root will be reached odd times and there are sqrt(n) of them because
 for every x > sqrt(n), x*x > n and thus should not be considered as the answer.

'''


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(math.sqrt(n))