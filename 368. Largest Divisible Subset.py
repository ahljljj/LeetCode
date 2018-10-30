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