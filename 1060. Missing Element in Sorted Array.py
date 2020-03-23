'''
1060. Missing Element in Sorted Array
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.



Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.


Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

Runtime: 316 ms, faster than 54.94% of Python3 online submissions for Missing Element in Sorted Array.
Memory Usage: 19.2 MB, less than 100.00% of Python3 online submissions for Missing Element in Sorted Array.
'''


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            left_gap = (nums[m] - nums[l]) - (m - l)
            if k > left_gap:
                l = m
                k -= left_gap
            else:
                r = m
        gap = (nums[r] - nums[l]) - (r - l)
        if k <= gap:
            return nums[l] + k
        else:
            return nums[r] + k - gap