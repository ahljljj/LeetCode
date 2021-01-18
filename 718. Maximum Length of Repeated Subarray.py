# 718. Maximum Length of Repeated Subarray


#2021/01/17， dp


# Runtime: 2588 ms, faster than 88.75% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.6 MB, less than 40.64% of Python3 online submissions for Maximum Length of Repeated Subarray.

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        return max(max(row) for row in dp)
