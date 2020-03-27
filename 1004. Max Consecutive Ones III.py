'''
1004. Max Consecutive Ones III

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1


2020/03/27, sliding window

Runtime: 692 ms, faster than 45.77% of Python3 online submissions for Max Consecutive Ones III.
Memory Usage: 14.4 MB, less than 16.67% of Python3 online submissions for Max Consecutive Ones III.

'''



class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r, zeros = 0, 0, 0
        res = 0
        for r in range(len(A)):
            if A[r] == 0: zeros += 1
            while l <= r and zeros > K:
                if A[l] == 0: zeros -= 1
                l += 1
            res = max(res, r - l + 1)
        return res