'''
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''


#24ms 29.58%
#recursion


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtqype: TreeNode
        """
        if not root:
            return None
        right=self.invertTree(root.right)
        left=self.invertTree(root.left)
        root.left=right
        root.right=left

        return root