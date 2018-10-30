"""
368. Largest Divisible Subset


Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

"""

'''
wrong

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        hashmap = {}
        res = 0
        for num in nums:
            if not hashmap:
                hashmap[num] = [num]
                res = 1
                continue
            tmp = hashmap.copy()
            for key in tmp:
                if num % key == 0:
                    if num in hashmap:
                        if len(hashmap[key] + [num]) > res:
                            hashmap[num] = hashmap[key] + [num]
                            res = max(res, len(hashmap[num]))
                            hashmap.pop(key, None)
                        else:
                            hashmap.pop(key, None)   
                    else:
                        hashmap[num] = hashmap[key] + [num]
                        res = max(res, len(hashmap[num]))
                        hashmap.pop(key, None)
                        
            if num not in hashmap:
                hashmap[num] = [num]
#        print(hashmap)
        for key in hashmap:
            if len(hashmap[key]) == res:
                return hashmap[key]



'''


# hashtable time complexity O(n^2)



class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        hashmap = {}
        res = 0
        for num in nums:
            if not hashmap:
                hashmap[num] = [num]
                res = 1
                continue
            tmp = hashmap.copy()
            for key in tmp:
                if num % key == 0:
                    if num in hashmap:
                        if len(hashmap[key] + [num]) >= res: # equality is essential due to sort
                            hashmap[num] = hashmap[key] + [num]
                            res = max(res, len(hashmap[num]))
                    else:
                        hashmap[num] = hashmap[key] + [num]
                        res = max(res, len(hashmap[num]))
            if num not in hashmap:
                hashmap[num] = [num]
        for key in hashmap:
            if len(hashmap[key]) == res:
                return hashmap[key]


# dynamic programming


'''
idea

The basic idea is like:

1. Sort
2. Find the length of longest subset
3. Record the largest element of it.
4. Do a loop from the largest element to nums[0], add every element belongs to the longest subset.

'''


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n  # dp[i]: length of the maximal possible subset at nums[i]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], 1 + dp[j])
        # find the max index: the maximal element in the longest subset
        maxidx = 0
        for i in range(n):
            maxidx = i if dp[i] > dp[maxidx] else maxidx
        # going backwards, use the max index to find the corresponding subset
        tmp = nums[maxidx]
        res = []
        curdp = dp[maxidx]
        for i in range(maxidx, -1, -1):
            if tmp % nums[i] == 0 and dp[i] == curdp:
                res = [nums[i]] + res
                tmp = nums[i]
                curdp -= 1
        return res



