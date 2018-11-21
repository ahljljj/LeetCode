"""
437. Path Sum III


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


"""

# dfs: ridiculous slow


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
        :rtype: int
        """
        if not root:
            return 0
        self.count = 0
        self.used = set()
        self.dfs(root, sum, root.val)
        return self.count

    def dfs(self, root, sum, curr):
        if not root:
            return
        if sum == curr:
            self.count += 1
        if root.left:
            self.dfs(root.left, sum, curr + root.left.val)
            if root.left not in self.used:
                self.dfs(root.left, sum, root.left.val)
            self.used.add(root.left)
        if root.right:
            self.dfs(root.right, sum, curr + root.right.val)
            if root.right not in self.used:
                self.dfs(root.right, sum, root.right.val)
            self.used.add(root.right)
        return
