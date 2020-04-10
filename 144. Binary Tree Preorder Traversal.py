"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?


"""

'''
#recursion

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.res = []
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if root == None: return
        self.res.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
        
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res

# 2020/04/10, iterative

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = [root]
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right: stack.append(top.right)
            if top.left: stack.append(top.left)
        return res


# morris transversal
'''
Runtime: 28 ms, faster than 67.50% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 13.7 MB, less than 6.52% of Python3 online submissions for Binary Tree Preorder Traversal.
'''

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                curr = root
                root = root.left
                while root.right and root.right != curr:
                    root = root.right
                if not root.right:
                    res.append(curr.val)
                    root.right = curr
                    root = curr.left
                else:
                    root.right = None
                    root = curr.right
        return res