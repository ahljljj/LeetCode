'''
1300. Sum of Mutated Array Closest to Target

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.



Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361


Constraints:

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

2020/03/23, binary search

Runtime: 156 ms, faster than 29.65% of Python3 online submissions for Sum of Mutated Array Closest to Target.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Sum of Mutated Array Closest to Target.

idea: similar to copy books

'''


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        l, r = 0, max(arr)
        if r * len(arr) <= target: return r
        while l + 1 < r:
            m = (l + r) // 2
            if self.find_sum(arr, m) > target:
                r = m
            else:
                l = m
        if abs(self.find_sum(arr, l) - target) <= abs(self.find_sum(arr, r) - target):
            return l
        else:
            return r

    def find_sum(self, nums, target):
        res = 0
        for num in nums:
            if num > target:
                res += target
            else:
                res += num
        return res