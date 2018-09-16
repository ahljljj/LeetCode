'''
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
             according to the LCA definition.
Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

'''


# not my idea


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # just make p the smaller one to make things simpler
        if not p.val < q.val:
            p, q = q, p
        anchor = root

        if p.val == anchor.val:
            # p is equal to the new root then it must be the ancestor of q
            return p
        if q.val == anchor.val:
            # q is equal to the new root then it must be the ancestor of p
            return q
        elif p.val < anchor.val and q.val > anchor.val:
            # p and q are on either side of root, so root must be the ancestor
            return anchor
        elif p.val > anchor.val and q.val > anchor.val:
            # both p and q are on right side of root, recurse on right side
            return self.lowestCommonAncestor(anchor.right, p, q)
        elif p.val < anchor and q.val < anchor.val:
            # both p and q are left side of root, recurse on left side
            return self.lowestCommonAncestor(anchor.left, p, q)