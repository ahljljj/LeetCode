"""
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7


return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root: return res

        queue = [root]
        layer = 0

        while len(queue) > 0:
            layer += 1
            if layer % 2 == 1:
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue][::-1])
            tmp = []
            for node in queue:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            queue = tmp
        return res