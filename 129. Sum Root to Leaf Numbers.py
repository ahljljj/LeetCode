"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = 0
        self.helper(0, root)
        return self.res

    def helper(self, tmp, root):
        if root == None:
            return
        tmp = tmp * 10
        tmp = tmp + root.val
        if root.left == None and root.right == None:
            self.res = self.res + tmp
            return
        self.helper(tmp, root.left)
        self.helper(tmp, root.right)

# 2020/04/11, too complicated solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root, [])
        return self.res

    def dfs(self, root, tmp):
        if not root:
            return
        tmp.append(root.val)
        if not root.left and not root.right:
            self.res += self.get_sum(tmp)
        self.dfs(root.left, tmp)
        self.dfs(root.right, tmp)
        tmp.pop()

    def get_sum(self, nums):
        if not nums: return 0
        res = 0
        for num in nums:
            res = res * 10 + num
        return res
