"""
250. Count Univalue Subtrees


Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4


"""


# wrong solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #        self.count = 0
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        #        print(root, root.left, root.right)
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l and r and root.left.val == root.val and root.right.val == root.val:
            return l + r + 1
        if l and not r and root.left.val == root.val:
            return l + 1
        if not l and r and root.right.val == root.val:
            return r + 1
        return l + r

# dfs, not very neat

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return False
        if not root.left and not root.right:
            self.count += 1
            return True
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        if l and r and root.left.val == root.val and root.right.val == root.val:
            self.count += 1
            return True
        if l and not root.right and root.left.val == root.val:
            self.count += 1
            return True
        if not root.left and r and root.right.val == root.val:
            self.count += 1
            return True
        return False

