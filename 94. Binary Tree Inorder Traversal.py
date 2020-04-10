"""
94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?


"""

# recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root == None: return res
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root == None: return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

# 2020/04/08, divide and conquer
'''
Runtime: 28 ms, faster than 66.10% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.7 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = self.div_conq(root)
        return res

    def div_conq(self, root):
        if not root: return []
        left = self.div_conq(root.left)
        right = self.div_conq(root.right)
        curr = []
        for val in left: curr.append(val)
        curr.append(root.val)
        for val in right: curr.append(val)
        return curr

# iterative way

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        dummy = TreeNode(None)
        dummy.right = root
        stack = [dummy]
        res = []
        while stack:
            top = stack.pop()
            if top.right:
                top = top.right
                while top:
                    stack.append(top)
                    top = top.left
            if stack: res.append(stack[-1].val)
        return res


# Morris traversal, too hard

'''
Runtime: 28 ms, faster than 66.29% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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
                    root.right = curr
                    root = curr.left
                else:
                    root.right = None
                    res.append(curr.val)
                    root = curr.right
        return res