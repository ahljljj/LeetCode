"""
462. Minimum Moves to Equal Array Elements II

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]


"""

'''

# try binary search but not work

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l, r = nums[0], nums[-1]
        lCost, rCost = self.cost(nums, l), self.cost(nums, r)
        while l <= r:
            mid = (l + r) >> 1
            mCost = self.cost(nums, mid)
            if 
        
        
    def cost(self, nums, target):
        res = 0
        for num in nums:
            if num < target:
                res += target - num
            else:
                res += num - target
        return res

'''

'''
# seems correct, but memory error

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        freq = [1] * (nums[-1] + 1)
        for i in range(1, len(nums)):
            freq[nums[i]] = freq[nums[i - 1]] + 1
            
        extra = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: continue
            incr = freq[nums[i - 1]] # (nums[i] - nums[i - 1])
            decr = len(nums) - freq[nums[i - 1]]
            if decr < incr:
                return self.cost(nums, nums[i - 1])
        
        return self.cost(nums, nums[-1])
    
    def cost(self, nums, target):
        res = 0
        for num in nums:
            if num < target:
                res += target - num
            else:
                res += num - target
        return res
            
'''

# math + hashtable, passed with ridiculous slow speed
# change vector to hashtable

class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        freq = {}
        freq[nums[0]] = 1
        for i in range(1, len(nums)):
            freq[nums[i]] = freq[nums[i - 1]] + 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: continue
            incr = freq[nums[i - 1]]  # (nums[i] - nums[i - 1])
            decr = len(nums) - freq[nums[i - 1]]
            if decr < incr:
                return self.cost(nums, nums[i - 1])

        return self.cost(nums, nums[-1])

    def cost(self, nums, target):
        res = 0
        for num in nums:
            if num < target:
                res += target - num
            else:
                res += num - target
        return res

