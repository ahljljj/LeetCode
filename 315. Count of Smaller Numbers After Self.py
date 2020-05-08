'''
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Accepted
118,775
Submissions
289,318

'''


# 2020/05/07, binary indexed tree, not that good

'''
Runtime: 180 ms, faster than 41.64% of Python3 online submissions for Count of Smaller Numbers After Self.
Memory Usage: 17.7 MB, less than 37.50% of Python3 online submissions for Count of Smaller Numbers After Self.
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        bit = BITree(100000)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = bit.prefix_sum(nums[i] + 1000)
            bit.update(nums[i] + 1000, 1)
        return res


class BITree:
    def __init__(self, n):
        self.bit = [0] * (1 + n)

    def update(self, i, val):
        i += 1
        while i < len(self.bit):
            self.bit[i] += val
            i += self.lowbit(i)

    def lowbit(self, x):
        return x & (-x)

    def prefix_sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self.lowbit(i)
        return res

