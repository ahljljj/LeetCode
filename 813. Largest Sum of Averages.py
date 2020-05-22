'''
813. Largest Sum of Averages

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
Accepted
21,621
Submissions
44,070

'''

#2020/05/14, 2d dp, too hard

'''
Runtime: 512 ms, faster than 32.89% of Python3 online submissions for Largest Sum of Averages.
Memory Usage: 14.2 MB, less than 33.33% of Python3 online submissions for Largest Sum of Averages.
'''

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        dp = [[0] * K for _ in range(n)]
        for i in range(n):
            dp[i][0] = prefix_sum[i + 1] / (i + 1)
        for k in range(1, K):
            for i in range(1, n):
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + (prefix_sum[i + 1] - prefix_sum[j + 1]) / (i - j))
        return dp[n - 1][K - 1]

