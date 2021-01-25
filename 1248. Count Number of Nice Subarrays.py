# 1248. Count Number of Nice Subarrays
#
# Runtime: 916 ms, faster than 38.07% of Python3 online submissions for Count Number of Nice Subarrays.
# Memory Usage: 21.2 MB, less than 35.27% of Python3 online submissions for Count Number of Nice Subarrays.

# 2021/01/24, prefix sum + sliding window
# 和 leetcode 930 完全一样
# 将奇数转化为1，偶数变为0。原题则变成count有多少个subarry的和刚好等于k。


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i] % 2
        m = {}
        ans = 0
        for i in range(len(prefix_sum)):
            m[prefix_sum[i]] = m.get(prefix_sum[i], 0) + 1
            if prefix_sum[i] - k in m:
                ans += m[prefix_sum[i] - k]
        return ans


