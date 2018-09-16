"""
31. Next Permutation



Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


"""


class Solution(object):
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

