"""
230. Kth Smallest Element in a BST


Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


"""


'''
# wrong solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.helper(root, k)
        return self.res
    
    def helper(self, root, k):
        if not root:
            return
        self.helper(root.left, k)
        k -= 1
        if k == 0:
            self.res = root.val
            return
        self.helper(root.right, k)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.res = None
        self.k = k
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)

# 2020/04/08, divide and conquer

'''
Runtime: 56 ms, faster than 34.92% of Python3 online submissions for Kth Smallest Element in a BST.
Memory Usage: 17.9 MB, less than 5.45% of Python3 online submissions for Kth Smallest Element in a BST.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _, node = self.div_conq(root, k)
        return node.val

    def div_conq(self, root, k):
        if not root: return (0, None)
        left_size, left_subtree = self.div_conq(root.left, k)
        right_size, right_subtree = self.div_conq(root.right, k - left_size - 1)
        if left_size + 1 == k: return (k, root)
        if left_subtree: return (k, left_subtree)
        if right_subtree: return (k, right_subtree)
        return (left_size + 1 + right_size, None)

# slight modification

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _, node = self.div_conq(root, k)
        return node.val

    def div_conq(self, root, k):
        if not root: return (0, None)
        left_size, left_subtree = self.div_conq(root.left, k)
        right_size, right_subtree = self.div_conq(root.right, k - left_size - 1)
        if left_size + 1 == k: return (k, root)
        return (left_size + 1 + right_size, left_subtree or right_subtree)

# for fun

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.dfs(root, res, [k])
        return res[0]

    def dfs(self, root, res, k):
        if not root: return None
        self.dfs(root.left, res, k)
        k[0] -= 1
        if k[0] == 0:
            res.append(root.val)
            return
        self.dfs(root.right, res, k)