'''

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# not my idea

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            temp = []
            tempq = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    tempq.append(node.left)
                if node.right:
                    tempq.append(node.right)
            queue = tempq
            res.append(temp)
        return res[::-1]