class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], n, k, 0)
        return res

    def helper(self, res, tmp, n, k, start):
        if k == 0:
            res.append(tmp)
            return
        for i in range(start, n + 1):
            tmp.append(i)
            self.helper(res, tmp, n, k - 1, i + 1)
            tmp.pop()


s = Solution()

print(s.combine(4,2))