"""
413. Arithmetic Slices


A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""

# greedy algorithm
# time complexity O(n) - one pass


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        prev = A[1] - A[0]
        res = 0
        start, end = 0, None
        for i in range(1, len(A) - 1):
            curr = A[i + 1] - A[i]
            if curr == prev:
                end = i + 1
            else:
                if end:
                    l = end - start + 1
                    res += (l - 2) * (l - 1) / 2
                start, end = i, None
            prev = curr
        if end:
            l = end - start + 1
            res += (l - 2) * (l - 1) / 2
        return res

# dynamic programming

'''
intuitioon

nstead of going in the reverse order as in the recursive approach, we can start filling the dpdp in a forward manner. The intuition remains the same as in the last approach. For the i^{th}i 
th
  element being considered, we check if this element satsfies the common difference criteria with the previous element. If so, we know the number of new arithmetic slices added will be 1+dp[i-1]1+dp[i−1] as discussed in the last approach. The sumsum is also updated by the same count to reflect the new arithmetic slices added.


'''


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        dp = [0] * len(A)
        for i in range(1, len(A) - 1):
            if A[i + 1] - A[i] == A[i] - A[i - 1]:
                dp[i] = 1 + dp[i - 1]
                res += dp[i]
        return res


