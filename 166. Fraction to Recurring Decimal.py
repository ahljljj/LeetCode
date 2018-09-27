"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"


"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return str('0')
        sign = ''
        if numerator < 0 and denominator < 0:
            numerator, denominator = -numerator, -denominator
        elif numerator < 0 and denominator > 0:
            numerator = -numerator
            sign = '-'
        elif numerator > 0 and denominator < 0:
            denominator = -denominator
            sign = '-'

        res = '' if numerator >= denominator else '0.'
        decimals = {}
        if numerator >= denominator:
            res += str(numerator / denominator)
            numerator = numerator % denominator
            if numerator > 0:
                res += '.'
            else:
                return sign + res
        decimals[numerator] = len(res)
        numerator *= 10
        q = numerator
        d = denominator
        idx = len(res) + 1
        while True:
            tmp = q / d
            res += str(tmp)
            r = q % d
            if r > 0:
                if r not in decimals:
                    decimals[r] = idx
                else:
                    return sign + res[:decimals[r]] + '(' + res[decimals[r]:] + ')'
            else:
                print(sign)
                return sign + res
            q = r * 10
            idx += 1


