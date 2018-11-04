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
                return res
        decimals[numerator] = len(res)
        numerator *= 10
        #       while numerator < denominator:
        #           numerator *= 10
        #          res += '0'
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
                return sign + res
            q = r * 10
            idx += 1


s = Solution()

print(s.fractionToDecimal(-2147483648,1))


