"""
287. Find the Duplicate Number


Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.


"""

# cycle detection
# Intuition
'''
If we interpret nums such that for each pair of index i and value v_i, the "next" value v_j  is at index v_i
, we can reduce this problem to cycle detection. See the solution to Linked List Cycle II for more details.
'''

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = nums[0]
        # find the intersection of the two runners
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# binary search: time complexity: O(nlg(n)
'''
intuition

This solution is based on binary search.

At first the search space is numbers between 1 to n. Each time I select a number mid (which is the one in the middle) and count all the numbers equal to or less than mid. Then if the count is more than mid, the search space will be [1 mid] otherwise [mid+1 n]. I do this until search space is only one number.


'''

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        lower = 1
        upper = n
        mid = upper
        while lower < upper:
            mid = (lower + upper) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                upper = mid
            else:
                lower = mid + 1
        return lower

