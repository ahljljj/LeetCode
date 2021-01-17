'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

#744ms 21%

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nb = len(nums)
        res = []
        nums.sort()
        for i in range(nb):
            for j in range(i + 1, nb):
                l, r = j + 1, nb - 1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp < target:
                        l += 1
                    elif tmp > target:
                        r -= 1
                    else:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1;
                        r -= 1
        return res

# hashtable
# time complexity O(n^2 ~ n^3)

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        getSum = {}
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                tmp = nums[i] + nums[j]
                if tmp not in getSum:
                    getSum[tmp] = set([(i, j)])
                else:
                    getSum[tmp].add((i, j))
        res = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                r = target - nums[i] - nums[j]
                if r in getSum:
                    for (idx1, idx2) in getSum[r]:
                        if j < idx1 and [nums[i], nums[j], nums[idx1], nums[idx2]] not in res:
                            res.append([nums[i], nums[j], nums[idx1], nums[idx2]])
        return res

# 2021/01/17, two pointer

# Runtime: 792 ms, faster than 55.99% of Python3 online submissions for 4Sum.
# Memory Usage: 14.4 MB, less than 58.13% of Python3 online submissions for 4Sum.

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        i = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                pair = self.search(nums, j + 1, target - nums[i] - nums[j])
                if pair:
                    for c, d in pair:
                        ans.append([nums[i], nums[j], nums[c], nums[d]])
        return ans

    def search(self, nums, start, target):
        l, r = start, len(nums) - 1
        ans = []
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                ans.append([l, r])
                l += 1;
                r -= 1
                while l < r and nums[l] == nums[l - 1] and nums[r] == nums[r + 1]:
                    l += 1;
                    r -= 1
        return ans






