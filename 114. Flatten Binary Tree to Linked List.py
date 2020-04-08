"""
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.helper(root)

    def helper(self, root):
        if root == None: return None

        self.helper(root.right)
        self.helper(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root

# 2020/04/07, divide and conquer

'''
Runtime: 36 ms, faster than 67.11% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14.5 MB, less than 8.70% of Python3 online submissions for Flatten Binary Tree to Linked List.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        return right_last or left_last or root