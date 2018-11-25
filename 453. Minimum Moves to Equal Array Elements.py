"""
453. Minimum Moves to Equal Array Elements


Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


"""

# math


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal = min(nums)
        nums = [num - minVal + 1 for num in nums]

        return sum(nums) - len(nums)

# oneline math

'''
nums: min, ..., max
result: a, ..., a
 sum + (a - min) * (n - 1) = n * a --> a = sum - min * (n - 1)
 num of steps = a - min = sum - min * n



'''

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)

