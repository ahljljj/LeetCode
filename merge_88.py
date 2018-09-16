'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''

#59 / 59 test cases passed. Runtime: 48 ms
#This running time beats 34.43% of python 3 submissions. May 2018

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l1=len(nums1)
        j=0
        for num2 in nums2:
            i=0
            temp=nums1[0]
            while i<m+j and num2>temp:
                i+=1
                temp=nums1[i]
            nums1[i+1:l1]=nums1[i:l1-1]
            nums1[i]=num2
            j+=1