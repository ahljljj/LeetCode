"""
415. Add Strings


Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.



"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        curr = ""
        res = ""
        for idx, (n1, n2) in enumerate(zip(num1[::-1], num2[::-1])):
            tmp = ord(n1) - ord("0") + ord(n2) - ord("0") + carry
            if tmp > 9:
                carry = 1
            else:
                carry = 0
            curr = tmp % 10
            res += chr(curr + ord("0"))

        for i, n1 in enumerate(num1[::-1][idx + 1:]):
            tmp = ord(n1) - ord("0") + carry
            if tmp > 9:
                carry = 1
            else:
                carry = 0
            curr = tmp % 10
            res += chr(curr + ord("0"))

        for i, n2 in enumerate(num2[::-1][idx + 1:]):
            tmp = ord(n2) - ord("0") + carry
            if tmp > 9:
                carry = 1
            else:
                carry = 0
            curr = tmp % 10
            res += chr(curr + ord("0"))

        if carry:
            res += "1"
        return res[::-1]
