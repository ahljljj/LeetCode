'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

# not my solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.balanced = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.height(root)
        return self.balanced

    def height(self, root):
        if root == None:
            return 0

        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False

        return 1 + max(leftHeight, rightHeight)