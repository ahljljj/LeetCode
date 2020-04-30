'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Accepted
278,627
Submissions
629,656

'''

# 2020/04/30, hashtable, too hard

'''
Runtime: 60 ms, faster than 45.86% of Python3 online submissions for Longest Consecutive Sequence.
Memory Usage: 15.1 MB, less than 7.41% of Python3 online submissions for Longest Consecutive Sequence.
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                start = num
                curr = 1
                while start + 1 in nums:
                    start += 1
                    curr += 1
                res = max(res, curr)

        return res
