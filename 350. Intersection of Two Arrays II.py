"""
350. Intersection of Two Arrays II


Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

"""
follow up

If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

If both nums1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), then read 2 elements from each array at a time in memory, record intersections.

"""

#hash table
#time complexityL O(n) space complexity: O(n + m)


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash1 = {}
        hash2 = {}
        for num in nums1:
            hash1[num] = hash1.get(num, 0) + 1
        for num in nums2:
            hash2[num] = hash2.get(num, 0) + 1
        res = []
        for num in hash1:
            if num in hash2:
                res.extend([num] * min(hash1[num], hash2[num]))

        return res

#two pointers also works
