
"""
247. Strobogrammatic Number II


A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]



"""

# dfs

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.hMap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        res = []
        self.dfs(res, '', n)
        return res

    def dfs(self, res, tmp, n):
        if len(tmp) == n // 2:
            rHalf = tmp[::-1]
            if n % 2 == 0:
                for s in rHalf:
                    tmp += self.hMap[s]
                res.append(tmp)
            else:
                r = ''
                for s in rHalf:
                    r += self.hMap[s]
                for ch in '018':
                    res.append(tmp + ch + r)
            return
        s = '01689'
        for i in range(len(s)):
            if not tmp and i == 0:
                continue
            self.dfs(res, tmp + s[i], n)
        return


