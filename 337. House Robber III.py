"""
337. House Robber III


The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.



"""

'''

#dfs TLE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root, 0, False)
        return self.res
    
    def helper(self, root, tmp, rob):
        if not root:
            if tmp > self.res:
                self.res = tmp
            return tmp
        if rob == False:
            self.res = max(self.helper(root.left, tmp, False) + self.helper(root.right, tmp, False),
                       root.val + self.helper(root.left, tmp, True) + self.helper(root.right, tmp, True))
        else:
            self.res = self.helper(root.left, tmp, False) + self.helper(root.right, tmp, False)
        return self.res
            
            
'''