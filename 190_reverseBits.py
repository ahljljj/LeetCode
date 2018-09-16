'''
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?


'''


#600 / 600 test cases passed. Runtime: 32 ms
#Your runtime beats 16.48% of python 3 submissions.

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ns=bin(n)[2:].zfill(32)
        ns=ns[::-1]
        return int(ns, 2)