'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

'''
The following code has both time ans space complexity as O(m+n). not good.

It only beats 77% of the python3 submissions 



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist=[]
        l1=nums1
        l2=nums2
        i1=0
        i2=0
        while i1<len(nums1) and i2<len(nums2):
            if (l1[i1] < l2[i2]):
                newlist.append(l1[i1])
                i1+=1
            else:
                newlist.append(l2[i2])
                i2+=1
        while i1<len(nums1):
            newlist.append(l1[i1])
            i1+=1
        while i2<len(nums2):
            newlist.append(l2[i2])
            i2+=1
            
        n=len(newlist)
        if (n%2==0):
            return (newlist[n//2-1]+newlist[n//2])/2
        else:
            return newlist[(n-1)//2]
'''


# 2020/05/10, binary search

'''
Runtime: 136 ms, faster than 9.58% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.1 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.
'''


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2

    def findKth(self, nums1, i, nums2, j, k):
        if i >= len(nums1): return nums2[j + k - 1]
        if j >= len(nums2): return nums1[i + k - 1]
        if k == 1: return min(nums1[i], nums2[j])
        kth_1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float("inf")
        kth_2 = nums2[j + k // 2 - 1] if j + k // 2 - 1 < len(nums2) else float("inf")
        if kth_1 < kth_2:
            return self.findKth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.findKth(nums1, i, nums2, j + k // 2, k - k // 2)