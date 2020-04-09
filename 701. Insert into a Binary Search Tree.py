'''
701. Insert into a Binary Search Tree

Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example,

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4
Accepted
91,419
Submissions
115,538

'''


# 2020/04/09, iterative

'''
Runtime: 148 ms, faster than 13.31% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 16 MB, less than 8.00% of Python3 online submissions for Insert into a Binary Search Tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        dummy = root
        target = TreeNode(val)
        while root and root != target:
            if val < root.val:
                if not root.left: root.left = target
                root = root.left
            else:
                if not root.right: root.right = target
                root = root.right
        return dummy

# recursion

'''
Runtime: 136 ms, faster than 85.93% of Python3 online submissions for Insert into a Binary Search Tree.
Memory Usage: 15.8 MB, less than 8.00% of Python3 online submissions for Insert into a Binary Search Tree.
'''

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

