'''
285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Example 1:

Input: root = [2,1,3], p = 1

  2
 / \
1   3

Output: 2
Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

Output: null



'''

# brilliant dfs

'''
The inorder traversal of a BST is the nodes in ascending order. To find a successor, you just need to find the smallest one that is larger than the given value since there are no duplicate values in a BST. It just like the binary search in a sorted list. The time complexity should be O(h) where h is the depth of the result node. succ is a pointer that keeps the possible successor. Whenever you go left the current root is the new possible successor, otherwise the it remains the same.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            l = self.inorderSuccessor(root.left, p)
            return l if l != None else root

# iterative inorder 2020/04/08

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        dummy = TreeNode(None)
        dummy.right = root
        stack = [dummy]
        while stack:
            top = stack.pop()
            node = top
            if top.right:
                top = top.right
                while top:
                    stack.append(top)
                    top = top.left
            if node == p and stack: return stack[-1]
        return None

# variation 1

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return root
        left = self.inorderSuccessor(root.left, p)
        right = self.inorderSuccessor(root.right, p)
        if root.val <= p.val:
            return right
        return left if left else root

# variation 2, rewrite of old codes

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return root
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        left = self.inorderSuccessor(root.left, p)
        return left if left else root
