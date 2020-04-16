"""
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(res, [], root, sum)
        return res

    def helper(self, res, tmp, root, target):
        if not root: return
        tmp.append(root.val)
        if root.left == None and root.right == None:
            if sum(tmp) == target:
                res.append(tmp[:])
                return
        if root.left:
            self.helper(res, tmp, root.left, target)
            tmp.pop()
        if root.right:
            self.helper(res, tmp, root.right, target)
            tmp.pop()

# 2020/04/16, DFS traversal

'''
Runtime: 36 ms, faster than 97.07% of Python3 online submissions for Path Sum II.
Memory Usage: 14.8 MB, less than 75.86% of Python3 online submissions for Path Sum II.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.paths = []
        self.dfs(root, [], sum)
        return self.paths

    def dfs(self, root, path, target):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:
            if target == root.val:
                self.paths.append(path[:])
        self.dfs(root.left, path, target - root.val)
        self.dfs(root.right, path, target - root.val)
        path.pop()




