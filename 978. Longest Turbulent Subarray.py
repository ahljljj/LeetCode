'''
978. Longest Turbulent Subarray

A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.



Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1


Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9

2020/03/27, sliding window

Runtime: 608 ms, faster than 18.36% of Python3 online submissions for Longest Turbulent Subarray.
Memory Usage: 17.9 MB, less than 25.00% of Python3 online submissions for Longest Turbulent Subarray.

'''

class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) < 2: return len(A)
        if len(A) == 2:
            if A[0] == A[1]: return 1
            else: return 2
        l, r = 0, 0
        res = 0
        for r in range(2, len(A)):
            # detect duplicate
            while l < r and A[l] == A[l + 1]:
                l += 1
            if (A[r] >= A[r - 1] >= A[r - 2]) or\
            (A[r] <= A[r - 1] <= A[r - 2]):
                l = max(l, r - 1)
            res = max(res, r - l + 1)
        return res