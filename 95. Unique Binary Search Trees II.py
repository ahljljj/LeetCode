"""
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []

        return self.helper(1, n)

    def helper(self, start, end):

        if start > end: return [None]

        res = []

        for curr in range(start, end + 1):
            left = self.helper(start, curr - 1)
            right = self.helper(curr + 1, end)
            for l in left or [None]:
                for r in right or [None]:
                    root = TreeNode(curr)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
