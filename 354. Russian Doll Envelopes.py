'''
354. Russian Doll Envelopes

ou have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Accepted
62,035
Submissions
176,486


'''


# 2020/05/12, binary search, transfer to longer increasing subsequence, lc 300
# dp will lead to time limit exceed


'''
Runtime: 184 ms, faster than 33.80% of Python3 online submissions for Russian Doll Envelopes.
Memory Usage: 16 MB, less than 20.00% of Python3 online submissions for Russian Doll Envelopes.
'''

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes: return 0
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        lis = []
        for env in envelopes:
            self.search(lis, env)
        return len(lis)

    def search(self, nums, env):
        target = env[1]
        if not nums or target > nums[-1]:
            nums.append(target)
            return
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if nums[m] < target:
                l = m
            else:
                r = m
        if nums[l] >= target:
            nums[l] = target
        else:
            nums[r] = target




