'''
1080. Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.



Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]


Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]


Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9

'''

'''
2020/04/26, too hard, not my idea

Runtime: 160 ms, faster than 5.92% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.
Memory Usage: 15.4 MB, less than 100.00% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root: return None
        max_sum = self.dfs(root, root.val, limit)
        return None if max_sum < limit else root

    def dfs(self, root, path_sum, limit):
        if not root.left and not root.right:
            return path_sum
        if root.left:
            left_max = self.dfs(root.left, path_sum + root.left.val, limit)
            if left_max < limit:
                root.left = None
        if root.right:
            right_max = self.dfs(root.right, path_sum + root.right.val, limit)
            if right_max < limit:
                root.right = None
        if not root.left and not root.right:
            return -float("inf")
        if not root.left: return right_max
        if not root.right: return left_max
        return max(left_max, right_max)
