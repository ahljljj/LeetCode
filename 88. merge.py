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


# cpp, others

'''
The idea is to go from the last indexes of both arrays, compare and put elements from either A or B to the final position, which can easily get since we know that A have enough space to store them all and we know size of A and B. Please refer to the comments for details.

class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        
        int a=m-1;
        int b=n-1;
        int i=m+n-1;    // calculate the index of the last element of the merged array
        
        // go from the back by A and B and compare and put to the A element which is larger
        while(a>=0 && b>=0){
            if(A[a]>B[b])   A[i--]=A[a--];
            else            A[i--]=B[b--];
        }
        
        // if B is longer than A just copy the rest of B to A location, otherwise no need to do anything
        while(b>=0)         A[i--]=B[b--];
    }
};

'''


# 2020/03/29

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        p = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1; p -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1; p -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1