'''

191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:

Input: 11
Output: 3
Explanation: Integer 11 has binary representation 00000000000000000000000000001011
Example 2:

Input: 128
Output: 1
Explanation: Integer 128 has binary representation 00000000000000000000000010000000
'''


#600 / 600 test cases passed. Runtime: 28 ms
#Your runtime beats 20.78% of python3 submissions.


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ns = bin(n)[2:]
        count = 0
        for s in ns:
            if int(s):
                count += 1
        return count
