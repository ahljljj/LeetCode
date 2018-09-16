"""
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


"""
time limit exceeded

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res=''
        nums = list(range(1,n+1))
        for i in range(0,k-1):
            self.nextPermutation(nums)
        for l in nums:
            res += str(l)
        return res
                
        
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        def reverse(nums, i, j):
            nb = len(nums)
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1

        nb = len(nums)
        idx = nb - 2
        while idx >= 0 and nums[idx + 1] <= nums[idx]:
            idx -= 1
        if idx >= 0:
            j = nb - 1
            while j >= 0 and nums[j] <= nums[idx]:
                j -= 1
            swap(nums, idx, j)
        reverse(nums, idx + 1, nb - 1)

"""

# not my idea, division algorithm

class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        tmp = list(range(1, n + 1))
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i * fact[i - 1]
        k = k - 1
        for i in range(1, n + 1):
            idx = k // fact[n - i]
            k = k % fact[n - i]
            res.append(tmp[idx])
            tmp.remove(tmp[idx])

        res_str = ''
        for s in res:
            res_str += str(s)
        return res_str




