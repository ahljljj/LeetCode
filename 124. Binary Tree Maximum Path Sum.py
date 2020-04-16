'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
Accepted
294,153
Submissions
900,880

'''


# 2020/04/16, divide and conquer

'''
Runtime: 96 ms, faster than 41.76% of Python3 online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 21 MB, less than 66.67% of Python3 online submissions for Binary Tree Maximum Path Sum.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        _, _, res = self.div_conq(root)
        return res

    def div_conq(self, root):
        if not root: return -float("inf"), -float("inf"), -float("inf")
        if not root.left and not root.right:
            return root.val, root.val, root.val
        left_path_max, left_root_max, left_max = self.div_conq(root.left)
        right_path_max, right_root_max, right_max = self.div_conq(root.right)
        curr_path_max = max([root.val, root.val + left_path_max, root.val + right_path_max])
        curr_root_max = max([curr_path_max, root.val + left_path_max + right_path_max])
        curr_max = max([left_max, right_max, curr_root_max])
        return curr_path_max, curr_root_max, curr_max
