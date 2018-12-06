
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

# brilliant

'''

Some observation to the sequence:

n == 1: [0, 1, 8]

n == 2: [11, 88, 69, 96]

How about n == 3?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2

n == 4?
=> it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2

n == 5?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4

the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

'''

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMid = ["00", "11", "69", "88", "96"]
        oddMid = ["0", "1", "8"]
        if n == 1:
            return oddMid
        if n == 2:
            return evenMid[1:]
        if n % 2 == 0:
            prev, mid = self.findStrobogrammatic(n - 2), evenMid
        else:
            prev, mid = self.findStrobogrammatic(n - 1), oddMid
        idx = (n - 1) >> 1
        return [p[:idx] + c + p[idx:] for c in mid for p in prev]



