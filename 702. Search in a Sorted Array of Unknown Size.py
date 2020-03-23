'''
702. Search in a Sorted Array of Unknown Size

Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.



Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].

Runtime: 40 ms, faster than 24.21% of Python3 online submissions for Search in a Sorted Array of Unknown Size.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Search in a Sorted Array of Unknown Size.

'''


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        upper = 0
        while upper < 10000:
            if reader.get(upper) == target:
                return upper
            elif reader.get(upper) < target:
                upper = 2 * upper + 1
            else:
                break
        l, r = 0, upper
        while l + 1 < r:
            m = (l + r) // 2
            if reader.get(m) == target:
                return m
            elif reader.get(m) > target:
                r = m
            else:
                l = m
        if reader.get(r) == target:
            return r
        elif reader.get(l) == target:
            return l
        else:
            return -1

