"""
457. Circular Array Loop


You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.

Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.

Example 2: Given the array [-1, 2], there is no loop.

Note: The given array is guaranteed to contain no element "0".

Can you do it in O(n) time complexity and O(1) space complexity?


"""

# slow/ fast pointer

'''
Just think it as finding a loop in Linkedlist, except that loops with only 1 element do not count. Use a slow and fast pointer, slow pointer moves 1 step a time while fast pointer moves 2 steps a time. If there is a loop (fast == slow), we return true, else if we meet element with different directions, then the search fail, we set all elements along the way to 0. Because 0 is fail for sure so when later search meet 0 we know the search will fail.


A nested loop structure does not necessarily imply O(n^2) time complexity. We can apply amortized analysis: the algorithm visits each index a maximum of 4 times (visit fast, visit fast, mark zero, skip zero), and because 4 is a constant factor we have O(4n)->O(n) time complexity. 
'''

class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, step in enumerate(nums):
            if step == 0:
                continue
            # i: starting point, illustrate all possible entrance of the cycle
            j = i  # j: slow pointer
            k = self.getIdx(nums, j)  # k: fast pointer
            # move along the same direction
            while nums[k] * nums[i] > 0 and nums[self.getIdx(nums, k)] * nums[i] > 0:
                if j == k:
                    if j == self.getIdx(nums, j):
                        break
                    return True
                j = self.getIdx(nums, j)
                k = self.getIdx(nums, self.getIdx(nums, k))
            j = i
            while nums[j] * step > 0:
                nums[j] = 0
                j = self.getIdx(nums, j)
        return False

    def getIdx(self, nums, i):
        return (i + nums[i]) % len(nums)
