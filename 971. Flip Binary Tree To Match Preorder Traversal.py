'''
971. Flip Binary Tree To Match Preorder Traversal

Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

If we cannot do so, then return the list [-1].



Example 1:



Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:



Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:



Input: root = [1,2,3], voyage = [1,2,3]
Output: []


Note:

1 <= N <= 100
Accepted
10,850
Submissions
24,282

'''

# 2020/04/25, too hard
'''
Runtime: 28 ms, faster than 95.45% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        self.i = 0

        return res if self.dfs(root, voyage, res) else [-1]

    def dfs(self, root, voyage, res):
        if not root: return True
        if root.val != voyage[self.i]:
            return False
        self.i += 1
        if root.left and root.left.val != voyage[self.i]:
            res.append(root.val)
            root.left, root.right = root.right, root.left
        return self.dfs(root.left, voyage, res) and self.dfs(root.right, voyage, res)

