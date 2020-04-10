'''
145. Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# 2020/04/10, recursion

'''
Runtime: 24 ms, faster than 88.10% of Python3 online submissions for Binary Tree Postorder Traversal.
Memory Usage: 13.9 MB, less than 5.72% of Python3 online submissions for Binary Tree Postorder Traversal.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root: return
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)