"""
338. Counting Bits


Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

# brute force: but pass the test

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            res[n] = self.countbits(n)
        return res

    def countbits(self, n):
        if n == 0:
            return 0
        count = 0
        while n >= 1:
            if n % 2 == 1:
                count += 1
            n //= 2
        return count

'''

# An easy recurrence for this problem is f[i] = f[i / 2] + i % 2.

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            res[n] = res[n >> 1] + (n & 1)
        return res
'''