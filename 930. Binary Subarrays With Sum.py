# 930. Binary Subarrays With Sum


# 2021/01/23

# Runtime: 1132 ms, faster than 5.13% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 16.1 MB, less than 56.46% of Python3 online submissions for Binary Subarrays With Sum.

# 用二分法 + prefix sum 暴力做出来了
# 时间复杂度是 O(nlgn)


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix_sum = [0] * (1 + len(A))
        ans = 0
        for i in range(len(A)):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        for i in range(len(A)):
            first = self.search_first(A, prefix_sum, i, S)
            if first == -1: continue
            last = self.search_last(A, prefix_sum, i, S)
            ans += last - first + 1
        return ans

    def search_first(self, nums, prefix_sum, start, target):
        l, r = start, len(nums) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if prefix_sum[m + 1] - prefix_sum[start] >= target:
                r = m
            else:
                l = m
        if prefix_sum[l + 1] - prefix_sum[start] == target:
            return l
        if prefix_sum[r + 1] - prefix_sum[start] == target:
            return r
        return -1

    def search_last(self, nums, prefix_sum, start, target):
        l, r = start, len(nums) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if prefix_sum[m + 1] - prefix_sum[start] <= target:
                l = m
            else:
                r = m
        if prefix_sum[r + 1] - prefix_sum[start] == target:
            return r
        if prefix_sum[l + 1] - prefix_sum[start] == target:
            return l
        return -1

# 2021/01/24, prefix sum + hash table

# Runtime: 268 ms, faster than 63.69% of Python3 online submissions for Binary Subarrays With Sum.
# Memory Usage: 18 MB, less than 14.26% of Python3 online submissions for Binary Subarrays With Sum.


# 哈希表 + 前缀和
# 遍历前缀和数组。如果 prefix_sum[i] - S 存在，表明在此之前有m[prefix_sum[i] - S ]个subarray的和等于prefix_sum[i] - S
# 那么update 结果
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        prefix_sum = [0] * (1 + len(A))
        for i in range(len(A)):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        m = {}
        ans = 0
        for i in range(len(prefix_sum)):
            ans += m.get(prefix_sum[i] - S, 0)
            m[prefix_sum[i]] = m.get(prefix_sum[i], 0) + 1
        return ans