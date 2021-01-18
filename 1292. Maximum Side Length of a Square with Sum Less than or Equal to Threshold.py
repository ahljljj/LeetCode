#1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold


# 2021/01/18, prefix sum (lc 304) + binary search
# Runtime: 1728 ms, faster than 28.83% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.
# Memory Usage: 19.9 MB, less than 29.20% of Python3 online submissions for Maximum Side Length of a Square with Sum Less than or Equal to Threshold.

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        prefix_sum = self.prefix_sum_matrix(mat)
        # print(prefix_sum)
        l, r = 0, min(len(mat), len(mat[0]))
        while l + 1 < r:
            m = (l + r) >> 1
            if self.check_validity(prefix_sum, m, threshold):
                l = m
            else:
                r = m
        if self.check_validity(prefix_sum, r, threshold):
            return r
        if self.check_validity(prefix_sum, l, threshold):
            return l
        return 0

    def prefix_sum_matrix(self, mat):
        n, m = len(mat), len(mat[0])
        dp = [[0] * (1 + m) for _ in range(1 + n)]
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] \
                                   - dp[i][j] + mat[i][j]
        return dp

    def check_validity(self, prefix_sum, side_len, threshold):
        n, m = len(prefix_sum), len(prefix_sum[0])
        for i in range(n - side_len):
            for j in range(m - side_len):
                sum_region = prefix_sum[i + side_len][j + side_len] - prefix_sum[i][j + side_len] \
                             - prefix_sum[i + side_len][j] + prefix_sum[i][j]
                if sum_region <= threshold:
                    return True
        return False








