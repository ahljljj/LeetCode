'''
907. Sum of Subarray Minimums

Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000


Accepted
24,122
Submissions
75,992


'''

# 2020/06/21, increasing stack

'''
Runtime: 496 ms, faster than 67.06% of Python3 online submissions for Sum of Subarray Minimums.
Memory Usage: 17.7 MB, less than 97.10% of Python3 online submissions for Sum of Subarray Minimums.
'''


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        mod = 10 ** 9 + 7
        ans = 0
        A.append(-1)
        for r in range(len(A)):
            while stack and A[stack[-1]] > A[r]:
                top = stack.pop()
                cnt_large = r - top - 1
                cnt_small = top - (stack[-1] + 1) if stack else top
                ans += A[top] * (cnt_large + 1) * (cnt_small + 1)
                ans %= mod
            stack.append(r)
        return ans

# 2020/06/21, slight modification

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        mod = 10**9 + 7
        ans = 0
        A.append(-1)
        for i in range(len(A)):
            while stack and A[stack[-1]] > A[i]:
                top = stack.pop()
                r, l = i-1, stack[-1]+1 if stack else 0
                cnt_large = r - top
                cnt_small = top - l
                ans += A[top] *(cnt_large+1)*(cnt_small+1)
                ans %= mod
            stack.append(i)
        return ans