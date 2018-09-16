'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

# bit by bit adding
# not my idea

class Solution:
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        result = ""
        i = len(a) - 1
        carry = 0
        while i >= 0:
            result = str((int(a[i]) + int(b[i]) + carry) % 2) + result
            carry = int((int(a[i]) + int(b[i]) + carry) / 2)
            i -= 1
        if carry == 1:
            result = str(carry) + result
        return result