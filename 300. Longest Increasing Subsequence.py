"""
300. Longest Increasing Subsequence


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


"""

# dynamic programming: time complexity: O(n^2), space complexity: O(n)

'''
intuition

This method relies on the fact that the longest increasing subsequence possible upto the i 
th index in a given array is independent of the elements coming later on in the array. Thus, if we know the length of the LIS upto i 
th index, we can figure out the length of the LIS possible by including the (i+1) th
  element based on the elements with indices j such that 0 \leq j \leq (i + 1).

We make use of a dp array to store the required data. dp[i] represents the length of the longest increasing subsequence possible considering the array elements upto the ith index only ,by necessarily including the ith
 element. In order to find out dp[i], we need to try to append the current element(nums[i]) in every possible increasing subsequences upto the (i−1)th index(including the (i−1)th index), such that the new sequence formed by adding the current element is also an increasing subsequence. Thus, we can easily determine dp[i]dp[i] using:

dp[i] = max(dp[j]) + 1, forall 0\leq j 

At the end, the maximum out of all the dp[i]'s to determine the final result.

LIS_{length}= text{max}(dp[i]), forall 0\leq i 	
'''


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 1
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            res = max(res, dp[i])
        return res

'''
网上的思路：先建立一个数组dummy，把首元素放进去，然后比较之后的元素，如果遍历到的新元素比 ends 数组中的首元素小的话，替换首元素为此新元素，如果遍历到的新元素比 dummy数组中的末尾元素还大的话，将此新元素添加到 dummy数组末尾(注意不覆盖原末尾元素)。如果遍历到的新元素比 dummy数组首元素大，比尾元素小时，此时用二分查找法找到第一个不小于此新元素的位置，覆盖掉位置的原来的数字，以此类推直至遍历完整个 nums 数组，此时 dummy 数组的长度就是要求的LIS的长度.

2020/03/22

Runtime: 40 ms, faster than 88.16% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 13.2 MB, less than 69.23% of Python3 online submissions for Longest Increasing Subsequence
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        dummy = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == dummy[0] or nums[i] == dummy[-1]: continue
            if nums[i] > dummy[-1]:
                dummy.append(nums[i])
            elif nums[i] < dummy[0]:
                dummy[0] = nums[i]
            else:
                k = self.search(dummy, nums[i])
                dummy[k] = nums[i]
        return len(dummy)

    def search(self, dummy, target):
        # find the first element no less than target
        l, r = 0, len(dummy) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if dummy[m] >= target:
                r = m
            else:
                l = m
        if dummy[r] >= target: return r
        if dummy[l] >= target: return l

# 2020/05/12, dp

'''
Runtime: 1272 ms, faster than 20.34% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = 1
                continue
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 2020/05/12, binary search, O(nlgn), too clever

'''
Runtime: 36 ms, faster than 96.12% of Python3 online submissions for Longest Increasing Subsequence.
Memory Usage: 14.1 MB, less than 5.13% of Python3 online submissions for Longest Increasing Subsequence.
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            self.search(dp, num)
        return len(dp)

    def search(self, dp, num):
        if not dp or num > dp[-1]:
            dp.append(num)
            return
        if num <= dp[0]:
            dp[0] = num
            return
        l, r = 0, len(dp) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if dp[m] < num:
                l = m
            else:
                r = m
        if dp[l] > num:
            dp[l] = num
        else:
            dp[r] = num