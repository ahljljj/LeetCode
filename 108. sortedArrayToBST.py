'''

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

#not my solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid_idx = len(nums)//2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root

# 2020/04/11, dfs rewrite

'''
Runtime: 72 ms, faster than 75.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
Memory Usage: 16.1 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums) - 1)

    def dfs(self, nums, l, r):
        if not nums or l > r: return None
        m = (l + r) >> 1
        root = TreeNode(nums[m])
        root.left = self.dfs(nums, l, m - 1)
        root.right = self.dfs(nums, m + 1, r)
        return root