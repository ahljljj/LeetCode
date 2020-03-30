"""
349. Intersection of Two Arrays


Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.


"""

#hashmap O(n + m)

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
        return res


# two pointers

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                if nums1[i] not in res:
                    res.append(nums1[i])
                i += 1
                j += 1

        return res


# 2020/03/29, two pointer

'''
Runtime: 36 ms, faster than 97.73% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14.2 MB, less than 5.88% of Python3 online submissions for Intersection of Two Arrays.
'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i1, i2 = 0, 0
        res = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif not res:
                res.append(nums1[i1])
                i1 += 1; i2 += 1
            else:
                if res[-1] != nums1[i1]: res.append(nums1[i1])
                i1 += 1; i2 += 1
        return res