"""
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


"""

# dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        self.dfs(root, None)
        return self.sum

    def dfs(self, root, left):
        if not root:
            return
        if not root.left and not root.right and left: # only count when it is a left leave
            self.sum += root.val
        self.dfs(root.left, True)
        self.dfs(root.right, False)

