# 1712. Ways to Split Array Into Three Subarrays

# 2021/01/19， binary search, too hard

# Runtime: 5396 ms, faster than 6.20% of Python3 online submissions for Ways to Split Array Into Three Subarrays.
# Memory Usage: 27.4 MB, less than 86.55% of Python3 online submissions for Ways to Split Array Into Three Subarrays.

# 注意：1、用前缀和计算出任意两个结点之间的和；2、给定第一个cut point: i，用二分法求出第二个cut point 的最小值 left，即，nums[i + 1 : left + 1] >= nums[:i + 1]
# 2、同时用二分法求出第二个cut point 的最大值right，即，nums[i + 1: right + 1] <= (nums[i + 1:}) / 2
# 3、如果 left <= right，那么 update: ans += right - left + 1


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]
        ans = 0
        for i in range(len(nums) - 1):
            left = self.search_left(nums, i, prefix_sum)
            if left == -1: continue
            right = self.search_right(nums, i, prefix_sum)
            if left > right: continue
            ans += (right - left + 1) % (10 ** 9 + 7)
        return ans % (10 ** 9 + 7)

    def search_left(self, nums, i, prefix_sum):
        l, r = i + 1, len(nums) - 2
        while l + 1 < r:
            m = (l + r) >> 1
            if prefix_sum[m + 1] - prefix_sum[i + 1] < prefix_sum[i + 1]:
                l = m
            else:
                r = m
        if prefix_sum[l + 1] - prefix_sum[i + 1] >= prefix_sum[i + 1]:
            return l
        if prefix_sum[r + 1] - prefix_sum[i + 1] >= prefix_sum[i + 1]:
            return r
        return -1

    def search_right(self, nums, i, prefix_sum):
        l, r = i + 1, len(nums) - 2
        while l + 1 < r:
            m = (l + r) >> 1
            if prefix_sum[m + 1] - prefix_sum[i + 1] > (prefix_sum[-1] - prefix_sum[i + 1]) // 2:
                r = m
            else:
                l = m
        if prefix_sum[r + 1] - prefix_sum[i + 1] <= (prefix_sum[-1] - prefix_sum[i + 1]) // 2:
            return r
        if prefix_sum[l + 1] - prefix_sum[i + 1] <= (prefix_sum[-1] - prefix_sum[i + 1]) // 2:
            return l
        return -1

